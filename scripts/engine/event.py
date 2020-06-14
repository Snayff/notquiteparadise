from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from snecs.typedefs import EntityID
from scripts.engine.core.constants import EventTopic, GameStateType, MessageTypeType, DirectionType, TravelMethodType
from scripts.engine.core.event_core import Event

if TYPE_CHECKING:
    from typing import Tuple, Union, Type, List
    from scripts.engine.world_objects.tile import Tile


class EntityCollisionEvent(Event):
    """
    Event for handling two entities colliding.
    """
    def __init__(self, active_entity: EntityID, blocking_entity: EntityID, direction: Tuple[int, int],
            start_pos: Tuple[int, int]):
        Event.__init__(self, "ENTITY_COLLISION", EventTopic.INTERACTION)
        self.start_pos = start_pos
        self.direction = direction
        self.entity = active_entity
        self.blocking_entity = blocking_entity


class TerrainCollisionEvent(Event):
    """
    Event for handling an entity colliding with terrain.
    """
    def __init__(self, active_entity: EntityID, blocking_tile: Tile, direction: Tuple[int, int],
            start_pos: Tuple[int, int]):
        Event.__init__(self, "TERRAIN_COLLISION", EventTopic.INTERACTION)
        self.start_pos = start_pos
        self.direction = direction
        self.entity = active_entity
        self.blocking_tile = blocking_tile