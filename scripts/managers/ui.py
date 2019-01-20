import pygame

from scripts.panels.message_log import MessageLog
from scripts.core.colours import Palette, Colour
from scripts.core.constants import WINDOW_HEIGHT, WINDOW_WIDTH, TILE_SIZE
from scripts.core.fonts import Font


class UIManager:
    """
    Manage the UI, such as windows, resource bars etc
    """

    def __init__(self):
        self.focused_window = None
        self.colour = Colour()
        self.palette = Palette()
        self.font = Font()
        self.main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.message_log = MessageLog()
        self.show_message_log = True

    def draw_game(self, game_map=None, entities=None, debug_active=False, debug_messages=None):
        # clear last frames drawing
        self.main_surface.fill(self.colour.black)

        if game_map:
            self.draw_map(game_map)
            self.draw_entities(game_map, entities)

        if debug_active:
            self.draw_debug_info(debug_messages)

        if self.show_message_log:
            self.draw_message_log()

        # update the display
        pygame.display.flip()  # make sure to do this as the last drawing element in a frame

    def draw_map(self, game_map):

        for x in range(0, game_map.width):
            for y in range(0, game_map.height):

                if game_map.is_tile_visible(x, y):
                    tile_position = (x * TILE_SIZE, y * TILE_SIZE)
                    self.main_surface.blit(game_map.tiles[x][y].sprite, tile_position)

    def draw_entities(self, game_map, entities):
        for entity in entities:
            if game_map.is_tile_visible(entity.x, entity.y):
                self.main_surface.blit(entity.sprite, (entity.x * TILE_SIZE, entity.y * TILE_SIZE))

    def draw_debug_info(self, messages):
        font = self.font.debug
        font_size = font.size

        # loop all lines in message and use line index to amend msg position
        for line in range(len(messages)):
            gap_between_lines = font_size / 2
            y_pos = 0 + (line * font_size) + (line * gap_between_lines)  # 0 is starting y coord
            font.render_to(self.main_surface, (0, y_pos), messages[line], self.palette.debug_font_colour,
                           self.colour.black)

    def draw_message_log(self):
        # show only as many messages as we can or have
        messages_to_show = min(len(self.message_log.messages), self.message_log.number_of_messages_to_show)

        # render the panel
        bg_colour = self.message_log.background_colour
        x = self.message_log.panel_x
        y = self.message_log.panel_y
        width = self.message_log.panel_width
        height = self.message_log.panel_height
        pygame.draw.rect(self.main_surface, bg_colour, [x, width, y, height])

        # render the messages
        msg_x = x + self.message_log.border_size + self.message_log.message_indent
        msg_y = y + self.message_log.border_size
        font = self.message_log.font
        messages = self.message_log.messages
        fg_colour = self.colour.white  # TODO remove when messages parse their own colour

        for message_count in range(messages_to_show):
            adjusted_y = msg_y + (message_count * (self.message_log.font.size + self.message_log.gap_between_lines))
            font.render_to(self.main_surface, (msg_x, adjusted_y), messages[message_count][1], fg_colour)
