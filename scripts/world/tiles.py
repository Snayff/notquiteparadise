import pygame

from scripts.core.constants import TILE_SIZE


class Tile:
    def __init__(self, x, y):
        self.blocks_movement = False
        self.blocks_sight = False
        self.sprite = False
        self.is_visible = False
        self.x = x
        self.y = y
        self.name = ""


class Floor(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "floor tile"
        self.sprite = pygame.image.load("assets/world/placeholder/_test.png").convert_alpha()

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))


class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.blocks_movement = True
        self.blocks_sight = True
        self.name = "wall tile"
        self.sprite = pygame.image.load("assets/world/placeholder/_testWall.png").convert_alpha()

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))
