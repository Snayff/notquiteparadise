from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from scripts.engine import entity, chrono, state
from scripts.engine.core.constants import GameState
from scripts.engine.core.event_core import publisher, Subscriber
from scripts.engine.state import get_current


from scripts.engine.event import EndTurnEvent, ExitGameEvent, ChangeGameStateEvent

if TYPE_CHECKING:
    pass


class GameHandler(Subscriber):
    """
    Handle core Game related actions, driven by events. Turn changes exist here, too.
    """

    def __init__(self, event_hub):
        Subscriber.__init__(self, "game_handler", event_hub)

    def process_event(self, event):
        """
        Process game events.
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.__class__.__name__}.")

        if isinstance(event, ExitGameEvent):
            publisher.publish(ChangeGameStateEvent(GameState.EXIT_GAME))

        elif isinstance(event, EndTurnEvent):
            self.process_end_turn(event)

        elif isinstance(event, ChangeGameStateEvent):
            self.process_change_game_state(event)

    @staticmethod
    def process_change_game_state(event: ChangeGameStateEvent):
        """
        Transition to another game state as specified by the event.
        """
        new_game_state = event.new_game_state

        if new_game_state == GameState.GAME_INITIALISING:
            # transition to post-initialisation game state
            # TODO - set default post-init game state
            publisher.publish(EndTurnEvent(entity.get_player(), 1))  # trigger new turn actions (entity queue)

        elif new_game_state == GameState.NEW_TURN:
            # if turn holder is the player then update to player turn
            if chrono.get_turn_holder() == entity.get_player():
                publisher.publish(ChangeGameStateEvent(GameState.PLAYER_TURN))
            # if turn holder is not player and we aren't already in enemy turn then update to enemy turn
            else:
                publisher.publish(ChangeGameStateEvent(GameState.ENEMY_TURN))

        elif new_game_state == GameState.TARGETING_MODE:
            if event.skill_to_be_used:
                state.set_active_skill(event.skill_to_be_used)
            else:
                logging.warning("Entered targeting mode with no active skill.")

        # PREVIOUS must be last as it overwrites new_game_state
        elif new_game_state == GameState.PREVIOUS:
            new_game_state = state.get_previous()

        # update the game state to the intended state
        if new_game_state != state.get_current():
            state.set_new(new_game_state)
        else:
            # handle wasted attempt to change the game state
            log_string = f"-> new game state {new_game_state} is same as current" \
                         f" {state.get_current()} so state not updated."
            logging.info(log_string)

    @staticmethod
    def process_end_turn(event: EndTurnEvent):
        """
        End turn, move to next turn, change game state to new turn.
        """
        chrono.next_turn()
        publisher.publish(ChangeGameStateEvent(GameState.NEW_TURN))
