from scripts.core.constants import GameEventTypes, EventTopics
from scripts.event_handlers.pub_sub_hub import Event


class EndTurnEvent(Event):
    def __init__(self, time_spent):
        Event.__init__(self, GameEventTypes.END_TURN, EventTopics.GAME)
        self.time_spent = time_spent


class ExitEvent(Event):
    def __init__(self):
        Event.__init__(self, GameEventTypes.EXIT, EventTopics.GAME)


class ChangeGameStateEvent(Event):
    def __init__(self, new_game_state, skill_to_be_used=None):
        Event.__init__(self, GameEventTypes.CHANGE_GAME_STATE, EventTopics.GAME)
        self.new_game_state = new_game_state
        self.skill_to_be_used = skill_to_be_used