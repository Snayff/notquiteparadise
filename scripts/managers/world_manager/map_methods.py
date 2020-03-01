from __future__ import annotations

import logging
import math
import scipy.spatial

from typing import TYPE_CHECKING
from scripts.engine.core.constants import TargetTags
from scripts.engine.components import Position, Blocking
from scripts.engine.world_objects.game_map import GameMap
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import List, Tuple, Union
    from scripts.managers.world_manager.world_manager import WorldManager


class MapMethods:
    """
    Methods for querying game map and game map related info and taking game map actions.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """

    def __init__(self, manager):
        self._manager: WorldManager = manager
        self._current_game_map = None




