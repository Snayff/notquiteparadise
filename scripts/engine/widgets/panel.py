from __future__ import annotations

from abc import ABC

import pygame
from pygame_gui.elements import UIPanel

__all__ = ["Panel"]


class Panel(ABC, UIPanel):

    def process_event(self, event: pygame.event.Event):
        """
        Gives UI Windows access to pygame events. Derived windows should super() call this class if they implement
        their own process_event method.
        """
        super().process_event(event)

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)
