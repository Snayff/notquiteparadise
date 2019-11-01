from typing import Tuple, List

import pygame
from pygame import surface


class WidgetStyle:
    def __init__(self, font: pygame.freetype.Font, background_image: surface = None,
            background_colour: Tuple = None, border_colour: Tuple = None, vertical_border: surface = None,
            horizontal_border: surface = None, top_left_border: surface = None, top_right_border: surface = None,
            bottom_left_border: surface = None, bottom_right_border: surface = None):
        # text
        self.font = font  # TODO: set default

        # background
        self.background_image = background_image
        self.background_colour = background_colour

        # border
        self.border_colour = border_colour
        self.vertical_border = vertical_border
        self.horizontal_border = horizontal_border
        self.top_left_border = top_left_border
        self.top_right_border = top_right_border
        self.bottom_left_border = bottom_left_border
        self.bottom_right_border = bottom_right_border



class Widget:
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle):
        # aesthetics
        self.base_style = base_style

        # position and size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(x, y, width, height)


class TextBox(Widget):
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, text: str = "text"):
        super().__init__(x, y, width, height, base_style)
        self.text_surfaces = [self.base_style.font.render(text)]

    def draw(self, surface):
        for text_surface in self.text_surfaces:
            # TODO - update to adjust x and y as needed (e.g. y per line)
            surface.blit(text_surface, (0, 0))


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

    def draw(self):
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


class Container:
    """
    Holds a collection of UI objects; a container for widgets and other containers.
    """

    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, contained_widgets: List = []):
        # aesthetics
        self.base_style = base_style

        # position and size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(x, y, width, height)

        # state and info
        self.contained_widgets = contained_widgets


class Frame(Container):
    """
    A container that respects the x y given of each widget.
    """
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, contained_widgets: List = []):
        super().__init__(x, y, width, height, base_style, contained_widgets)

    def draw(self):
        # draw all contained widgets and containers
        for widget in self.contained_widgets:
            widget.draw()

class UIElement:
    def __init__(self, container: Container):
        self.container = container
        self.is_visible = False



class AnotherMessageLog(UIElement):
    def __init__(self, container):
        super().__init__(container)

        self.message_list = []
        self.messages_to_draw = []
        self.keywords = {}
        self.icons = {}
        self.commands = {}

# TODO - NEXT ACTION
#  continue trying to recreate a simplified message log
#  instance Frame, add Texbox and generic message, add to AnotherMessageLog