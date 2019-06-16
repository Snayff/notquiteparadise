import tcod

from scripts.ui_elements.colours import Colour
from scripts.ui_elements.palette import Palette
from scripts.core.constants import BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT, TargetTags
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
            self.tiles[0][5].set_terrain(Wall())
            self.tiles[10][2].set_terrain(Wall())
            self.tiles[0][2].set_aspect(Bog())

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
        from scripts.global_instances.managers import ui_manager
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

                if self.is_tile_visible_to_player(x, y):
                    self.tiles[x][y].draw(self.panel.surface)

        # panel border
        self.panel.draw_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

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
        Update the player`s fov
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

        if type(tile.terrain) is Wall:
            return TargetTags.WALL
        elif type(tile.terrain) is Floor:
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
        return self.tiles[tile_x][tile_y]

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