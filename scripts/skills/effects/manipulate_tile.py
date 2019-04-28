
from scripts.skills.effects.effect import Effect


class ManipulateTileEffect(Effect):
    """
    Effect to change a Tile
    """

    def __init__(self, target_type, tags, new_tile):
        super().__init__("Manipulate Tile", "This is the Manipulate Tile effect", target_type, tags)

        self.new_tile = new_tile


    def trigger(self, tile_to_change):
        pass