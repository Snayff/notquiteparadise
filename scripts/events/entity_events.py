from scripts.core.constants import EntityEventTypes, EventTopics
from scripts.events.pub_sub_hub import Event


class UseSkillEvent(Event):
    def __init__(self, entity_using_skill, target, skill_name):
        Event.__init__(self, EntityEventTypes.SKILL, EventTopics.ENTITY)
        self.entity = entity_using_skill
        self.target = target
        self.skill_name = skill_name


class GetMoveTargetEvent(Event):
    def __init__(self, moving_entity, target_entity):
        Event.__init__(self, EntityEventTypes.GET_MOVE_TARGET, EventTopics.ENTITY)
        self.moving_entity = moving_entity
        self.target_entity = target_entity


class DieEvent(Event):
    def __init__(self, dying_entity):
        Event.__init__(self, EntityEventTypes.DIE, EventTopics.ENTITY)
        self.dying_entity = dying_entity