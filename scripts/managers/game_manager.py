import logging
import pygame
from scripts.core.constants import GameStates, VisualInfo


class GameManager:
    """
    Manager of Game Functions and data, such as the window details
    """
    def __init__(self):
        self.game_state = GameStates.GAME_INITIALISING
        self.previous_game_state = GameStates.GAME_INITIALISING
        self.internal_clock = pygame.time.Clock()

        logging.info( f"GameManager initialised.")

    def update(self):
        """
        Update the GameManager:
            internal_clock ticks
        """

        # set frame rate
        self.internal_clock.tick(VisualInfo.GAME_FPS)

    def update_game_state(self, new_game_state):
        """

        Args:
            new_game_state:
        """
        self.previous_game_state = self.game_state
        self.game_state = new_game_state

        log_string = f"Game_state updated from {self.previous_game_state} to {self.game_state}"
        logging.info(log_string)


game = GameManager()