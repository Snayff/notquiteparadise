from scripts.core.constants import SPRITE_FLOOR, SPRITE_WALL


class Tile:
    def __init__(self):
        self.blocks_movement = False
        self.blocks_sight = False
        self.sprite = False
        self.is_visible = False


class Floor(Tile):
    def __init__(self):
        super().__init__()
        self.sprite = SPRITE_FLOOR


class Wall(Tile):
    def __init__(self):
        super().__init__()
        self.blocks_movement = True
        self.blocks_sight = True
        self.sprite = SPRITE_WALL
