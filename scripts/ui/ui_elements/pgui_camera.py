import logging
import pygame
from typing import List

import pygame_gui
from pygame_gui.core import UIWindow

from scripts.core.constants import VisualInfo, InputStates, TILE_SIZE, Directions, UIElementTypes
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.frame import Frame
from scripts.ui.templates.grid import Grid
from scripts.ui.templates.text_box import TextBox
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


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

        # TODO - need to add a game map for terrain, aspect, entity
        # TODO - add invisible grid for identifying where the mouse is
        # TODO - add overlay for skill use (could this be the grid?)

        # create game map
        blank_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        self.game_map = pygame_gui.elements.UIImage(relative_rect=rect, image_surface=blank_surf, manager=manager,
                                                    container=self.get_container(), object_id="#game_map")

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
            print(f"{x},{y}")

            if tile.terrain:
                map_surf.blit(tile.terrain.sprite, (x, y))

            if tile.entity:
                map_surf.blit(tile.entity.icon, (x, y))

            if tile.aspects:
                for key, aspect in tile.aspects.items():
                    map_surf.blit(aspect.sprite, (x, y))

        self.game_map.image = map_surf

    def set_tiles(self, tiles: List):
        self.tiles = tiles
