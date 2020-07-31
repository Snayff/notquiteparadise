from __future__ import annotations

from typing import TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine import library
from scripts.engine.action import Affliction, properties_set_by_data
from scripts.engine.core.constants import (DamageType,
    PrimaryStat)
from scripts.engine.effect import AffectStatEffect, DamageEffect

if TYPE_CHECKING:
    from typing import List


@properties_set_by_data
class BoggedDown(Affliction):
    name = "bogged_down"

    def build_effects(self, entity: EntityID) -> List[AffectStatEffect]:
        # TODO - externalise effect data to allow specifying in json

        affect_stat_effect = AffectStatEffect(
            origin=self.creator,
            cause_name=self.name,
            success_effects=[],
            failure_effects=[],
            target=self.affected_entity,
            stat_to_target=PrimaryStat.BUSTLE,
            affect_amount=2
        )

        return [affect_stat_effect]


@properties_set_by_data
class Flaming(Affliction):
    name = "flaming"

    def build_effects(self, entity: EntityID) -> List[DamageEffect]:
        """
        Build the effects of this skill applying to a single entity.
        """
        # TODO - externalise effect data to allow specifying in json
        damage_effect = DamageEffect(
            origin=self.creator,
            success_effects=[],
            failure_effects=[],
            target=entity,
            stat_to_target=PrimaryStat.BUSTLE,
            accuracy=library.GAME_CONFIG.base_values.accuracy,
            damage=int(library.GAME_CONFIG.base_values.damage / 2),
            damage_type=DamageType.BURN,
            mod_stat=PrimaryStat.SKULLDUGGERY,
            mod_amount=0.1
        )

        return [damage_effect]
