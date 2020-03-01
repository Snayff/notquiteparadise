from __future__ import annotations

import tcod
from typing import TYPE_CHECKING
from scripts.engine.core.constants import FOVInfo, SkillShapes

if TYPE_CHECKING:
    from scripts.managers.world_manager.world_manager import WorldManager


class FOVMethods:
    """
    Methods for querying the fov and fov related info and taking fov actions.
    """
    def __init__(self, manager):
        self._manager: WorldManager = manager
        self._players_fov_map: tcod.map.Map = None

    def create_player_fov_map(self, width, height):
        """
        Create the fov map for the player
        """
        fov_map = tcod.map_new(width, height)

        for x in range(width):
            for y in range(height):
                tile = self._manager.Map.get_tile((x, y))
                if tile:
                    tcod.map_set_properties(fov_map, x, y, not tile.blocks_sight, not tile.blocks_movement)

        self._players_fov_map = fov_map

    def recompute_player_fov(self, x, y, radius):
        """
        Recalc the player's fov
        """
        tcod.map_compute_fov(self.get_player_fov(), x, y, radius, FOVInfo.LIGHT_WALLS, FOVInfo.FOV_ALGORITHM)
        self._manager.FOV.update_tile_visibility(self.get_player_fov())

    def is_tile_in_fov(self, tile_x: int, tile_y: int) -> bool:
        """
        Check if  target tile is in player`s FOV
        """
        return tcod.map_is_in_fov(self.get_player_fov(), tile_x, tile_y)

    def get_player_fov(self):
        """
        Get the player fov map

        Returns:
            tcod.map.Map
        """
        return self._players_fov_map

    def update_tile_visibility(self, fov_map):
        """
        Update the player`s fov

        Args:
            fov_map:
        """
        game_map = self._manager.Map.get_game_map()

        for x in range(0, game_map.width):
            for y in range(0, game_map.height):
                game_map.tiles[x][y].is_visible = tcod.map_is_in_fov(fov_map, x, y)

    def get_tiles_in_range_and_fov_of_player(self, range_from_centre):
        """
        Get all of the tiles within a specified range of the player that are also in the FOV

        Args:
            range_from_centre (int):

        Returns:
            list[Tile]: A list of tiles
        """
        player = self._manager.Entity.get_player()

        # get the tiles in range
        coords = self._manager.Skill.create_shape(SkillShapes.SQUARE, range_from_centre)  # square as LOS is square
        tiles_in_range = self._manager.Map.get_tiles(player.x, player.y, coords)
        tiles_in_range_and_fov = []

        # only take tiles in range and FOV
        in_fov = self.is_tile_in_fov
        for tile in tiles_in_range:
            if in_fov(tile.x, tile.y):
                tiles_in_range_and_fov.append(tile)

        return tiles_in_range_and_fov
