from __future__ import annotations

import logging

import numpy as np
import pygame
import tcod
from snecs.typedefs import EntityID

from scripts.engine.core import chronicle, query, world
from scripts.engine.internal.component import (
    Afflictions,
    FOV,
    IsActive,
    Knowledge,
    Lifespan,
    Opinion, Physicality,
    Position,
    Reaction, Tracked,
)
from scripts.engine.internal.constant import FOV_ALGORITHM, FOV_LIGHT_WALLS, GameEvent, INFINITE, InteractionEvent, \
    MAX_ACTIVATION_DISTANCE, ReactionTrigger, ReactionTriggerType

__all__ = [
    "process_activations",
    "process_light_map",
    "process_fov",
    "process_tile_visibility",
    "reduce_skill_cooldowns",
    "reduce_affliction_durations",
    "reduce_lifespan_durations",
    "process_interaction_event"
]

from scripts.engine.internal.definition import EffectData, ReactionData


def process_activations():
    """
    Allocate active component to  appropriate NPCs. Entity with no position or with position and close to player.
    """
    # all entities with no position must be active
    for entity, (_,) in query.not_position:
        if not world.entity_has_component(entity, IsActive):
            world.add_component(entity, IsActive())

    # check entities in range of player
    player = world.get_player()
    player_pos: Position = world.get_entitys_component(player, Position)
    for entity, (pos,) in query.position:
        # check if they're close enough that we care
        distance_x = abs(player_pos.x - pos.x)
        distance_y = abs(player_pos.y - pos.y)
        if max(distance_x, distance_y) < MAX_ACTIVATION_DISTANCE:
            # they're close, now check they arent already active
            if not world.entity_has_component(entity, IsActive):
                world.add_component(entity, IsActive())

                # update tracked to current time (otherwise they will be behind and act repeatedly)
                if world.entity_has_component(entity, Tracked):
                    tracked = world.get_entitys_component(entity, Tracked)

                    tracked.time_spent = chronicle.get_time() + 1

        else:
            # not close enough, remove active
            if world.entity_has_component(entity, IsActive):
                world.remove_component(entity, IsActive)


def process_light_map():
    """
    Update light map and light box  using light sources of all entities
    """
    # get game map details
    game_map = world.get_game_map()
    light_map = game_map.light_map

    # create transparency layer
    block_sight_map = game_map.block_sight_map

    # reset light map
    light_map[:] = False

    for entity, (
        is_active,
        light_source,
        pos,
    ) in query.active_and_light_source_and_position:
        radius = light_source.radius

        # create fov for light source and add to light map
        fov = tcod.map.compute_fov(block_sight_map, (pos.x, pos.y), radius, FOV_LIGHT_WALLS, FOV_ALGORITHM)
        light_map |= fov

    # assign back post updates
    game_map.light_map = light_map


def process_fov():
    """
    Update FOV for all active entities
    """
    # get game map details
    game_map = world.get_game_map()

    # create transparency layer
    block_sight_map = game_map.block_sight_map

    for entity, (
        is_active,
        pos,
        fov,
        stats,
        physicality,
    ) in query.active_and_position_and_fov_and_combat_stats_and_physicality:

        # get all entities blocking sight
        updated_block_sight_map = block_sight_map.copy()
        for other_entity, (_, other_pos, other_physicality) in query.active_and_position_and_physicality:
            assert isinstance(other_pos, Position)
            assert isinstance(other_physicality, Physicality)

            # dont check against self
            if entity == other_entity:
                continue

            # is viewing_entity taller and therefore their sight isnt blocked?
            if physicality.height > other_physicality.height:
                continue

            # set all positions to blocking
            for x, y in other_pos.coordinates:
                updated_block_sight_map[x, y] = 0

        # update entities fov map
        stats = world.create_combat_stats(entity)
        fov.map = tcod.map.compute_fov(
            updated_block_sight_map, (pos.x, pos.y), stats.sight_range, FOV_LIGHT_WALLS, FOV_ALGORITHM
        )


def process_tile_visibility():
    """
    Update tile visibility based on player fov
    """
    # get player info
    player = world.get_player()
    fov_map = world.get_entitys_component(player, FOV).map

    # get game map details
    game_map = world.get_game_map()
    width = game_map.width
    height = game_map.height
    light_map = game_map.light_map
    tile_map = game_map.tile_map

    # set all tiles to not visible
    for x in range(0, width):
        for y in range(0, height):
            game_map.tile_map[x][y].is_visible = False

    # combine maps
    visible_map = fov_map & light_map

    # loop all map
    for x in range(0, width):
        for y in range(0, height):
            tile_map[x][y].is_visible = bool(visible_map[x, y])  # cast to bool as it is numpy _bool


def reduce_skill_cooldowns():
    """
    Reduce skill cool down for all entities.
    """
    for entity, (knowledge,) in query.knowledge:
        assert isinstance(knowledge, Knowledge)
        for skill_name in knowledge.skill_names:
            skill_cooldown = knowledge.cooldowns[skill_name]
            if skill_cooldown > 0:
                knowledge.set_skill_cooldown(skill_name, skill_cooldown - 1)


