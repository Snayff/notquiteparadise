

class Font:
    """
    Renderable font.
    """
    def __init__(self):
        import pygame.freetype
        pygame.freetype.init()

        font_dir = "assets/fonts/"
        self.debug = pygame.freetype.Font(font_dir + "Kenney Future Narrow.ttf", 12)
        self.debug.pad = True  # have font rect be consistent
        self.message_log = pygame.freetype.Font(None,  14)
        self.message_log.pad = True
        self.default = pygame.freetype.Font(font_dir + "Barlow-Regular.otf", 12)
        self.default.pad = True
