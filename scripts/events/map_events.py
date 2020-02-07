
from scripts.core.constants import EventTopics, MapEventTypes
from scripts.core.event_hub import Event


class TileInteractionEvent(Event):
    """
    Event for updating a tile in response to actions taken

    Args:
        tiles(list[Tile]): a list of effected tiles
        cause (str): name of the effect or affliction that has taken place on the tile
    """
    def __init__(self, tiles, cause):
        Event.__init__(self, MapEventTypes.TILE_INTERACTION, EventTopics.MAP)
        self.tiles = tiles
        self.cause = cause