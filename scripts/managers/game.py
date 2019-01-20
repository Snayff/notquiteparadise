import pygame

from scripts.core.constants import GameStates, LoggingEventTypes, GAME_FPS
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import EventHub, Publisher


class GameManager:

    def __init__(self):
        self.game_state = GameStates.GAME_INITIALISING
        self.previous_game_state = GameStates.GAME_INITIALISING
        self.event_hub = EventHub()
        self.internal_clock = pygame.time.Clock()

    def update(self):
        self.event_hub.update()

        # set frame rate
        self.internal_clock.tick(GAME_FPS)

    def update_game_state(self, new_game_state):
        """
        :type new_game_state: Code.Core.constants.GameStates
        """
        self.previous_game_state = self.game_state
        self.game_state = new_game_state

        log_string = f"game_state updated to {self.game_state} from {self.previous_game_state}"
        self.create_event(LoggingEvent(LoggingEventTypes.MUNDANE, log_string))

    def create_event(self, event):
        pub = Publisher(self.event_hub)
        pub.publish(event)