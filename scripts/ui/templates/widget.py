from typing import List

import pygame
from abc import ABC
from scripts.ui.templates.widget_style import WidgetStyle


class Widget(ABC):
    """
    A simple widget to display something on the UI. A base class.
    """
    def __init__(self, base_style: WidgetStyle, x: int = 0, y: int = 0, width: int = 0, height: int = 0,
            children: List = None, name: str = "widget"):
        # aesthetics
        self.base_style = base_style

        # position and size
        self.rect = pygame.rect.Rect(x, y, width, height)

        # state and info
        self.name = name
        self.children = children or []

        # now that we know the size adjust the images to correct their sizes
        if self.base_style.background_image:
            self.resize_image(self.base_style.background_image, self.rect.width, self.rect.height )

    def draw(self, surface):
        """
        Base base style and all children of the widget.
        """
        self.base_style.draw(surface, self.rect)

        # draw all contained widgets
        for child in self.children:
            child.draw(surface)

    def resize_image(self, image, desired_width, desired_height):
        """
        Ensure the image is the expected size
        """
        resized_image = image

        if image.get_size() != (desired_width, desired_height):
            resized_image = pygame.transform.smoothscale(image, (desired_width, desired_height))

        return resized_image