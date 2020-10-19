from __future__ import annotations

from typing import TYPE_CHECKING

import tcod

from scripts.engine import utility, world
from scripts.engine.component import FOV, LightSource, Position
from scripts.engine.core import queries
from scripts.engine.core.constants import FOV_ALGORITHM, FOV_LIGHT_WALLS, MAX_ACTIVATION_DISTANCE, TILE_SIZE
from scripts.engine.world_objects import lighting

if TYPE_CHECKING:
    pass

__all__ = ["process_lighting", "process_fov", "process_tile_visibility"]


def process_lighting():
    """
    Update light map and light box  using light sources of all entities
    """
    # get player details
    player = world.get_player()
    player_pos: Position = world.get_entitys_component(player, Position)

    # get game map details
    game_map = world.get_game_map()
    light_map = game_map.light_map
    light_box = game_map.light_box

    # create transparency layer
    block_sight_map = game_map.block_sight_map

    # reset light map
    light_map[:] = False

    # remove existing lights in light box
    light_box.lights = {}

    # process all light sources
    for entity, (light_source, pos) in queries.light_source_and_position:
        light_source: LightSource
        pos: Position
        radius = light_source.radius

        # check if they're close enough that we care
        offset_x = player_pos.x - pos.x
        offset_y = player_pos.y - pos.y
        if max(abs(offset_x), abs(offset_y)) < MAX_ACTIVATION_DISTANCE:

            # create fov for light source
            fov = tcod.map.compute_fov(block_sight_map, (pos.x, pos.y), radius, FOV_LIGHT_WALLS, FOV_ALGORITHM)
            light_map |= fov

            # add light to light box
            side_length = (radius * 2) * TILE_SIZE
            light_img = utility.get_image("world/light_mask.png", (side_length, side_length))
            light_img.set_alpha(15)
            light_box.add_light(lighting.Light([pos.x * TILE_SIZE, pos.y * TILE_SIZE], radius * TILE_SIZE, light_img))



def process_fov():
    """
    Update FOV for all entities within MAX_ACTIVATION_DISTANCE of player.
    """
    # get player details
    player = world.get_player()
    player_pos: Position = world.get_entitys_component(player, Position)

    # create transparency layer
    game_map = world.get_game_map()
    block_sight_map = game_map.block_sight_map

    for entity, (fov, pos, stats) in queries.position_and_fov_and_combat_stats:

        # check if they're close enough that we care
        offset_x = player_pos.x - pos.x
        offset_y = player_pos.y - pos.y
        if max(abs(offset_x), abs(offset_y)) < MAX_ACTIVATION_DISTANCE:
            # get sight range
            stats = world.create_combat_stats(entity)
            sight_range = stats.sight_range

            fov.map = tcod.map.compute_fov(block_sight_map, (pos.x, pos.y), sight_range, FOV_LIGHT_WALLS, FOV_ALGORITHM)


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
