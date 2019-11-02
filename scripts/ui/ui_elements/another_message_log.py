
from scripts.ui.templates.ui_element import UIElement


class AnotherMessageLog(UIElement):
    def __init__(self, container):
        super().__init__(container)

        self.message_list = []
        self.messages_to_draw = []

    def draw(self, main_surface):
        # draw all contained widgets to the ui element's surface
        self.container.draw(self.surface)

        # blit to the main surface
        main_surface.blit(self.surface, (self.container.x, self.container.y))