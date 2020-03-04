import pygame


class Font:
    """
    Renderable font.
    """
    def __init__(self):
        pygame.freetype.init()
        pygame.font.init()

        font_dir = "assets/fonts/"
        self.default = pygame.freetype.Font(font_dir + "Barlow-Regular.otf", 12)
        self.default.pad = True

        self.debug = pygame.freetype.Font(font_dir + "Kenney Future Narrow.ttf", 12)
        self.debug.pad = True  # have font rect be consistent

        self.message_log = pygame.freetype.Font(None,  14)
        self.message_log.pad = True

        self.entity_info = pygame.freetype.Font(None, 12)
        self.entity_info.pad = True

        self.targeting_overlay = pygame.freetype.Font(font_dir + "Barlow-Regular.otf", 10)
        self.targeting_overlay.pad = True

        self.skill_bar = pygame.freetype.Font(font_dir + "Barlow-Regular.otf", 14)
        self.skill_bar.pad = True

        self.entity_queue = pygame.freetype.Font(font_dir + "Barlow-Regular.otf", 8)
        self.entity_queue.pad = True

        self.camera = pygame.freetype.Font(font_dir + "Barlow-Regular.otf", 8)
        self.camera.pad = True
