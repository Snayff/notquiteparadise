from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.engine import chapter, state, utility, world
from scripts.engine.core.constants import GameState
from scripts.engine.core.event_core import publisher, Subscriber
from scripts.engine.event import ExitGameEvent

if TYPE_CHECKING:
    pass


class GameHandler(Subscriber):
    """
    Handle core game related actions, driven by events. Turn changes exist here, too.
    """

    def __init__(self, event_hub):
        super().__init__("game_handler", event_hub)

    @staticmethod
    def _process_change_game_state(event: ChangeGameStateEvent):
        """
        Transition to another game state as specified by the event.
        """
        new_game_state = event.new_game_state
        current_game_state = state.get_current()

        if new_game_state == GameState.TARGETING_MODE:
            if event.skill_to_be_used:
                state.set_active_skill(event.skill_to_be_used)
            else:
                logging.warning("Entered targeting mode with no active skill.")

