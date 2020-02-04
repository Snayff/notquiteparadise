from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.core.constants import EntityEventTypes, EventTopics
from scripts.core.event_hub import Event

if TYPE_CHECKING:
    from typing import Tuple
    from scripts.world.entity import Entity


class UseSkillEvent(Event):
    """
    Event for entity skill

    Args:
        entity_using_skill(int): entity id
        direction (Tuple): x, y
        skill_name (str): skill name
    """
    def __init__(self, entity_using_skill: int, skill_name: str, start_pos: Tuple[int, int], direction: Tuple[
        int, int]):
        Event.__init__(self, EntityEventTypes.SKILL, EventTopics.ENTITY)
        self.entity = entity_using_skill
        self.direction = direction
        self.skill_name = skill_name
        self.start_pos = start_pos


class DieEvent(Event):
    """
    Event for handling the death of an entity.
    """
    def __init__(self, dying_entity):
        Event.__init__(self, EntityEventTypes.DIE, EventTopics.ENTITY)
        self.dying_entity = dying_entity


class MoveEvent(Event):
    """
    Event to move an entity as a basic move action
    """
    def __init__(self, entity_to_move: int, start_pos: Tuple[int, int], direction: Tuple[int, int], distance: int = 1):

        Event.__init__(self, EntityEventTypes.MOVE, EventTopics.ENTITY)
        self.entity = entity_to_move
        self.direction = direction
        self.distance = distance
        self.start_pos = start_pos