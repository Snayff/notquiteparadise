from scripts.core.constants import EntityEventTypes, EventTopics
from scripts.events.pub_sub_hub import Event

class UseSkillEvent(Event):
    def __init__(self, entity, target, skill_name):
        Event.__init__(self, EntityEventTypes.SKILL, EventTopics.ENTITY)
        self.entity = entity
        self.target = target
        self.skill_name = skill_name


class GetMoveTargetEvent(Event):
    def __init__(self, moving_entity, target_entity):
        Event.__init__(self, EntityEventTypes.GET_MOVE_TARGET, EventTopics.ENTITY)
        self.moving_entity = moving_entity
        self.target_entity = target_entity


class AttackEvent(Event):
    def __init__(self, attacking_entity, defending_entity):
        Event.__init__(self, EntityEventTypes.ATTACK, EventTopics.ENTITY)
        self.attacker = attacking_entity
        self.defender = defending_entity


class DieEvent(Event):
    def __init__(self, dying_entity):
        Event.__init__(self, EntityEventTypes.DIE, EventTopics.ENTITY)
        self.dying_entity = dying_entity