
from scripts.core.constants import SecondaryStatTypes
from scripts.global_singletons.data_library import library


class SecondaryStats:
    """
    Stats derived from the primary stats.
    """
    # TODO - load the modifiers and base values from a json

    def __init__(self, owner):
        self.owner = owner

    @property
    def max_hp(self):
        """
        Total damage an entity can take before death.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.MAX_HP)
        base_value = stat_data.base_value
        
        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude
        return int(stat_total)

    @property
    def accuracy(self):
        """
        Base value of an entities likelihood to hit.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.ACCURACY)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude
        return int(stat_total)
        return int(stat_total)

    # TODO - update below stats to use library data and align to new damage types

    @property
    def resist_blunt(self):
        vigour = self.owner.primary_stats.vigour
        vigour_modifier = 1

        stat_total = (vigour * vigour_modifier)
        return int(stat_total)

    @property
    def resist_pierce(self):
        bustle = self.owner.primary_stats.bustle
        bustle_modifier = 1

        stat_total = (bustle * bustle_modifier)
        return int(stat_total)

    @property
    def resist_elemental(self):
        skullduggery = self.owner.primary_stats.skullduggery
        subtlety_modifier = 2

        stat_total = (skullduggery * subtlety_modifier)
        return int(stat_total)


