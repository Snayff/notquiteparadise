import logging
import pygame
from scripts.core.constants import InputStates, VisualInfo, MouseButtons
from scripts.events.entity_events import UseSkillEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.grid import Grid
from scripts.ui.templates.text_box import TextBox
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
        cell_gap = 2
        edge = 5

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

        for skill_number in range(0, self.max_skills):
            colour = (50, 50, 20*skill_number)
            base_style = WidgetStyle(font=font, background_colour=colour, border_colour=border_colour,
                                     font_colour=font_colour, border_size=border_size)
            # TODO - convert to text box to add skill number/hotkey
            textbox = TextBox(base_style=base_style, name=f"skill{skill_number}", text=f"skill{skill_number}",
                              width=width - (edge * 2), height=height - edge * 2)
            grid_children.append(textbox)

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)
        # create child Grid
        children = []
        grid = Grid(base_style, edge, edge, width - (edge * 2), height - (edge * 2), grid_children, "grid",
                    grid_rows, grid_columns, cell_gap)
        children.append(grid)

        # complete base class init
        super().__init__(base_style, x, y, width, height, children)

        for child in self.all_children():
            child.is_dirty = True

        # confirm init complete
        logging.debug(f"EntityInfo initialised.")

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
        # Use a skill
        if input_key == MouseButtons.LEFT_BUTTON:
            from scripts.global_singletons.managers import ui
            mouse_pos = ui.Mouse.get_relative_scaled_mouse_pos()

            for child in self.all_children():
                if child.rect.collidepoint(mouse_pos) and child.name.startswith("skill"):
                    from scripts.global_singletons.managers import world
                    # get skill number by splitting the number from child's name
                    skill_number = int(child.name.split("skill", 1)[1])

                    # get the skill
                    skill = world.player.actor.known_skills[skill_number]

                    # attempt to use skill
                    # TODO - put logic for testing if skill can be used in handler
                    publisher.publish((UseSkillEvent(world.player, skill)))

                    break

    def set_skill(self, slot_number, skill):
        """
        Set skill in the skill bar slot

        Args:
            slot_number ():
            skill ():
        """
        self.skills[slot_number] = skill

        for child in self.all_children():
            if child.name == f"skill{slot_number}":
                data = library.get_skill_data(skill.skill_tree_name, skill.name)
                icon = pygame.image.load("assets/skills/" + data.icon).convert_alpha()
                icon = child.resize_image(icon, child.rect.width, child.rect.height)
                child.base_style.background_image = icon

                break
