from __future__ import annotations

import logging
import esper
from typing import TYPE_CHECKING
from scripts.managers.world_methods.entity_methods import EntityMethods
from scripts.managers.world_methods.fov_methods import FOVMethods
from scripts.managers.world_methods.god_methods import GodMethods
from scripts.managers.world_methods.map_methods import MapMethods
from scripts.managers.world_methods.skill_methods import SkillMethods

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
        self.God = GodMethods(self)

        logging.info(f"WorldManager initialised.")

    def update(self):
        """
        None but method must exist
        """


world = WorldManager()