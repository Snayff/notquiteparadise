
import logging

from scripts.global_singletons.managers import ui
from scripts.event_handlers.pub_sub_hub import Subscriber


class MessageHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "message_handler", event_hub)

    def run(self, event):
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}...")

        ui.Element.add_to_message_log(event.message)