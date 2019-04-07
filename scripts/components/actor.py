from scripts.core.skill import Skill



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

    def learn_skill(self, skill_name):
        """
        Add a skill to the Actor's known skills
        Args:
            skill_name(str): Name of the skill to learn
        """
        skill = Skill(skill_name)
        skill.owner = self
        self.known_skills[skill.name] = skill

    def spend_time(self, time_spent):
        """
        Apply time spent from last action.

        Args:
            time_spent (int) : amount of time expended by last action

        """
        # TODO - apply any modifiers to time
        self.time_of_next_action += time_spent
