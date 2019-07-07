import tcod

from scripts.core.constants import TILE_SIZE, LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_singletons.event_hub import publisher
from scripts.managers.world_methods.affliction_methods import AfflictionMethods
from scripts.managers.world_methods.entity_methods import EntityMethods
from scripts.managers.world_methods.fov_methods import FOVMethods
from scripts.managers.world_methods.map_methods import MapMethods
from scripts.managers.world_methods.skill_methods import SkillMethods

from scripts.world.entity import Entity
from scripts.world.game_map import GameMap


class WorldManager:
    """
    Contains all world related functionality
    """
    def __init__(self):

        self.Entity = EntityMethods(self)
        self.Skill = SkillMethods(self)
        self.Affliction = AfflictionMethods(self)
        self.Map = MapMethods(self)
        self.FOV = FOVMethods(self)

        self.game_map = None  # type: GameMap
        self.player = None  # type: Entity
        self.entities = []
        self.player_fov_map = None  # type: tcod.map.Map
        self.player_fov_is_dirty = False

        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, f"WorldManager initialised."))

    def update(self):
        """
        Update the world manager:
            player fov
            cleanse expired afflictions
        """
        if self.player_fov_is_dirty and self.player:
            player = self.player
            self.FOV.recompute_player_fov(player.x, player.y, player.sight_range)

        # remove expired afflictions
        self.Affliction.cleanse_expired_afflictions()





