import logging

import pygame

from scripts.core.constants import VisualInfo, InputStates, TILE_SIZE
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.frame import Frame
from scripts.ui.templates.grid import Grid
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class NewCamera(UIElement):
    """
    Hold the visual info for the Game Map
    """

    def __init__(self):

        self.rows = 10
        self.columns = 10
        self.start_tile_x = 0
        self.start_tile_y = 0
        self.edge_size = 3  # # of tiles to control camera movement

        # size and position
        width = TILE_SIZE * self.columns
        height = TILE_SIZE * self.rows
        x = 0
        y = 2
        cell_gap = 2
        edge = 5

        # create style
        palette = Palette().camera
        font = Font().camera
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2

        # create grid's children
        grid_rows = self.rows
        grid_columns = self.columns
        grid_children = []

        for row in range(0, grid_rows):
            for col in range(0, grid_columns):
                base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                         font_colour=font_colour, border_size=border_size)
                frame = Frame(base_style=base_style, name=f"cell{row},{col}")
                grid_children.append(frame)

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)

        # create child Grid
        children = []
        grid = Grid(base_style, edge, edge, width - (edge * 2), height - (edge * 2), grid_children, "grid",
                    grid_rows, grid_columns, cell_gap)
        children.append(grid)

        # complete base class init
        super().__init__(base_style, x, y, width, height, children)

        # confirm init complete
        logging.debug(f"Camera initialised.")

    def update(self):
        """
        Ensure all the children update in response to changes.
        """
        super().update()

    def draw(self, main_surface):
        """
        Draw the skill bar.

        Args:
            main_surface ():
        """
        super().draw(self.surface)

        # blit to the main surface
        main_surface.blit(self.surface, (self.rect.x, self.rect.y))

    def handle_input(self, input_key, input_state: InputStates = InputStates.PRESSED):
        """
        Process received input

        Args:
            input_key (): input received. Mouse, keyboard, gamepad.
            input_state (): pressed or released
        """

        pass

    def set_cell_background_image(self, row: int, col: int, image: pygame.Surface):
        """
        Set the background image of a cell in the camera

        Args:
            row ():
            col ():
            image ():
        """
        cell = self.get_child(f"cell{row},{col}")

        if cell:
            cell.base_style.background_image = image
            cell.is_dirty = True


# TODO - add targeting overlay