from __future__ import annotations

from typing import TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine import world
from scripts.engine.core.constants import PrimaryStat, SecondaryStat


if TYPE_CHECKING:
    pass


class CombatStats:
    """
    Object to hold all of an entities stats. Derived from various components.
    """

    def __init__(self, entity: EntityID):
        self.entity = entity

    ##############  PRIMARY STATS ##########################

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

    ############## SECONDARY STATS ##########################

    @property
    def max_health(self) -> int:
        """
        Total damage an entity can take before death.
        """
        stat = SecondaryStat.MAX_HEALTH
        return world.get_secondary_stat(self.entity, stat)

    @property
    def max_stamina(self) -> int:
        """
        an entities energy to take actions.

        """
        stat = SecondaryStat.MAX_STAMINA
        return world.get_secondary_stat(self.entity, stat)

    @property
    def accuracy(self) -> int:
        """
        an entities likelihood to hit.
        """
        stat = SecondaryStat.ACCURACY
        return world.get_secondary_stat(self.entity, stat)

    @property
    def resist_burn(self) -> int:
        """
        an entities resistance to burn damage.

        """
        stat = SecondaryStat.RESIST_BURN
        return world.get_secondary_stat(self.entity, stat)

    @property
    def resist_cold(self) -> int:
        """
        an entities resistance to cold damage.

        """
        stat = SecondaryStat.RESIST_COLD
        return world.get_secondary_stat(self.entity, stat)

    @property
    def resist_chemical(self) -> int:
        """
        an entities resistance to chemical damage.
        """
        stat = SecondaryStat.RESIST_CHEMICAL
        return world.get_secondary_stat(self.entity, stat)

    @property
    def resist_astral(self) -> int:
        """
        an entities resistance to astral damage.
        """
        stat = SecondaryStat.RESIST_ASTRAL
        return world.get_secondary_stat(self.entity, stat)

    @property
    def resist_mundane(self) -> int:
        """
        an entities resistance to mundane damage.
        """
        stat = SecondaryStat.RESIST_MUNDANE
        return world.get_secondary_stat(self.entity, stat)

    @property
    def sight_range(self) -> int:
        """
        Highest value among base contributions then modifiers applied. Cant be less than 0.
        """

        stat = SecondaryStat.SIGHT_RANGE
        return world.get_secondary_stat(self.entity, stat)

    @property
    def rush(self) -> int:
        """
        how quickly an entity does things. Reduce time cost of actions.
        """
        stat = SecondaryStat.RUSH
        return world.get_secondary_stat(self.entity, stat)
