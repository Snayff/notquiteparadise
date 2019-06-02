from scripts.core.constants import EventTopics
from scripts.events.pub_sub_hub import Event


class LoggingEvent(Event):
    def __init__(self, logging_type,  log_string):
        Event.__init__(self, logging_type, EventTopics.LOGGING)
        self.log_string = log_string
