from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Type

import pygame
import pygame_gui
from pygame import Rect
from pygame_gui.elements import UIButton, UIPanel

from scripts.engine.core.constants import GameEvent, InputEvent, RenderLayer

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List
    from pygame_gui import UIManager


class TitleScreen(UIPanel):
    """
    Initial screen menu
    """

    def __init__(self, rect: Rect, manager: UIManager):

        self.button_events = {
            "new_game": pygame.event.Event(GameEvent.NEW_GAME),
            "load_game": pygame.event.Event(GameEvent.LOAD_GAME),
            "exit_game": pygame.event.Event(GameEvent.EXIT_GAME),
        }

        width = rect.width
        height = rect.height
        self.button_height = int(height / 8)
        self.button_width = int(width / 4)
        self.button_start_x = int((width / 2) - (self.button_width / 2))
        self.button_start_y = int(height / 4)
        self.space_between_buttons = int(((height - self.button_start_y) / len(self.button_events)) -
                                         self.button_height)

        self.buttons: List[UIButton] = []

        # complete base class init
        super().__init__(rect, RenderLayer.BOTTOM, manager, element_id="title_screen")

        self._init_buttons()

        # confirm init complete
        logging.debug(f"TitleScreen initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

            # Find out which button we are clicking
            button = event.ui_element

            # post the new event
            if button in self.buttons:
                # get the id
                ids = event.ui_object_id.split(".")
                button_id = ids[-1]  # get last element
                new_event = self.button_events[button_id]
                pygame.event.post(new_event)

                logging.debug(f"TitleScreen button '{button_id}' pressed.")

    def _init_buttons(self):
        """
        Init the buttons for the menu
        """
        # extract values for performance
        x = self.button_start_x
        start_y = self.button_start_y
        info = self.button_events
        width = self.button_width
        height = self.button_height
        gap = self.space_between_buttons
        manager = self.ui_manager

        count = 0
        for name in info.keys():
            y = start_y + ((height + gap) * count)
            friendly_name = name.replace("_", " ")

            button = UIButton(
                relative_rect=Rect((x, y), (width, height)),
                text=friendly_name.title(),
                manager=manager,
                container=self.get_container(),
                object_id=f"{name}",
            )

            self.buttons.append(button)

            count += 1
