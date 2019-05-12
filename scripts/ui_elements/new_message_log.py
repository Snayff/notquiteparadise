import textwrap
from typing import Dict, Tuple

from scripts.core.constants import MessageEventTypes, BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT, LoggingEventTypes
from scripts.core.fonts import Font
from scripts.events.logging_events import LoggingEvent
from scripts.ui_elements.colours import Colour
from scripts.ui_elements.palette import Palette
from scripts.ui_elements.templates.panel import Panel


class NewMessageLog:
    """
    Store messages, and related functionality, to be shown in the message log.

    Attributes:
        palette (Palette): Palette of Colours
        message_list (List(Tuple(MessageEventTypes, string))):  list of messages and their type
        message_type_to_show  (MessageEventTypes): Type of message to show in log
        expressions  (Dict): Dictionary of expressions to look for and their colour to show.
        icons (Dict): Dictionary of icons to look for and the icon to show.
        hyperlinks (Dict): Dictionary of hyperlinks to look for and the linked info to show.
        is_dirty
        displayed_hyperlinks
        index_of_active_hyperlink
    """

    def __init__(self):
        # log setup
        self.font = Font().message_log
        self.colour = Colour()
        self.palette = Palette().message_log
        self.message_list = []
        self.messages_to_draw = []
        self.keywords = {}  # type: Dict[str, Tuple[int, int, int]]
        self.is_dirty = True

        # panel info
        panel_width = int((BASE_WINDOW_WIDTH / 4) * 1)
        panel_height = int(BASE_WINDOW_HEIGHT / 2)
        panel_x = BASE_WINDOW_WIDTH - panel_width
        panel_y = BASE_WINDOW_HEIGHT - panel_height
        panel_border = 2
        panel_background_colour = self.palette.background
        panel_border_colour = self.palette.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

        # set panel to be rendered
        from scripts.core.global_data import ui_manager
        ui_manager.update_panel_visibility("message_log", self, True)

        # log info
        self.edge_size = 1
        self.message_indent = 5
        self.gap_between_lines = int(self.font.size / 3)
        self.first_message_index = 0
        self.number_of_messages_to_show = int((panel_height - 2 * self.edge_size) / (self.font.size +
                                                                                     self.gap_between_lines))

        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, f"MessageLog initialised."))

    def update(self):
        if self.is_dirty:
            # update first message index
            if len(self.message_list) > self.number_of_messages_to_show:
                self.first_message_index = len(self.message_list) - self.number_of_messages_to_show

            # clear messages to draw
            self.messages_to_draw.clear()

            # update message to draw
            messages_to_show = min(self.number_of_messages_to_show, len(self.message_list))
            for counter in range(0, messages_to_show):
                self.messages_to_draw.append(self.message_list[counter + self.first_message_index])

    def draw(self, surface):
        """
        Draw the message log and all included text and icons
        Args:
            surface(Surface): Main surface to draw to.
        """
        # get the surface to draw to
        panel_surface = self.panel.surface

        # panel background
        self.panel.draw_background()

        # init info for message render
        msg_x = self.edge_size + self.message_indent
        msg_y = self.edge_size
        font = self.font
        font_size = font.size
        line_count = 0

        # render the messages_to_draw
        for line_list in self.messages_to_draw:
            # reset offset
            x_offset = 0

            # get y position of line to write to
            adjusted_y = msg_y + (line_count * (font_size + self.gap_between_lines))

            # update  line count
            line_count += 1

            # pull each surface from each line_list and render to the panel surface
            for message in line_list:
                panel_surface.blit(message, (msg_x + x_offset, adjusted_y))
                message_width = message.get_width()
                x_offset += message_width + 2  # 2 for space between words

        # panel border
        self.panel.draw_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

    def add_message(self, message_type, message):

        # TODO - remove message_type

        surface = None

        # text wrap message
        wrapped_message = self.text_wrap_message(message)

        # parse message
        parsed_message_list = self.parse_message_and_convert_to_surface(wrapped_message)

        # add each line to the main message list
        for message in parsed_message_list:
            self.message_list.append(message)

        # flag need to update
        self.is_dirty = True


    def text_wrap_message(self, message):

        return textwrap.fill(message, self.panel.width - self.message_indent)

    def parse_message_and_convert_to_surface(self, message):

        parsed_message_list = []

        # check for new lines
        message_list = message.split("\n")

        # now we have a list of strings, one string per line
        for line_count in range(len(message_list)):
            line_list = []
            outstanding_word_string = ""

            # get the line to work on
            line = message_list[line_count]

            # break line into words
            word_list = line.split()

            # check each word in the line
            for word_count in range(len(word_list)):
                word = word_list[word_count] + " "

                # check for COMMANDS
                if word[0] == "[":

                    # if any words waiting to be converted to a surface then do so
                    if outstanding_word_string != "":
                        text_surface = self.font.render(outstanding_word_string, self.palette.default_text)
                        line_list.append(text_surface)

                    # check there is a word to process after the command
                    if len(word_list) > word_count + 1:
                        # process the command
                        command = word
                        # get the next word (the one to process) and remove from the list
                        word_to_process = word_list.pop(word_count + 1)
                        text_surface, text_bounding_rect = self.process_message_command(command, word_to_process)
                        line_list.append(text_surface)

                # check for KEYWORDS
                elif word in self.keywords:
                    # if any words waiting to be converted to a surface then do so
                    if outstanding_word_string != "":
                        text_surface, text_bounding_rect = self.font.render(outstanding_word_string,
                                                                            self.palette.default_text)
                        line_list.append(text_surface)

                    # render the key word
                    colour = self.keywords.get(word)
                    text_surface, text_bounding_rect = self.font.render(word, colour)
                    line_list.append(text_surface)

                # handle NORMAL WORDS
                else:
                    outstanding_word_string += word

            # handle any remaining word
            if outstanding_word_string != "":
                text_surface, text_bounding_rect = self.font.render(outstanding_word_string, self.palette.default_text)
                line_list.append(text_surface)

            # add the line_list (of surfaces) to the parsed message list
            parsed_message_list.append(line_list)

        # return the parsed message list (a list, of lists, of surfaces)
        return parsed_message_list



    def process_message_command(self, command, word_to_process):
        text_surface = ""
        return text_surface