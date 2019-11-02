
from scripts.ui.templates.widget_style import WidgetStyle


class Widget:
    """
    A simple widget to display something on the UI. A base class.
    """
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle):
        # aesthetics
        self.base_style = base_style

        # position and size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        import pygame
        self.rect = pygame.rect.Rect(x, y, width, height)

        # now that we know the size adjust the images to correct their sizes
        self.resize_style_images()

    def resize_style_images(self):
        style = self.base_style

        if style.background_image:
            if style.background_image.get_size() != self.rect.size:
                import pygame
                style.background_image = pygame.transform.smoothscale(style.background_image, (self.rect.width,
                self.rect.height))