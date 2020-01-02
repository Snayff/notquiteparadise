import logging
import pygame
from scripts.managers.input_methods.config_methods import ConfigMethods
from scripts.managers.input_methods.intents import Intents
from scripts.managers.input_methods.processing_methods import ProcessingMethods
from scripts.managers.input_methods.value_methods import ValueMethods


class InputManager:
    """
    Manage the input events. Convert input value to an intent and then process that intent.
    """

    def __init__(self):
        self.Config = ConfigMethods(self)
        self.Intent = Intents()
        self.Values = ValueMethods(self)
        self.Process = ProcessingMethods(self)

        logging.info(f"InputManager initialised.")

    def update(self, event: pygame.event):
        """
        Get the input event and process it
        """
        self.Values.reset_intents()