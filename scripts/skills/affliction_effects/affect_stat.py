from scripts.skills.affliction_effects.affliction_effect import AfflictionEffect


class AffectStatAfflictionEffect(AfflictionEffect):
    """
    SkillEffect to affect an Entity's stats

    Attributes:

    """

    def __init__(self, owner, stat_to_affect, amount):
        super().__init__(owner, "Affect stat", "This is the Affect Stat effect")
        self.stat_to_affect = stat_to_affect
        self.amount = amount

    def trigger(self):
        """
        Trigger the effect

        """
        super().trigger()