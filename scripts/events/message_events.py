
from scripts.core.constants import EventTopics
from scripts.event_handlers.pub_sub_hub import Event


class MessageEvent(Event):
    def __init__(self, event_type,  message):
        Event.__init__(self, event_type, EventTopics.MESSAGE)
        self.message = message