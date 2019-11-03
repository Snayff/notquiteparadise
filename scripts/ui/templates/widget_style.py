
import pygame
from pygame import surface, freetype
from scripts.ui.basic.colours import Colour


class WidgetStyle:
    """
    Aesthetic settings for a widget or parent_widget
    """
    def __init__(self, font: freetype.Font, font_colour: Colour = (255, 255, 255), background_image: surface
            = None, background_colour: Colour = None, border_colour: Colour = None, border_size: int = 0,
            vertical_border: surface = None, horizontal_border: surface = None, top_left_border: surface = None,
            top_right_border: surface = None, bottom_left_border: surface = None, bottom_right_border: surface = None):
        # text
        self.font = font  # TODO: set default
        self.font_colour = font_colour

        # background
        self.background_image = background_image
        self.background_colour = background_colour

        # border
        self.border_colour = border_colour
        self.border_size = border_size
        self.vertical_border = vertical_border
        self.horizontal_border = horizontal_border
        self.top_left_border = top_left_border
        self.top_right_border = top_right_border
        self.bottom_left_border = bottom_left_border
        self.bottom_right_border = bottom_right_border

    def draw(self, surface, rect):
        """
        Draw the basic style info for the widget

        Args:
            surface ():
            rect ():
        """
        # add border and background
        if self.background_colour:
            pygame.draw.rect(surface, self.background_colour, rect)

        if self.border_colour and self.border_size > 0:
            pygame.draw.rect(surface, self.border_colour, rect, self.border_size)

        # add images
        if self.background_image:
            surface.blit(self.background_image, (rect.x, rect.y))