import pygame.freetype


class Font:
    def __init__(self):
        pygame.freetype.init()
        self.debug = pygame.freetype.Font(None, 12)