from scripts.skills.affliction_effects.affliction_effect import AfflictionEffect


class AffectStatAfflictionEffect(AfflictionEffect):
    """
    SkillEffect to affect an Entity`s stats

    Attributes:

    """

    def __init__(self, owner, stat_to_affect, amount):
        super().__init__(owner, "affect_stat", "This is the Affect Stat effect")

        from scripts.global_singletons.managers import world_manager
        stat = world_manager.Skill.get_stat_from_string(stat_to_affect)

        self.stat_to_affect = stat
        self.amount = amount

    def trigger(self):
        """
        Trigger the effect

        """
        super().trigger()