from __future__ import annotations

from typing import TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine.core.effect import AffectStatEffect, DamageEffect
from scripts.engine.internal import library
from scripts.engine.internal.action import Affliction
from scripts.engine.internal.constant import DamageType, PrimaryStat

if TYPE_CHECKING:
    from typing import List


class BoggedDown(Affliction):
    def _build_effects(self, entity: EntityID, potency: float = 1.0) -> List[AffectStatEffect]:  # type: ignore

        affect_stat_effect = AffectStatEffect(
            origin=self.origin,
            cause_name=self.name,
            success_effects=[],
            failure_effects=[],
            target=self.affected_entity,
            stat_to_target=PrimaryStat.BUSTLE,
            affect_amount=2,
        )

        return [affect_stat_effect]


class Flaming(Affliction):
    def _build_effects(self, entity: EntityID, potency: float = 1.0) -> List[DamageEffect]:  # type: ignore
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
