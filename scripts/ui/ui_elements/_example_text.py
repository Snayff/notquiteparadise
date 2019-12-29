# import pygame
# from math import sin, cos
#
# WHITE = (250, 250, 250)
# BLACK = (5, 5, 5)
#
# HUE_MAX = 360
#
#
# class NormalText:
#     def __init__(self, text: str, pos=(0, 0),
#             font=pygame.font.Font(pygame.font.get_default_font(), 40)):
#         self.text = text
#         self.font = font
#         self.surface = self.font.render(text, True, WHITE)
#         self.pos = pos
#
#     def update(self):
#         pass
#
#     def draw(self, screen):
#         screen.blit(self.surface, self.pos)
#
#
# class WaveText:
#
#     def __init__(self, text: str, pos=(0, 0), frequency=5, speed=-0.3, radius=4, spread_x=1.5,
#             font=pygame.font.Font(pygame.font.get_default_font(), 40), huestep=3):
#         """
#        A basic wavy text widget.
#        :param text: The string to render
#        :param pos: Top left corner of the text. Note that because of the circles it will move outside of it
#        :param frequency: How often a new wave is stared
#        :param speed: the speed of each wave (~difference of position with the next letter)
#        :param radius: radius on which letters move
#        :param spread_x: to have an ellipse stretched in the x axis set this to > 1 and < 1 for the y axis.
#        :param font:
#        """
#         self.speed = speed
#         self.frequency = frequency
#         self.radius = radius
#         self.pos = pos
#         self.spread_x = spread_x
#
#         self.t = 0
#
#         self.text = text
#         self.font = font
#         self.char_to_surf = {}
#
#         self.hue = 0
#         self.huestep = huestep
#
#         col = pygame.Color(*WHITE)
#         self.char_surfs = []
#         for hue in range(0, HUE_MAX, huestep):
#             col.hsva = (hue, 100, 100, 100)
#             self.char_surfs.extend([self.get_surf(c, col) for c in self.text])
#
#     def get_surf(self, c, col):
#         key = c + str(col)
#         surf = self.char_to_surf.get(key)
#         if not surf:
#             surf = self.font.render(c, True, col)
#             self.char_to_surf[key] = surf
#         return surf
#
#     def update(self):
#         self.t += 1
#
#         self.hue = (self.hue + 1) % (HUE_MAX // self.huestep)
#
#     def draw(self, screen):
#         x0, y0 = self.pos
#
#         xr = self.radius / self.spread_x
#         yr = self.radius
#         offset = self.t / self.frequency
#         speed = self.speed
#
#         screen_blit = screen.blit
#
#         numchars = len(self.text)
#         charoffset = self.hue * numchars
#
#         for char in self.char_surfs[charoffset:charoffset + numchars]:
#             dx = xr * cos(offset)
#             dy = yr * sin(offset)
#             screen_blit(char, (x0 + dx, y0 + dy))
#             x0 += char.get_width()
#             offset += speed
#
#
# def example_usage():
#     SCREEN_SIZE = 1920, 1080
#     FPS = 60
#
#     screen = pygame.display.set_mode(SCREEN_SIZE)
#     clock = pygame.time.Clock()
#
#     opt_sel = 0
#     options = ("Of course not!", "Guess again, nerd!")
#     options_objects = [
#         (NormalText(t, (800, 500 + 50 * i)), WaveText(t, (800, 500 + 50 * i)))
#         for i, t in enumerate(options)]
#
#     while "I want to read the same text":
#         for e in pygame.event.get():
#             if e.type == pygame.QUIT:
#                 return 0
#             if e.type == pygame.KEYDOWN:
#                 if e.key == pygame.K_q:
#                     return 0
#                 elif e.key == pygame.K_UP:
#                     if opt_sel > 0:
#                         opt_sel -= 1
#                 elif e.key == pygame.K_DOWN:
#                     if opt_sel + 1 < len(options):
#                         opt_sel += 1
#
#         screen.fill(BLACK)
#
#         for i, option in enumerate(options_objects):
#             option[1].update()
#             option[1 if opt_sel == i else 0].draw(screen)
#
#         pygame.display.update()
#
#         clock.tick(FPS)