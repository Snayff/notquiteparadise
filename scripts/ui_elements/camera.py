
from scripts.ui_elements.templates.panel import Panel
from scripts.core.constants import VisualInfo, TILE_SIZE
from scripts.ui_elements.colours import Colour
from scripts.ui_elements.palette import Palette


class Camera:
    """
    Hold the visual info for the Game Map
    """

    def __init__(self):
        self.tiles_to_draw = []  # the tile passed from the GameMap to draw
        self.is_visible = False
        self.rows_in_view_from_centre = 5
        self.cols_in_view_from_centre = 5

        # TODO - add centre pos and tolerance around that, update when exceeding tolerance area so camera centres on
        #  that and not the player.

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
        for x in range(0, len(self.tiles_to_draw)):
            self.draw_tile(self.tiles_to_draw[x])

    def draw_tile(self, tile):
        """
        Draw the tile on the panel surface

        Args:
            tile (Tile):
        """

        from scripts.global_singletons.managers import world_manager
        player = world_manager.player
        draw_position = ((tile.x - player.x) * TILE_SIZE, (tile.y - player.y) * TILE_SIZE)

        if tile.terrain:
            self.panel.surface.blit(tile.terrain.sprite, draw_position)

        if tile.entity:
            self.panel.surface.blit(tile.entity.icon, draw_position)

        if tile.aspects:
            for key, aspect in tile.aspects.items():
                self.panel.surface.blit(aspect.sprite, draw_position)

