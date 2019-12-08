import logging

from scripts.core.constants import VisualInfo, InputStates, MouseButtons, UIElementTypes
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.text_box import TextBox
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class PguiMessageLog(UIElement):
    """
    Hold text relating to the game's events, to display to the player.
    """
    def __init__(self):
        # REGARDING EXTENDING ON HOVER
        # You can do whatever you like by sub-classing the UITextBox class, it's just python code :)
        #
        # class MyFancyTextBox(UITextBox):
        #     def __init__(self, blah, blah, blah):
        #         super().__init__(blah, blah, blah)
        # The text box doesn't do anything in particular when it's on_hovered right now unless you are using links.
        #  So you should be able to just write an on_hovered function for your new subclass without worrying about
        #   the base class.
        #
        #  I think there is a set_dimensions() method though which you could call to make the box larger which will
        #  recompute the text wrapping and all that.


        # size and position
        width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 1)
        height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        x = VisualInfo.BASE_WINDOW_WIDTH - width
        y = VisualInfo.BASE_WINDOW_HEIGHT - height

        # create style
        palette = Palette().message_log
        font = Font().message_log
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2

        # create child text box and style
        children = []
        edge = 5
        text_box_base_style = WidgetStyle(font=font, background_colour=bg_colour, font_colour=font_colour)
        text_box = TextBox(text_box_base_style, edge, edge, width - (edge * 2), height - (edge * 2), [],
                           "message_box")
        children.append(text_box)

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)

        # complete base class init
        super().__init__(UIElementTypes.MESSAGE_LOG, base_style, x, y, width, height, children)

        # confirm init complete
        logging.debug(f"MessageLog initialised.")

    def update(self):
        """
        Ensure all the children update in response to changes.
        """
        super().update()

    def draw(self, main_surface):
        """
        Draw the message log.

        Args:
            main_surface ():
        """
        super().draw(main_surface)

    def handle_input(self, input_key, input_state: InputStates = InputStates.PRESSED):
        """
        Process received input

        Args:
            input_key (): input received. Mouse, keyboard, gamepad.
            input_state (): pressed or released
        """
        # Text scrolling
        if input_key == MouseButtons.WHEEL_UP:
            for child in self.children:
                if child.name == "message_box":
                    child.first_line_index = max(child.first_line_index - 1, 0)
                    child.is_dirty = True
                    break

        elif input_key == MouseButtons.WHEEL_DOWN:
            for child in self.children:
                if child.name == "message_box":
                    max_index = max(len(child.text_list) - child.max_lines, 0)
                    child.first_line_index = min(child.first_line_index + 1, max_index)
                    child.is_dirty = True
                    break

    def add_message(self, message: str):
        """
        Add a message to the message log

        Args:
            message ():
        """
        for child in self.children:
            if child.name == "message_box":
                child.add_text(message)
