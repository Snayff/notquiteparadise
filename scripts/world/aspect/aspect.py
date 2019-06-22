from scripts.world.tile import Tile


class Aspect:
    """
    The Aspect of a Tile, such as smoke or fire
    
    Attributes:
        owner(Tile):
        blocks_movement(bool):
        blocks_sight(bool):
        sprite(pygame.Sprite):
        name(str):
        
    """
    def __init__(self):
        self.owner = None  # type: Tile
        self.blocks_movement = False
        self.blocks_sight = False
        self.sprite = None
        self.name = ""
        self.aspect_type = None

    @property
    def x(self):
        """
        Get the tile_x of the Aspect.

        Returns:

        """
        return self.owner.x

    @property
    def y(self):
        """
        Get the tile_y of the Aspect.

        Returns:

        """
        return self.owner.y