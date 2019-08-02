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
        base_amount = 5
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.vigour

        if entity.savvy:
            stat_total += entity.savvy.vigour

        if entity.homeland:
            stat_total += entity.homeland.vigour

        return int(stat_total + base_amount)

    @property
    def clout(self):
        """
        Influences forceful things.

        Returns:
            int: How much clout.
        """
        base_amount = 5
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.clout

        if entity.savvy:
            stat_total += entity.savvy.clout

        if entity.homeland:
            stat_total += entity.homeland.clout

        return int(stat_total + base_amount)

    @property
    def skullduggery(self):
        """
        Influences sneaky things.

        Returns:
            int: How skullduggery-y.
        """
        base_amount = 5
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.skullduggery

        if entity.savvy:
            stat_total += entity.savvy.skullduggery

        if entity.homeland:
            stat_total += entity.homeland.skullduggery

        return int(stat_total + base_amount)

    @property
    def bustle(self):
        """
        Influences speedy things.

        Returns:
            int: How much bustle.
        """
        base_amount = 5
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.bustle

        if entity.savvy:
            stat_total += entity.savvy.bustle

        if entity.homeland:
            stat_total += entity.homeland.bustle

        return int(stat_total + base_amount)

    @property
    def exactitude(self):
        """
        Influences preciseness.

        Returns:
            int: How exacting.
        """
        base_amount = 5
        entity = self.owner.owner
        stat_total = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            stat_total += race_data.exactitude

        if entity.savvy:
            stat_total += entity.savvy.exactitude

        if entity.homeland:
            stat_total += entity.homeland.exactitude

        return int(stat_total + base_amount)