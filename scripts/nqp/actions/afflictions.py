from __future__ import annotations

from typing import TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine import library
from scripts.engine.action import Affliction, init_action
from scripts.engine.core.constants import DamageType, PrimaryStat
from scripts.engine.effect import AffectStatEffect, DamageEffect

if TYPE_CHECKING:
    from typing import List


@init_action
class BoggedDown(Affliction):
    key = "bogged_down"

    def build_effects(self, entity: EntityID, potency: float = 1.0) -> List[AffectStatEffect]:  # type: ignore

        affect_stat_effect = AffectStatEffect(
            origin=self.origin,
            cause_name=self.key,
            success_effects=[],
            failure_effects=[],
            target=self.affected_entity,
            stat_to_target=PrimaryStat.BUSTLE,
            affect_amount=2,
        )

        return [affect_stat_effect]


@init_action
class Flaming(Affliction):
    key = "flaming"

    def build_effects(self, entity: EntityID, potency: float = 1.0) -> List[DamageEffect]:  # type: ignore
        """
        Build the effects of this skill applying to a single entity.
        """
        damage_effect = DamageEffect(
            origin=self.origin,
            success_effects=[],
            failure_effects=[],
            target=entity,
            stat_to_target=PrimaryStat.BUSTLE,
            accuracy=library.GAME_CONFIG.base_values.accuracy,
            damage=int(library.GAME_CONFIG.base_values.damage / 2),
            damage_type=DamageType.BURN,
            mod_stat=PrimaryStat.SKULLDUGGERY,
            mod_amount=0.1,
        )

        return [damage_effect]
