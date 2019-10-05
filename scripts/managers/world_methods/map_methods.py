import logging

from scripts.core.constants import TargetTags, TILE_SIZE
from scripts.world.game_map import GameMap
from scripts.world.terrain.floor import Floor
from scripts.world.terrain.wall import Wall
from scripts.world.tile import Tile
from typing import List, Tuple
from scripts.global_singletons.data_library import library


class MapMethods:
    """
    Methods for querying game map and game map related info and taking game map actions.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """
    def __init__(self, manager):
        from scripts.managers.world_manager import WorldManager
        self.manager = manager  # type: WorldManager

    def get_game_map(self) -> GameMap:
        """
        Get current game_map

        Returns:
            GameMap
        """
        return self.manager.game_map

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

        if type(tile.terrain) is Wall:
            return TargetTags.WALL
        elif type(tile.terrain) is Floor:
            return TargetTags.FLOOR

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

    def get_tile(self, tile_x, tile_y):
        """
        Get the tile at the specified location

        Args:
            tile_x(int): x position of tile
            tile_y(int): y position of tile

        Returns:
            Tile: the tile at the location
        """
        game_map = self.get_game_map()

        return game_map.tiles[tile_x][tile_y]

    def get_tiles(self, start_tile_x, start_tile_y, coords):
        """
        Get multiple tiles based on starting position and coordinates given

        Args:
            start_tile_x (int):
            start_tile_y (int):
            coords (list[Tuple]): List of tuples holding x y. E.g. (x, y)

        Returns:
            List[Tile]:
        """
        game_map = self.get_game_map()
        tiles = []

        for coord in coords:
            tile_x = coord[0] + start_tile_x
            tile_y = coord[1] + start_tile_y

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

    @staticmethod
    def convert_xy_to_tile(x, y):
        """
        Convert an x y position to a tile ref

        Args:
            x:
            y:

        Returns :
            Tuple[int, int]

        """
        tile_x = int(x / TILE_SIZE)
        tile_y = int(y / TILE_SIZE)

        return tile_x, tile_y

    def create_game_map(self, width, height):
        """
        Create new GameMap and create player FOV
        """
        self.manager.game_map = GameMap(width, height)

    @staticmethod
    def tile_has_tag(tile, target_tag, active_entity=None):
        """
        Check if a given tag applies to the tile

        Args:
            tile ():
            target_tag (TargetTags): tag to check
            active_entity (Entity): entity using a skill

        Returns:
            bool: True if tag applies.
        """
        if target_tag == TargetTags.FLOOR:
            return tile.is_floor
        elif target_tag == TargetTags.WALL:
            return tile.is_wall
        elif target_tag == TargetTags.SELF:
            # ensure active entity is the same as the targeted one
            if active_entity == tile.entity:
                return True
            else:
                return False
        elif target_tag == TargetTags.OTHER_ENTITY:
            # ensure active entity is NOT the same as the targeted one
            if active_entity != tile.entity and tile.has_entity:
                return True
            else:
                return False
        elif target_tag == TargetTags.NO_ENTITY:
            return not tile.has_entity
        elif target_tag == TargetTags.ANY:
            return True
        else:
            return False  # catch all

    @staticmethod
    def set_entity_on_tile(tile, entity):
        """
        Set the new entity on the tile.

        Args:
            tile ():
            entity:
        """
        tile.entity = entity
        if entity:
            tile.entity.owner = tile

    @staticmethod
    def get_entity_on_tile(tile):
        """
        Get the entity from the Tile

        Returns:
            Entity: The Entity on the tile

        """
        return tile.entity

    @staticmethod
    def set_terrain_on_tile(tile, terrain):
        """
        Set the new terrain on the tile.

        Args:
            tile (Tile):
            terrain (TargetTags):
        """
        new_terrain = None

        if terrain == TargetTags.WALL:
            new_terrain = Wall()
        elif terrain == TargetTags.FLOOR:
            new_terrain = Floor()

        if new_terrain:
            tile.terrain = new_terrain
            tile.terrain.owner = tile

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
        if tile.aspects:
            for key, aspect in tile.aspects.items():
                aspect.trigger()

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