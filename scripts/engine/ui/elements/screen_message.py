from __future__ import annotations

from typing import TYPE_CHECKING
from pygame.rect import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UITextBox
from scripts.engine.core.constants import VisualInfo

if TYPE_CHECKING:
    pass


class ScreenMessage(UITextBox):
    """
    Show messages on the centre of the screen for a limited time
    """
    def __init__(self, text, manager: UIManager,):

        # TODO - consider moving to pygame_gui.windows.ui_message_window module

        # TODO - centre the text on the screen
        x = VisualInfo.BASE_WINDOW_WIDTH / 4
        y = VisualInfo.BASE_WINDOW_HEIGHT / 4
        width = VisualInfo.BASE_WINDOW_WIDTH / 2  # TODO - get width of text
        height = -1  # force auto size
        rect = Rect((x, y), (width, height))

        super().__init__(html_text=text, relative_rect=rect, manager=manager, wrap_to_height=True,
                         layer_starting_height=100, object_id="screen_message")

        self.view_time = 2  # time in seconds
        self.lifespan = 3  # time in seconds
        self.time_alive: float = 0.0

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

        self.time_alive += time_delta

        if self.time_alive >= self.view_time:
            self.set_active_effect("fade_out")

            if self.time_alive >= self.lifespan:
                self.kill()

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        pass