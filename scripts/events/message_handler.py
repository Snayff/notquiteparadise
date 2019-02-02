from scripts.core.constants import LoggingEventTypes, EventTopics
from scripts.core.global_data import game_manager, ui_manager
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber, Event


class MessageHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "message_handler", event_hub)

    def run(self, event):
        log_string = f"{self.name} received {event.type}"
        game_manager.create_event(LoggingEvent(LoggingEventTypes.MUNDANE, log_string))

        ui_manager.message_log.add_message(event.type, event.message)
        ui_manager.message_log_is_dirty = True