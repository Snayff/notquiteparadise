from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type

from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class BaseSkill(ABC):
    def __init__(self, name):
        self.effects = []
        self.name = name
        self.cooldown = 0

    @abstractmethod
    def get_target_tiles(self, skill_name: str, start_position: Tuple[int, int],
            target_position: Tuple[int, int]) -> List[Tile]:
        """
        Get the target tiles based on the skills expectations
        """
        pass


class BasicAttack(BaseSkill):

    def __init__(self):
        super().__init__("basic_attack")

    def get_target_tiles(self, skill_name: str, start_position: Tuple[int, int],
            target_position: Tuple[int, int]) -> List[Tile]:
        pass