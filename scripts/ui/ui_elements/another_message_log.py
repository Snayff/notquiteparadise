from typing import List

from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class AnotherMessageLog(UIElement):
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, children: List = []):
        super().__init__(x, y, width, height, base_style, children)

    def draw(self, main_surface):
        """
        Draw the text log.

        Args:
            main_surface ():
        """
        super().draw(self.surface)

        # blit to the main surface
        main_surface.blit(self.surface, (self.rect.x, self.rect.y))

    def add_message(self, message):

        for child in self.children:
            if child.name == "message_box":
                child.add_text(message)
                child.update_text_shown()

# 1. check mouse scroll input
# 2. check mouse collides with text log.
# 3. increment first line index