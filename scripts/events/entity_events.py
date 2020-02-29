from __future__ import annotations

from typing import TYPE_CHECKING
from scripts.core.constants import EventTopics, Directions
from scripts.core.event_hub import Event
from scripts.world.components import Position

if TYPE_CHECKING:
    from typing import Tuple, Union, Type


class WantToUseSkillEvent(Event):
    """
    Event for player pressing a skill number
    """
    def __init__(self, skill_number: int):
        Event.__init__(self, "WANT_TO_USE_SKILL", EventTopics.ENTITY)
        self.skill_number = skill_number


class UseSkillEvent(Event):
    """
    Event for entity using a skill
    """
    def __init__(self, entity_using_skill: int, skill_name: str, start_pos: Tuple[int, int],
            direction: Union[Tuple[int, int], Type[Directions]]):
        Event.__init__(self, "SKILL", EventTopics.ENTITY)
        self.entity = entity_using_skill
        self.direction = direction
        self.skill_name = skill_name
        self.start_pos = start_pos


class DieEvent(Event):
    """
    Event for handling the death of an entity.
    """
    def __init__(self, dying_entity: int):
        Event.__init__(self, "DIE", EventTopics.ENTITY)
        self.dying_entity = dying_entity


class MoveEvent(Event):
    """
    Event to move an entity as a basic move action
    """
    def __init__(self, entity_to_move: int, direction: Union[Tuple[int, int], Type[Directions]], distance: int = 1):
        Event.__init__(self, "MOVE", EventTopics.ENTITY)
        self.entity = entity_to_move
        self.direction = direction
        self.distance = distance

        # TODO - moving to the top creates circular import. Resolve this.
        from scripts.managers.world_manager.world_manager import world

        # determine start pos
        position = world.Entity.get_entitys_component(entity_to_move, Position)
        self.start_pos: Tuple[int, int] = (position.x, position.y)