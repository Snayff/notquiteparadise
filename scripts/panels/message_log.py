import pygame

from scripts.core.colours import Palette
from scripts.core.constants import MessageEventTypes, LoggingEventTypes
from scripts.core.fonts import Font
from scripts.events.logging_events import LoggingEvent


class MessageLog:
    def __init__(self):
        # log setup
        self.palette = Palette()
        self.message_list = [(MessageEventTypes.BASIC, "Welcome to Not Quite Paradise")]
        self.message_type_to_show = MessageEventTypes.BASIC
        self.expressions = self.create_expressions_list()
        self.icons = self.create_icons_list()
        self.hyperlinks = self.create_hyperlinks_list()

        # panel info
        self.font = Font().message_log
        self.panel_x = 0
        self.panel_y = 400
        self.panel_width = 400  # TODO remove magic numbers
        self.panel_height = 200
        self.border_size = 3
        self.message_indent = 10
        self.background_colour = self.palette.message_log_background

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

        expressions["orc"] = self.palette.message_log_expressions_player

        return expressions

    def create_icons_list(self):
        """
        Create list of icons to look for in log and render

        Returns:
            Dict
        """
        icons = {}

        icons["player"] = pygame.image.load("assets/actor/player.png")

        return icons

    def create_hyperlinks_list(self):
        """
        Create list of hyperlinks to look for in log and render

        Returns:
            Dict
        """
        hyperlinks = {}

        hyperlinks["deals"] = "This is linked text"

        return hyperlinks