import pygame

from scripts.core.constants import GameStates, LoggingEventTypes, GAME_FPS
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher
from scripts.managers.game_methods.affliction_action import AfflictionAction
from scripts.managers.game_methods.skill_action import SkillAction
from scripts.managers.game_methods.skill_query import SkillQuery


class GameManager:
    """
    Manager of Game Functions
    """
    def __init__(self):
        self.game_state = GameStates.GAME_INITIALISING
        self.previous_game_state = GameStates.GAME_INITIALISING
        self.internal_clock = pygame.time.Clock()
        self.skill_action = SkillAction(self)
        self.skill_query = SkillQuery(self)
        self.affliction_action = AfflictionAction(self)

        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, f"GameManager initialised."))

    def update(self):
        """
        Update the GameManager:
            internal_clock ticks
        """

        # set frame rate
        self.internal_clock.tick(GAME_FPS)

    def update_game_state(self, new_game_state):
        """

        Args:
            new_game_state:
        """
        self.previous_game_state = self.game_state
        self.game_state = new_game_state

        log_string = f"Game_state updated to {self.game_state} from {self.previous_game_state}"
        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))