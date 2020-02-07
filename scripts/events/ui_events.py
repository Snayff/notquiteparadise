from __future__ import annotations

from typing import TYPE_CHECKING
from scripts.core.constants import UIEventTypes, EventTopics
from scripts.core.event_hub import Event

if TYPE_CHECKING:
    from scripts.core.constants import MessageTypes
    from scripts.world.entity import Entity


class SelectEntity(Event):
    """
    Event for selecting an entity.
    """
    def __init__(self, entity):
        Event.__init__(self, UIEventTypes.SELECT_ENTITY, EventTopics.UI)

        self.selected_entity = entity


class ClickTile(Event):
    """
    Event for clicking a tile
    """
    def __init__(self, tile_pos_string):
        Event.__init__(self, UIEventTypes.CLICK_TILE, EventTopics.UI)

        self.tile_pos_string = tile_pos_string


class MessageEvent(Event):
    """
    Event to share messages with the player
    """
    def __init__(self, message_type: MessageTypes,  message: str, colour: str = None, size: int = 4,
            entity: Entity = None):
        Event.__init__(self, UIEventTypes.MESSAGE, EventTopics.UI)
        self.message = message
        self.message_type = message_type
        self.entity = entity
        self.colour = colour

        # max size is 7
        if size > 7:
            self.size = 7
        else:
            self.size = size