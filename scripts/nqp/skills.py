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
        Trigger any use effects. e.g. create projectile. If no projectile call activate directly.
        """
        pass

    @abstractmethod
    def create_effects(self) -> List[EffectData]:
        """
        Create the skills effects.
        """
        pass

    @abstractmethod
    def activate(self, target_tiles: List[Tile]):
        """
        Trigger the effects on the given tiles.
        """
        pass

    def _process_result(self, result: bool, effect: EffectData) -> Optional[EffectData]:
        """
        Get the success/fail effect, if there is one
        """
        if result and effect.success_effect:
            return effect.success_effect
        elif not result and effect.fail_effect:
            return effect.fail_effect

        return None

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
        # no projectile so call activate directly
        self.activate(target_tiles)

    def activate(self, target_tiles: List[Tile]):
        effects = self.create_effects()
        entity = self.entity

        # process all effects on all tiles
        while effects:
            effect = effects.pop()  # FIFO
            for tile in target_tiles:
                coords = utility.get_coords_from_shape(effect.shape, effect.shape_size)
                effected_tiles = world.get_tiles(tile.x, tile.y, coords)
                result = act.process_effect(effect, effected_tiles, entity)
                result_effect = self._process_result(result, effect)
                if result_effect:
                    effects.append(result_effect)


    def create_effects(self) -> List[EffectData]:
        effects = []
        success_effect_dict = {
            "originator": self.entity,
            "creator": self.name,
            "accuracy": BASE_ACCURACY + 5,
            "stat_to_target": PrimaryStat.VIGOUR,
            "shape": Shape.TARGET,
            "shape_size": 1,
            "required_tags": [
                TargetTag.OTHER_ENTITY
            ],
            "damage": BASE_DAMAGE + 99,
            "damage_type": DamageType.MUNDANE,
            "mod_amount": 0.1,
            "mod_stat": PrimaryStat.CLOUT,
        }
        success_effect = DamageEffectData(**success_effect_dict)

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
            "mod_stat": PrimaryStat.CLOUT,
            "success_effect": success_effect
        }
        effects.append(DamageEffectData(**effect_dict))

        return effects