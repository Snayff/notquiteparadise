from scripts.core.constants import MessageEventTypes, LoggingEventTypes, TargetTags
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.skills.effects.skill_effect import SkillEffect
from scripts.world.terrain.floor import Floor
from scripts.world.terrain.terrain import Terrain
from scripts.world.terrain.wall import Wall
from scripts.world.tile import Tile


class ChangeTerrainSkillEffect(SkillEffect):
    """
    SkillEffect to change the terrain of a tile
    """

    def __init__(self, required_target, required_tags, new_terrain):
        super().__init__("Manipulate Terrain", "This is the Manipulate Terrain effect", required_target, required_tags)

        # get class from enum and store in self
        if new_terrain == TargetTags.FLOOR:
            self.new_terrain = Floor()
        elif new_terrain == TargetTags.WALL:
            self.new_terrain = Wall()

    def trigger(self, terrain_to_change):
        """
        Trigger the effect; check tags and then, if all True, apply the effect

        Args:
            terrain_to_change (Terrain):
        """
        super().trigger()

        from scripts.core.global_data import game_manager

        tags_checked = {}  # bool list of tags checked
        tile = terrain_to_change.owner
        terrain = terrain_to_change
        starting_terrain_name = terrain.name
        target_type = self.get_target_type(terrain)

        # check the type is correct, then that the tags match
        if target_type == self.required_target_type:

            # assess all tags
            for tag in self.required_tags:
                tags_checked[tag] = tile.has_tag(tag)

            # if all tags came back true apply the change
            if all(value for value in tags_checked.values()):
                tile.set_terrain(self.new_terrain)

                # success message
                entity = self.owner.owner.owner
                msg = f"{entity.name} changed the {starting_terrain_name} to {tile.terrain.name}."
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

            else:
                # log why
                log_string = f"-> target tags incorrect; tag results:{tags_checked}"
                game_manager.create_event(LoggingEvent(LoggingEventTypes.WARNING, log_string))
        else:
            # confirm can't do it
            msg = f"You can't do that there!"
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

            # log why
            log_string = f"-> target type incorrect; selected:{target_type}, needed:{self.required_target_type}"
            game_manager.create_event(LoggingEvent(LoggingEventTypes.WARNING, log_string))