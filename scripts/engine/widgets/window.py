from __future__ import annotations

from abc import ABC, abstractmethod

import pygame
from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui.elements import UIWindow

__all__ = ["Window"]


class Window(ABC, UIWindow):
    def process_event(self, event: pygame.event.Event):
        """
        Gives UI Windows access to pygame events. Derived windows should super() call this class if they implement
        their own process_event method.

        NOTE: Copied check for button close from pygame_gui UIWindow to allow overwriting use of close button.

        """
        super().process_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button in [
            pygame.BUTTON_LEFT,
            pygame.BUTTON_MIDDLE,
            pygame.BUTTON_RIGHT,
        ]:
            scaled_mouse_pos = self.ui_manager.calculate_scaled_mouse_position(event.pos)

            edge_hovered = (
                self.edge_hovering[0] or self.edge_hovering[1] or self.edge_hovering[2] or self.edge_hovering[3]
            )
            if self.is_enabled and event.button == pygame.BUTTON_LEFT and edge_hovered:
                self.resizing_mode_active = True
                self.start_resize_point = scaled_mouse_pos
                self.start_resize_rect = self.rect.copy()

        if event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT and self.resizing_mode_active:
            self.resizing_mode_active = False

        if (
            event.type == pygame.USEREVENT
            and event.user_type == UI_BUTTON_PRESSED
            and event.ui_element == self.close_window_button
        ):
            self.process_close_button()

    @abstractmethod
    def process_close_button(self):
        """
        Process closure of a window. Must be overriden in subclass. Usual use is creation of an event.

        Example:
            def process_close_button(self):
                event = pygame.event.Event(EventType.GAME, subtype=GameEvent.EXIT_MENU,
                    menu=UIElement.ACTOR_INFO)
                pygame.event.post(event)
        """
        pass

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)
