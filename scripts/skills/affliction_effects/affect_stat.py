from scripts.core.constants import AfflictionEffectTypes
from scripts.skills.affliction_effects.affliction_effect import AfflictionEffect


class AffectStatAfflictionEffect(AfflictionEffect):
    """
    SkillEffect to affect an Entity`s stats

    Attributes:

    """

    def __init__(self, owner):
        super().__init__(owner, "affect_stat", "This is the Affect Stat effect", AfflictionEffectTypes.AFFECT_STAT)

    def trigger(self):
        """
        Trigger the effect

        """
        super().trigger()

        # TODO - implement stat change (?is this already held in the stat, under the entity? if so confirm here)