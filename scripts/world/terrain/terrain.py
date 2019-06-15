

class Terrain:
    """
        Base terrain class

        Attributes:
            owner(Tile):
            blocks_movement(bool):
            blocks_sight(bool):
            sprite(pygame.Sprite):
            name(str):

        """

    def __init__(self):
        self.owner = None
        self.blocks_movement = False
        self.blocks_sight = False
        self.sprite = None
        self.name = ""

    @property
    def x(self):
        """
        Get the tile_x of the Terrain.

        Returns:

        """
        return self.owner.x

    @property
    def y(self):
        """
        Get the tile_y of the Terrain.

        Returns:

        """
        return self.owner.y