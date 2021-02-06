from __future__ import annotations

from pygame.rect import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UITextBox


class ScreenMessage(UITextBox):
    """
    Show messages on the centre of the screen for a limited time
    """

    def __init__(
        self,
        rect: Rect,
        text: str,
        manager: UIManager,
    ):

        super().__init__(
            html_text=text,
            relative_rect=rect,
            manager=manager,
            wrap_to_height=True,
            layer_starting_height=100,
            object_id="#screen_message",
        )

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
