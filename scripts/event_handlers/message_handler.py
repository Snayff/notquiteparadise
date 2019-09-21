
import logging

from scripts.global_singletons.managers import ui_manager
from scripts.event_handlers.pub_sub_hub import Subscriber


class MessageHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "message_handler", event_hub)

    def run(self, event):
        log_string = f"{self.name} received {event.event_type}..."
        logging.debug(log_string)

        ui_manager.Message.add_message(event.message)