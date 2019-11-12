import pygame
from abc import ABC, abstractmethod
from typing import List
from scripts.ui.templates.widget_style import WidgetStyle


class UIElement(ABC):
    """
    A grouping of widgets to create a specific UI element.
    """
    def __init__(self, base_style: WidgetStyle, x: int, y: int, width: int, height: int, children: List = None):
        # aesthetics
        self.base_style = base_style

        # position and size
        self.rect = pygame.rect.Rect(x, y, width, height)

        # state and info
        self.children = children
        self.is_visible = False
        self.surface = pygame.Surface((self.rect.width, self.rect.height))

    @abstractmethod
    def draw(self, main_surface):
        """
        Base draw method of the ui element.
        """
        # adjust the rect of the ui element as it is absolute, not relative
        # we dont adjust the actual rect as that would change the ui elements position
        adjusted_rect = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        self.base_style.draw(main_surface, adjusted_rect)

        # draw all contained widgets
        for child in self.children:
            child.draw(self.surface)

    @abstractmethod
    def handle_input(self, input_key, input_state):
        """
        Base input method of the widget. Must be overridden.
        """
        raise NotImplementedError(f"handle_input method must be overridden for {self!r}")

    def all_children(self):
        """
        Returns all children, recursively.
        """
        yield from self.children
        for child in self.children:
            yield from child.all_children()