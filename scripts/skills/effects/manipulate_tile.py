
from scripts.skills.effects.effect import Effect


class ManipulateTileEffect(Effect):
    """
    Effect to change a Tile
    """

    def __init__(self, target_type, tags):
        super().__init__("Manipulate Tile", "This is the Manipulate Tile effect", target_type, tags)
