import logging

import pygame

from scripts.core.constants import InputStates, VisualInfo
from scripts.global_singletons.data_library import library
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
        # state info
        self.skills = []
        self.max_skills = 5
        for skill_slot in range(0, self.max_skills):
            self.skills += [None]

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

        # create grid's children
        grid_rows = self.max_skills
        grid_columns = 1
        grid_children = []

        for skill_number in range(0, grid_rows + grid_columns):
            base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                     font_colour=font_colour, border_size=border_size)
            # TODO - convert to text box to add skill number/hotkey
            frame = Frame(base_style=base_style, name=f"skill{skill_number}")
            grid_children.append(frame)

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)
        # create child Grid
        children = []
        cell_gap = 2
        edge = 5
        grid = Grid(base_style, edge, edge, width - (edge * 2), height - (edge * 2), grid_children, "grid",
                    grid_rows, grid_columns, cell_gap)
        children.append(grid)

        # complete base class init
        super().__init__(base_style, x, y, width, height, children)

        # confirm init complete
        logging.debug(f"EntityInfo initialised.")

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
        pass

    def set_skill(self, slot_number, skill):
        self.skills[slot_number] = skill

        # TODO - find better way of recursively checking for children
        for child in self.children[0].children:
            if child.name == f"skill{slot_number}":
                data = library.get_skill_data(skill.skill_tree_name, skill.name)
                icon = pygame.image.load("assets/skills/" + data.icon).convert_alpha()
                icon = child.resize_image(icon, child.rect.width, child.rect.height)
                child.base_style.background_image = icon
