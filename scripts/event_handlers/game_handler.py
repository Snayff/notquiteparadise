import logging

from scripts.core.constants import GameEventTypes, GameStates, AfflictionTriggers
from scripts.global_singletons.event_hub import publisher
from scripts.global_singletons.managers import game_manager, turn_manager, world_manager
from scripts.events.game_events import ChangeGameStateEvent

from scripts.event_handlers.pub_sub_hub import Subscriber


class GameHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "game_handler", event_hub)

    def run(self, event):
        log_string = f"{self.name} received {event.event_type}"
        logging.info(log_string)

        if event.event_type == GameEventTypes.EXIT:
            publisher.publish(ChangeGameStateEvent(GameStates.EXIT_GAME))

        elif event.event_type == GameEventTypes.END_TURN:
            turn_manager.end_turn(event.time_spent)

        elif event.event_type == GameEventTypes.CHANGE_GAME_STATE:
            if event.new_game_state != game_manager.game_state:
                game_manager.update_game_state(event.new_game_state)
            else:
                log_string = f"-> new game state {event.new_game_state} is same " \
                    f"as current {game_manager.game_state} so state not updated."
                logging.info( log_string)

