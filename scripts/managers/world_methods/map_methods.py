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

    def get_game_map(self) -> GameMap:
        """
        Get current game_map

        Returns:
            GameMap
        """
        return self.game_map

    def create_game_map(self, width, height):
        """
        Create new GameMap and create player FOV
        """
        self.game_map = GameMap(width, height)

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

    def tile_has_tag(self, tile, target_tag, active_entity=None):
        """
        Check if a given tag applies to the tile

        Args:
            tile ():
            target_tag (TargetTags): tag to check
            active_entity (Entity): entity using a skill

        Returns:
            bool: True if tag applies.
        """

        if target_tag == TargetTags.OPEN_SPACE:
            return not tile.blocks_movement
        elif target_tag == TargetTags.BLOCKED_SPACE:
            return tile.blocks_movement
        elif target_tag == TargetTags.SELF:
            # ensure active entity is the same as the targeted one
            for entity, position in self.manager.World.get_components(Position):
                if position.x == tile.x and position.y == tile.y:
                    if active_entity == entity:
                        return True

            # no matching entity found
            return False
        elif target_tag == TargetTags.OTHER_ENTITY:
            # ensure active entity is NOT the same as the targeted one
            for entity, position in self.manager.World.get_component(Position):
                if position.x == tile.x and position.y == tile.y:
                    if active_entity != entity:
                        return True
            # no different entity found
            return False
        elif target_tag == TargetTags.NO_ENTITY:
            return not tile.has_entity
        elif target_tag == TargetTags.ANY:
            return True
        else:
            return False  # catch all

    def get_entity_on_tile(self, tile) -> Union[int, None]:
        """
        Get the entity from the Tile

        Returns:
            int: The entity on the tile

        """
        entities = self.manager.Entity.get_entities(Position)
        for entity in entities:
            pos = self.manager.Entity.get_component(entity, Position)
            if pos.x == tile.x and pos.y == tile.y:
                return entity
        else:
            return None

    @staticmethod
    def set_terrain_on_tile(tile, terrain):
        """
        Set the new terrain on the tile.

        Args:
            tile (Tile):
            terrain (TargetTags):
        """
        new_terrain = None

        # TODO - rewrite for EC
        # if terrain == TargetTags.BLOCKED_SPACE:
        #     new_terrain = Wall()
        # elif terrain == TargetTags.OPEN_SPACE:
        #     new_terrain = Floor()
        #
        # if new_terrain:
        #     tile.terrain = new_terrain
        #     tile.terrain.owner = tile

    @staticmethod
    def get_terrain_on_tile(tile):
        """
        Get the terrain from the Tile

        Returns:
            Terrain: The terrain on the tile

        """
        return tile.terrain

    @staticmethod
    def add_aspect_to_tile(tile, aspect_name):
        """
        Add a new aspects on the tile. If it already exists reset duration.

        Args:
            tile (Tile):
            aspect_name(str):
        """
        data = library.get_aspect_data(aspect_name)

        # check if the aspect already exists
        if aspect_name in tile.aspects:
            # reset duration
            tile.aspects[aspect_name].duration = data.duration
        else:
            from scripts.world.aspect import Aspect
            if data.duration:
                tile.aspects[aspect_name] = Aspect(tile, aspect_name, data.duration)
            else:
                tile.aspects[aspect_name] = Aspect(tile, aspect_name)

    @staticmethod
    def remove_aspect_from_tile(tile, aspect_name):
        """
        Aspect is removed from the tile.

        Args:
            tile (Tile):
            aspect_name(str):
        """
        if aspect_name in tile.aspects:
            del tile.aspects[aspect_name]

    @staticmethod
    def trigger_aspects_on_tile(tile):
        """
        Trigger the effect of the Aspect
        """
        # TODO - change to EC approach
        pass
        # if tile.aspects:
        #     for key, aspect in tile.aspects.items():
        #         aspect.trigger()

    @staticmethod
    def reduce_aspect_durations_on_tile(tile):
        """
        Reduce duration of all non-permanent afflictions on an entity.

        Args:
            tile (Tile):
        """
        for key, aspect in tile.aspects.items():
            if aspect.duration is not None:
                aspect.duration -= 1

                log_string = f"({aspect.x},{aspect.y}) {aspect.name}`s duration reduced to " \
                             f" {aspect.duration}"
                logging.debug(log_string)

    @staticmethod
    def cleanse_expired_aspects(tile):
        """
        Delete expired aspects

        Args:
            tile (Tile):
        """
        removed_aspects = []
        expired_aspects = []

        # check if aspects has expired
        for key, aspect in tile.aspects.items():

            # make sure it isnt none before checking duration
            if aspect.duration is not None:
                if aspect.duration <= 0:
                    # log on expired list. Not removing now to avoid amending the currently iterating list
                    expired_aspects.append(aspect)

        # remove all expired aspects from the tile and delete each instance
        # pop removes the element so we keep looking at element 0 and popping it
        index = 0
        while index < len(expired_aspects):
            # get the aspect
            aspect = expired_aspects.pop(index)

            # remove from tile
            del tile.aspects[aspect.name]

            # add info to logging
            removed_aspects.append(f"{aspect.x},{aspect.y}:{aspect.name}")

            # delete the instance
            del aspect

        # if we removed anything log it
        if removed_aspects:
            log_string = f"Removed the following aspects: {removed_aspects}"
            logging.debug(log_string)