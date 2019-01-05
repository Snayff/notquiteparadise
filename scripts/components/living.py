
class Living:
    def __init__(self, hp=0):
        self.hp = hp
        self.base_max_hp = hp
        self.base_power = 0
        self.base_defense = 0
        self.xp_given_on_death = 0

    @property
    def max_hp(self):
        bonus = 0

        if self.owner and self.owner.equipment:
            bonus = bonus + self.owner.equipment.max_hp_bonus
        else:
            bonus = bonus + 0

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

        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = bonus + 0

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
    def defense(self):
        bonus = 0

        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = bonus + 0

        if self.owner and self.owner.race:
            bonus = bonus + self.owner.race.defense
        else:
            bonus = bonus + 0

        if self.owner and self.owner.youth:
            bonus = bonus + self.owner.youth.defense
        else:
            bonus = bonus + 0

        if self.owner and self.owner.adulthood:
            bonus = bonus + self.owner.adulthood.defense
        else:
            bonus = bonus + 0

        return self.base_defense + bonus

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp_given_on_death})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        # results = []
        #
        # damage = self.power - target.living.defense
        #
        # if damage > 0:
        # 	results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(
        # 		self.owner.name.capitalize(), target.name, str(damage)), tcod.white)})
        # 	results.extend(target.living.take_damage(damage))
        # else:
        # 	results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
        # 		self.owner.name.capitalize(), target.name), tcod.white)})
        #
        # return results

        damage = self.power - target.living.defense

        # if damage > 0:
        #     outcome_message = Message(f"{self.owner.name.capitalize()} "
        #                               f"attacks {target.name} for {str(damage)} hit points.", tcod.white)
        #
        # else:
        #     outcome_message = Message(f"{self.owner.name.capitalize()} "
        #                               f" flails harmlessly at {target.name} ")
        #
        # create_event(event_hub, Event(MessageEventNames.BASIC, EventTopics.MESSAGE, [outcome_message]))
        #
        # log_string = f"{self.name} ({self}) attacked {target.name} ({target}) "
        # create_event(event_hub, Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))

    def to_json(self):
        json_data = {
            'hp': self.hp,
            # "base_max_hp": self.base_max_hp, # TODO remove comments when Living updated to take vars
            # "base_power": self.base_power,
            # "base_defense": self.defense,
            # "xp_given_on_death": self.xp_given_on_death
        }

        return json_data

    @staticmethod
    def from_json(json_data):
        hp = json_data.get('hp')
        # base_max_hp = json_data.get("base_max_hp")
        # base_power = json_data.get("base_power")
        # base_defense = json_data.get("base_defense")
        # xp_given_on_death = json_data.get("xp_given_on_death")

        return Living(hp)
