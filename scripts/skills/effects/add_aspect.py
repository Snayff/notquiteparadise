
from scripts.core.constants import MessageEventTypes, EffectTypes
from scripts.events.message_events import MessageEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.skills.effects.effect import Effect


class AddAspectEffect(Effect):
    """
    Effect to add an aspects to a tile
    """

    def __init__(self, owner):
        super().__init__(owner, "add_aspect", "This is the Add Aspect effect",
                         EffectTypes.ADD_ASPECT)

    def trigger(self, tiles):
        """
        Trigger the effect

        Args:
            tiles (list[Tile]):
        """
        super().trigger()

        data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.effect_type)

        for tile in tiles:

            from scripts.managers.world_manager import world
            world.Map.add_aspect_to_tile(tile, data.aspect_name)

            entity = self.owner.owner.owner
            msg = f"{entity.name} added {data.aspect_name} to {tile.terrain.name}."
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))