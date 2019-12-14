import logging

import pygame
import pygame_gui
from pygame_gui.core import UIWindow
from pygame_gui.elements import UITextBox


class MessageLog(UIWindow):
    """
    Hold text relating to the game's events, to display to the player.
    """
    def __init__(self, rect: pygame.Rect, manager: pygame_gui.ui_manager.UIManager,):

        # create empty attributes to hold state info
        self.text = ""
        self.text_box = None

        # complete base class init
        super().__init__(rect, manager, ["message_log"])

        self.add_message("Welcome to Not Quite Paradise!")
        # confirm init complete
        logging.debug(f"MessageLog initialised.")

    def add_message(self, message: str):
        """
        Add message to the message log.

        Formatting the text is done via a subset of HTML tags. Currently supported tags are:

        <b></b> or <strong></strong> - to encase bold styled text.
        <i></i>, <em></em> or <var></var> - to encase italic styled text.
        <u></u> - to encase underlined text.
        <a href=’id’></a> - to encase ‘link’ text that can be clicked on to generate events with the id given in href.
        <body bgcolor=’#FFFFFF’></body> - to change the background colour of encased text.
        <br> - to start a new line.
        <font face=’verdana’ color=’#000000’ size=3.5></font> - To set the font, colour and size of encased text.

        Args:
            message ():
        """

        self.text += message + "<br>"

        self.text_box = UITextBox(html_text=self.text, relative_rect=self.rect, manager=self.ui_manager,
                                  wrap_to_height=False, layer_starting_height=1,  object_id="#text_box")


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