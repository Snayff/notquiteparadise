from __future__ import annotations

from typing import TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine import world
from scripts.engine.component import Homeland, People, Savvy
from scripts.engine.core.constants import PrimaryStat, SecondaryStat
from scripts.engine.core.definitions import CharacteristicData
from scripts.engine.library import library

if TYPE_CHECKING:
    pass


class CombatStats:
    """
    Object to hold all of an entities stats. Derived from various components.
    """

    def __init__(self, entity: EntityID):
        self.entity = entity

    @property
    def vigour(self) -> int:
        """
        Influences healthiness. Never below 1.
        """
        stat = PrimaryStat.VIGOUR

        return world.get_primary_stat(self.entity, stat)

    @property
    def clout(self) -> int:
        """
        Influences forceful things. Never below 1.
        """
        stat = PrimaryStat.CLOUT

        return world.get_primary_stat(self.entity, stat)

    @property
    def skullduggery(self) -> int:
        """
        Influences sneaky things. Never below 1.
        """
        stat = PrimaryStat.SKULLDUGGERY

        return world.get_primary_stat(self.entity, stat)

    @property
    def bustle(self) -> int:
        """
        Influences speedy things. Never below 1.
        """
        stat = PrimaryStat.BUSTLE

        return world.get_primary_stat(self.entity, stat)

    @property
    def exactitude(self) -> int:
        """
        Influences preciseness. Never below 1.
        """
        stat = PrimaryStat.EXACTITUDE

        return world.get_primary_stat(self.entity, stat)

    @property
    def max_health(self) -> int:
        """
        Total damage an entity can take before death.
        """
        stat = SecondaryStat.MAX_HEALTH
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def max_stamina(self) -> int:
        """
        an entities energy to take actions.

        """
        stat = SecondaryStat.MAX_STAMINA
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def accuracy(self) -> int:
        """
        an entities likelihood to hit.
        """
        stat = SecondaryStat.ACCURACY
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_burn(self) -> int:
        """
        an entities resistance to burn damage.

        """
        stat = SecondaryStat.RESIST_BURN
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_cold(self) -> int:
        """
        an entities resistance to cold damage.

        """
        stat = SecondaryStat.RESIST_COLD
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_chemical(self) -> int:
        """
        an entities resistance to chemical damage.
        """
        stat = SecondaryStat.RESIST_CHEMICAL
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_astral(self) -> int:
        """
        an entities resistance to astral damage.
        """
        stat = SecondaryStat.RESIST_ASTRAL
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_mundane(self) -> int:
        """
        an entities resistance to mundane damage.
        """
        stat = SecondaryStat.RESIST_MUNDANE
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def sight_range(self) -> int:
        """
        Highest value among base contributions then modifiers applied. Cant be less than 0.
        """

        stat = SecondaryStat.SIGHT_RANGE
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value
        entity = self.entity
        # from characteristics
        checks = {
            1: (Homeland, library.get_homeland_data),
            2: (People, library.get_people_data),
            3: (Savvy, library.get_savvy_data)
        }
        for characteristic in checks.values():
            if world.entity_has_component(self.entity, characteristic[0]):
                component = world.get_entitys_component(entity, characteristic[0])
                if component:
                    data: CharacteristicData = characteristic[1](component.name)  # type: ignore
                    base_value = max(base_value, data.sight_range)

        # from stats
        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd afflictions
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def rush(self) -> int:
        """
        how quickly an entity does things. Reduce time cost of actions.
        """
        stat = SecondaryStat.RUSH
        stat_data = library.get_secondary_stat_data(stat)
        base_value = stat_data.base_value

        from_vigour = self.vigour * stat_data.vigour_mod
        from_clout = self.clout * stat_data.clout_mod
        from_skullduggery = self.skullduggery * stat_data.skullduggery_mod
        from_bustle = self.bustle * stat_data.bustle_mod
        from_exactitude = self.exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        # TODO - readd affliction changes
        affliction_changes = 0  # world.Afflictions.get_stat_change_from_afflictions_on_entity(self.entity, stat)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total
