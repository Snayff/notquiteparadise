
from typing import List
from scripts.ui.templates.widget import Widget
from scripts.ui.templates.widget_style import WidgetStyle


class Frame(Widget):
    """
    The simplest widget; to create a border and background around a surface (image, text etc.).
    """

    def __init__(self, base_style: WidgetStyle, x: int = 0, y: int = 0, width: int = 0, height: int = 0,
            children: List = [],  name: str = "frame", image=None):
        super().__init__(base_style, x, y, width, height, children, name)

        self.image = image

        if self.image:
            self.resize_image(self.image, self.rect.width, self.rect.height)

    def draw(self, surface):
        """
        Draw the border, background and any children.

        Args:
            surface ():
        """
        super().draw(surface)

        if self.image:
            surface.blit(self.image, self.rect)

    def set_image(self, image):
        """
        Set the framed image

        Args:
            image ():
        """
        self.image = image