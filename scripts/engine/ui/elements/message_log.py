from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from pygame_gui.elements import UIPanel, UITextBox

from scripts.engine.core.constants import  RenderLayer

if TYPE_CHECKING:
    import pygame_gui


class MessageLog(UIPanel):
    """
    Hold text relating to the game's events, to display to the player. This should be a log of all notable things
    that have happened. It is recommended that all messages are in the past tense.
    """

    def __init__(self, rect: Rect, manager: pygame_gui.ui_manager.UIManager):
        # hold state info
        self.text = ""
        self.text_box = None

        # complete base class init
        super().__init__(rect, RenderLayer.UI_BASE, manager, element_id="message_log",
                         anchors={"left": "left",
                             "right": "right",
                             "top": "bottom",
                             "bottom": "bottom"})

        self.text_box = self._create_text_box()
        self.add_message("Welcome to Not Quite Paradise!")

        # confirm init complete
        logging.debug(f"MessageLog initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        pass

    ########### CREATE ################

    def _create_text_box(self) -> UITextBox:
        """
        Create the text box to show the messages
        """
        rect = pygame.Rect((0, 0), (self.rect.width, self.rect.height))
        textbox = UITextBox(html_text=self.text, relative_rect=rect, manager=self.ui_manager,
                  wrap_to_height=False, layer_starting_height=1, object_id="#text_box", container=self.get_container())

        return textbox

    ########## ACTIONS ##############

    # noinspection PyArgumentList,PyArgumentList
    def add_message(self, message: str):
        """
        Add message to the message log. Formatting the text is done via a subset of HTML tags. Currently supported
        tags are:
        <b></b> or <strong></strong> - to encase bold styled text.
        <i></i>, <em></em> or <var></var> - to encase italic styled text.
        <u></u> - to encase underlined text.
        <a href=’id’></a> - to encase ‘link’ text that can be clicked on to generate events with the id given in href.
        <body bgcolor=’#FFFFFF’></body> - to change the background colour of encased text.
        <br> - to start a new line.
        <font face=’verdana’ color=’#000000’ size=3.5></font> - To set the font, colour and size of encased text.
        """
        self.text += message + "<br>"

        if self.text_box:
            self.text_box.kill()
        self.text_box = self._create_text_box()

        # update the position of the text in the text box
        # N.B. this is taken from the UIVerticalScrollBar update method
        if self.text_box.scroll_bar:
            scroll_bar = self.text_box.scroll_bar
            scroll_bar.scroll_wheel_down = False
            scroll_bar.scroll_position += (250.0 * 1)
            scroll_bar.scroll_position = min(scroll_bar.scroll_position,
                                             scroll_bar.bottom_limit - scroll_bar.sliding_button.rect.height)
            x_pos = scroll_bar.rect.x + scroll_bar.shadow_width + scroll_bar.border_width
            y_pos = scroll_bar.scroll_position + scroll_bar.rect.y + scroll_bar.shadow_width + \
                    scroll_bar.border_width + scroll_bar.button_height
            scroll_bar.sliding_button.set_position(Vector2(x_pos, y_pos))

            scroll_bar.start_percentage = scroll_bar.scroll_position / scroll_bar.scrollable_height
            if not scroll_bar.has_moved_recently:
                scroll_bar.has_moved_recently = True
