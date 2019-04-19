import pygame


class Panel:
    """
    A panel for an element on the UI

    Attributes:
        x (int) = X position of the panel.
        y (int) = Y position of the panel.
        width (int) = Width of the panel.
        height (int) = Height of the panel.
        colour (Colour)= Colour of background.
        border_size (int)= Size of border. If 0 no border is drawn.
        border_colour (Colour) = Colour of the border


    """

    def __init__(self, x, y, width, height, background_colour, border_size, border_colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_size = border_size
        self.background_colour = background_colour
        self.surface = pygame.Surface((self.width, self.height))
        self.border_colour = border_colour
        self.rect = pygame.rect.Rect(x, y, width, height)

    def draw_background(self):
        """
        Draw a panel surface, including background
        """
        self.surface.fill(self.background_colour)
        offset = self.border_size
        pygame.draw.rect(self.surface, self.background_colour,  [0 + offset,  0 + offset, self.width - offset,
                            self.height - offset], 0)

    def draw_panel_border(self):
        """
        Draw a panel's border if bordersize > 0
        """
        if self.border_size > 0:
            pygame.draw.rect(self.surface, self.border_colour,  [0, 0, self.width, self.height],
                             self.border_size)