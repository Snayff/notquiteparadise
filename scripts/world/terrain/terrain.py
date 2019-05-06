

class Terrain:
    """
        Base terrain class
        """

    def __init__(self, x, y):
        self.blocks_movement = False
        self.blocks_sight = False
        self.sprite = False
        self.is_visible = False
        self.x = x
        self.y = y
        self.name = ""