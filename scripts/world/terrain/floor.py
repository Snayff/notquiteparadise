import pygame

from scripts.core.constants import TILE_SIZE
from scripts.world.terrain.terrain import Terrain


class Floor(Terrain):
    """
    Floor tile, doesnt block movement or sight
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "floor tile"
        self.sprite = pygame.image.load("assets/world/placeholder/_test.png").convert_alpha()

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))