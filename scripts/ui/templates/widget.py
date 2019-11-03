from typing import List

import pygame
from abc import ABC
from scripts.ui.templates.widget_style import WidgetStyle


class Widget(ABC):
    """
    A simple widget to display something on the UI. A base class.
    """
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, children: List = [],
            name: str = "widget"):
        # aesthetics
        self.base_style = base_style

        # position and size
        self.rect = pygame.rect.Rect(x, y, width, height)

        # state and info
        self.name = name
        self.children = children

        # now that we know the size adjust the images to correct their sizes
        self.resize_style_images()

    def draw(self, surface):
        """
        Base base style and all children of the widget.
        """
        self.base_style.draw(surface, self.rect)

        # draw all contained widgets
        for child in self.children:
            child.draw(surface)

    def resize_style_images(self):
        """
        Ensure the style images are the required size
        """
        style = self.base_style

        if style.background_image:
            if style.background_image.get_size() != self.rect.size:
                style.background_image = pygame.transform.smoothscale(style.background_image, (self.rect.width,
                self.rect.height))