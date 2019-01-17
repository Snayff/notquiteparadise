from scripts.core.constants import LoggingEventNames, GameEventNames, GameStates
from scripts.core.global_data import game_manager, turn_manager
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber


class GameHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "game_handler", event_hub)

    def run(self, event):
        log_string = f"{self.name} received {event.name}"
        game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

        if event.name == GameEventNames.EXIT:
            game_manager.update_game_state(GameStates.EXIT_GAME)

        elif event.name == GameEventNames.END_TURN:
            turn_manager.end_turn(event.time_spent)

    # if event.name == GameEventNames.NEW_GAME:
    # 	from Code.Core.initialisers import initialise_new_game
    # 	initialise_new_game()