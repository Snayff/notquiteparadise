from scripts.core.constants import MessageEventTypes
from scripts.events.message_events import MessageEvent


class Actor:
    """
    [Component] Can move and interact with the game world.
    """

    def __init__(self):
        """
        Attributes:
            time_of_next_action (int) : number of rounds before next action can occur

        """
        self.time_of_next_action = 0
        self.learnt_skills = []

    def move(self, target_x, target_y):
        """
        Move the Actor to a new tile.

        Args:
            target_x (int): tile's x location
            target_y (int): tile's y location

        """

        self.owner.x = target_x
        self.owner.y = target_y

        from scripts.core.global_data import game_manager
        msg = f"{self.owner.name} moved to [{target_x},{target_y}]."
        game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

    def spend_time(self, time_spent):
        """
        Apply time spent from last action.

        Args:
            time_spent (int) : amount of time expedned by last action

        """
        self.time_of_next_action += time_spent
