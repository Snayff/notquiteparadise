from scripts.core.constants import LoggingEventTypes, EventTopics
from scripts.core.global_data import game_manager, ui_manager
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber


class UiHandler(Subscriber):
    """
    Handle events that effect the UI
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "ui_handler", event_hub)

    def run(self, event):
        """
        Process the events
        """

        # log that event has been received
        log_string = f"{self.name} received {event.type}"
        game_manager.create_event(LoggingEvent(LoggingEventTypes.MUNDANE, log_string))

        if event.topic == EventTopics.ENTITY:
            self.hide_entity_info()

    @staticmethod
    def hide_entity_info():
        """
        Hide the entity info panel
        """
        ui_manager.entity_info.set_visibility(False)
        log_string = f"Entity info hidden."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.MUNDANE, log_string))