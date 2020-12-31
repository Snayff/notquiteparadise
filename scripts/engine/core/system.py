from __future__ import annotations

import logging

import pygame
import tcod
from snecs.typedefs import EntityID

from scripts.engine.core import chronicle, query, world
from scripts.engine.core.event import (
    AffectCooldownEvent,
    AffectStatEvent,
    AfflictionEvent,
    DamageEvent,
    event_hub,
    MoveEvent,
    Subscriber,
    WinConditionMetEvent,
)
from scripts.engine.internal.component import (
    Afflictions,
    FOV,
    Immunities, IsActive,
    Knowledge,
    Lifespan,
    Opinion,
    Physicality,
    Position,
    Reaction,
    Tracked,
)
from scripts.engine.internal.constant import (
    Direction,
    EventType,
    FOV_ALGORITHM,
    FOV_LIGHT_WALLS,
    INFINITE,
    MAX_ACTIVATION_DISTANCE,
    ReactionTrigger,
    ReactionTriggerType,
)
from scripts.engine.internal.definition import EffectData, ReactionData
from scripts.engine.world_objects.tile import Tile

__all__ = [
    "process_activations",
    "process_light_map",
    "process_fov",
    "process_tile_visibility",
    "reduce_skill_cooldowns",
    "reduce_affliction_durations",
    "reduce_lifespan_durations",
    "reduce_immunity_durations",
]

########################### GENERAL ################################


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


########################## VISION ##################################


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


########################## TIME ####################################


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
                logging.debug(f"Removed {affliction.f_name} from '{world.get_name(entity)}'.")


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
            world.kill_entity(entity)
            logging.debug(f"'{world.get_name(entity)}'s lifespan has expired and they have been killed.")


def reduce_immunity_durations():
    """
    Reduce all immunity durations
    """
    for entity, (immunities,) in query.immunities:
        assert isinstance(immunities, Immunities)
        _active = immunities.active.copy()
        for immunity_name, duration in _active.items():

            if duration != INFINITE:
                # reduce duration if not infinite
                immunities.active[immunity_name] -= 1
                duration -= 1

            # handle expiry
            if duration <= 0:
                immunities.active.pop(immunity_name)
                logging.debug(f"Removed {immunity_name} from '{world.get_name(entity)}'s "
                              f"list of immunities.")

########################### GENERIC REACTION HANDLING ##############################


class InteractionEventSubscriber(Subscriber):
    """
    Handle interaction events.
    """

    def __init__(self):
        super().__init__("interaction_subscriber")
        self.subscribe(EventType.INTERACTION)

    def process_event(self, event):
        if isinstance(event, MoveEvent):
            _handle_proximity_reaction_trigger(event)
            _process_win_condition(event)

            _handle_reaction_trigger(event.origin, ReactionTrigger.MOVE)
            _handle_reaction_trigger(event.target, ReactionTrigger.MOVED)

        elif isinstance(event, DamageEvent):
            _handle_reaction_trigger(event.origin, ReactionTrigger.DEAL_DAMAGE)
            _handle_reaction_trigger(event.target, ReactionTrigger.TAKE_DAMAGE)

            if event.remaining_hp <= 0:
                _handle_reaction_trigger(event.origin, ReactionTrigger.KILL)
                _handle_reaction_trigger(event.target, ReactionTrigger.DIE)

        elif isinstance(event, AffectStatEvent):
            _handle_reaction_trigger(event.origin, ReactionTrigger.CAUSED_AFFECT_STAT)
            _handle_reaction_trigger(event.target, ReactionTrigger.STAT_AFFECTED)

        elif isinstance(event, AffectCooldownEvent):
            _handle_reaction_trigger(event.origin, ReactionTrigger.CAUSED_AFFECT_COOLDOWN)
            _handle_reaction_trigger(event.target, ReactionTrigger.COOLDOWN_AFFECTED)

        elif isinstance(event, AfflictionEvent):
            _handle_reaction_trigger(event.origin, ReactionTrigger.CAUSED_AFFLICTION)
            _handle_reaction_trigger(event.target, ReactionTrigger.AFFLICTED)


interaction_subscriber = InteractionEventSubscriber()


def _process_opinions(causing_entity: EntityID, reaction_trigger: ReactionTriggerType):
    """
    Adjust opinion of entity for any other entities that have an attitude towards the reaction trigger.
    """
    for entity, (opinion,) in query.opinion:
        assert isinstance(opinion, Opinion)
        if reaction_trigger in opinion.attitudes:
            if causing_entity in opinion.opinions:
                opinion.opinions[causing_entity] += opinion.attitudes[reaction_trigger]
            else:
                opinion.opinions[causing_entity] = opinion.attitudes[reaction_trigger]

            logging.debug(
                f"{world.get_name(entity)}`s opinion of {world.get_name(causing_entity)} is now "
                f"{opinion.opinions[causing_entity]} due to {reaction_trigger}."
            )


