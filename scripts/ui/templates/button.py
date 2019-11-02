from scripts.ui.templates.widget import Widget
from scripts.ui.templates.widget_style import WidgetStyle


class Button (Widget):
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle,  hover_style: WidgetStyle,
            clicked_style: WidgetStyle, label: str = "label"):
        super().__init__(x, y, width, height, base_style)
        # additional aesthetics
        self.hover_style = hover_style
        self.clicked_style = clicked_style

        # state and info
        self.label = label
        self.hovered = False
        self.clicked = False

    def draw(self, surface):
        # which to draw?
        if self.hovered:
            style = self.hover_style
        elif self.clicked:
            style = self.clicked_style
        else:
            style = self.base_style

        if style.background_colour is not None:
            pass
            # draw colour

        if style.background_image is not None:
            # draw background image
            pass


