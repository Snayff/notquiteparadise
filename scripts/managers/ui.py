import pygame

from scripts.panels.message_log import MessageLog
from scripts.core.colours import Palette, Colour
from scripts.core.constants import BASE_WINDOW_HEIGHT, BASE_WINDOW_WIDTH, TILE_SIZE
from scripts.core.fonts import Font


class UIManager:
    """
    Manage the UI, such as windows, resource bars etc

    Attributes:
        focused_window (pygame.surface) : The window currently in focus.
        colour (Colour): Game Colours.
        palette (Palette): Palette of Colours
        font (Font): Renderable Font
        main_surface (pygame.surface): The main sufrace to render to
        message_log (MessageLog): Object holding message log functionality
    """

    def __init__(self):
        self.focused_window = None
        self.colour = Colour()
        self.palette = Palette()
        self.font = Font()
        self.desired_width = 1920  # TODO - allow for selection by player but only multiples of base (16:9)
        self.desired_height = 1080
        self.screen_scaling_mod_x = self.desired_width // BASE_WINDOW_WIDTH
        self.screen_scaling_mod_y = self.desired_height // BASE_WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.desired_width, self.desired_height))
        self.main_surface = pygame.Surface((BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT))

        self.message_log = MessageLog()

    def draw_game(self, game_map=None, entities=None, debug_active=False, debug_messages=None):
        """
        Draw the entire game.

        Args:
            game_map (GameMap): the current game map
            entities (list[Entitiy]): list of entities
            debug_active (bool): whether to show the debug messages
            debug_messages (str): the debug message to show
        """
        # TODO - draw dirty only

        # clear last frames drawing
        self.main_surface.fill(self.colour.black)

        # draw new frame
        if game_map:
            self.draw_map(game_map)
            self.draw_entities(game_map, entities)

        if debug_active:
            self.draw_debug_info(debug_messages)

        if self.message_log.show:
            if self.message_log.is_dirty:
                self.draw_message_log()

        self.draw_tooltips()

        # resize the surface to the dersired resolution
        scaled_surface = pygame.transform.scale(self.main_surface, (self.desired_width, self.desired_height))
        self.screen.blit(scaled_surface, (0, 0))

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
                from scripts.core.global_data import entity_manager
                sprite = entity_manager.get_entity_current_frame(entity)  # TODO - decouple link to entity_manager
                self.main_surface.blit(sprite, (entity.x * TILE_SIZE, entity.y * TILE_SIZE))

                # TESTING - show frames
                font = self.message_log.font
                font.render_to(self.main_surface, (entity.x * TILE_SIZE, entity.y * TILE_SIZE),
                                    str(entity.current_sprite_frame), self.colour.white)


    def draw_debug_info(self, messages):
        """
        Draw the debug info
        Args:
            messages (str): Strings to show in the debug info section
        """
        font = self.font.debug
        font_size = font.size

        # loop all lines in message and use line index to amend msg position
        for line in range(len(messages)):
            gap_between_lines = font_size / 2
            y_pos = 0 + (line * font_size) + (line * gap_between_lines)  # 0 is starting y coord
            font.render_to(self.main_surface, (0, y_pos), messages[line], self.palette.debug_font_colour,
                           self.colour.black)

    def draw_message_log(self):
        """
        Draw the MessageLog, and all message_list that can be shown
        """
        # show only as many message_list as we can or have
        messages_to_show = min(len(self.message_log.message_list), self.message_log.number_of_messages_to_show)
        first_message_index = self.message_log.first_message_to_show

        # render the panel
        bg_colour = self.palette.message_log.background
        x = self.message_log.panel_x
        y = self.message_log.panel_y
        width = self.message_log.panel_width
        height = self.message_log.panel_height
        pygame.draw.rect(self.main_surface, bg_colour, [x, y, width, height])

        # init info for message render
        msg_x = x + self.message_log.border_size + self.message_log.message_indent
        msg_y = y + self.message_log.border_size
        font = self.message_log.font
        messages = self.message_log.message_list
        font_size = int(self.message_log.font.size)

        # render the message_list
        for message_count in range(messages_to_show):
            # reset offset
            current_msg_x_offset = 0

            # get y position of line to write to
            adjusted_y = msg_y + (message_count * (font_size + self.message_log.gap_between_lines))

            # parse message for expressions
            parsed_message = self.message_log.parse_message(messages[message_count + first_message_index][1])

            # render all parsed messages
            for counter in range(len(parsed_message)):

                # get the message to render and position to render to
                msg_to_render = parsed_message[counter][1]
                adjusted_x = msg_x + current_msg_x_offset

                # check if it exists in the icon list
                if msg_to_render == "icon":
                    icon = parsed_message[counter][0]
                    self.main_surface.blit(icon, (adjusted_x, adjusted_y))

                    # update x offset based on width of image
                    image_size = icon.get_width()

                    current_msg_x_offset += image_size + (font_size / 3)

                # its not an icon so must be text.
                else:
                    #  Check for a hyperlink
                    if msg_to_render in self.message_log.hyperlinks:

                        link_already_logged = False
                        msg_colour = self.palette.message_log.hyperlink

                        # check we havent already logged it
                        for link_counter in range(len(self.message_log.displayed_hyperlinks)):
                            if msg_to_render == self.message_log.displayed_hyperlinks[link_counter][1]:
                                link_already_logged = True

                        if not link_already_logged:

                            # get the hyperlink rect
                            hyperlink_rect = font.render_to(self.main_surface,  (adjusted_x, adjusted_y),
                                                            msg_to_render, msg_colour)

                            # update the rect to reflect current position
                            hyperlink_rect.x = adjusted_x
                            hyperlink_rect.y = adjusted_y

                            # add rect of hyperlink to active list
                            self.message_log.displayed_hyperlinks.append((hyperlink_rect, msg_to_render, 0))
                                # 0 is mouse over timer
                    else:
                        msg_colour = parsed_message[counter][0]

                    font.render_to(self.main_surface, (adjusted_x, adjusted_y), msg_to_render, msg_colour)

                    # update x offset based on length of string just rendered
                    msg_length = len(msg_to_render)
                    current_msg_x_offset += (msg_length + 2) * (font_size / 2)  # Not sure about the formula, but it
                                                                                # works.

        # no longer dirty # TODO - uncomment when able to setup message log is dirty
        # self.is_dirty = False

    def draw_tooltips(self):
        """
        draw the tooltips and  their text
        """
        # Message log tooltips
        if self.message_log.show:
            font = self.message_log.font
            font_colour = self.palette.message_log.tooltip_text

            # update message log tooltip info
            self.message_log.check_mouse_over_link()

            tooltip_info = self.message_log.get_active_tooltip()

            if tooltip_info:
                text_rect, tooltip_text, extended_text_x, extended_text_y, extended_tooltip_text = tooltip_info

                pygame.draw.rect(self.main_surface, self.colour.black, text_rect)
                font.render_to(self.main_surface, (text_rect.x, text_rect.y), tooltip_text, font_colour)

                if extended_text_x != -1:
                    font.render_to(self.main_surface, (extended_text_x, extended_text_y), extended_tooltip_text,
                                   font_colour)
