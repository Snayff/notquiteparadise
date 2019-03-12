import pygame.freetype


class Font:
    """
    Renderable font.
    """
    def __init__(self):
        pygame.freetype.init()
        self.debug =  pygame.freetype.Font(None, 9) #pygame.freetype.Font("assets/fonts/Kenney Future Narrow.ttf", 8)
        self.debug.pad = True  # have font rect consistent
        self.message_log = pygame.freetype.Font(None, 12)
        self.message_log.pad = True
        self.default = pygame.freetype.Font(None, 12)