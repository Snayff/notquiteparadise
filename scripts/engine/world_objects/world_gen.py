from scripts.engine.world_objects.world_gen_algorithms import RoomAddition
from scripts.engine import utility, library
from scripts.engine.world_objects.tile import Tile
from scripts.engine.core.constants import TILE_SIZE
from typing import List, Tuple, Dict, Set, Any


class DungeonGeneration:

    generation_algorithms = {
        'room_addition': RoomAddition,
    }

    def __init__(self, seed: int, algorithm_name: str, width: int, height: int):
        self.floor_sprite_path = "assets/world/placeholder/_test.png"
        self.wall_sprite_path = "assets/world/placeholder/_testWall.png"
        self.floor_sprite = utility.get_image(self.floor_sprite_path, (TILE_SIZE, TILE_SIZE))
        self.wall_sprite = utility.get_image(self.wall_sprite_path, (TILE_SIZE, TILE_SIZE))
        self.algorithm_name = algorithm_name
        self.seed = seed
        self.width = width
        self.height = height
        self.min_room_space = library.GAME_CONFIG.world_values.min_room_space
        self.algorithm = self._create_algorithm()
        self.tiles: List[List[Tile]] = \
            [[Tile(x, y, self.floor_sprite, self.floor_sprite_path)
                for y in range(self.height)] for x in range(self.width)]

    def _create_algorithm(self):
        """
        Create the algorithm to be used from the name
        """
        return DungeonGeneration.generation_algorithms[self.algorithm_name](
            self.min_room_space
        )

    # def generate(self) -> Tuple[List[List[Tile]], List[Tuple[Tuple[int, int], List[List[int]]]],
    # List[Tuple[Tuple[int, int], Tuple[int, int], int]]]:
    #     """
    #     Generate the map using the specified algorithm
    #     """
    #     self.algorithm.generate_level(self.seed, self.width, self.height)
    #
    #     for x in range(self.width):
    #         for y in range(self.height):
    #             # Is this a wall? Or is this a border?
    #             if self.algorithm.level[x][y] == 1 or self._is_map_border(x, y):
    #                 self._make_wall(x, y)
    #     return self.tiles, self.algorithm.rooms, self.algorithm.tunnels

    # def generate_steps(self):
    #     """
    #     Generates the map using the specified algorithm, returning each step of the generation
    #     :return: The state of the map at a step
    #     """
    #     algorithm = self._create_algorithm()
    #     for step in algorithm.generate_level_steps(self.seed, self.width, self.height):
    #         yield step

    # def _is_map_border(self, x: int, y: int) -> bool:
    #     """
    #     Returns a bool that represents if this is a map border
    #     """
    #     border_size = 4
    #
    #     if (x <= border_size or x >= (self.width - border_size)) or (y <= border_size or y >=
    #                                                                  (self.height - border_size)):
    #         return True
    #     else:
    #         return False

    # def _make_wall(self, x: int, y: int):
    #     """
    #     Makes the tile at the coordinate a wall
    #     """
    #     self.tiles[x][y].blocks_sight = True
    #     self.tiles[x][y].blocks_movement = True
    #     self.tiles[x][y].sprite = self.wall_sprite
    #     self.tiles[x][y].sprite_path = self.wall_sprite_path

    # def visualize(self):
    #     pass

    # def get_gen_info(self) -> Dict[str, Any]:
    #     """
    #     Returns the generation parameters
    #     :return: A dict with the parameters
    #     """
    #     return {
    #         'seed': self.seed,
    #         'algorithm': self.algorithm_name,
    #         'width': self.width,
    #         'height': self.height,
    #         'min_room_space': self.min_room_space,
    #     }
