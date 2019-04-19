import tcod

from scripts.core.colours import Palette, Colour
from scripts.core.constants import BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT, TILE_SIZE, TargetTags
from scripts.ui_elements.templates.panel import Panel
from scripts.world.tiles import Floor, Wall, Tile


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
        self.tiles = [[Floor(y, x) for y in range(0, self.height)] for x in range(0, self.width)]

        if self.width > 10 and self.height > 10:
            self.tiles[0][5] = Wall(0, 5)  # TODO remove - only for test
            self.tiles[10][2] = Wall(10, 2)

        # setup the panel
        panel_x = 0
        panel_y = 0
        panel_width = int((BASE_WINDOW_WIDTH / 4) * 3)
        panel_height = BASE_WINDOW_HEIGHT
        panel_border = 2
        panel_background_colour = Palette().game_map.background
        panel_border_colour = Palette().game_map.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

        # set panel to be rendered
        from scripts.core.global_data import ui_manager
        ui_manager.update_panel_visibility("game_map", self,  True)

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

                if self.is_tile_visible_to_player(x, y):
                    tile_position = (x * TILE_SIZE, y * TILE_SIZE)
                    self.panel.surface.blit(self.tiles[x][y].sprite, tile_position)

        # entities
        for entity in entities:
            if self.is_tile_visible_to_player(entity.x, entity.y):
                from scripts.core.global_data import entity_manager
                if entity_manager.animation_enabled:
                    sprite = entity_manager.animation.get_entity_current_frame(entity)  # TODO - decouple link to
                                                                                        #  entity_manager_methods
                else:
                    sprite = entity.icon

                self.panel.surface.blit(sprite, (entity.x * TILE_SIZE, entity.y * TILE_SIZE))

                # TESTING - show frames
                # font = self.message_log.font
                # font.render_to(self.main_surface, (entity.x * TILE_SIZE, entity.y * TILE_SIZE),
                #                     str(entity.current_sprite_frame), self.colour.white)

        # panel border
        self.panel.draw_panel_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

    def is_tile_blocking_movement(self, tile_x, tile_y):
        """

        Args:
            tile_x:
            tile_y:

        Returns:
            bool:

        """
        if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
            return self.tiles[tile_x][tile_y].blocks_movement
        else:
            return True

    def is_tile_blocking_sight(self, tile_x, tile_y):
        """

        Args:
            tile_x:
            tile_y:

        Returns:
            bool:
        """
        if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
            return self.tiles[tile_x][tile_y].blocks_sight
        else:
            return True

    def update_tile_visibility(self, fov_map):
        """
        Update the player's fov
        Args:
            fov_map:
        """
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.tiles[x][y].is_visible = tcod.map_is_in_fov(fov_map, x, y)

    def is_tile_visible_to_player(self, tile_x, tile_y):
        """

        Args:
            tile_x:
            tile_y:

        Returns:
            bool:
        """
        if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
            return self.tiles[tile_x][tile_y].is_visible
        else:
            return False

    def get_target_type_from_tile(self, tile_x, tile_y):
        """
        Get type of target tile

        Args:
            tile_x(int):  x position of the tile
            tile_y(int):  y position of the tile
        """
        tile = self.tiles[tile_x][tile_y]

        if not self.is_tile_in_bounds(tile_x, tile_y):
            return TargetTags.OUT_OF_BOUNDS

        if type(tile) is Wall:
            return TargetTags.WALL
        elif type(tile) is Floor:
            return TargetTags.FLOOR

    def is_tile_in_bounds(self, tile_x, tile_y):
        """

        Args:
            tile_x:
            tile_y:

        Returns:
            bool:
        """
        if (0 <= tile_x <= self.width) and (0 <= tile_y <= self.height):
            return True
        else:
            return False

    def get_tile(self, tile_x, tile_y):
        """
        Get the tile at the specified location

        Args:
            tile_x(int): x position of tile
            tile_y(int): y position of tile

        Returns:
            Tile: the tile at the location
        """
        # NOTE: It should be Y then X. Do not change not matter how much you want to.
        return self.tiles[tile_y][tile_x]