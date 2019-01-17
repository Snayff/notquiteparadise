from scripts.core.constants import LoggingEventNames, EventTopics
from scripts.core.global_data import game_manager
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber, Event


class MessageHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "message_handler", event_hub)

    def run(self, event):
        log_string = f"{self.name} received {event.name}"
        game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

    # TODO add message to message log