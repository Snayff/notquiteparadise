import logging
import pygame
from scripts.core.constants import GameStates
from scripts.managers.input_methods.config_methods import ConfigMethods
from scripts.managers.input_methods.intents import Intents
from scripts.managers.input_methods.control_methods import ControlMethods


class InputManager:
    """
    Manage the input events. Convert input value to an intent and then process that intent.
    """

    def __init__(self):
        self.Intents = Intents()
        self.Config = ConfigMethods(self)
        self.Control = ControlMethods(self)

        logging.info(f"InputManager initialised.")

    def update(self, event: pygame.event, game_state: GameStates):
        """
        Get the input event and process it
        """
        # clear any held values
        self.Control.reset_intents()

        # convert input to intent
        if event.type == pygame.KEYDOWN or event.type == pygame.USEREVENT:
            self.Control.check_actions(event)
            self.Control.check_directions(event)
            self.Control.check_dev_actions(event)

        # process intent
        self.Control.process_stateless_intents(event)

        if game_state == GameStates.PLAYER_TURN:
            self.Control.process_player_turn_intents(event)
        elif game_state == GameStates.TARGETING_MODE:
            self.Control.process_targeting_mode_intents(event)
        elif game_state == GameStates.DEV_MODE:
            self.Control.process_dev_mode_intents(event)


input = InputManager()
