from scripts.core.colours import Palette
from scripts.core.constants import MessageEventTypes, LoggingEventTypes
from scripts.core.fonts import Font
from scripts.events.logging_events import LoggingEvent


class MessageLog:
    def __init__(self):
        # log setup
        self.palette = Palette()
        self.messages = [(MessageEventTypes.BASIC, "Welcome to Not Quite Paradise")]
        self.message_type_to_show = MessageEventTypes.BASIC

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
        self.gap_between_lines = 4
        self.message_log_first_message_to_show = 0
        self.number_of_messages_to_show = int((self.panel_height - 2 * self.border_size) / (self.font.size +
                                                                                self.gap_between_lines))

    def add_message(self, message_type, message):
        log_string = f"{message} added to message log"
        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventTypes.MUNDANE, log_string))

        self.messages.append((message_type, message))

    def update_message_logs_first_message(self, increment):
        # TODO add limits to ensure stays in length of array
        self.message_log_first_message_to_show += increment

    def change_message_type_to_show(self, message_type):
        self.message_type_to_show = message_type

