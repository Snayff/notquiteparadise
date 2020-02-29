from typing import Type

from scripts.core.constants import EventTopics, GameStates
from scripts.core.event_hub import Event


class EndTurnEvent(Event):
    """
    Event to end an entities ability to act.

    Args:
        entity(Entity):
        time_spent(int):

    """
    def __init__(self, entity, time_spent):
        Event.__init__(self, "END_TURN", EventTopics.GAME)
        self.entity = entity
        self.time_spent = time_spent


class ExitGameEvent(Event):
    """
    Event to exit the game
    """
    def __init__(self):
        Event.__init__(self, "EXIT", EventTopics.GAME)


class ChangeGameStateEvent(Event):
    """
    Event to change the current game state
    """
    def __init__(self, new_game_state: Type[GameStates], skill_to_be_used: str = None):
        Event.__init__(self, "CHANGE_GAME_STATE", EventTopics.GAME)
        self.new_game_state = new_game_state
        self.skill_to_be_used = skill_to_be_used


class EndRoundEvent(Event):
    """
    Event to process the end of a round
    """
    def __init__(self):
        Event.__init__(self, "END_ROUND", EventTopics.GAME)