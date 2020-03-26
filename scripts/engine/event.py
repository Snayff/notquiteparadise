from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from snecs.typedefs import EntityID
from scripts.engine.core.constants import EventTopic, GameStateType, MessageTypeType, DirectionType, TravelMethodType
from scripts.engine.core.event_core import Event

if TYPE_CHECKING:
    from typing import Tuple, Union, Type, List
    from scripts.engine.world_objects.tile import Tile


####################### ENTITY ############################################

class WantToUseSkillEvent(Event):
    """
    Event for entity wanting to use a skill. Should be used for all instances where you want checks to be completed
    before using the skill.
    """
    def __init__(self, entity_using_skill: EntityID, skill_name: str, start_pos: Tuple[int, int],
            direction: Optional[Union[Tuple[int, int], DirectionType]]):
        Event.__init__(self, "WANT_TO_USE_SKILL", EventTopic.ENTITY)
        self.entity = entity_using_skill
        self.direction = direction
        self.skill_name = skill_name
        self.start_pos = start_pos


class UseSkillEvent(Event):
    """
    Event for entity using a skill. Should only be called as a result of WantToUseSkillEvent being processed
    successfully.
    """
    def __init__(self, entity_using_skill: EntityID, skill_name: str, target_tiles: List[Tile]):
        Event.__init__(self, "USE_SKILL", EventTopic.ENTITY)
        self.entity = entity_using_skill
        self.skill_name = skill_name
        self.target_tiles = target_tiles


class DieEvent(Event):
    """
    Event for handling the death of an entity.
    """
    def __init__(self, dying_entity: EntityID):
        Event.__init__(self, "DIE", EventTopic.ENTITY)
        self.entity = dying_entity


class MoveEvent(Event):
    """
    Event to move an entity as a basic move action
    """
    def __init__(self, entity_to_move: int, start_pos: Tuple[int, int], direction: Tuple[int, int],
            travel_type: TravelMethodType):
        Event.__init__(self, "MOVE", EventTopic.ENTITY)
        self.start_pos = start_pos
        self.travel_type = travel_type
        self.entity = entity_to_move
        self.direction = direction


####################### GAME ############################################


class EndTurnEvent(Event):
    """
    Event to end an entities ability to act.
    """
    def __init__(self, ent: EntityID, time_spent):
        Event.__init__(self, "END_TURN", EventTopic.GAME)
        self.entity = ent
        self.time_spent = time_spent


class ExitGameEvent(Event):
    """
    Event to exit the game
    """
    def __init__(self):
        Event.__init__(self, "EXIT", EventTopic.GAME)


class ChangeGameStateEvent(Event):
    """
    Event to change the current game state
    """
    def __init__(self, new_game_state: GameStateType, skill_to_be_used: str = None):
        Event.__init__(self, "CHANGE_GAME_STATE", EventTopic.GAME)
        self.new_game_state = new_game_state
        self.skill_to_be_used = skill_to_be_used


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
    def __init__(self, ent: EntityID):
        Event.__init__(self, "SELECT_ENTITY", EventTopic.UI)

        self.selected_entity = ent


class ClickTile(Event):
    """
    Event for clicking a tile
    """
    def __init__(self, tile_pos_string: str):
        Event.__init__(self, "CLICK_TILE", EventTopic.UI)

        self.tile_pos_string = tile_pos_string


class MessageEvent(Event):
    """
    Event to share messages with the player
    """
    def __init__(self, message_type: MessageTypeType,  message: str, colour: str = None, size: int = 4,
            ent: int = None):
        Event.__init__(self, "MESSAGE", EventTopic.UI)
        self.message = message
        self.message_type = message_type
        self.entity = ent
        self.colour = colour

        # max size is 7
        if size > 7:
            self.size = 7
        else:
            self.size = size