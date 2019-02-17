import tcod

from scripts.core.colours import Palette
from scripts.core.constants import BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT
from scripts.ui_element.panel import Panel
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

        if self.width > 10 and self.height > 10:
            self.tiles[0][5] = Wall()  # TODO remove - only for test
            self.tiles[10][2] = Wall()

        # setup the panel
        panel_x = 0
        panel_y = 0
        panel_width = BASE_WINDOW_WIDTH
        panel_height = int(BASE_WINDOW_HEIGHT / 3) * 2
        panel_border = 2
        palette = Palette()
        panel_colour = palette.map.background
        border_colour = palette.map.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_colour, panel_border, border_colour)


    def is_tile_blocking_movement(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[x][y].blocks_movement
        else:
            return True

    def is_tile_blocking_sight(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[x][y].blocks_sight
        else:
            return True

    def update_tile_visibility(self, fov_map):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.tiles[x][y].is_visible = tcod.map_is_in_fov(fov_map, x, y)

    def is_tile_visible(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[x][y].is_visible
        else:
            return False