
from typing import List
from scripts.ui.templates.widget_container import WidgetContainer
from scripts.ui.templates.widget_style import WidgetStyle


class Frame(WidgetContainer):
    """
    A container that respects the x y given of each widget.
    """
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, contained_widgets: List = []):
        super().__init__(x, y, width, height, base_style, contained_widgets)

    def draw(self, surface):
        """
        Draw the style and and attached children

        Args:
            surface ():
        """
        # draw style
        self.base_style.draw(surface, self.rect)

        # draw all contained widgets and containers
        for child in self.children:
            child.draw(surface)