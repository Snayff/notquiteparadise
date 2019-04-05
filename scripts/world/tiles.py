import pygame

from scripts.core.constants import TILE_SIZE


class Tile:
    def __init__(self):
        self.blocks_movement = False
        self.blocks_sight = False
        self.sprite = False
        self.is_visible = False


class Floor(Tile):
    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load("assets/world/placeholder/_test.png").convert_alpha()

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))


class Wall(Tile):
    def __init__(self):
        super().__init__()
        self.blocks_movement = True
        self.blocks_sight = True
        self.sprite = pygame.image.load("assets/world/placeholder/_testWall.png").convert_alpha()

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))
