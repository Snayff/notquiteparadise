
from typing import List
from scripts.ui.templates.widget_style import WidgetStyle


class WidgetContainer:
    """
    Holds a collection of UI objects; a container for widgets and other containers.
    """

    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, children: List = []):
        # aesthetics
        self.base_style = base_style

        # position and size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        import pygame
        self.rect = pygame.rect.Rect(x, y, width, height)

        # state and info
        self.children = children