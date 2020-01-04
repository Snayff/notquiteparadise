import logging
from scripts.core.constants import GameEventTypes, GameStates
from scripts.core.event_hub import publisher
from scripts.managers.turn_manager import turn
from scripts.managers.world_manager import world
from scripts.managers.game_manager import game
from scripts.event_handlers.pub_sub_hub import Subscriber
from scripts.events.game_events import ChangeGameStateEvent, EndTurnEvent, ExitGameEvent


class GameHandler(Subscriber):
    """
    Handle core Game related actions, driven by events. Turn changes exist here, too.
    """

    def __init__(self, event_hub):
        Subscriber.__init__(self, "game_handler", event_hub)

    def process_event(self, event):
        """
        Process game events.

        Args:
            event ():
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}.")

        if event.event_type == GameEventTypes.EXIT:
            event: ExitGameEvent
            publisher.publish(ChangeGameStateEvent(GameStates.EXIT_GAME))

        elif event.event_type == GameEventTypes.END_TURN:
            event: EndTurnEvent
            self.process_end_turn(event)

        elif event.event_type == GameEventTypes.CHANGE_GAME_STATE:
            event: ChangeGameStateEvent
            self.process_change_game_state(event)

    @staticmethod
    def process_change_game_state(event: ChangeGameStateEvent):
        """
        Transition to another game state as specified by the event.

        Args:
            event ():
        """
        new_game_state = event.new_game_state

        if new_game_state == GameStates.GAME_INITIALISING:
            # transition to post-initialisation game state
            # TODO - set default post-init game state
            publisher.publish(EndTurnEvent(world.player, 1))  # trigger new turn actions (entity queue) fresh

        elif new_game_state == GameStates.NEW_TURN:
            # if turn holder is the player then update to player turn
            if turn.turn_holder == world.player:
                publisher.publish(ChangeGameStateEvent(GameStates.PLAYER_TURN))
            # if turn holder is not player and we aren't already in enemy turn then update to enemy turn
            else:
                publisher.publish(ChangeGameStateEvent(GameStates.ENEMY_TURN))

        elif new_game_state == GameStates.TARGETING_MODE:
            game.active_skill = event.skill_to_be_used

        # update the game state to the intended state
        if new_game_state != game.game_state:
            game.update_game_state(new_game_state)
        else:
            # handle wasted attempt to change the game state
            log_string = f"-> new game state {new_game_state} is same as current" \
                         f" {game.game_state} so state not updated."
            logging.info(log_string)

    @staticmethod
    def process_end_turn(event: EndTurnEvent):
        """
        End turn, move to next turn, change game state to new turn.

        Args:
            event (EndTurnEvent):
        """
        turn.end_turn(event.time_spent)
        turn.next_turn()
        publisher.publish(ChangeGameStateEvent(GameStates.NEW_TURN))
