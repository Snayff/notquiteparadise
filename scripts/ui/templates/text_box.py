import logging
from typing import List

from scripts.core.constants import ICON_IN_TEXT_SIZE
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.widget import Widget
from scripts.ui.templates.widget_style import WidgetStyle


class TextBox(Widget):
    """
    A widget to show text.
    """
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle,  children: List = [],
            name: str = "text_box", text: str = "text"):
        super().__init__(x, y, width, height, base_style, children, name)

        # aesthetics
        self.line_gap = int(self.base_style.font.size / 3)

        if self.base_style.border_size:
            border_size = self.base_style.border_size
        else:
            border_size = 0

        self.max_lines = int((self.rect.height - (border_size * 2)) / (self.base_style.font.size + self.line_gap))

        # state and info
        self.text_list = []
        self.text_to_draw = []
        self.keywords = {}  # TODO - move to library
        self.icons = {}  # TODO - move to library
        self.commands = {}  # TODO - move to library
        self.first_line_index = 0

        # add the initial text
        self.add_text(text)
        self.update_text_shown()

    def add_text(self, text):
        if self.base_style.border_size:
            border_size = self.base_style.border_size
        else:
            border_size = 0
        max_width = self.rect.width - (border_size * 2)  # *2 to offer border on each side
        wrapped_text = self.line_wrap_text(text, self.base_style.font, max_width)
        parsed_text_list = self.parse_text(wrapped_text, self.base_style.font)

        for text in parsed_text_list:
            self.text_list.append(text)

    @staticmethod
    def line_wrap_text(text, font, max_width):
        """
        Break a text into lines based on max_width

        Args:
            font (pygame.font):
            max_width (int):
            text (str): text to wrap

        Returns:
            list[strings]: list of strings comprising wrapped lines of text

        """

        words = text.split()
        line_break = " \n "
        x = 0
        wrapped_text = ""

        # check size of each word and if it extends past total width
        for word in words:
            # add space back to the word
            word += " "

            # if next word is a command then don't add it to calculations
            if word[0] != "#":
                # get size
                palette = Palette().message_log  # Note: can be any palette
                word_surface, world_rect = font.render(word, palette.text_default, palette.background)
                word_width, word_height = word_surface.get_size()

                # if word will run outside of size insert a break
                if x + word_width >= max_width:
                    # start counting new line width
                    x = 0
                    wrapped_text += line_break
            else:
                word_width = 0

            # add current word to new string
            wrapped_text += word
            x += word_width

        return wrapped_text

    def parse_text(self, text, font):
        """
        Check for keywords and commands and apply effects as required.

        Args:
            text ():
            font ():

        Returns:
            list[list[pygame.Surface]] : A list (one per line) containing lists of surfaces for each set of words
        """
        parsed_message_list = []
        palette = Palette().message_log

        # check for new lines
        message_list = text.split("\n")

        # now we have a list of strings, one string per line
        for line_count in range(len(message_list)):
            line_list = []
            outstanding_word_string = ""

            # get the line to work on
            line = message_list[line_count]

            # break line into words
            word_list = line.split()
            processed_indices = []

            # check each word in the line
            for word_count in range(len(word_list)):
                word = word_list[word_count]

                # check index hasn't been processed already (commands look forward...)
                if word_count not in processed_indices:
                    # check for COMMANDS
                    if word[0] == "#":
                        # TODO - handle specifying an end point, e.g. ##, rather than just next word


                        # if any words waiting to be converted to a surface then do so
                        if outstanding_word_string != "":
                            text_surface, text_rect = font.render(outstanding_word_string, palette.text_default)
                            # TODO - use info from base style
                            line_list.append(text_surface)

                            # we've used the outstanding word so clear it
                            outstanding_word_string = ""

                        # check there is a word to process after the command
                        if len(word_list) > word_count + 1:
                            # process the command
                            command = word
                            # get the next word (the one to process) and remove from the list
                            word_to_process = word_list[word_count + 1]
                            text_surface, text_rect = self.process_formatting_command(command, word_to_process, font)
                            line_list.append(text_surface)

                            # note that the next word has already been processed
                            processed_indices.append(word_count + 1)
                        else:
                            logging.warning(f"Text box: Command received {word} with no following word.")

                    # check for KEYWORDS
                    elif word.lower() in self.keywords:
                        # if any words waiting to be converted to a surface then do so
                        if outstanding_word_string != "":
                            text_surface, text_rect = font.render(outstanding_word_string, palette.text_default)
                            line_list.append(text_surface)

                            # we've used the outstanding word so clear it
                            outstanding_word_string = ""

                        # render the key word
                        colour = self.keywords.get(word.lower())
                        text_surface, text_rect = font.render(word + " ", colour)
                        line_list.append(text_surface)

                    # handle NORMAL WORDS
                    else:
                        outstanding_word_string += word + " "

            # handle any remaining word
            if outstanding_word_string != "":
                text_surface, text_rect = font.render(outstanding_word_string, palette.text_default)
                line_list.append(text_surface)

            # add the line_list (of surfaces) to the parsed text list
            parsed_message_list.append(line_list)

        # return the parsed text list (a list, of lists, of surfaces)
        return parsed_message_list

    def process_formatting_command(self, command, word_to_affect, font):
        """
        Process text formatting commands

        Args:
            font ():
            command (str): The command dictating the change. In format of #prefix.suffix
            word_to_affect (str): The word that will be changed by the command

        Returns:
            Tuple(pygame.Surface, pygame.Rect): tuple of surface then rect
        """
        default_text_colour = Palette().message_log.text_default

        # remove the command (#) from the string
        cleaned_command = command.replace("#", "")

        # split command prefix
        command_prefix, command_suffix = cleaned_command.split(".")

        # check which command to execute
        # COLOUR CHANGE
        if command_prefix == "col":
            # get the colour to apply to the text
            if command_suffix in self.commands:
                colour = self.commands[command_suffix]
            else:
                colour = default_text_colour

                log_string = f"Process text command: {cleaned_command} Suffix not understood."
                logging.warning(log_string)

            # create the surface
            new_surface = font.render(word_to_affect, colour)

        # REPLACE WORD WITH AN ICON
        elif command_prefix == "ico":
            icon = self.icons[command_suffix]

            # catch any images not resized and resize them
            if icon.get_size() != (ICON_IN_TEXT_SIZE, ICON_IN_TEXT_SIZE):
                import pygame
                icon = pygame.transform.smoothscale(icon, (ICON_IN_TEXT_SIZE, ICON_IN_TEXT_SIZE))

            # return is expecting surface, rect
            new_surface = icon, icon.get_rect()

        # catch all; render as default
        else:
            new_surface = font.render(word_to_affect, default_text_colour)

        return new_surface

    def update_text_shown(self):
        """
        Update the text in the text box, ensuring correct messages are shown
        """
        # TODO - register / unregister tooltips

        # update first text index
        if len(self.text_list) > self.max_lines:
            self.first_line_index = len(self.text_list) - self.max_lines

        # clear messages to draw
        self.text_to_draw.clear()

        # update text to draw
        text_to_draw = min(self.max_lines, len(self.text_list))
        for counter in range(0, text_to_draw):
            self.text_to_draw.append(self.text_list[counter + self.first_line_index])

    def draw(self, surface):
        """
        Draw the text in the text box, as well as the base style.

        Args:
            surface ():
        """
        style = self.base_style
        style.draw(surface, self.rect)

        # formatting info
        text_indent = 5
        msg_x = style.border_size + text_indent
        msg_y = style.border_size + text_indent
        font = style.font
        font_size = font.size
        line_gap = int(font_size / 3)
        line_count = 0

        # render the messages_to_draw
        for line_list in self.text_to_draw:
            # reset offset
            x_offset = 0

            # get y position of line to write to
            adjusted_y = msg_y + (line_count * (font_size + line_gap))

            # update  line count
            line_count += 1

            # pull each surface from each line_list and render to the panel surface
            for text in line_list:
                surface.blit(text, (msg_x + x_offset, adjusted_y))
                message_width = text.get_width()
                x_offset += message_width + 2  # 2 for space between words