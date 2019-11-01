import logging

from scripts.core.constants import UIElements, ICON_IN_TEXT_SIZE
from scripts.core.fonts import Font


class MessageMethods:
    """
    Methods for taking actions with messages

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.ui_manager import UIManager
        self.manager = manager  # type: UIManager

    def init_keywords(self):
        """
        Initialise the keywords for highlighting in the message log

        Returns:
            dict[str, Tuple[int, int, int]]: keyword: colour

        """
        keywords = {}
        palette = self.manager.Palette.message_log

        keywords["grazes"] = palette.keyword_grazes
        keywords["crits"] = palette.keyword_crits

        message_log = self.manager.Element.get_ui_element(UIElements.MESSAGE_LOG)
        message_log.keywords = keywords

    def init_icons(self):
        """
        Load the list of icons

        Returns:
            Dict[str, pygame.Surface]
        """
        icons = {}

        import pygame
        icons["info"] = pygame.image.load("assets/icons/placeholder/book.PNG").convert_alpha()

        message_log = self.manager.Element.get_ui_element(UIElements.MESSAGE_LOG)
        message_log.icons = icons

    def init_commands(self):
        """
        Initialise the commands
        """
        commands = {}
        palette = self.manager.Palette.message_log

        commands["negative"] = palette.text_negative
        commands["positive"] = palette.text_positive
        commands["info"] = palette.text_info

        message_log = self.manager.Element.get_ui_element(UIElements.MESSAGE_LOG)
        message_log.commands = commands

    def add_message(self, message):
        """
        Add a message to the message log. Includes processing of the message.

        Args:
            message (str):
        """
        try:
            message_log = self.manager.Element.get_ui_element(UIElements.MESSAGE_LOG)

            # text wrap message
            max_width = message_log.panel.width - (message_log.message_indent * 2)  # *2 to offer border on each side
            font = self.manager.Font.message_log
            wrapped_message = self.line_wrap_message(message, font, max_width)

            # parse message
            parsed_message_list = self.parse_message_and_convert_to_surface(wrapped_message, font)

            # add each line to the main message list
            for message in parsed_message_list:
                message_log.message_list.append(message)

            self.update_messages_shown()

            # flag need to update
            message_log.is_dirty = True

        except KeyError:
            logging.debug(f"Tried to set message in MessageLog but key not found. Is the MessageLog init'd?")

    def line_wrap_message(self, message, font, max_width):
        """
        Break a message into lines based on panel width

        Args:
            font (pygame.font):
            max_width (int):
            message (str): message to wrap

        Returns:
            list[strings]: list of strings comprising wrapped lines of text

        """

        words = message.split()
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
                palette = self.manager.Palette.message_log  # Note: can be any palette
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

    def parse_message_and_convert_to_surface(self, message, font):
        """
        Check for keywords and commands and apply effects as required.

        Args:
            message ():
            font ():

        Returns:
            list[list[pygame.Surface]] : A list (one per line) containing lists of surfaces for each set of words
        """
        message_log = self.manager.Element.get_ui_element(UIElements.MESSAGE_LOG)
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
            processed_indices = []

            palette = self.manager.Palette.message_log

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
                            line_list.append(text_surface)

                            # we've used the outstanding word so clear it
                            outstanding_word_string = ""

                        # check there is a word to process after the command
                        if len(word_list) > word_count + 1:
                            # process the command
                            command = word
                            # get the next word (the one to process) and remove from the list
                            word_to_process = word_list[word_count + 1]
                            text_surface, text_rect = self.process_message_command(command, word_to_process, font)
                            line_list.append(text_surface)

                            # note that the next word has already been processed
                            processed_indices.append(word_count + 1)
                        else:
                            logging.warning(f"Message log: Command received {word} with no following word.")

                    # check for KEYWORDS
                    elif word.lower() in message_log.keywords:
                        # if any words waiting to be converted to a surface then do so
                        if outstanding_word_string != "":
                            text_surface, text_rect = font.render(outstanding_word_string, palette.text_default)
                            line_list.append(text_surface)

                            # we've used the outstanding word so clear it
                            outstanding_word_string = ""

                        # render the key word
                        colour = message_log.keywords.get(word.lower())
                        text_surface, text_rect = font.render(word + " ", colour)
                        line_list.append(text_surface)

                    # handle NORMAL WORDS
                    else:
                        outstanding_word_string += word + " "

            # handle any remaining word
            if outstanding_word_string != "":
                text_surface, text_rect = font.render(outstanding_word_string, palette.text_default)
                line_list.append(text_surface)

            # add the line_list (of surfaces) to the parsed message list
            parsed_message_list.append(line_list)

        # return the parsed message list (a list, of lists, of surfaces)
        return parsed_message_list

    def process_message_command(self, command, word_to_affect, font):
        """
        Process text formatting commands

        Args:
            font ():
            command (str): The command dictating the change. In format of #prefix.suffix
            word_to_affect (str): The word that will be changed by the command

        Returns:
            Tuple(pygame.Surface, pygame.Rect): tuple of surface then rect
        """
        default_text_colour = self.manager.Palette.message_log.text_default

        try:
            message_log = self.manager.Element.get_ui_element(UIElements.MESSAGE_LOG)

            # remove the hash from the string
            cleaned_command = command.replace("#", "")

            # split command prefix
            command_prefix, command_suffix = cleaned_command.split(".")

            # check which command to execute
            # COLOUR CHANGE
            if command_prefix == "col":
                # get the colour to apply to the text
                if command_suffix in message_log.commands:
                    colour = message_log.commands[command_suffix]
                else:
                    colour = default_text_colour

                    log_string = f"Process message command: {cleaned_command} Suffix not understood."
                    logging.warning(log_string)

                # create the surface
                new_surface = font.render(word_to_affect, colour)

            # REPLACE WORD WITH AN ICON
            elif command_prefix == "ico":
                icon = message_log.icons[command_suffix]

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

        except KeyError:
            logging.debug(f"Tried to parse message command in MessageLog but key not found.")
            new_surface = font.render(word_to_affect, default_text_colour)

            return new_surface

    def update_messages_shown(self):
        """
        Update the message log, ensuring correct messages are shown
        """
        # TODO - register / unregister tooltips

        try:
            message_log = self.manager.Element.get_ui_element(UIElements.MESSAGE_LOG)

            # update first message index
            if len(message_log.message_list) > message_log.number_of_messages_to_show:
                message_log.first_message_index = len(message_log.message_list) - message_log.number_of_messages_to_show

            # clear messages to draw
            message_log.messages_to_draw.clear()

            # update message to draw
            messages_to_show = min(message_log.number_of_messages_to_show, len(message_log.message_list))
            for counter in range(0, messages_to_show):
                message_log.messages_to_draw.append(message_log.message_list[counter + message_log.first_message_index])

        except KeyError:
            logging.debug(f"Tried to update messages shown in MessageLog but key not found.")

