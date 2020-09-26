from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING, Type

import tcod

from scripts.engine import world
from scripts.engine.component import FOV, HasCombatStats, LightSource, Position
from scripts.engine.core import queries
from scripts.engine.core.constants import FOV_ALGORITHM, FOV_LIGHT_WALLS, MAX_ACTIVATION_DISTANCE

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


def process_light_map():
    """
    Update light map using light sources of all entities
    """
    start_time = time.time()

    # get player details
    player = world.get_player()
    player_pos: Position = world.get_entitys_component(player, Position)

    # get game map details
    game_map = world.get_game_map()
    light_map = game_map.light_map

    # create transparency layer
    transparency = world.create_fov_map()

    # reset light map
    light_map[:] = False

    for entity, (light_source, pos) in queries.light_source_and_position:
        light_source: LightSource
        pos: Position
        radius = light_source.radius

        # check if they're close enough that we care
        offset_x = player_pos.x - pos.x
        offset_y = player_pos.y - pos.y
        if max(abs(offset_x), abs(offset_y)) < MAX_ACTIVATION_DISTANCE:

            # create fov for light source
            fov = tcod.map.compute_fov(transparency, (pos.x, pos.y), radius, FOV_LIGHT_WALLS, FOV_ALGORITHM)
            light_map |= fov

    end_time = time.time()
    logging.debug(f"Completed process_light_map in {format(end_time - start_time, '.5f')}")


def process_fov():
    """
    Update FOV for all entities within MAX_ACTIVATION_DISTANCE of player.
    """
    start_time = time.time()

    # get player details
    player = world.get_player()
    player_pos: Position = world.get_entitys_component(player, Position)

    # create transparency layer
    transparency = world.create_fov_map()

    for entity, (fov, pos, stats) in queries.fov_and_position_and_combat_stats:

        # check if they're close enough that we care
        offset_x = player_pos.x - pos.x
        offset_y = player_pos.y - pos.y
        if max(abs(offset_x), abs(offset_y)) < MAX_ACTIVATION_DISTANCE:
            # get sight range
            stats = world.create_combat_stats(entity)
            sight_range = stats.sight_range

            # compute the fov
            maps = []
            for coordinate in pos.coordinates:
                fov_map = tcod.map.compute_fov(transparency, coordinate, sight_range, FOV_LIGHT_WALLS,
                                               FOV_ALGORITHM)
                maps.append(fov_map)

            fov.map = maps[0]
            for m in maps:
                fov.map |= m

    end_time = time.time()
    logging.debug(f"Completed process_fov in {format(end_time - start_time, '.5f')}")


def process_tile_visibility():
    """
    Update tile visibility based on player fov
    """
    start_time = time.time()

    # get player info
    player = world.get_player()
    fov_map = world.get_entitys_component(player, FOV).map
    stats = world.create_combat_stats(player)
    sight_range = stats.sight_range
    pos = world.get_entitys_component(player, Position)

    # get game map details
    game_map = world.get_game_map()
    light_map = game_map.light_map
    tile_map = game_map.tile_map

    # set all tiles to not visible
    game_map = world.get_game_map()
    width = game_map.width
    height = game_map.height
    for x in range(0, width):
        for y in range(0, height):
            game_map.tile_map[x][y].is_visible = False

    # loop sight range
    for offset_x in range(0, sight_range):
        for offset_y in range(0, sight_range):
            x = pos.x + offset_x
            y = pos.y + offset_y
            # if in player fov set to visible
            if fov_map[x][y] and light_map[x][y]:
                tile_map[x][y].is_visible = True

    end_time = time.time()
    logging.debug(f"Completed process_tile_visibility in {format(end_time - start_time, '.5f')}")
