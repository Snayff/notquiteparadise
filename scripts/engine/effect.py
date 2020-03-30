from __future__ import annotations

import logging
from abc import ABC
from typing import TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine import world
from scripts.engine.core.constants import PrimaryStatType, DamageTypeType
from scripts.engine.core.event_core import publisher
from scripts.engine.event import DieEvent

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class Effect(ABC):
    def __init__(self, origin: EntityID, success_effects: List[Effect], failure_effects: List[Effect]):
        self.origin = origin
        self.success_effects: List[Effect] = success_effects
        self.failure_effects: List[Effect] = failure_effects


class DamageEffect(Effect):
    def __init__(self, origin: EntityID, victim: EntityID, success_effects: List[Effect],
                failure_effects: List[Effect], stat_to_target: PrimaryStatType, accuracy: int,
                damage: int, damage_type: DamageTypeType, mod_stat: PrimaryStatType, mod_amount: float):

        super().__init__(origin, success_effects, failure_effects)

        self.accuracy = accuracy
        self.stat_to_target = stat_to_target
        self.victim = victim
        self.damage = damage
        self.damage_type = damage_type
        self.mod_amount = mod_amount
        self.mod_stat = mod_stat

    def evaluate(self) -> List[Optional[Effect]]:
        """
        Resolve the damage effect and return the conditional effects based on if the damage is greater than 0.
        """
        logging.debug("Evaluating Damage Effect...")
        defenders_stats = world.create_combat_stats(self.victim)
        attackers_stats = world.create_combat_stats(self.origin)

        # get hit type
        stat_to_target_value = getattr(defenders_stats, self.stat_to_target.lower())
        to_hit_score = world.calculate_to_hit_score(attackers_stats.accuracy, self.accuracy, stat_to_target_value)
        hit_type = world.get_hit_type(to_hit_score)

        # calculate damage
        resist_value = getattr(defenders_stats, "resist_" + self.damage_type.lower())
        mod_value = getattr(attackers_stats, self.mod_stat.lower())
        damage = world.calculate_damage(self.damage, mod_value, resist_value, hit_type)

        if world.apply_damage(self.victim, damage) <= 0:
            publisher.publish(DieEvent(self.victim))

        if damage > 0:
            return self.success_effects
        else:
            return self.failure_effects


class MoveActorEffect(Effect):
    def __init__(self, origin: EntityID, success_effects: List[Effect], failure_effects: List[Effect]):
        super().__init__(origin, success_effects, failure_effects)

    # TODO - rebuild effect