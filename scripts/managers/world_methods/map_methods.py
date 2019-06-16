import tcod

from scripts.core.constants import TargetTags, TILE_SIZE
from scripts.world.game_map import GameMap
from scripts.world.terrain.floor import Floor
from scripts.world.terrain.wall import Wall


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

    def update_tile_visibility(self, fov_map):
        """
        Update the player`s fov

        Args:
            fov_map:
        """
        game_map = self.get_game_map()

        for x in range(0, game_map.width):
            for y in range(0, game_map.height):
                game_map.tiles[x][y].is_visible = tcod.map_is_in_fov(fov_map, x, y)

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