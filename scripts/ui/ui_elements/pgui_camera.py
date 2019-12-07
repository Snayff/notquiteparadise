import logging
import pygame
import pygame_gui
from typing import List
from pygame_gui.core import UIWindow, UIContainer
from pygame_gui.elements import UIButton, UIImage
from scripts.core.constants import TILE_SIZE, UIElementTypes


class PguiCamera(UIWindow):
    """
    Hold the visual info for the Game Map
    """

    def __init__(self, rect: pygame.Rect, manager: pygame_gui.ui_manager.UIManager, rows: int, cols: int):
        # general info
        self.rows = rows
        self.columns = cols
        self.start_tile_col = 0
        self.start_tile_row = 0
        self.edge_size = 3  # # of tiles to control camera movement

        # game map info
        self.player_cell = None  # the tile in which the player resides
        self.tiles = []

        # overlay info
        self.is_overlay_visible = False
        self.overlay_directions = []  # hold list of cardinal directions to show in the overlay

        # grid info
        self.selected_tile = None  # the tile in the grid currently being selected

        # complete base class init
        super().__init__(rect, manager, ["camera"])

        # TODO - add overlay for skill use (could this be the grid?)

        # create game map
        blank_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        self.game_map = UIImage(relative_rect=rect, image_surface=blank_surf, manager=manager,
                                container=self.get_container(), object_id="#game_map")

        # create grid
        self.grid = UIContainer(relative_rect=rect, manager=manager,  container=self.get_container(),
                                object_id="grid")

        from scripts.managers.ui_manager import ui  # imported locally to prevent circular import
        ui.Element.pgui_elements[UIElementTypes.CAMERA_GRID.name] = self.grid

        # create tiles in grid
        for row in range(0, rows):
            for col in range(0, cols):
                tile_rect = pygame.Rect(TILE_SIZE * col, TILE_SIZE * row, TILE_SIZE, TILE_SIZE)
                tile = UIButton(relative_rect=tile_rect, manager=manager, text="", container=self.grid,
                                parent_element=self.grid, object_id=f"#tile({row},{col})")

        # TODO - amend grid
        #  allow being rebuiilt
        #  only created in range of fov (for now...)
        #  use start tile rather than 0, to start tile + row/col

        # confirm init complete
        logging.debug(f"Camera initialised.")

    def update_game_map(self):
        rows = self.rows
        cols = self.columns

        # create new surface for the game map
        map_width = self.game_map.rect.width
        map_height = self.game_map.rect.height
        map_surf = pygame.Surface((map_width, map_height), pygame.SRCALPHA)

        # prep for loop
        tile_width = int(map_width / cols)
        tile_height = int(map_height / rows)

        tiles = self.tiles

        # blit all tiles info to the new surface
        for tile in tiles:

            x = (tile.x - self.start_tile_col) * tile_width
            y = (tile.y - self.start_tile_row) * tile_height

            if tile.terrain:
                map_surf.blit(tile.terrain.sprite, (x, y))

            if tile.entity:
                map_surf.blit(tile.entity.icon, (x, y))

            if tile.aspects:
                for key, aspect in tile.aspects.items():
                    map_surf.blit(aspect.sprite, (x, y))

        self.game_map.image = map_surf

    def update_grid(self):

        # clear existing grid tiles
        self.grid.clear()

        # prep for loop
        rows = self.rows
        cols = self.columns
        map_width = self.game_map.rect.width
        map_height = self.game_map.rect.height
        tile_width = int(map_width / cols)
        tile_height = int(map_height / rows)
        manager = self.ui_manager
        tiles = self.tiles

        # blit all tiles info to the new surface
        for tile in tiles:
            x = (tile.x - self.start_tile_col) * tile_width
            y = (tile.y - self.start_tile_row) * tile_height

            # get current row and col
            if y == 0:
                row = 0
            else:
                row = int(y / tile_height)
            if x == 0:
                col = 0
            else:
                col = int(x / tile_width)

            tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            tile = UIButton(relative_rect=tile_rect, manager=manager, text="", container=self.grid,
                            parent_element=self.grid, object_id=f"#tile({row},{col})")


    def set_tiles(self, tiles: List):
        self.tiles = tiles
