from __future__ import annotations

import tcod
from typing import TYPE_CHECKING
from scripts.engine.core.constants import FOVInfo, SkillShapes

if TYPE_CHECKING:
    from scripts.managers.world_manager.world_manager import WorldManager


class FOVMethods:
    """
    Methods for querying the fov and fov related info and taking fov actions.
    """
    def __init__(self, manager):
        self._manager: WorldManager = manager
        self._players_fov_map: tcod.map.Map = None


