import tcod

from scripts.core.colours import Palette, Colour
from scripts.core.constants import BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT, TILE_SIZE
from scripts.ui_elements.templates.panel import Panel
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
        panel_background_colour = Palette().map.background
        panel_border_colour = Palette().map.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

        # set panel to be rendered
        from scripts.core.global_data import ui_manager
        ui_manager.update_panel_visibility("game_map", self.panel, True)

    def draw(self, entities, surface):
        """
        Draw the specified game_map

        Args:
            entities(list[Entity]): List of entities
            surface(Surface): Surface to draw to

        """
        # panel background
        self.panel.surface.fill(Colour().black)
        self.panel.draw_background()

        # tiles
        for x in range(0, self.width):
            for y in range(0, self.height):

                if self.is_tile_visible(x, y):
                    tile_position = (x * TILE_SIZE, y * TILE_SIZE)
                    self.panel.surface.blit(self.tiles[x][y].sprite, tile_position)

        # entities
        for entity in entities:
            if self.is_tile_visible(entity.x, entity.y):
                from scripts.core.global_data import entity_manager
                sprite = entity_manager.get_entity_current_frame(entity)  # TODO - decouple link to entity_manager
                self.panel.surface.blit(sprite, (entity.x * TILE_SIZE, entity.y * TILE_SIZE))

                # TESTING - show frames
                # font = self.message_log.font
                # font.render_to(self.main_surface, (entity.x * TILE_SIZE, entity.y * TILE_SIZE),
                #                     str(entity.current_sprite_frame), self.colour.white)

        # panel border
        self.panel.draw_panel_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

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