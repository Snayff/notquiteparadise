from scripts.core.constants import PrimaryStatTypes
from scripts.global_singletons.data_library import library


class PrimaryStats:
    """
    The base stats of an entity.
    """
    def __init__(self, owner):
        self.owner = owner

    @property
    def vigour(self):
        """
        Influences healthiness.

        Returns:
            int: How vigorous.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.VIGOUR)
        base_value = stat_data.base_value
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.vigour

        if entity.savvy:
            stat_total += entity.savvy.vigour

        if entity.homeland:
            stat_total += entity.homeland.vigour

        return int(stat_total + base_value)

    @property
    def clout(self):
        """
        Influences forceful things.

        Returns:
            int: How much clout.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.CLOUT)
        base_value = stat_data.base_value
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.clout

        if entity.savvy:
            stat_total += entity.savvy.clout

        if entity.homeland:
            stat_total += entity.homeland.clout

        return int(stat_total + base_value)

    @property
    def skullduggery(self):
        """
        Influences sneaky things.

        Returns:
            int: How skullduggery-y.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.SKULLDUGGERY)
        base_value = stat_data.base_value
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.skullduggery

        if entity.savvy:
            stat_total += entity.savvy.skullduggery

        if entity.homeland:
            stat_total += entity.homeland.skullduggery

        return int(stat_total + base_value)

    @property
    def bustle(self):
        """
        Influences speedy things.

        Returns:
            int: How much bustle.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.BUSTLE)
        base_value = stat_data.base_value
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.bustle

        if entity.savvy:
            stat_total += entity.savvy.bustle

        if entity.homeland:
            stat_total += entity.homeland.bustle

        return int(stat_total + base_value)

    @property
    def exactitude(self):
        """
        Influences preciseness.

        Returns:
            int: How exacting.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.EXACTITUDE)
        base_value = stat_data.base_value
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.exactitude

        if entity.savvy:
            stat_total += entity.savvy.exactitude

        if entity.homeland:
            stat_total += entity.homeland.exactitude

        return int(stat_total + base_value)