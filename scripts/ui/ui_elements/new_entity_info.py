import logging

from scripts.core.constants import InputStates, VisualInfo, ICON_SIZE
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.frame import Frame
from scripts.ui.templates.text_box import TextBox
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class EntityInfo(UIElement):
    """
    Hold text relating to the game's events, to display to the player.
    """
    def __init__(self):
        # state and info
        self.selected_entity = None

        # size and position
        width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 1)
        height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        x = VisualInfo.BASE_WINDOW_WIDTH - width
        y = VisualInfo.BASE_WINDOW_HEIGHT - height

        # create style
        palette = Palette().entity_info
        font = Font().entity_info
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)

        children = []
        edge = 5
        text_box_base_style = WidgetStyle(font=font, background_colour=bg_colour, font_colour=font_colour)

        # create child widgets
        frame_x = (width / 2) - (ICON_SIZE / 2)  # find centre and then move half the width of the icon to the left
        frame_y = (ICON_SIZE / 2) + edge
        frame = Frame(frame_x, frame_y, ICON_SIZE, ICON_SIZE, base_style, [], "icon_frame")

        primary_y = frame_y + ICON_SIZE + edge
        text_height = (height - ICON_SIZE + (edge * 2)) / 2
        primary_text_box = TextBox(edge, primary_y, width - (edge * 2), text_height - (edge * 2),
                                   base_style, [], "primary_stats")
        secondary_y = primary_y + text_height + edge
        secondary_text_box = TextBox(edge, secondary_y, width - (edge * 2), text_height - (edge * 2),
                                     base_style, [], "secondary_stats")

        # add children
        children.append(frame)
        children.append(primary_text_box)
        children.append(secondary_text_box)

        # complete base class init
        super().__init__(x, y, width, height, base_style, children)

        # confirm init complete
        logging.debug(f"EntityInfo initialised.")

    def draw(self, main_surface):
        """
        Draw the text log.

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

    def update_entity_info(self, entity):
        self.selected_entity = entity
        self.update_primary_stats()
        self.update_secondary_stats()

    def update_icon(self):
        pass

    def update_primary_stats(self):
        pass

    def update_secondary_stats(self):
        pass