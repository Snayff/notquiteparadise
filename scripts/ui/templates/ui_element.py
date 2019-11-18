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
    def update(self):
        """
        Base update method of the ui element. Must be overridden.
        """
        for child in self.children:
            child.update()

    @abstractmethod
    def draw(self, main_surface):
        """
        Base draw method of the ui element. Must be overridden. Override must also include a blit to the main surface
         as the final step in the method.
        """
        # adjust the rect of the ui element as it is absolute, not relative
        # we dont adjust the actual rect as that would change the ui elements position
        adjusted_rect = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        self.base_style.draw(self.surface, adjusted_rect)

        # draw all contained widgets
        for child in self.children:
            child.draw(self.surface)

        # blit to the main surface
        main_surface.blit(self.surface, (self.rect.x, self.rect.y))

    @abstractmethod
    def handle_input(self, input_key, input_state):
        """
        Base input method of the element. Must be overridden.
        """
        raise NotImplementedError(f"handle_input method must be overridden for {self!r}")

    def all_children(self):
        """
        Returns all children, recursively.
        """
        yield from self.children
        for child in self.children:
            yield from child.all_children()

    def get_child(self, child_name: str):
        """
        Get a child from among all children. Returns first child with matching name.

        Args:
            child_name ():

        Returns:
            Widget: Returns found widget or None if nothing found.
        """
        for child in self.all_children():
            if child.name == child_name:
                return child

        return None
