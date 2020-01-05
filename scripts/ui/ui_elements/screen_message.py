from __future__ import annotations

import logging
import pygame
from typing import TYPE_CHECKING
from pygame_gui.elements import UITextBox

from scripts.core.constants import VisualInfo

if TYPE_CHECKING:
    import pygame_gui


class ScreenMessage(UITextBox):
    """
    Show messages on the centre of the screen for a limited time
    """
    def __init__(self, text, manager: pygame_gui.ui_manager.UIManager,):

        x = VisualInfo.BASE_WINDOW_WIDTH / 4
        y = VisualInfo.BASE_WINDOW_HEIGHT / 3
        width = VisualInfo.BASE_WINDOW_WIDTH / 4
        height = -1  # force auto size
        rect = pygame.Rect((x, y), (width, height))

        super().__init__(html_text=text, relative_rect=rect, manager=manager, wrap_to_height=True,
                         layer_starting_height=100, object_id="screen_message")

        self.lifespan = 2  # time in seconds
        self.time_alive = 0

        self.set_active_effect("typing_appear")

    def update(self, time_delta: float):
        super().update(time_delta)

        self.time_alive += time_delta

        if self.time_alive >= self.lifespan:
            self.kill()