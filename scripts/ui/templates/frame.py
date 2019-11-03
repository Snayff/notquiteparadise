from typing import List

import pygame

from scripts.ui.templates.widget import Widget
from scripts.ui.templates.widget_style import WidgetStyle


class Frame(Widget):
    """
    The simplest widget to create a border and background around a surface (image, text etc.).
    """

    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, children: List = [],
            name: str = "frame", image=None):
        super().__init__(x, y, width, height, base_style, children, name)

        self.image = image

        self.resize_image()

    def draw(self, surface):
        """
        Draw the border, background and any children.

        Args:
            surface ():
        """
        super().draw(surface)

    def resize_image(self):
        """
        Ensure the image is the size of the rect
        """
        if self.image:
            if self.image.get_size() != self.rect.size:
                self.image = pygame.transform.smoothscale(self.image, (self.rect.width, self.rect.height))

    def set_image(self, image):
        """
        Set the framed image

        Args:
            image ():
        """
        self.image = image