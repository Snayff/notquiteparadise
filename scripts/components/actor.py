import logging

from scripts.skills.skill import Skill



class Actor:
    """
    [Component] Can move and interact with the game world. Knows skills.

    Attributes:
        time_of_next_action (int) : length of time before next action can occur
    """

    def __init__(self):
        self.time_of_next_action = 0
        self.known_skills = []
        self.max_known_skills = 4

    def learn_skill(self, skill_tree_name,  skill_name):
        """
        Add a skill to the Actor`s known skills
        Args:
            skill_tree_name(str): Name of the skill tree the skill is in
            skill_name(str): Name of the skill to learn
        """
        from scripts.managers.world_manager import world
        skill = world.Skill.create_skill(self, skill_tree_name, skill_name)

        # place skill at next free slot
        self.known_skills.append(skill)

    def spend_time(self, time_spent):
        """
        Apply time spent from last action.

        Args:
            time_spent (int) : amount of time expended by last action

        """
        # TODO - apply any modifiers to time
        self.time_of_next_action += time_spent

    def is_at_max_known_skills(self):
        """
        Check if known skills >= max known

        Returns:
            bool: True if learnt max number of skills
        """
        if len(self.known_skills) >= self.max_known_skills:
            return True
        else:
            return False

    def get_skill_from_known_skills(self, skill_name):
        """
        Get a skill from the known skills

        Args:
            skill_name(str): name of the skill

        Returns:
            Skill: skill if found, None if nothing found.
        """
        for skill in self.known_skills:
            if skill.name == skill_name:
                return skill

        log_string = f"Looked in {self.owner.name}`s known skills to find {skill_name}, but found nothing. "
        logging.error(log_string)

        return None
