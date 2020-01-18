from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.core.constants import TargetTags, TILE_SIZE
from scripts.world.components import Position
from scripts.world.game_map import GameMap
from scripts.world.tile import Tile
from scripts.core.library import library

if TYPE_CHECKING:
    from typing import List, Tuple, Union
    from scripts.managers.world_manager import WorldManager


class MapMethods:
    """
    Methods for querying game map and game map related info and taking game map actions.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """
    def __init__(self, manager):
        self.manager = manager  # type: WorldManager
        self.game_map = None

    ########## CREATE ###############
    
    def create_game_map(self, width, height):
        """
        Create new GameMap and create player FOV
        """
        self.game_map = GameMap(width, height)
        
    ############# GET ###############
    
    def get_game_map(self) -> GameMap:
        """
        Get current game_map

        Returns:
            GameMap
        """
        return self.game_map
    
    def get_tile(self, tile_pos: Union[Tuple[int, int], str]) -> Tile:
        """
        Get the tile at the specified location. Use tile_x and tile_y OR tile_pos_string

        Args:
            tile_pos (): str expects "x,y", or handles tuples (x, y)

        Returns:
            Tile: the tile at the location
        """
        game_map = self.get_game_map()

        if isinstance(tile_pos, str):
            x, y = tile_pos.split(",")
            x = int(x)  # str to int
            y = int(y)
        else:
            x = tile_pos[0]
            y = tile_pos[1]

        return game_map.tiles[x][y]

    def get_direction(self, start_pos: Union[Tuple[int, int], str], target_pos: Union[Tuple[int, int],
    str]) -> Tuple[int, int]:
        """
        Get the direction between two locations.

        Args:
            start_pos (): str expects "x,y", or handles tuples (x, y)
            target_pos (): str expects "x,y", or handles tuples (x, y)

        Returns:

        """
        start_tile = self.get_tile(start_pos)
        target_tile = self.get_tile(target_pos)

        dir_x = target_tile.x - start_tile.x
        dir_y = target_tile.y - start_tile.y

        # handle any mistaken values coming in
        if dir_x > 1:
            dir_x = 1
        elif dir_x < -1:
            dir_x = -1

        if dir_y > 1:
            dir_y = 1
        elif dir_y < -1:
            dir_y = -1

        return dir_x, dir_y

    def get_tiles(self, start_tile_col, start_tile_row, coords):
        """
        Get multiple tiles based on starting position and coordinates given

        Args:
            start_tile_col (int):
            start_tile_row (int):
            coords (list[Tuple]): List of tuples holding x y. E.g. (x, y)

        Returns:
            List[Tile]:
        """
        game_map = self.get_game_map()
        tiles = []

        for coord in coords:
            tile_x = coord[0] + start_tile_col
            tile_y = coord[1] + start_tile_row

            # make sure it is in bounds
            if self.is_tile_in_bounds(tile_x, tile_y):
                tiles.append(game_map.tiles[tile_x][tile_y])

        return tiles

    ############# CHECKS ############

    def is_tile_blocking_sight(self, tile_x, tile_y):
        """
        Check if a tile is blocking sight

        Args:
            tile_x:
            tile_y:

        Returns:
            bool:
        """
        game_map = self.get_game_map()

        if 0 <= tile_x < game_map.width and 0 <= tile_y < game_map.height:
            return game_map.tiles[tile_x][tile_y].blocks_sight
        else:
            return True

    def is_tile_visible_to_player(self, tile_x, tile_y):
        """
        Check if the specified tile is visible to the player

        Args:
            tile_x:
            tile_y:

        Returns:
            bool:
        """
        game_map = self.get_game_map()

        if 0 <= tile_x < game_map.width and 0 <= tile_y < game_map.height:
            return game_map.tiles[tile_x][tile_y].is_visible
        else:
            return False

    def get_target_type_from_tile(self, tile_x, tile_y):
        """
        Get type of target tile

        Args:
            tile_x(int):  x position of the tile
            tile_y(int):  y position of the tile
        """
        # TODO - convert to properties of tile class

        game_map = self.get_game_map()
        tile = game_map.tiles[tile_x][tile_y]

        if not self.is_tile_in_bounds(tile_x, tile_y):
            return TargetTags.OUT_OF_BOUNDS

        # TODO - rewrite as terrain no longer an object
        # if type(tile.terrain) is Wall:
        #
        #     return TargetTags.BLOCKED_SPACE
        # elif type(tile.terrain) is Floor:
        #     return TargetTags.OPEN_SPACE

    def is_tile_in_bounds(self, tile_x, tile_y):
        """
        Check if specified tile is in the map.

        Args:
            tile_x:
            tile_y:

        Returns:
            bool:
        """
        game_map = self.get_game_map()

        if (0 <= tile_x < game_map.width) and (0 <= tile_y < game_map.height):
            return True
        else:
            return False

    def is_tile_blocking_movement(self, tile_x, tile_y):
        """
        Check if the specified tile is blocking movement
        Args:
            tile_x:
            tile_y:

        Returns:
            bool:

        """
        game_map = self.get_game_map()

        if 0 <= tile_x < game_map.width and 0 <= tile_y < game_map.height:
            return game_map.tiles[tile_x][tile_y].blocks_movement
        else:
            return True

    def tile_has_tag(self, tile: Tile, tag: TargetTags, active_entity: int = None):
        """
        Check if a given tag applies to the tile

        Args:
            tile ():
            tag (TargetTags): tag to check
            active_entity (int): entity using a skill

        Returns:
            bool: True if tag applies.
        """

        if tag == TargetTags.OPEN_SPACE:
            return not tile.blocks_movement
        elif tag == TargetTags.BLOCKED_SPACE:
            return tile.blocks_movement
        elif tag == TargetTags.SELF:
            # ensure active entity is the same as the targeted one
            for entity, position in self.manager.World.get_components(Position):
                if position.x == tile.x and position.y == tile.y:
                    if active_entity == entity:
                        return True

            # no matching entity found
            return False
        elif tag == TargetTags.OTHER_ENTITY:
            # ensure active entity is NOT the same as the targeted one
            for entity, position in self.manager.World.get_component(Position):
                if position.x == tile.x and position.y == tile.y:
                    if active_entity != entity:
                        return True
            # no different entity found
            return False
        elif tag == TargetTags.NO_ENTITY:
            return not tile.has_entity
        elif tag == TargetTags.ANY:
            return True
        else:
            return False  # catch all

    def tile_has_tags(self, target_tile: Tile, tags: List[TargetTags], active_entity: int = None):
        """
        Check a tile has all required tags

        Args:
            target_tile(Tile):
            tags(List):
            active_entity(int):

        Returns:
            bool: True if tile has all tags
        """
        tags_checked = {}

        # assess all tags
        for tag in tags:
            tags_checked[tag.name] = self.tile_has_tag(target_tile, tag, active_entity)

        # if all tags came back true return true
        if all(value for value in tags_checked.values()):
            return True
        else:
            return False