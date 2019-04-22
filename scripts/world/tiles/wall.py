import pygame

from scripts.core.constants import TILE_SIZE
from scripts.world.tiles.tile import Tile


class Wall(Tile):
    """
    Wall tile, blocks movement and sight.
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.blocks_movement = True
        self.blocks_sight = True
        self.name = "wall tile"
        self.sprite = pygame.image.load("assets/world/placeholder/_testWall.png").convert_alpha()

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))