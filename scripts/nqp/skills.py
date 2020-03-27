from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type

from snecs.typedefs import EntityID

from scripts.engine import world, utility, act, existence
from scripts.engine.core.constants import Direction, BASE_ACCURACY, PrimaryStat, Shape, TargetTag, BASE_DAMAGE, \
    DamageType, DirectionType, ProjectileSpeed, TravelMethod, TerrainCollision, ProjectileExpiry
from scripts.engine.core.definitions import EffectData, DamageEffectData, ProjectileData
from scripts.engine.library import library
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class BaseSkill(ABC):
    def __init__(self, name: str, owning_entity: EntityID):
        self.name = name
        self.entity = owning_entity
        self.cooldown = 0

    def get_use_tiles_and_directions(self, start_position: Tuple[int, int],
            target_position: Tuple[int, int]) -> List[Optional[Tuple[Tile, DirectionType]]]:
        """
        Get the target tiles and relative directions
        """
        target_tiles = []
        data = library.get_skill_data(self.name)
        tags = data.use_required_tags

        # target centre of target pos
        tiles = world.get_tiles(target_position[0], target_position[1], [(0, 0)])

        for tile in tiles:
            if world.tile_has_tags(tile, tags, self.entity):
                direction = world.get_direction(start_position, (tile.x, tile.y))
                target_tiles.append((tile, direction))

        return target_tiles

    @abstractmethod
    def use(self, use_tiles_and_directions: List[Tuple[Tile, DirectionType]]):
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

    @staticmethod
    def _process_result(result: bool, effect: EffectData) -> Optional[EffectData]:
        """
        Get the success/fail effect, if there is one
        """
        if result and effect.success_effect:
            return effect.success_effect
        elif not result and effect.fail_effect:
            return effect.fail_effect

        return None


################# EXAMPLES ################################
########## "use" a projectile ###########################
#         _name = self.name + "s projectile"
#         _desc = existence.get_name(self.entity) + self.name + "s projectile"
#         proj_data = ProjectileData(
#             creator=self.entity,
#             skill_name=self.name,
#             name=_name,
#             description=_desc,
#             sprite="skills/placeholder/icon_01.png",
#             required_tags=[TargetTag.OTHER_ENTITY],
#             speed=ProjectileSpeed.SLOW,
#             travel_type=TravelMethod.STANDARD,
#             range=3,
#             terrain_collision=TerrainCollision.FIZZLE,
#             expiry_type=ProjectileExpiry.FIZZLE
#         )
#
#         for tile, direction in use_tiles_and_directions:
#             proj_data.direction = direction
#             existence.create_projectile(self.entity, tile.x, tile.y, proj_data)
#
############### "use" without projectile ###############
#         tiles = []
#         for tile, direction in use_tiles_and_directions:
#             tiles.append(tile)
#         self.activate(tiles)


class BasicAttack(BaseSkill):
    """
    Purpose: To provide a simple damaging effect as the fall back option for entities. Also for use with bump attacks.
    """
    def __init__(self, owning_entity):
        super().__init__("basic_attack", owning_entity)

    def use(self, use_tiles_and_directions: List[Tuple[Tile, DirectionType]]):
        # no projectile so call activate directly
        tiles = []
        for tile, direction in use_tiles_and_directions:
            tiles.append(tile)
        self.activate(tiles)

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
        }
        effects.append(DamageEffectData(**effect_dict))

        return effects
