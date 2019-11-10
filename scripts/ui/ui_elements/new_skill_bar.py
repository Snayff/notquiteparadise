import logging

import pygame

from scripts.core.constants import InputStates, VisualInfo
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.frame import Frame
from scripts.ui.templates.grid import Grid
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class NewSkillBar(UIElement):
    """
    Display and hold the info for the skills in the skill bar.
    """

    def __init__(self):
        # size and position
        width = 80
        height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        x = VisualInfo.BASE_WINDOW_WIDTH - width
        y = 2

        # create style
        palette = Palette().skill_bar
        font = Font().skill_bar
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)

        # create grid's children
        grid_rows = 5
        grid_columns = 1
        grid_children = []
        img = pygame.image.load("assets/icons/placeholder/book.PNG").convert_alpha()
        for skill_number in range(0, grid_rows + grid_columns):
            frame = Frame(base_style=base_style, name=f"skill{skill_number}", image=img)
            grid_children.append(frame)

        # create child Grid
        children = []
        cell_gap = 2
        edge = 5
        # x: int, y: int, width: int, height: int, base_style: WidgetStyle, children: List = [],
        #             name: str = "frame", rows: int = 1, columns: int = 1, gap_between_cells: int = 2
        grid = Grid(base_style, edge, edge, width - (edge * 2), height - (edge * 2), grid_children, "grid",
                    grid_rows, grid_columns, cell_gap)
        children.append(grid)

        # complete base class init
        super().__init__(x, y, width, height, base_style, children)

        # confirm init complete
        logging.debug(f"EntityInfo initialised.")

    def handle_input(self, input_key, input_state: InputStates = InputStates.PRESSED):
        pass