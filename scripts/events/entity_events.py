from scripts.core.constants import EntityEventNames, EventTopics
from scripts.events.pub_sub_hub import Event


class MoveEvent(Event):
    def __init__(self, entity, destination_x, destination_y):
        Event.__init__(self, EntityEventNames.MOVE, EventTopics.ENTITY)
        self.entity = entity
        self.destination_x = destination_x
        self.destination_y = destination_y


class GetMoveTargetEvent(Event):
    def __init__(self, moving_entity, target_entity):
        Event.__init__(self, EntityEventNames.GET_MOVE_TARGET, EventTopics.ENTITY)
        self.moving_entity = moving_entity
        self.target_entity = target_entity


class AttackEvent(Event):
    def __init__(self, attacking_entity, defending_entity):
        Event.__init__(self, EntityEventNames.ATTACK, EventTopics.ENTITY)
        self.attacker = attacking_entity
        self.defender = defending_entity


class DieEvent(Event):
    def __init__(self, dying_entity):
        Event.__init__(self, EntityEventNames.DIE, EventTopics.ENTITY)
        self.dying_entity = dying_entity