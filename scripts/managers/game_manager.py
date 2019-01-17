from scripts.core.constants import GameStates, LoggingEventNames
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import EventHub, Publisher


class GameManager:

    def __init__(self):
        self.game_state = GameStates.GAME_INITIALISING
        self.previous_game_state = GameStates.GAME_INITIALISING
       # self.message_log = None
        self.event_hub = EventHub()

    # def new_message_log(self, message_log):
    #     """
    #     :type message_log: MessageLog
    #     """
    #     self.message_log = message_log

    def update_game_state(self, new_game_state):
        """
        :type new_game_state: Code.Core.constants.GameStates
        """
        self.previous_game_state = self.game_state
        self.game_state = new_game_state

        log_string = f"game_state updated to {self.game_state} from {self.previous_game_state}"
        self.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

    def create_event(self, event):
        pub = Publisher(self.event_hub)
        pub.publish(event)