def _handle_affliction(entity: EntityID, reaction_trigger: ReactionTriggerType):
    """
    Check for any afflictions triggered by the interaction and trigger that interaction.
    """
    if world.entity_has_component(entity, Afflictions):
        afflictions = world.get_entitys_component(entity, Afflictions)
        for affliction in afflictions.active:
            if reaction_trigger in affliction.triggers:
                world.trigger_affliction(affliction)


def _handle_reaction_trigger(entity: EntityID, reaction_trigger: ReactionTriggerType):
    """
    Check for any entities with a reaction to the trigger and handle that reaction.
    """
    # loop all entities sharing same position that have a reaction
    for reacting_entity, (reaction,) in query.reaction:
        assert isinstance(reaction, Reaction)

        if reaction_trigger in reaction.reactions:
            data = reaction.reactions[reaction_trigger]
            _process_opinions(entity, reaction_trigger)
            _handle_affliction(entity, reaction_trigger)
            _handle_reaction(reacting_entity, entity, data)


def _handle_reaction(observer: EntityID, triggering_entity: EntityID, data: ReactionData):
    """
    Process a reaction, checking opinion is sufficient and rolling for chance to trigger.
    """
    diff_mod = 0.5  # the amount of the opinion difference to consider
    required_opinion = data.required_opinion

    # if we dont have a required opinion or have enough opinion carry on
    if required_opinion is None or not world.entity_has_component(observer, Opinion):
        opinion_diff = 0

    else:
        opinion = world.get_entitys_component(observer, Opinion)
        current_opinion = opinion.opinions[triggering_entity]

        # reverse if negative to make it simpler
        if required_opinion < 0:
            required_opinion = -required_opinion
            current_opinion = -current_opinion

        if required_opinion < current_opinion:
            opinion_diff = current_opinion - required_opinion

        else:
            # has opinion and doesnt meet requirement
            return

    # roll for chance to react
    from scripts.engine.core import utility

    roll = utility.roll()
    modified_chance = int(data.chance + (opinion_diff * diff_mod))  # the greater the opinion diff the more chance

    # if roll was unsuccessful return now
    if roll > modified_chance:
        return

    # we need position to react to so check we have one (this also prevents triggering on gods)
    if world.entity_has_component(triggering_entity, Position):
        # get tile of the acting entity
        position = world.get_entitys_component(triggering_entity, Position)
        target_tile = world.get_tile((position.x, position.y))

        _apply_reaction(observer, triggering_entity, target_tile, data)

        # reacted so reduce opinion towards 0
        if required_opinion is None or not world.entity_has_component(observer, Opinion):
            return

        # check if negative value
        if 0 >= opinion.opinions[triggering_entity]:
            opinion.opinions[triggering_entity] = min(0, opinion.opinions[triggering_entity] + required_opinion)
        else:
            opinion.opinions[triggering_entity] = max(0, opinion.opinions[triggering_entity] - required_opinion)


def _apply_reaction(observer: EntityID, triggering_entity: EntityID, target_tile: Tile, data: ReactionData):
    """
    Create the skill or effect from the reaction and apply it.
    """
    if isinstance(data.reaction, EffectData):
        effect = world.create_effect(observer, triggering_entity, data.reaction)
        effect.evaluate()
    else:  # skill data
        from scripts.engine.internal.data import store

        skill = store.skill_registry[data.reaction]
        world.use_skill(observer, skill, target_tile, Direction.CENTRE)


############### NON-GENERIC REACTION HANDLING ##########################


def _handle_proximity_reaction_trigger(event: pygame.event):
    """
    Special case of _handle_reaction_trigger. Checks for overlapping positions. Check for any entities with a
    reaction to proximity and handle that reaction.
    """
    # loop all entities sharing same position that have a reaction
    for entity, (position, reaction) in query.position_and_reaction:
        assert isinstance(position, Position)
        assert isinstance(reaction, Reaction)
        for coord in position.coordinates:
            if coord == event.new_pos:
                if ReactionTrigger.PROXIMITY in reaction.reactions:
                    data = reaction.reactions[ReactionTrigger.PROXIMITY]
                    _handle_reaction(entity, event.origin, data)


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
            # post game event
            event_hub.post(WinConditionMetEvent())
            break
