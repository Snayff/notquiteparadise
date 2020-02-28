from typing import List

import pygame

from scripts.core import utilities
from scripts.core.constants import TILE_SIZE
from scripts.managers.game_manager.game_manager import game
from scripts.world.tile import Tile


class GameMap:
    """
    object to hold tile and fov
    """
    def __init__(self, width, height):
        self.tiles = []  # type: List[List[Tile]]
        self.width = width
        self.height = height

        floor_sprite = utilities.get_image("assets/world/placeholder/_test.png", (TILE_SIZE, TILE_SIZE))
        wall_sprite = utilities.get_image("assets/world/placeholder/_testWall.png", (TILE_SIZE, TILE_SIZE))

        # populate map with tiles
        for x in range(self.width):
            # give each new row an empty list
            self.tiles.append([])
            for y in range(self.height):
                # add to the column
                self.tiles[x].append(Tile(x, y, floor_sprite))

        # create some walls for testing
        wall1 = self.tiles[3][4]
        wall1._blocks_sight = True
        wall1._blocks_movement = True
        wall1.sprite = wall_sprite