
from scripts.ui_elements.templates.panel import Panel
from scripts.core.constants import VisualInfo
from scripts.ui_elements.colours import Colour
from scripts.ui_elements.palette import Palette


class Camera:
    """
    Hold the visual info for the Game Map
    """

    def __init__(self):
        self.tiles_to_draw = []  # the tile passed from the GameMap to draw

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

        # tiles
        for x in range(0, len(self.tiles_to_draw)):
            for y in range(0, len(self.tiles_to_draw)):

                from scripts.global_singletons.managers import world_manager
                if world_manager.Map.is_tile_visible_to_player(x, y):
                    # TODO - move the draw out of the tile
                    self.tiles[x][y].draw(self.panel.surface)

        # panel border
        self.panel.draw_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

