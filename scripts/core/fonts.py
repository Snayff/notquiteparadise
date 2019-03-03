import pygame.freetype


class Font:
    """
    Renderable font.
    """
    def __init__(self):
        pygame.freetype.init()
        self.debug = pygame.freetype.Font("assets/fonts/Kenney Future Narrow.ttf", 8)
        self.debug.pad = True
        self.message_log = pygame.freetype.Font(None, 12)
        self.message_log.pad = True