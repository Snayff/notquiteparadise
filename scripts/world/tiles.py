import pygame

class Tile:
    def __init__(self):
        self.blocks_movement = False
        self.blocks_sight = False
        self.sprite = False
        self.is_visible = False


class Floor(Tile):
    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load("assets/world/floor.png")


class Wall(Tile):
    def __init__(self):
        super().__init__()
        self.blocks_movement = True
        self.blocks_sight = True
        self.sprite = pygame.image.load("assets/world/wall.png")
