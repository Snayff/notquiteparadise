
from scripts.core.constants import TargetTags, TILE_SIZE
from scripts.world.game_map import GameMap
from scripts.world.terrain.floor import Floor
from scripts.world.terrain.wall import Wall
from scripts.world.tile import Tile


class MapMethods:
    """
    Methods for querying game map and game map related info and taking game map actions.
    """
    def __init__(self, manager):
        self.manager = manager

    def get_game_map(self):
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

        if (0 <= tile_x <= game_map.width) and (0 <= tile_y <= game_map.height):
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

    def create_new_map(self, width, height):
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
            if active_entity != tile.entity:
                return True
            else:
                return False
        elif target_tag == TargetTags.NO_ENTITY:
            return not tile.has_entity
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
    def set_aspect_on_tile(tile, aspect):
        """
        Set the new aspect on the tile.

        Args:
            tile ():
            aspect:
        """
        tile.aspect = aspect
        tile.aspect.owner = tile

    @staticmethod
    def trigger_aspect_effect_on_tile(tile):
        """
        Trigger the effect of the Aspect
        """
        if tile.aspect:
            tile.aspect.trigger()