def reduce_affliction_durations():
    """
    Reduce all affliction durations
    """
    for entity, (afflictions,) in query.afflictions:
        assert isinstance(afflictions, Afflictions)
        for affliction in afflictions.active:

            if affliction.duration != INFINITE:
                # reduce duration if not infinite
                affliction.duration -= 1

            # handle expiry
            if affliction.duration <= 0:
                world.remove_affliction(entity, affliction)


def reduce_lifespan_durations():
    """
    Reduce all lifespan durations
    """
    for entity, (lifespan,) in query.lifespan:
        assert isinstance(lifespan, Lifespan)

        if lifespan.duration != INFINITE:
            # reduce duration if not infinite
            lifespan.duration -= 1

        # handle expiry
        if lifespan.duration <= 0:
            logging.debug(f"{world.get_name(entity)}`s lifespan has expired. ")
            world.kill_entity(entity)


def process_interaction_event(event: pygame.event):
    """
    Passes an interaction event to the relevant functions.
    """
    if event.type == InteractionEvent.MOVE:
        # print(f"Caught MOVE: {event.origin}, {event.target}, {event.direction}, {event.new_pos}")
        _handle_proximity(event)
        _handle_affliction(event.target, ReactionTrigger.MOVE)
        _process_win_condition(event)

    elif event.type == InteractionEvent.DAMAGE:
        # print(f"Caught DAMAGE: {event.origin}, {event.target}, {event.amount}, {event.damage_type},
        # {event.remaining_hp}")
        _handle_affliction(event.origin, ReactionTrigger.DEAL_DAMAGE)
        _handle_affliction(event.target, ReactionTrigger.TAKE_DAMAGE)

        if event.remaining_hp <= 0:
            _handle_affliction(event.origin, ReactionTrigger.KILL)
            _handle_affliction(event.target, ReactionTrigger.DIE)

    elif event.type == InteractionEvent.AFFECT_STAT:
        # print(f"Caught AFFECT_STAT: {event.origin}, {event.target}, {event.stat}, {event.amount}")
        _handle_affliction(event.origin, ReactionTrigger.CAUSED_AFFECT_STAT)
        _handle_affliction(event.target, ReactionTrigger.AFFECTED_STAT)

    elif event.type == InteractionEvent.AFFECT_COOLDOWN:
        # print(f"Caught AFFECT_COOLDOWN: {event.origin}, {event.target}, {event.amount}")
        _handle_affliction(event.origin, ReactionTrigger.CAUSED_AFFECT_COOLDOWN)
        _handle_affliction(event.target, ReactionTrigger.AFFECTED_COOLDOWN)

    elif event.type == InteractionEvent.AFFLICTION:
        # print(f"Caught AFFLICTION: {event.origin}, {event.target}, {event.name}")
        _handle_affliction(event.origin, ReactionTrigger.CAUSED_AFFLICTION)
        _handle_affliction(event.target, ReactionTrigger.AFFLICTED)


def _handle_proximity(event: pygame.event):
    """
    Check for any entities with a reaction to proximity and trigger that reaction.
    """

    # loop all entities sharing same position that have a reaction
    for entity, (position, reaction) in query.position_and_reaction:
        assert isinstance(position, Position)
        assert isinstance(reaction, Reaction)
        if (position.x, position.y) == event.new_pos:
            if ReactionTrigger.PROXIMITY in reaction.reactions:
                data = reaction.reactions[ReactionTrigger.PROXIMITY]

                # if we dont have a required opinion then just apply reaction
                if not data.required_opinion:
                    _create_skill_or_effect(event, data)
                else:
                    # check we meet opinion requirement
                    if world.has_enough_opinion(entity, event.origin, data.required_opinion):
                        _create_skill_or_effect(event, data)


def _process_win_condition(event: pygame.event):
    """
    Checking if the win condition has been met. Post event if it is.
    """
    player = world.get_player()

    # only progress if its the player as only the player can win
    if not player == event.target:
        return

    player_pos = world.get_entitys_component(player, Position)

    for entity, (position, _) in query.position_and_win_condition:
        assert isinstance(position, Position)
        if player_pos.x == position.x and player_pos.y == position.y:
            event = pygame.event.Event(GameEvent.WIN_CONDITION_MET)
            pygame.event.post(event)
            break


def _handle_affliction(entity: EntityID, reaction_trigger: ReactionTriggerType):
    """
    Check for any afflictions triggered by the interaction and trigger that interaction.
    """
    if world.entity_has_component(entity, Afflictions):
        afflictions = world.get_entitys_component(entity, Afflictions)
        for affliction in afflictions.active:
            if reaction_trigger in affliction.triggers:
                world.trigger_affliction(affliction)


def _create_skill_or_effect(event: pygame.event, data: ReactionData):
    if isinstance(data.reaction, EffectData):
        effect = world.create_effect(event.origin, event.target, data.reaction)
        effect.evaluate()
    else:  # skill data
        skill = world.get_known_skill(event.origin, data.name)
        world.use_skill(event.origin, skill, world.get_tile(event.new_pos), event.direction)

