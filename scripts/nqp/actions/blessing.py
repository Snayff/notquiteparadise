from typing import List

from scripts.engine.core.effect import Effect
from scripts.engine.internal.action import SkillModifier

"""
Use Blessing.custom_args to set custom effect initialization for a blessing if
an object needs to be used (since objects can't be created in JSON).
"""


class MoveFast(SkillModifier):
    pass


class NoMove(SkillModifier):
    pass


"""
This is one example of how the blessing class can be used to modify blessings
in a way that the JSON can't. The move target must be changed to the owner
or this blessing won't work with skills that don't self-target.
"""


class AttackMove(SkillModifier):
    def apply(self, effects: List[Effect], owner, target):
        super().apply(effects, owner, owner)
