from scripts.core.constants import GameEventNames, EventTopics
from scripts.events.pub_sub_hub import Event


class EndTurnEvent(Event):
    def __init__(self, time_spent):
        Event.__init__(self, GameEventNames.END_TURN, EventTopics.GAME)
        self.time_spent = time_spent


class ExitEvent(Event):
    def __init__(self):
        Event.__init__(self, GameEventNames.EXIT, EventTopics.GAME)
