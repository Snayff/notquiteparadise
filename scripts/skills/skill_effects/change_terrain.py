from scripts.core.constants import MessageEventTypes, LoggingEventTypes, TargetTags, SkillEffectTypes
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.skill_effects.skill_effect import SkillEffect
from scripts.world.terrain.floor import Floor
from scripts.world.terrain.terrain import Terrain
from scripts.world.terrain.wall import Wall


class ChangeTerrainSkillEffect(SkillEffect):
    """
    SkillEffect to change the terrain of a tile
    """

    def __init__(self, owner):
        super().__init__(owner, "change_terrain", "This is the Manipulate Terrain effect",
                         SkillEffectTypes.CHANGE_TERRAIN)

    def trigger(self, tile):
        """
        Trigger the effect; check tags and then, if all True, apply the effect

        Args:
            tile (tile):
        """
        super().trigger()

        terrain = tile.terrain
        starting_terrain_name = terrain.name



        data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.skill_effect_type.name)

        # that the tags match
        from scripts.global_singletons.managers import world_manager
        if world_manager.Skill.has_required_tags(tile, data.required_tags):
            world_manager.Map.set_terrain_on_tile(tile, data.new_terrain)

            # success message
            entity = self.owner.owner.owner
            msg = f"{entity.name} changed the {starting_terrain_name} to {tile.terrain.name}."
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

        else:
            # confirm can't do it
            # N.B. the reason why is logged in has_required_tags
            msg = f"You can't do that there!"
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
