import pygame

from scripts.panels.message_log import MessageLog
from scripts.core.colours import Palette, Colour
from scripts.core.constants import WINDOW_HEIGHT, WINDOW_WIDTH, TILE_SIZE, GAME_FPS
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
        show_message_log (bool): Should we draw the message log?
    """

    def __init__(self):
        self.focused_window = None
        self.colour = Colour()
        self.palette = Palette()
        self.font = Font()
        self.main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.message_log = MessageLog()
        self.show_message_log = True
        self.displayed_hyperlinks = []
        self.mouse_over_timer = 0
        self.index_of_active_hyperlink = -1

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
        Draw the MessaegeLog, and all message_list that can be shown
        """

        # show only as many message_list as we can or have
        messages_to_show = min(len(self.message_log.message_list), self.message_log.number_of_messages_to_show)
        first_message_position = self.message_log.first_message_to_show

        # render the panel
        bg_colour = self.message_log.background_colour
        x = self.message_log.panel_x
        y = self.message_log.panel_y
        width = self.message_log.panel_width
        height = self.message_log.panel_height
        pygame.draw.rect(self.main_surface, bg_colour, [x, width, y, height]) # TODO move bg_colour to palette

        # render the message_list
        msg_x = x + self.message_log.border_size + self.message_log.message_indent
        msg_y = y + self.message_log.border_size
        font = self.message_log.font
        messages = self.message_log.message_list
        font_size = int(self.message_log.font.size)

        for message_count in range(messages_to_show):
            # reset offset
            current_msg_x_offset = 0

            # get y position of line to write to
            adjusted_y = msg_y + (message_count * (font_size + self.message_log.gap_between_lines))

            # parse message for expressions
            parsed_message = self.parse_message(messages[message_count + first_message_position][1])

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

                    current_msg_x_offset += image_size + 1

                # its not an icon so must be text.
                else:
                    #  Check for a hyperlink
                    if msg_to_render in self.message_log.hyperlinks:
                        msg_colour = self.palette.message_log_hyperlink
                        # get the hyperlink rect
                        hyperlink_rect = font.render_to(self.main_surface, (adjusted_x, adjusted_y), msg_to_render,
                                                   msg_colour)

                        # update the rect to reflect current position
                        hyperlink_rect.x = adjusted_x
                        hyperlink_rect.y = adjusted_y

                        # add rect of hyperlink to active list
                        self.displayed_hyperlinks.append((hyperlink_rect, msg_to_render))
                    else:
                        msg_colour = parsed_message[counter][0]

                        font.render_to(self.main_surface, (adjusted_x, adjusted_y), msg_to_render, msg_colour)

                    # update x offset based on length of string just rendered
                    msg_length = len(msg_to_render)

                    current_msg_x_offset += (msg_length + 1) * (font_size / 2)  # Not sure about the formula, but it
                                                                                # works.

                # TODO - move to separate function (in message log and return true/false?)
                # TODO - increment displayed_hyperlinks rect positions when new lines added
                # TODO - second hyperlink doesnt work?? check icons and expressions, too
                # TODO - tooltip to hover over word, rather than follow mouse
                # TESTING MOUSE HOVER
                for link in range(len(self.displayed_hyperlinks)):
                    # get the link rect
                    mouse_pos = pygame.mouse.get_pos()
                    link_rect = self.displayed_hyperlinks[link][0]

                    if link_rect.collidepoint(mouse_pos):
                        self.mouse_over_timer += 1  # one per frame
                        self.index_of_active_hyperlink = link
                    else:
                        self.mouse_over_timer = 0  # one per frame

                # TESTING TOOLTIP
                seconds_before_tooltip = 2
                if self.mouse_over_timer / GAME_FPS > seconds_before_tooltip:

                    # get location to show message, and linked text
                    active_link = self.displayed_hyperlinks[self.index_of_active_hyperlink]
                    linked_text = self.message_log.hyperlinks.get(active_link[1])
                    mouse_pos = pygame.mouse.get_pos()
                    text_x = mouse_pos[0] + 20
                    text_y = mouse_pos[1] - font_size

                    # create the text on a surface to get dimensions
                    text_rect = font.render(linked_text, self.colour.white)[1]

                    # move tooltip_rect to the place in the message_log, and resize
                    text_rect.x = text_x
                    text_rect.y = text_y
                    text_rect.inflate_ip(5, 10)

                    # draw the tooltip and text
                    pygame.draw.rect(self.main_surface, self.colour.black, text_rect)
                    font.render_to(self.main_surface, (text_x, text_y), linked_text, self.colour.white)

    def parse_message(self, message):
        """
        Parse for colours, tags and formatting

        Args:
             message (str): The message string that needs parsing.

        Returns:
             List[Tuple[Colour, str]]: List of Tuples containing message and colour
        """

        # break message out by spaces
        message_list = message.split()

        parsed_message_list = []
        default_colour = self.palette.message_log_default_text
        msg_in_progress = ""

        # check each word for inclusion in lists and rebuild as new list
        for message_count in range(len(message_list)):
            msg = message_list[message_count]

            # EXPRESSIONS
            if msg in self.message_log.expressions:

                # expression found so let's deal with any in progress message
                if msg_in_progress != "":
                    # apply currently built string and then increment line
                    parsed_message_list.append((default_colour, msg_in_progress))

                # create the expression as a new message
                colour = self.message_log.expressions.get(msg)
                parsed_message_list.append((colour, msg))

            # ICONS
            elif msg in self.message_log.icons:

                # icon found so let's deal with any in progress message
                if msg_in_progress != "":
                    # apply currently built string and then increment line
                    parsed_message_list.append((default_colour, msg_in_progress))

                # create the icon as a new message
                icon = self.message_log.icons.get(msg)
                parsed_message_list.append((icon, "icon"))

            # HYPERLINKS
            elif msg in self.message_log.hyperlinks:

                # hyperlink found so let's deal with any in progress message
                if msg_in_progress != "":
                    # apply currently built string and then increment line
                    parsed_message_list.append((default_colour, msg_in_progress))

                # amend the colour to indicate the message is a  hyperlink
                parsed_message_list.append((self.palette.message_log_hyperlink, msg))

            # NORMAL TEXT
            else:
                # No match so extend current message line
                if msg_in_progress != "":
                    msg_in_progress += " " + msg
                else:
                    msg_in_progress += msg

        # add any remaining "in progress" messages
        parsed_message_list.append((default_colour, msg_in_progress))

        return parsed_message_list