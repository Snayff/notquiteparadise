

class Terrain:
    """
        Base terrain class
        """

    def __init__(self):
        self.blocks_movement = False
        self.blocks_sight = False
        self.sprite = False
        self.name = ""

    @property
    def x(self):
        """
        Get the tile_x of the Entity.

        Returns:

        """
        return self.owner.x

    @property
    def y(self):
        """
        Get the tile_y of the Entity.

        Returns:

        """
        return self.owner.y