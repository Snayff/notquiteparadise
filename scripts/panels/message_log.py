import pygame

from scripts.core.colours import Palette, Colour
from scripts.core.constants import MessageEventTypes, LoggingEventTypes, GAME_FPS
from scripts.core.fonts import Font
from scripts.events.logging_events import LoggingEvent


class MessageLog:
    """
    Store messages, and related functionality, to be shown in the message log.

    Attributes:
        palette (Palette): Palette of Colours
        message_list (List(Tuple(MessageEventTypes, string))):  list of messages and their type
        message_type_to_show  (MessageEventTypes): Type of message to show in log
        expressions  (Dict): Dictionary of expressions to look for and their colour to show.
        icons (Dict): Dictionary of icons to look for and the icon to show.
        hyperlinks (Dict): Dictionary of hyperlinks to look for and the linked info to show.
        show
        is_dirty
        displayed_hyperlinks
        index_of_active_hyperlink
    """
    def __init__(self):
        # log setup
        self.colour = Colour()
        self.palette = Palette()
        self.message_list = [(MessageEventTypes.BASIC, "Welcome to Not Quite Paradise")]
        self.message_type_to_show = MessageEventTypes.BASIC
        self.expressions = self.create_expressions_list()
        self.icons = self.create_icons_list()
        self.hyperlinks = self.create_hyperlinks_list()
        self.show = True

        # hyperlink info
        self.is_dirty = True
        self.displayed_hyperlinks = []
        self.index_of_active_hyperlink = -1

        # tooltip info # TODO - move to tooltip class when there is one
        self.seconds_before_tooltip = 0.2
        self.seconds_before_extended_text = 1


        # panel info
        self.font = Font().message_log
        self.panel_x = 0
        self.panel_y = 400
        self.panel_width = 400  # TODO remove magic numbers
        self.panel_height = 200
        self.border_size = 3
        self.message_indent = 10

        # log info
        self.gap_between_lines = 8
        self.first_message_to_show = 0
        self.number_of_messages_to_show = int((self.panel_height - 2 * self.border_size) / (self.font.size +
                                                                                self.gap_between_lines))

    def add_message(self, message_type, message):
        """
        Add a message to the MessageLog
        Args:
            message_type:
            message:
        """
        log_string = f"{message} added to message log"
        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventTypes.MUNDANE, log_string))

        self.message_list.append((message_type, message))

        # if more mesaages than we can show at once then increment first message position
        if len(self.message_list) > self.number_of_messages_to_show:
            self.update_first_message_position(1)

    def update_first_message_position(self, increment):
        #  prevent the first message going too far and showing less than max number of message_list to show
        self.first_message_to_show = min(self.first_message_to_show + increment, len(self.message_list) -
                                                                                 self.number_of_messages_to_show)

        # ensure first message position cannot be less than the start of the message_list
        self.first_message_to_show = max(self.first_message_to_show, 0)

    def change_message_type_to_show(self, message_type):
        self.message_type_to_show = message_type

    def create_expressions_list(self):
        """
        Create list of expressions to look for in log and apply formatting

        Returns:
            Dict
        """
        expressions = {}

        expressions["fighter"] = self.palette.message_log.expressions_player
        expressions["moved"] = self.palette.message_log.expressions_player

        return expressions

    def create_icons_list(self):
        """
        Create list of icons to look for in log and render

        Returns:
            Dict
        """
        icons = {}

        icons["player"] = pygame.image.load("assets/actor/player.png")
        icons["orc"] = pygame.image.load("assets/actor/enemy.png")

        return icons

    def create_hyperlinks_list(self):
        """
        Create list of hyperlinks to look for in log and render

        Returns:
            Dict
        """
        hyperlinks = {}

        hyperlinks["deals"] = ("This is linked text", "This is the extended linked text")
        hyperlinks["damage"] = ("2nd linked text", "2nd extended")

        return hyperlinks

    def check_mouse_over_link(self):
        # TODO - increment displayed_hyperlinks rect positions when new lines added

        for link in range(len(self.displayed_hyperlinks)):
            # get the link rect
            mouse_pos = pygame.mouse.get_pos()
            link_rect = self.displayed_hyperlinks[link][0]
            link_text = self.displayed_hyperlinks[link][1]
            link_mouse_over_timer = self.displayed_hyperlinks[link][2]

            # check mouse is over the lnk
            if link_rect.collidepoint(mouse_pos):
                # replace tuple with new one that has updated timer value
                self.displayed_hyperlinks[link] = (link_rect, link_text, link_mouse_over_timer + 1)
                self.index_of_active_hyperlink = link
                # TESTING TIMING OVER HOVER OVER  # FIXME - timing isnt working, ~30 frames is 1 sec
                #print(f"{link_mouse_over_timer + 1}")
                #from datetime import datetime
                #print(datetime.now().time())
            else:
                self.displayed_hyperlinks[link] = (link_rect, link_text, 0)

    def get_active_tooltip(self):
        """
        Get the info from the active tooltip, if there is one

        Returns:
            List: Either empty or contains text_rect, tooltip_text, extended_text_x, extended_text_y,
            extended_tooltip_text

        """
        font_size = self.font.size

        # is there an active link?
        if self.index_of_active_hyperlink >= 0:

            # init extended info, in case we don't load the real stuff
            text_rect = -1
            tooltip_text = ""
            extended_text_x = -1
            extended_text_y = -1
            extended_tooltip_text = ""

            # how long have we been hovering over it?
            seconds_hovering = self.displayed_hyperlinks[self.index_of_active_hyperlink][2] / GAME_FPS

            # is it long enough?
            if seconds_hovering > self.seconds_before_tooltip:
                #print(f"SHOW TOOLTIP")

                # get linked text
                active_link = self.displayed_hyperlinks[self.index_of_active_hyperlink]
                hyperlink_strings = self.hyperlinks.get(active_link[1])
                tooltip_text = hyperlink_strings[0]

                # get location to show message
                text_x = active_link[0].x + 20
                text_y = active_link[0].y - font_size

                # create the text on a surface to get dimensions
                text_rect = self.font.render(tooltip_text, self.colour.white)[1]

                # move tooltip_rect to the place in the message_log
                text_rect.x = text_x
                text_rect.y = text_y

                # is it time for the extended text?
                if seconds_hovering > self.seconds_before_extended_text:
                    #print(f"SHOW EXTENDED TOOLTIP")
                    extended_tooltip_text = hyperlink_strings[1]

                    # create the text on a surface to get dimensions
                    extended_text_rect = self.font.render(extended_tooltip_text, self.colour.white)[1]

                    # move tooltip_rect to the place in the message_log, adjusting to be below first tooltip
                    extended_text_x = text_x
                    extended_text_y = text_y + font_size
                    extended_text_rect.x = extended_text_x
                    extended_text_rect.y = extended_text_y

                    # align the tooltip rects
                    width_of_widest_rect = max(text_rect.width, extended_text_rect.width)
                    text_rect.width = width_of_widest_rect
                    text_rect.height = text_rect.height + extended_text_rect.height

                # resize the rect in place
                text_rect.inflate_ip(5, 10)

                return [text_rect, tooltip_text, extended_text_x, extended_text_y, extended_tooltip_text]
            else:
                return []
        else:
            return []

    def parse_message(self, message):
        """
        Parse for colours, tags and formatting

        Args:
             message (str): The message string that needs parsing.

        Returns:
             List[Tuple[Colour, str]]: List of Tuples containing message and colour
        """

        updated_message = message

        # add spaces around special chars
        for char in ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', '\'']:
            if char in message:
                updated_message = message.replace(char, " " + char)

        # break message out by spaces
        message_list = updated_message.split()

        parsed_message_list = []
        default_colour = self.palette.message_log.default_text
        msg_in_progress = ""

        # check each word for inclusion in lists and rebuild as new list
        for message_count in range(len(message_list)):

            msg = message_list[message_count]

            # EXPRESSIONS
            if msg in self.expressions:

                # expression found so let's deal with any in progress message
                if msg_in_progress != "":
                    # apply currently built string and then increment line
                    parsed_message_list.append((default_colour, msg_in_progress))
                    msg_in_progress = ""

                # create the expression as a new message
                colour = self.expressions.get(msg)
                parsed_message_list.append((colour, msg))

            # ICONS
            elif msg in self.icons:

                # icon found so let's deal with any in progress message
                if msg_in_progress != "":
                    # apply currently built string and then increment line
                    parsed_message_list.append((default_colour, msg_in_progress))
                    msg_in_progress = ""

                # create the icon as a new message
                icon = self.icons.get(msg)
                parsed_message_list.append((icon, "icon"))

            # HYPERLINKS
            elif msg in self.hyperlinks:

                # hyperlink found so let's deal with any in progress message
                if msg_in_progress != "":
                    # apply currently built string and then increment line
                    parsed_message_list.append((default_colour, msg_in_progress))
                    msg_in_progress = ""

                # amend the colour to indicate the message is a  hyperlink
                parsed_message_list.append((self.palette.message_log.hyperlink, msg))

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