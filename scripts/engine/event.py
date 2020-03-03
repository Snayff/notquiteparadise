from __future__ import annotations

from typing import TYPE_CHECKING, Tuple, Union, Type, List

from scripts.engine import entity
from scripts.engine.core.constants import EventTopic, Direction, GameState, MessageType, GameStateType, MessageTypeType, \
    DirectionType
from scripts.engine.core.event_core import Event
from scripts.engine.component import Position
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    pass


####################### ENTITY ############################################

class WantToUseSkillEvent(Event):
    """
    Event for player pressing a skill number
    """
    def __init__(self, skill_number: int):
        Event.__init__(self, "WANT_TO_USE_SKILL", EventTopic.ENTITY)
        self.skill_number = skill_number


class UseSkillEvent(Event):
    """
    Event for entity using a skill
    """
    def __init__(self, entity_using_skill: int, skill_name: str, start_pos: Tuple[int, int],
            direction: Union[Tuple[int, int], DirectionType]):
        Event.__init__(self, "SKILL", EventTopic.ENTITY)
        self.entity = entity_using_skill
        self.direction = direction
        self.skill_name = skill_name
        self.start_pos = start_pos


class DieEvent(Event):
    """
    Event for handling the death of an entity.
    """
    def __init__(self, dying_entity: int):
        Event.__init__(self, "DIE", EventTopic.ENTITY)
        self.dying_entity = dying_entity


class MoveEvent(Event):
    """
    Event to move an entity as a basic move action
    """
    def __init__(self, entity_to_move: int, direction: Union[Tuple[int, int], DirectionType], distance: int = 1):
        Event.__init__(self, "MOVE", EventTopic.ENTITY)
        self.entity = entity_to_move
        self.direction = direction
        self.distance = distance

        # determine start pos
        position = entity.get_entitys_component(entity_to_move, Position)
        self.start_pos: Tuple[int, int] = (position.x, position.y)

####################### GAME ############################################


class EndTurnEvent(Event):
    """
    Event to end an entities ability to act.
    """
    def __init__(self, ent, time_spent):
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


####################### MAP ############################################

class TileInteractionEvent(Event):
    """
    Event for updating a tile in response to actions taken

    Args:
        tiles(list[Tile]): a list of effected tiles
        cause (str): name of the effect or affliction that has taken place on the tile
    """
    def __init__(self, tiles: List[Tile], cause: str):
        Event.__init__(self, "TILE_INTERACTION", EventTopic.MAP)
        self.tiles = tiles
        self.cause = cause

####################### UI ############################################


class SelectEntity(Event):
    """
    Event for selecting an entity.
    """
    def __init__(self, ent: int):
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