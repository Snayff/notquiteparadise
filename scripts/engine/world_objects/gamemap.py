from __future__ import annotations

from typing import List
from scripts.engine.world_objects.world_gen import DungeonGeneration
from scripts.engine.world_objects.tile import Tile


class GameMap:
    """
    object to hold tile and fov
    """
    def __init__(self, seed: int, algorithm_name: str, width: int, height: int):
        self.tiles: List[List[Tile]] = []
        self.rooms: List[List[List[int]]] = []
        self.width = width
        self.height = height
        self.seed = seed
        self.world_gen = DungeonGeneration(seed, algorithm_name, width, height)
        tiles, rooms = self.world_gen.generate()
        self.tiles = tiles
        self.rooms = rooms



