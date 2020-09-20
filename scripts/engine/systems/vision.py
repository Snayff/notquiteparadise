from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING, Type

import tcod

from scripts.engine import world
from scripts.engine.component import FOV, HasCombatStats, LightSource, Position
from scripts.engine.core.constants import MAX_ACTIVATION_DISTANCE

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


def process_fov():
    """
    Update FOV for all entities within MAX_ACTIVATION_DISTANCE of player.
    """
    start_time = time.time()

    player = world.get_player()
    player_pos: Position = world.get_entitys_component(player, Position)

    for entity, (fov, pos, stats) in world.get_components([FOV, Position, HasCombatStats]):

        # check if they're close enough that we care
        for offset_x in range(-MAX_ACTIVATION_DISTANCE, MAX_ACTIVATION_DISTANCE):
            for offset_y in range(-MAX_ACTIVATION_DISTANCE, MAX_ACTIVATION_DISTANCE):
                x = pos.x + offset_x
                y = pos.y + offset_y
                if x == player_pos.x and y == player_pos.y:
                    # get sight range
                    stats = world.create_combat_stats(entity)

                    sight_range = stats.sight_range

                    # compute the fov
                    transparency = world.create_fov_map()
                    maps = []
                    for coordinate in pos.coordinates:
                        fov_map = tcod.map.compute_fov(transparency, coordinate, sight_range, fov.light_walls,
                                                       fov.algorithm)
                        maps.append(fov_map)

                    fov.map = maps[0]
                    for m in maps:
                        fov.map |= m

    end_time = time.time()
    logging.debug(f"Completed process_fov in {format(end_time - start_time, '.5f')}")


def process_tile_visibility():
    """
    Update tile visibility based on player fov and entities with light sources
    """
    start_time = time.time()

    player = world.get_player()
    fov_map = world.get_entitys_component(player, FOV).map

    # set all tiles to not visible
    gamemap = world.get_gamemap()
    width = gamemap.width
    height = gamemap.height
    for x in range(0, width):
        for y in range(0, height):
            gamemap.tiles[x][y].is_visible = False

    # check for light sources in player fov
    for entity, (light_source, pos) in world.get_components([LightSource, Position]):
        light_source: LightSource
        pos: Position
        radius = light_source.radius

        # loop light radius
        for offset_x in range(-radius, radius):
            for offset_y in range(-radius, radius):
                x = pos.x + offset_x
                y = pos.y + offset_y

                # if in player fov ste to visible
                if fov_map[x][y]:
                    gamemap.tiles[x][y].is_visible = True

    end_time = time.time()
    logging.debug(f"Completed process_tile_visibility in {format(end_time - start_time, '.5f')}")
