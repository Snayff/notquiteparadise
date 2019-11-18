
from typing import List
from scripts.ui.templates.widget import Widget
from scripts.ui.templates.widget_style import WidgetStyle


class Frame(Widget):
    """
    The simplest widget; to create a border and background around a surface (image, text etc.).
    """

    def __init__(self, base_style: WidgetStyle, x: int = 0, y: int = 0, width: int = 0, height: int = 0,
            children: List = None,  name: str = "frame"):
        super().__init__(base_style, x, y, width, height, children, name)

        self.update()

    def update(self):
        """
        Update frame
        """
        super().update()

    def draw(self, surface):
        """
        Draw the border, background and any children.

        Args:
            surface ():
        """
        super().draw(surface)
