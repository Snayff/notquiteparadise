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

    def take_damage(self, amount):
        """
        Apply damage to health.

        Args:
            amount (int): Amount to take from health.

        """
        self.hp -= amount

        log_string = f"{self.owner.name}  takes {amount} damage and has {self.hp} health remaining."
        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventTypes.MUNDANE, log_string))

        if self.hp <= 0:
            game_manager.create_event(DieEvent(self.owner))

    def heal(self, amount):
        """
        Apply heal to health.

        Args:
            amount (int): Amount to add to health.

        """
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        """
        Attack another entity.

        Args:
            target (Entity): Entity to get attacked.

        """
        damage = max(self.power - target.combatant.defence, 0)

        msg = f"{self.owner.name}  deals {damage} damage."
        from scripts.core.global_data import game_manager
        game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

        if damage > 0:
            target.combatant.take_damage(damage)


