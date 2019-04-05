

class EntityAction:
    def __init__(self, manager):
        self.manager = manager

    def use_skill(self, actor, skill):
        """
        Use an actor's skill

        Args:
            actor: The actor to use the skill
            skill: The actor's skill to use
        """

        # does the skill require targeting info?

        # target info received, do the skill

