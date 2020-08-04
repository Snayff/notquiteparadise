from __future__ import annotations
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List
    from scripts.engine.world_objects.tile import Tile


def generate(seed: int, algorithm, width: int, height: int, ) -> Tuple[List[List[Tile]], 
List[Tuple[Tuple[int, int], List[List[int]]]], List[Tuple[Tuple[int, int], Tuple[int, int], int]]]:
    """
    Generate the map using the specified algorithm
    """
    algorithm.generate_level(seed, width, height)

    for x in range(width):
        for y in range(height):
            # Is this a wall? Or is this a border?
            if algorithm.level[x][y] == 1 or _is_map_border(x, y):
                _make_wall(x, y)
    return tiles, algorithm.rooms, algorithm.tunnels


def _is_map_border(width: int, height: int, x: int, y: int) -> bool:
    """
    Returns a bool that represents if this is a map border
    """
    border_size = 4

    if (x <= border_size or x >= (width - border_size)) or (y <= border_size or y >=
                                                                 (height - border_size)):
        return True
    else:
        return False


def _make_wall(x: int, y: int):
    """
    Makes the tile at the coordinate a wall
    """
    self.tiles[x][y].blocks_sight = True
    self.tiles[x][y].blocks_movement = True
    self.tiles[x][y].sprite = self.wall_sprite
    self.tiles[x][y].sprite_path = self.wall_sprite_path


def generate_steps(algorithm, seed: int, width: int, height: int):
    """
    Generates the map using the specified algorithm, returning each step of the generation
    :return: The state of the map at a step
    """
    algorithm = self._create_algorithm()
    for step in algorithm.generate_level_steps(seed, width, height):
        yield step
