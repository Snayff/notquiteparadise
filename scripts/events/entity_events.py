from scripts.core.constants import EntityEventTypes, EventTopics
from scripts.events.pub_sub_hub import Event


class UseSkillEvent(Event):
    """
    Event for entity skill

    Args:
        entity_using_skill(Entity):
        target_pos (tuple): x, y
        skill_name:
    """
    def __init__(self, entity_using_skill, target_pos, skill_name):
        Event.__init__(self, EntityEventTypes.SKILL, EventTopics.ENTITY)
        self.entity = entity_using_skill
        self.target_pos = target_pos
        self.skill_name = skill_name


class DieEvent(Event):
    def __init__(self, dying_entity):
        Event.__init__(self, EntityEventTypes.DIE, EventTopics.ENTITY)
        self.dying_entity = dying_entity


class MoveEvent(Event):
    """
    Event to move an entity as a basic move action
    """
    def __init__(self, entity_to_move, target_pos):
        """

        Args:
            entity_to_move:
            target_pos (tuple):
        """
        Event.__init__(self, EntityEventTypes.MOVE, EventTopics.ENTITY)
        self.entity = entity_to_move
        self.target_pos = target_pos


class LearnEvent(Event):
    """
    Event for learning a new skill

    Args:
        entity_to_learn_skill:
        skill_tree_name:
        skill_name:
    """
    def __init__(self, entity_to_learn_skill, skill_tree_name,  skill_name):
        Event.__init__(self, EntityEventTypes.LEARN, EventTopics.ENTITY)
        self.entity = entity_to_learn_skill
        self.skill_tree_name = skill_tree_name
        self.skill_name = skill_name