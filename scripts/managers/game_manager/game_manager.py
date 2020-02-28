from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from scripts.managers.game_manager.debug_methods import DebugMethods
from scripts.managers.game_manager.state_methods import StateMethods

if TYPE_CHECKING:
    pass


class GameManager:
    """
    Manager of Game Functions and data, such as the window details
    """
    def __init__(self):
        self.State = StateMethods(self)
        self.Debug = DebugMethods(self)

        logging.info(f"GameManager initialised.")

    def update(self):
        """
        Update the GameManager
        """
        self.State.update_clock()


game = GameManager()