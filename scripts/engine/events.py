from __future__ import annotations

from typing import TYPE_CHECKING, Tuple, Union, Type

from scripts.engine.core.constants import EventTopics, Directions, GameStates, MessageTypes
from scripts.engine.core.event_core import Event
from scripts.engine.components import Position

if TYPE_CHECKING:
    pass

####################### ENTITY ############################################

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

####################### GAME ############################################


class EndTurnEvent(Event):
    """
    Event to end an entities ability to act.

    Args:
        entity(Entity):
        time_spent(int):

    """
    def __init__(self, entity, time_spent):
        Event.__init__(self, "END_TURN", EventTopics.GAME)
        self.entity = entity
        self.time_spent = time_spent


class ExitGameEvent(Event):
    """
    Event to exit the game
    """
    def __init__(self):
        Event.__init__(self, "EXIT", EventTopics.GAME)


class ChangeGameStateEvent(Event):
    """
    Event to change the current game state
    """
    def __init__(self, new_game_state: Type[GameStates], skill_to_be_used: str = None):
        Event.__init__(self, "CHANGE_GAME_STATE", EventTopics.GAME)
        self.new_game_state = new_game_state
        self.skill_to_be_used = skill_to_be_used


class EndRoundEvent(Event):
    """
    Event to process the end of a round
    """
    def __init__(self):
        Event.__init__(self, "END_ROUND", EventTopics.GAME)


####################### MAP ############################################

class TileInteractionEvent(Event):
    """
    Event for updating a tile in response to actions taken

    Args:
        tiles(list[Tile]): a list of effected tiles
        cause (str): name of the effect or affliction that has taken place on the tile
    """
    def __init__(self, tiles, cause):
        Event.__init__(self, "TILE_INTERACTION", EventTopics.MAP)
        self.tiles = tiles
        self.cause = cause

####################### UI ############################################


class SelectEntity(Event):
    """
    Event for selecting an entity.
    """
    def __init__(self, entity: int):
        Event.__init__(self, "SELECT_ENTITY", EventTopics.UI)

        self.selected_entity = entity


class ClickTile(Event):
    """
    Event for clicking a tile
    """
    def __init__(self, tile_pos_string: str):
        Event.__init__(self, "CLICK_TILE", EventTopics.UI)

        self.tile_pos_string = tile_pos_string


class MessageEvent(Event):
    """
    Event to share messages with the player
    """
    def __init__(self, message_type: MessageTypes,  message: str, colour: str = None, size: int = 4,
            entity: int = None):
        Event.__init__(self, "MESSAGE", EventTopics.UI)
        self.message = message
        self.message_type = message_type
        self.entity = entity
        self.colour = colour

        # max size is 7
        if size > 7:
            self.size = 7
        else:
            self.size = size