from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from snecs.typedefs import EntityID
from scripts.engine.core.constants import EventTopic, GameStateType, MessageTypeType, DirectionType, TravelMethodType
from scripts.engine.core.event_core import Event

if TYPE_CHECKING:
    from typing import Tuple, Union, Type, List
    from scripts.engine.world_objects.tile import Tile


####################### ENTITY ############################################


class UseSkillEvent(Event):
    """
    Event for entity using a skill. Should only be called as a result of WantToUseSkillEvent being processed
    successfully.
    """
    def __init__(self, entity_using_skill: EntityID, skill_name: str, target_tile: Tile, direction: DirectionType):
        Event.__init__(self, "USE_SKILL", EventTopic.ENTITY)
        self.entity = entity_using_skill
        self.skill_name = skill_name
        self.target_tile = target_tile
        self.direction = direction


class DieEvent(Event):
    """
    Event for handling the death of an entity.
    """
    def __init__(self, dying_entity: EntityID):
        Event.__init__(self, "DIE", EventTopic.ENTITY)
        self.entity = dying_entity



####################### GAME ############################################


class ExitGameEvent(Event):
    """
    Event to exit the game
    """
    def __init__(self):
        Event.__init__(self, "EXIT", EventTopic.GAME)



class EndRoundEvent(Event):
    """
    Event to process the end of a round
    """
    def __init__(self):
        Event.__init__(self, "END_ROUND", EventTopic.GAME)


####################### INTERACTION ############################################


class ExpireEvent(Event):
    """
    Event for handling the expiry of an entity, usually a projectile.
    """
    def __init__(self, expiring_entity: EntityID):
        Event.__init__(self, "EXPIRE", EventTopic.INTERACTION)
        self.entity = expiring_entity


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


####################### UI ############################################


class SelectEntity(Event):
    """
    Event for selecting an entity.
    """
    def __init__(self, entity: EntityID):
        Event.__init__(self, "SELECT_ENTITY", EventTopic.UI)

        self.selected_entity = entity


class ClickTile(Event):
    """
    Event for clicking a tile
    """
    def __init__(self, tile: Tile):
        Event.__init__(self, "CLICK_TILE", EventTopic.UI)

        self.tile = tile


class MessageEvent(Event):
    """
    Event to share messages with the player
    """
    def __init__(self, message_type: MessageTypeType,  message: str, colour: str = None, size: int = 4,
            entity: EntityID = None):
        Event.__init__(self, "MESSAGE", EventTopic.UI)
        self.message = message
        self.message_type = message_type
        self.entity = entity
        self.colour = colour

        # max size is 7
        if size > 7:
            self.size = 7
        else:
            self.size = size