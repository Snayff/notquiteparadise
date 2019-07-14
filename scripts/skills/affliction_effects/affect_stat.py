from scripts.skills.affliction_effects.affliction_effect import AfflictionEffect


class AffectStatAfflictionEffect(AfflictionEffect):
    """
    SkillEffect to affect an Entity`s stats

    Attributes:

    """

    def __init__(self, owner, affliction_effect_type):
        super().__init__(owner, "affect_stat", "This is the Affect Stat effect", affliction_effect_type)

    def trigger(self):
        """
        Trigger the effect

        """
        super().trigger()

        # TODO - implement stat change (is this already held in the stat, under the entity? if so confirm here)