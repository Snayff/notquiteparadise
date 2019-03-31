from scripts.core.constants import LoggingEventTypes, MessageEventTypes
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent


class Combatant:
    """
    [Component] Can fight.

    Attributes:
        hp (int): Health value.
    """
    def __init__(self, hp=0):
        """

        Args:
            hp (int): Starting health value.
        """
        self.hp = hp
        self.base_max_hp = hp
        self.base_power = 0
        self.base_defence = 0
        self.xp_given_on_death = 0

    @property
    def max_hp(self):
        """
        Maximum health.

        Returns:
            int: max_hp

        """
        bonus = 0

        if self.owner and self.owner.race:
            bonus = bonus + self.owner.race.max_hp
        else:
            bonus = bonus + 0

        if self.owner and self.owner.youth:
            bonus = bonus + self.owner.youth.max_hp
        else:
            bonus = bonus + 0

        if self.owner and self.owner.adulthood:
            bonus = bonus + self.owner.adulthood.max_hp
        else:
            bonus = bonus + 0

        return self.base_max_hp + bonus

    @property
    def power(self):
        """
        Current power.

        Returns:
            int: power

        """
        bonus = 0

        if self.owner and self.owner.race:
            bonus = bonus + self.owner.race.power
        else:
            bonus = bonus + 0

        if self.owner and self.owner.youth:
            bonus = bonus + self.owner.youth.power
        else:
            bonus = bonus + 0

        if self.owner and self.owner.adulthood:
            bonus = bonus + self.owner.adulthood.power
        else:
            bonus = bonus + 0

        return self.base_power + bonus

    @property
    def defence(self):
        """
        Current defence.

        Returns:
            int: defence

        """
        bonus = 0

        if self.owner and self.owner.race:
            bonus = bonus + self.owner.race.defence
        else:
            bonus = bonus + 0

        if self.owner and self.owner.youth:
            bonus = bonus + self.owner.youth.defence
        else:
            bonus = bonus + 0

        if self.owner and self.owner.adulthood:
            bonus = bonus + self.owner.adulthood.defence
        else:
            bonus = bonus + 0

        return self.base_defence + bonus
