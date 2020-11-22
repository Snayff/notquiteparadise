from __future__ import annotations

import logging

import tcod

from scripts.engine.core import chronicle, query, world
from scripts.engine.internal.component import Afflictions, FOV, IsActive, Knowledge, Lifespan, Position, Tracked
from scripts.engine.internal.constant import FOV_ALGORITHM, FOV_LIGHT_WALLS, INFINITE, MAX_ACTIVATION_DISTANCE

__all__ = [
    "process_activations",
    "process_light_map",
    "process_fov",
    "process_tile_visibility",
    "reduce_skill_cooldowns",
    "reduce_affliction_durations",
    "reduce_lifespan_durations",
]


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
    # create transparency layer
    game_map = world.get_game_map()
    block_sight_map = game_map.block_sight_map

    for entity, (
        is_active,
        pos,
        fov,
        stats,
    ) in query.active_and_position_and_fov_and_combat_stats:

        stats = world.create_combat_stats(entity)
        sight_range = stats.sight_range
        fov.map = tcod.map.compute_fov(block_sight_map, (pos.x, pos.y), sight_range, FOV_LIGHT_WALLS, FOV_ALGORITHM)


def process_tile_visibility():
    """
    Update tile visibility based on player fov
    FIXME - every entity has its own fov so gamemap doesnt need visibility anymore
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
