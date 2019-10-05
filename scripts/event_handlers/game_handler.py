import logging

from scripts.core.constants import GameEventTypes, GameStates
from scripts.global_singletons.event_hub import publisher
from scripts.global_singletons.managers import game_manager, turn_manager, world_manager
from scripts.events.game_events import ChangeGameStateEvent, EndTurnEvent
from scripts.event_handlers.pub_sub_hub import Subscriber


class GameHandler(Subscriber):
    """
    Handle core Game related actions, driven by events. Turn changes exist here, too.
    """

    def __init__(self, event_hub):
        Subscriber.__init__(self, "game_handler", event_hub)

    def run(self, event):
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}...")

        if event.event_type == GameEventTypes.EXIT:
            publisher.publish(ChangeGameStateEvent(GameStates.EXIT_GAME))

        elif event.event_type == GameEventTypes.END_TURN:
            turn_manager.end_turn(event.time_spent)
            turn_manager.next_turn()
            publisher.publish(ChangeGameStateEvent(GameStates.NEW_TURN))

        elif event.event_type == GameEventTypes.CHANGE_GAME_STATE:
            self.transition_to_another_game_state(event.new_game_state)

    @staticmethod
    def transition_to_another_game_state(new_game_state):
        """
        Transition to another game state as specified by the event.

        Args:
            new_game_state (GameStates):
        """
        if new_game_state == GameStates.GAME_INITIALISING:
            # transition to post-initialisation game state
            # TODO - set default post-init game state
            publisher.publish(EndTurnEvent(world_manager.player, 1))  # trigger new turn actions (entity queue) fresh

        elif new_game_state == GameStates.NEW_TURN:
            # if turn holder is the player then update to player turn
            if turn_manager.turn_holder == world_manager.player:
                publisher.publish(ChangeGameStateEvent(GameStates.PLAYER_TURN))
            # if turn holder is not player and we aren't already in enemy turn then update to enemy turn
            else:
                publisher.publish(ChangeGameStateEvent(GameStates.ENEMY_TURN))

        # handle wasted attempt to change the game state
        if new_game_state != game_manager.game_state:
            game_manager.update_game_state(new_game_state)
        else:
            log_string = f"-> new game state {new_game_state} is same as current" \
                         f" {game_manager.game_state} so state not updated."
            logging.info(log_string)
