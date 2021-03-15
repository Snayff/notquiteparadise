import random
from typing import List

from scripts.engine.core.effect import Effect, ApplyAfflictionEffect
from scripts.engine.internal.constant import HitType
from scripts.engine.internal.skill_modifier import SkillModifier
from scripts.engine.internal.data import store

"""
Use Blessing.custom_args to set custom effect initialization for a blessing if
an object needs to be used (since objects can't be created in JSON).
"""

class MoveFast(SkillModifier):
    pass

class NoMove(SkillModifier):
    pass

class Aftershock(SkillModifier):
    pass

class SaltTheWound(SkillModifier):
    def apply(self, effects: List[Effect], owner, target):
        for effect in effects[::-1]:
            if hasattr(effect, 'hit_type_effects'):
                affliction_choice = random.choice([affliction for affliction in store.affliction_registry if store.affliction_registry[affliction].category == 'bane'])

                new_affliction_effect = ApplyAfflictionEffect(
                    origin=effect.origin,
                    target=effect.target,
                    success_effects=[],
                    failure_effects=[],
                    affliction_name=affliction_choice,
                    duration=10,
                )
                effect.hit_type_effects[HitType.CRIT].append(new_affliction_effect) # type: ignore

# this blessing only needs to be written in code because HitTypes can't be written as JSON.
class KeepAnEvenKeel(SkillModifier):
    def apply(self, effects: List[Effect], owner, target):
        for effect in effects[::-1]:
            if hasattr(effect, 'force_hit_type'):
                effect.force_hit_type = HitType.HIT # type: ignore


"""
This is one example of how the blessing class can be used to modify blessings
in a way that the JSON can't. The move target must be changed to the owner
or this blessing won't work with skills that don't self-target.
"""
class AttackMove(SkillModifier):
    def apply(self, effects: List[Effect], owner, target):
        super().apply(effects, owner, owner)
