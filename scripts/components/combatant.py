from scripts.core.constants import LoggingEventNames
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent


class Combatant:
    """
    Component: entity can fight
    """
    def __init__(self, hp=0):
        self.hp = hp
        self.base_max_hp = hp
        self.base_power = 0
        self.base_defence = 0
        self.xp_given_on_death = 0

    @property
    def max_hp(self):
        bonus = 0

        # if self.owner and self.owner.equipment:
        #     bonus = bonus + self.owner.equipment.max_hp_bonus
        # else:
        #     bonus = bonus + 0

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
        bonus = 0

        # if self.owner and self.owner.equipment:
        #     bonus = self.owner.equipment.power_bonus
        # else:
        #     bonus = bonus + 0

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
        bonus = 0

        # if self.owner and self.owner.equipment:
        #     bonus = self.owner.equipment.defense_bonus
        # else:
        #     bonus = bonus + 0

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

        self.hp -= amount

        log_string = f"{self.owner.name}  takes {amount} damage and has {self.hp} health remaining."
        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

        if self.hp <= 0:
            game_manager.create_event(DieEvent(self.owner))

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        damage = self.power - target.combatant.defence

        log_string = f"{self.owner.name}  deals {damage} damage."
        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

        if damage > 0:
            target.combatant.take_damage(damage)


