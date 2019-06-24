import tcod

from scripts.ui_elements.colours import Colour
from scripts.ui_elements.palette import Palette
from scripts.core.constants import TargetTags, VisualInfo
from scripts.ui_elements.templates.panel import Panel
from scripts.world.aspect.bog import Bog
from scripts.world.tile import Tile
from scripts.world.terrain.floor import Floor
from scripts.world.terrain.wall import Wall


class GameMap:
    """
    object to hold tile and fov
    """
    def __init__(self, width, height):
        self.tiles = []
        self.width = width
        self.height = height

        # populate map with floor terrain
        for x in range(self.width):
            # give each new row an empty list
            self.tiles.append([])
            for y in range(self.height):
                # add to the column
                self.tiles[x].append(Tile(x, y, terrain=Floor()))

        # TODO remove - only for test
        if self.width > 10 and self.height > 10:
            from scripts.global_singletons.managers import world_manager
            world_manager.Map.set_terrain_on_tile(self.tiles[0][5], Wall())
            world_manager.Map.set_terrain_on_tile(self.tiles[10][2], Wall())
            world_manager.Map.set_aspect_on_tile(self.tiles[0][2], Bog())

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

        # set panel to be rendered
        from scripts.global_singletons.managers import ui_manager
        ui_manager.update_panel_visibility("game_map", self,  True)

    def draw(self, surface):
        """
        Draw the specified game_map

        Args:
            surface(Surface): Surface to draw to

        """
        # panel background
        self.panel.surface.fill(Colour().black)
        self.panel.draw_background()

        # terrain
        for x in range(0, self.width):
            for y in range(0, self.height):

                from scripts.global_singletons.managers import world_manager
                if world_manager.Map.is_tile_visible_to_player(x, y):
                    self.tiles[x][y].draw(self.panel.surface)

        # panel border
        self.panel.draw_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

