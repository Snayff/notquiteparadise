
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.widget import Widget
from scripts.ui.templates.widget_style import WidgetStyle


class TextBox(Widget):
    """
    A widget to show text.
    """
    def __init__(self, x: int, y: int, width: int, height: int, base_style: WidgetStyle, text: str = "text"):
        super().__init__(x, y, width, height, base_style)

        self.text_list = []
        self.text_to_draw = []
        self.first_line_index = 0
        self.line_gap = int(self.base_style.font.size / 3)

        if self.base_style.border_size:
            border_size = self.base_style.border_size
        else:
            border_size = 0

        self.max_lines = int((self.height - (border_size * 2)) / (self.base_style.font.size + self.line_gap))

        self.add_text(text)
        self.update_text_shown()

    def add_text(self, text):
        if self.base_style.border_size:
            border_size = self.base_style.border_size
        else:
            border_size = 0
        max_width = self.width - (border_size * 2)  # *2 to offer border on each side
        wrapped_text = self.line_wrap_text(text, self.base_style.font, max_width)
        parsed_text_list = self.parse_text(wrapped_text, self.base_style.font)

        for text in parsed_text_list:
            self.text_list.append(text)

    def line_wrap_text(self, message, font, max_width):
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

    def parse_text(self, message, font):
        """
        Check for keywords and commands and apply effects as required.

        Args:
            message ():
            font ():

        Returns:
            list[list[pygame.Surface]] : A list (one per line) containing lists of surfaces for each set of words
        """
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

            palette = Palette().message_log

            # check each word in the line
            for word_count in range(len(word_list)):
                word = word_list[word_count]

                # check index hasn't been processed already (commands look forward...)
                if word_count not in processed_indices:
                    outstanding_word_string += word + " "

            # handle any remaining word
            if outstanding_word_string != "":
                text_surface, text_rect = font.render(outstanding_word_string, palette.text_default)
                line_list.append(text_surface)

            # add the line_list (of surfaces) to the parsed message list
            parsed_message_list.append(line_list)

        # return the parsed message list (a list, of lists, of surfaces)
        return parsed_message_list

    def update_text_shown(self):
        """
        Update the text in the text box, ensuring correct messages are shown
        """
        # TODO - register / unregister tooltips

        # update first message index
        if len(self.text_list) > self.max_lines:
            self.first_line_index = len(self.text_list) - self.max_lines

        # clear messages to draw
        self.text_to_draw.clear()

        # update message to draw
        text_to_draw = min(self.max_lines, len(self.text_list))
        for counter in range(0, text_to_draw):
            self.text_to_draw.append(self.text_list[counter + self.first_line_index])


    def draw(self, surface):
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