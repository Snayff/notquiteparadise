from scripts.ui.templates.widget_container import WidgetContainer


class UIElement:
    def __init__(self, container: WidgetContainer):
        self.container = container
        self.is_visible = False
        import pygame
        self.surface = pygame.Surface((self.container.width, self.container.height))

        # update container's rect as it is the ultimate parent and therefore does not have a relative position
        # a container within a container is not affected
        self.container.rect.x = 0
        self.container.rect.y = 0