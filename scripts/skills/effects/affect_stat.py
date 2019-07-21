from scripts.core.constants import  EffectTypes
from scripts.skills.effects.effect import Effect


class AffectStatEffect(Effect):
    """
    Effect to affect an Entity`s stats

    Attributes:

    """

    def __init__(self, owner):
        super().__init__(owner, "affect_stat", "This is the Affect Stat effect", EffectTypes.AFFECT_STAT)

    def trigger(self):
        """
        Trigger the effect

        """
        super().trigger()

        # TODO - implement stat change (?is this already held in the stat, under the entity? if so confirm here)