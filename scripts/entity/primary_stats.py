from scripts.core.constants import PrimaryStatTypes
from scripts.core.data_library import library


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
            int: How vigorous. Never below 1.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.VIGOUR)
        base_value = stat_data.base_value
        entity = self.owner.owner
        component_changes = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            component_changes += race_data.vigour

        if entity.savvy:
            # TODO - add savvy data to stat
            component_changes += entity.savvy.vigour

        if entity.homeland:
            # TODO - add homeland data to stat
            component_changes += entity.homeland.vigour

        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, PrimaryStatTypes.VIGOUR)
        
        total = max(1, int(component_changes + base_value + affliction_changes))
        
        return total

    @property
    def clout(self):
        """
        Influences forceful things.

        Returns:
            int: How much clout. Never below 1.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.CLOUT)
        base_value = stat_data.base_value
        entity = self.owner.owner
        component_changes = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            component_changes += race_data.clout

        if entity.savvy:
            component_changes += entity.savvy.clout

        if entity.homeland:
            component_changes += entity.homeland.clout

        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.owner.owner,
                                                                                                PrimaryStatTypes.CLOUT)

        total = max(1, int(component_changes + base_value + affliction_changes))

        return total

    @property
    def skullduggery(self):
        """
        Influences sneaky things.

        Returns:
            int: How skullduggery-y. Never below 1.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.SKULLDUGGERY)
        base_value = stat_data.base_value
        entity = self.owner.owner
        component_changes = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            component_changes += race_data.skullduggery

        if entity.savvy:
            component_changes += entity.savvy.skullduggery

        if entity.homeland:
            component_changes += entity.homeland.skullduggery

        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.owner.owner,
                                PrimaryStatTypes.SKULLDUGGERY)

        total = max(1, int(component_changes + base_value + affliction_changes))

        return total

    @property
    def bustle(self):
        """
        Influences speedy things.

        Returns:
            int: How much bustle. Never below 1.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.BUSTLE)
        base_value = stat_data.base_value
        entity = self.owner.owner
        component_changes = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            component_changes += race_data.bustle

        if entity.savvy:
            component_changes += entity.savvy.bustle

        if entity.homeland:
            component_changes += entity.homeland.bustle

        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.owner.owner,
                                                                                        PrimaryStatTypes.BUSTLE)

        total = max(1, int(component_changes + base_value + affliction_changes))

        return total

    @property
    def exactitude(self):
        """
        Influences preciseness.

        Returns:
            int: How exacting. Never below 1.
        """
        stat_data = library.get_primary_stat_data(PrimaryStatTypes.EXACTITUDE)
        base_value = stat_data.base_value
        entity = self.owner.owner
        component_changes = 0

        if entity.race:
            race_data = library.get_race_data(entity.race.name)
            component_changes += race_data.exactitude

        if entity.savvy:
            component_changes += entity.savvy.exactitude

        if entity.homeland:
            component_changes += entity.homeland.exactitude

        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.owner.owner,
                                                                                            PrimaryStatTypes.EXACTITUDE)

        total = max(1, int(component_changes + base_value + affliction_changes))

        return total