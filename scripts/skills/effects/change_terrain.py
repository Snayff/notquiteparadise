
from scripts.core.constants import MessageEventTypes, EffectTypes
from scripts.events.message_events import MessageEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.skills.effects.effect import Effect


class ChangeTerrainEffect(Effect):
    """
    Effect to change the terrain of a tile
    """

    def __init__(self, owner):
        super().__init__(owner, "change_terrain", "This is the Change Terrain effect",
                         EffectTypes.CHANGE_TERRAIN)

    def trigger(self, tiles):
        """
        Trigger the effect

        Args:
            tiles (List[Tile]):
        """
        super().trigger()

        # loop all tiles in list
        for tile in tiles:

            terrain = tile.terrain
            starting_terrain_name = terrain.name

            data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.effect_type)

            # that the tags match
            from scripts.managers.world_manager import world
            if world.Skill.has_required_tags(tile, data.required_tags):
                world.Map.set_terrain_on_tile(tile, data.new_terrain)

                # success text
                entity = self.owner.owner.owner
                msg = f"{entity.name} changed the {starting_terrain_name} to {tile.terrain.name}."
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

            else:
                # confirm can't do it
                # N.B. the reason why is logged in has_required_tags
                msg = f"You can't do that there!"
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
