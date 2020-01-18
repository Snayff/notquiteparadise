from __future__ import annotations

from typing import TYPE_CHECKING
from scripts.core.constants import PrimaryStatTypes, SecondaryStatTypes
from scripts.core.library import library
from scripts.world.components import Race, Homeland, Savvy

if TYPE_CHECKING:
    pass


class CombatStats:
    """
    Object to hold all of an entities stats. Derived from various components.
    """
    def __init__(self, entity: int):
        self.entity = entity

    @property
    def vigour(self):
        """
        Influences healthiness.

        Returns:
            int: How vigorous. Never below 1.
        """
        stat = PrimaryStatTypes.VIGOUR
        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        return world.Entity.get_primary_stat(self.entity, stat)

    @property
    def clout(self):
        """
        Influences forceful things.

        Returns:
            int: How much clout. Never below 1.
        """
        stat = PrimaryStatTypes.CLOUT
        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        return world.Entity.get_primary_stat(self.entity, stat)

    @property
    def skullduggery(self):
        """
        Influences sneaky things.

        Returns:
            int: How skullduggery-y. Never below 1.
        """
        stat = PrimaryStatTypes.SKULLDUGGERY
        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        return world.Entity.get_primary_stat(self.entity, stat)

    @property
    def bustle(self):
        """
        Influences speedy things.

        Returns:
            int: How much bustle. Never below 1.
        """
        stat = PrimaryStatTypes.BUSTLE
        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        return world.Entity.get_primary_stat(self.entity, stat)

    @property
    def exactitude(self):
        """
        Influences preciseness.

        Returns:
            int: How exacting. Never below 1.
        """
        stat = PrimaryStatTypes.EXACTITUDE
        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        return world.Entity.get_primary_stat(self.entity, stat)

    @property
    def max_hp(self):
        """
        Total damage an entity can take before death.

        Returns:
            int:
        """
        stat = SecondaryStatTypes.MAX_HP
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def max_stamina(self):
        """
        an entities energy to take actions.

        Returns:
            int:
        """
        stat = SecondaryStatTypes.MAX_STAMINA
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def accuracy(self):
        """
        an entities likelihood to hit.

        Returns:
            int:
        """
        stat = SecondaryStatTypes.ACCURACY
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_burn(self):
        """
        an entities resistance to burn damage.

        Returns:
            int:
        """
        stat = SecondaryStatTypes.RESIST_BURN
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_cold(self):
        """
        an entities resistance to cold damage.

        Returns:
            int:
        """
        stat = SecondaryStatTypes.RESIST_COLD
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_chemical(self):
        """
        an entities resistance to chemical damage.

        Returns:
            int:
        """
        stat = SecondaryStatTypes.RESIST_CHEMICAL
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_astral(self):
        """
        an entities resistance to astral damage.

        Returns:
            int:
        """
        stat = SecondaryStatTypes.RESIST_ASTRAL
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_mundane(self):
        """
        an entities resistance to mundane damage.

        Returns:
            int:
        """
        stat = SecondaryStatTypes.RESIST_MUNDANE
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world
        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def sight_range(self):
        """
        Highest value among base contributions then modifiers applied. Cant be less than 0.

        Returns:
            int:
        """
        # TODO - moving to the top creates an import error. Resolve it.
        from scripts.managers.world_manager import world

        stat = SecondaryStatTypes.SIGHT_RANGE
        stat_data = library.get_secondary_stat_data(stat)

        # from characteristics
        components = world.Entity.get_components(self.entity)
        base_value = stat_data.base_value
        for component in components:
            if isinstance(component, Homeland):
                data = library.get_homeland_data(component.name)
                base_value = max(base_value, data.sight_range)
            elif isinstance(component, Savvy):
                data = library.get_savvy_data(component.name)
                base_value = max(base_value, data.sight_range)
            elif isinstance(component, Race):
                data = library.get_race_data(component.name)
                base_value = max(base_value, data.sight_range)

        # from stats
        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        affliction_changes = world.Affliction.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total


