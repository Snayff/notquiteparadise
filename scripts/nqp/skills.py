from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type

from snecs.typedefs import EntityID

from scripts.engine import world, utility, act
from scripts.engine.core.constants import Direction, BASE_ACCURACY, PrimaryStat, Shape, TargetTag, BASE_DAMAGE, \
    DamageType
from scripts.engine.core.definitions import EffectData, DamageEffectData
from scripts.engine.library import library
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class BaseSkill(ABC):
    def __init__(self, name: str, owning_entity: EntityID):
        self.effects = []
        self.name = name
        self.entity = owning_entity
        self.cooldown = 0

    @abstractmethod
    def get_target_tiles(self, start_position: Tuple[int, int],
            target_position: Tuple[int, int]) -> List[Optional[Tile]]:
        """
        Get the target tiles based on the skills expectations
        """
        pass

    @abstractmethod
    def use(self, target_tiles: List[Tile]):
        """
        Create the relevant effects for the skill.
        """
        pass

    @abstractmethod
    def create_effects(self) -> List[EffectData]:
        """
        Create the skills effects.
        """
        pass


class BasicAttack(BaseSkill):

    def __init__(self, owning_entity):
        super().__init__("basic_attack", owning_entity)

    def get_target_tiles(self, start_position: Tuple[int, int],
            target_position: Tuple[int, int]) -> List[Optional[Tile]]:
        tiles_with_tags = []
        data = library.get_skill_data(self.name)
        tags = data.use_required_tags

        # target centre of target pos
        tiles = world.get_tiles(target_position[0], target_position[1], [Direction.CENTRE])

        for tile in tiles:
            if world.tile_has_tags(tile, tags, self.entity):
                tiles_with_tags.append(tile)

        return tiles_with_tags

    def use(self, target_tiles: List[Tile]):
        effects = self.create_effects()
        entity = self.entity

        # process all effects on all tiles
        for effect in effects:
            for tile in target_tiles:
                coords = utility.get_coords_from_shape(effect.shape, effect.shape_size)
                effected_tiles = world.get_tiles(tile.x, tile.y, coords)
                act.process_effect(effect, effected_tiles, entity)

    def create_effects(self) -> List[EffectData]:
        effects = []

        effect_dict = {
            "originator": self.entity,
            "creator": self.name,
            "accuracy": BASE_ACCURACY + 5,
            "stat_to_target": PrimaryStat.VIGOUR,
            "shape": Shape.TARGET,
            "shape_size": 1,
            "required_tags": [
                TargetTag.OTHER_ENTITY
            ],
            "damage": BASE_DAMAGE + 20,
            "damage_type": DamageType.MUNDANE,
            "mod_amount": 0.1,
            "mod_stat": PrimaryStat.CLOUT
        }
        effects.append(DamageEffectData(**effect_dict))

        return effects