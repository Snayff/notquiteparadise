import pygame

from scripts.ui.templates.panel import Panel
from scripts.core.constants import VisualInfo, TILE_SIZE
from scripts.ui.basic.colours import Colour
from scripts.ui.basic.palette import Palette


class Camera:
    """
    Hold the visual info for the Game Map
    """

    def __init__(self):
        self.tiles_to_draw = []  # the tiles passed from the GameMap to draw
        self.is_visible = False

        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10
        self.edge_size = 3

        # setup the panel
        panel_x = 0
        panel_y = 0
        panel_width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 3)
        panel_height = VisualInfo.BASE_WINDOW_HEIGHT
        panel_border = 2
        panel_background_colour = Palette().game_map.background
        panel_border_colour = Palette().game_map.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)
        self.rect = pygame.rect.Rect(self.x, self.y, panel_width, panel_height)

    def draw(self, surface):
        """
        Draw the tiles in view

        Args:
            surface(Surface): Surface to draw to

        """
        # panel background
        self.panel.surface.fill(Colour().black)
        self.panel.draw_background()

        self.draw_cameras_tiles()

        # panel border
        self.panel.draw_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

    def draw_cameras_tiles(self):
        """
        Draw the game map on the panel surface
        """
        # TODO - draw visible only
        tiles = self.tiles_to_draw

        y_pos = 0
        x_pos = 0

        for x in range(0, len(tiles)):
            tile = tiles[x]

            if y_pos >= self.height:
                y_pos = 0
                x_pos += 1

            draw_position = (x_pos * TILE_SIZE, y_pos * TILE_SIZE)

            if tile.terrain:
                self.panel.surface.blit(tile.terrain.sprite, draw_position)

            if tile.entity:
                self.panel.surface.blit(tile.entity.icon, draw_position)

            if tile.aspects:
                for key, aspect in tile.aspects.items():
                    self.panel.surface.blit(aspect.sprite, draw_position)

            y_pos += 1


# Camera class from pygame tutorial
# class obj_Camera:
#
#     def __init__(self):
#
#         self.width = constants.CAMERA_WIDTH
#         self.height = constants.CAMERA_HEIGHT
#         self.x, self.y = (0, 0)
#
#     @property
#     def rectangle(self):
#
#         pos_rect = pygame.Rect((0, 0), (constants.CAMERA_WIDTH,
#                                         constants.CAMERA_HEIGHT))
#
#         pos_rect.center = (self.x, self.y)
#
#         return pos_rect
#
#     @property
#     def map_address(self):
#
#         map_x = self.x / constants.CELL_WIDTH
#         map_y = self.y / constants.CELL_HEIGHT
#
#         return (map_x, map_y)
#
#     def update(self):
#
#         target_x = PLAYER.x * constants.CELL_WIDTH + (constants.CELL_WIDTH/2)
#         target_y = PLAYER.y * constants.CELL_HEIGHT + (constants.CELL_HEIGHT/2)
#
#         distance_x, distance_y = self.map_dist((target_x, target_y))
#
#         self.x += int(distance_x)
#         self.y += int(distance_y)
#
#     def win_to_map(self, coords):
#
#         tar_x, tar_y = coords
#
#         #convert window coords to distace from camera
#         cam_d_x, cam_d_y = self.cam_dist((tar_x, tar_y))
#
#         #distance from cam -> map coord
#         map_p_x = self.x + cam_d_x
#         map_p_y = self.y + cam_d_y
#
#         return((map_p_x, map_p_y))
#
#
#     def map_dist(self, coords):
#
#         new_x, new_y = coords
#
#         dist_x = new_x - self.x
#         dist_y = new_y - self.y
#
#         return (dist_x, dist_y)
#
#     def cam_dist(self, coords):
#
#         win_x, win_y = coords
#
#         dist_x = win_x - (self.width / 2)
#         dist_y = win_y - (self.height / 2)
#
#         return (dist_x, dist_y)

