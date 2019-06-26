import logging
import time

from scripts.core.constants import LoggingEventTypes
from scripts.event_handlers.pub_sub_hub import Subscriber


class LoggingHandler(Subscriber):
    def __init__(self, event_hub):
        super().__init__("logging_handler", event_hub)

        self.log_file_name = "logs/" + "game.log"
        self.log_level = logging.DEBUG
        self.file_mode = "w"
            # File mode options:
            # 'r' - open for reading(default)
            # 'w' - open for writing, truncating the file first
            # 'x' - open for exclusive creation, failing if the file already exists
            # 'a' - open for writing, appending to the end of the file if it exists

        logging.basicConfig(filename=self.log_file_name, filemode=self.file_mode, level=self.log_level,
                            format="%(asctime)s| %(levelname)-8s| %(message)s")
                            # 8 adds space for 8 characters (CRITICAL)
        logging.Formatter.converter = time.gmtime


    def run(self, event):
        # Note: Does not create a log entry. Doing so causes infinite loops. Don't do that.
        if event.type == LoggingEventTypes.CRITICAL:
            self.process_critical_logging_event(event)
        elif event.type == LoggingEventTypes.ERROR:
            self.process_error_logging_event(event)
        elif event.type == LoggingEventTypes.WARNING:
            self.process_warning_logging_event(event)
        elif event.type == LoggingEventTypes.INFO:
            self.process_info_logging_event(event)
        elif event.type == LoggingEventTypes.DEBUG:
            self.process_debug_logging_event(event)

    def process_critical_logging_event(self, event):
        logging.critical(event.log_string)

    def process_error_logging_event(self, event):
        logging.error(event.log_string)

    def process_warning_logging_event(self, event):
        logging.warning(event.log_string)

    def process_info_logging_event(self, event):
        logging.info(event.log_string)

    def process_debug_logging_event(self, event):
        logging.debug(event.log_string)