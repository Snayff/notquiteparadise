from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.engine import chapter, state, utility, world
from scripts.engine.core.constants import GameState
from scripts.engine.core.event_core import publisher, Subscriber
from scripts.engine.event import ExitGameEvent, ChangeGameStateEvent

if TYPE_CHECKING:
    pass


class GameHandler(Subscriber):
    """
    Handle core game related actions, driven by events. Turn changes exist here, too.
    """

    def __init__(self, event_hub):
        super().__init__("game_handler", event_hub)

    def process_event(self, event):
        """
        Process game events.
        """
        if isinstance(event, ExitGameEvent):
            publisher.publish(ChangeGameStateEvent(GameState.EXIT_GAME))

        elif isinstance(event, ChangeGameStateEvent):
            self._process_change_game_state(event)

    @staticmethod
    def _process_change_game_state(event: ChangeGameStateEvent):
        """
        Transition to another game state as specified by the event.
        """
        new_game_state = event.new_game_state
        current_game_state = state.get_current()

        if new_game_state == GameState.GAME_INITIALISING:
            # transition to post-initialisation game state
            # TODO - set default post-init game state
            # trigger new turn actions (entity queue)
            player = world.get_player()
            if player:

                world.end_turn(player, 1)

        elif new_game_state == GameState.TARGETING_MODE:
            if event.skill_to_be_used:
                state.set_active_skill(event.skill_to_be_used)
            else:
                logging.warning("Entered targeting mode with no active skill.")

        # update the game state to the intended state
        if new_game_state != current_game_state:
            state.set_new(new_game_state)
        else:
            # handle wasted attempt to change the game state
            new_state_name = utility.value_to_member(new_game_state, GameState)
            current_state_name = utility.value_to_member(current_game_state, GameState)
            log_string = f"-> new game state {new_state_name} is same as current {current_state_name} so state not" \
                         f" updated. However, lower level details may still have changed."
            logging.debug(log_string)

