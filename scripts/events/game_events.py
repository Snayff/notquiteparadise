from scripts.core.constants import GameEventTypes, EventTopics
from scripts.events.pub_sub_hub import Event


class EndTurnEvent(Event):
    def __init__(self, time_spent):
        Event.__init__(self, GameEventTypes.END_TURN, EventTopics.GAME)
        self.time_spent = time_spent


class ExitEvent(Event):
    def __init__(self):
        Event.__init__(self, GameEventTypes.EXIT, EventTopics.GAME)
