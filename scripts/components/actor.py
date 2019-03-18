from scripts.core.constants import MessageEventTypes
from scripts.core.skill import Skill
from scripts.events.message_events import MessageEvent


class Actor:
    """
    [Component] Can move and interact with the game world.
    """

    def __init__(self):
        """
        Attributes:
            time_of_next_action (int) : length of time before next action can occur

        """
        self.time_of_next_action = 0
        self.known_skills = {}
        self.learn_skill("move")  # all actors know how to move

    def learn_skill(self, skill_name):
        """
        Add a skill to the Actor's known skills
        Args:
            skill_name(str): Name of the skill to learn
        """
        skill = Skill(skill_name)
        skill.owner = self
        self.known_skills[skill.name] = skill

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
            time_spent (int) : amount of time expended by last action

        """
        # TODO - apply any modifiers to time
        self.time_of_next_action += time_spent
