from scripts.core.constants import EventTopics
from scripts.events.pub_sub_hub import Event


class MessageEvent(Event):
    def __init__(self, type,  message):
        Event.__init__(self, type, EventTopics.MESSAGE)
        self.message = message