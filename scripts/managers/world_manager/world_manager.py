from __future__ import annotations

import logging
import esper
from typing import TYPE_CHECKING

from scripts.core import utilities
from scripts.managers.world_manager.entity_methods import EntityMethods
from scripts.managers.world_manager.fov_methods import FOVMethods
from scripts.managers.world_manager.map_methods import MapMethods
from scripts.managers.world_manager.skill_methods import SkillMethods
from scripts.world.components import Aesthetic

if TYPE_CHECKING:
    pass


class WorldManager:
    """
    Contains all world related functionality
    """
    def __init__(self):

        self.World = esper.World()
        self.Entity = EntityMethods(self)
        self.Skill = SkillMethods(self)
        self.Map = MapMethods(self)
        self.FOV = FOVMethods(self)

        logging.info(f"WorldManager initialised.")

    def update(self, delta_time: float):
        """
        Update real-time timers on entities
        """
        # move entities screen position towards target
        for entity, aesthetic in self.Entity.get_component(Aesthetic):
            # increment time
            aesthetic.current_sprite_duration += delta_time

            # do we need to show moving to a new position?
            if aesthetic.screen_x != aesthetic.target_screen_x or aesthetic.screen_y != aesthetic.target_screen_y:
                aesthetic.screen_x = utilities.lerp(aesthetic.screen_x, aesthetic.target_screen_x, 0.2)
                aesthetic.screen_y = utilities.lerp(aesthetic.screen_y, aesthetic.target_screen_y, 0.2)
            # not moving so reset to idle
            else:
                aesthetic.current_sprite = aesthetic.sprites.idle


world = WorldManager()