from scripts.world.tiles import Floor, Wall


class GameMap:
    """
    object to hold tile and fov
    """
    def __init__(self, width, height):
        self.tiles = []
        self.width = width
        self.height = height

        # populate map with floor tiles
        # N.B. the inner list should be the height which would mean that the first referenced index in list[][] is y.
        # Stop getting it wrong.
        self.tiles = [[Floor() for y in range(0, self.height)] for x in range(0, self.width)]

        self.tiles[0][5] = Wall()  # TODO remove - only for test
        self.tiles[10][2] = Wall()

    def tile_is_blocking_movement(self, x, y):
        return self.tiles[x][y].blocks_movement

    def tile_is_blocking_sight(self, x, y):
        return self.tiles[x][y].blocks_sight

