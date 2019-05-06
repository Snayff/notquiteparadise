import random

from scripts.core.constants import LoggingEventTypes, TargetTypes, TargetTags, MessageEventTypes, SecondaryStatTypes, \
    HitTypes, DamageTypes, PrimaryStatTypes
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.skills.effects.effect import Effect
from scripts.world.terrain.terrain import Terrain


class DamageEffect(Effect):
    """
    Effect to damage an entity

    Attributes:
        damage(int):
        damage_type(int):
        target_type(TargetTypes):
        tags(list): list of TargetType enums
        accuracy(int):
        stat_to_target(PrimaryStatTypes):
    """

    def __init__(self, damage, damage_type, target_type, tags, accuracy, stat_to_target):
        super().__init__("Damage", "This is the damage effect", target_type, tags)
        self.base_damage = damage
        self.damage_type = damage_type
        self.base_accuracy = accuracy
        self.stat_to_target = stat_to_target

    def trigger(self, attacking_entity, defending_entity):
        """
        Trigger the effect

        Args:
            attacking_entity:
            defending_entity:
        """
        attacker = attacking_entity
        defender = defending_entity
        damage = 0

        from scripts.core.global_data import game_manager
        log_string = f"Applying '{self.name}' effect from {self.owner.name}..."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        # store the base class type for comparison
        target_type_for_comparison = None
        if self.target_type == TargetTypes.TERRAIN:
            target_type_for_comparison = type(Terrain(0, 0))
        elif self.target_type == TargetTypes.ENTITY:
            target_type_for_comparison = type(attacker)

        # check the type is correct, then that the tags match
        if type(defender) == target_type_for_comparison:
            # if it needs to be another entity then it can't be looking at itself
            if TargetTags.OTHER_ENTITY in self.target_tags:
                if attacker != defender:
                    to_hit_score = self.calculate_to_hit_score(attacker, defender)
                    hit_type = self.get_hit_type(to_hit_score)
                    damage = self.calculate_damage(attacker, defender, hit_type)

            # apply damage
            if damage > 0:
                self.apply_damage(attacker, defender, damage)

                if hit_type == HitTypes.GRAZE:
                    hit_type_desc = "grazes"
                elif hit_type == HitTypes.HIT:
                    hit_type_desc = "hits"
                elif hit_type == HitTypes.CRIT:
                    hit_type_desc = "crits"
                else:
                    hit_type_desc = "does something unknown"

                msg = f"{attacker.name} {hit_type_desc} {defender.name} for {damage}."
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
                # TODO - add the damage type to the message and replace the type with an icon
                # TODO - add the explanation of the damage roll to a tooltip

                # check if defender died
                if defender.combatant.hp <= 0:
                    game_manager.create_event(DieEvent(defender))

            else:
                msg = f"{attacker.name} uses {self.owner.name} and deals no damage to {defender.name}."
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

        else:
            msg = f"You can't do that there!"
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

    def calculate_to_hit_score(self, attacker, defender):
        """
        Get the to hit score from the stats of both entities
        Args:
            attacker:
            defender:
        """
        roll = random.randint(1, 100)
        modified_to_hit_score = attacker.combatant.secondary_stats.chance_to_hit + self.base_accuracy + roll

        # get dodge score
        dodge_value = 0
        if self.stat_to_target == SecondaryStatTypes.DODGE_SPEED:
            dodge_value = defender.combatant.secondary_stats.dodge_speed
        elif self.stat_to_target == SecondaryStatTypes.DODGE_TOUGHNESS:
            dodge_value = defender.combatant.secondary_stats.dodge_toughness
        elif self.stat_to_target == SecondaryStatTypes.DODGE_INTELLIGENCE:
            dodge_value = defender.combatant.secondary_stats.dodge_intelligence

        # mitigate the to hit
        mitigated_to_hit_score = modified_to_hit_score - dodge_value

        # log the info
        from scripts.core.global_data import game_manager
        log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return mitigated_to_hit_score

    @staticmethod
    def get_hit_type(to_hit_score):
        """
        Get the hit type from the to hit score
        Args:
            to_hit_score:

        Returns:
            HitTypes:
        """
        if to_hit_score >= HitTypes.CRIT_VALUE.value:
            return HitTypes.CRIT
        elif to_hit_score >= HitTypes.HIT_VALUE.value:
            return HitTypes.HIT
        else:
            return HitTypes.GRAZE

    def calculate_damage(self, attacker, defender, hit_type):
        """
        Work out the damage to be dealt
        Args:
            attacker(Entity):
            defender(Entity):
            hit_type(HitTypes):
        Returns:
            int: damage to be dealt
        """

        initial_damage = self.base_damage  # TODO - add skill dmg modifier to allow dmg growth

        # get resistance value
        resist_value = 0
        if self.damage_type == DamageTypes.PIERCE:
            resist_value = defender.combatant.secondary_stats.resist_pierce
        elif self.damage_type == DamageTypes.BLUNT:
            resist_value = defender.combatant.secondary_stats.resist_blunt
        elif self.damage_type == DamageTypes.ELEMENTAL:
            resist_value = defender.combatant.secondary_stats.resist_elemental

        # mitigate damage with defence
        mitigated_damage = initial_damage - resist_value

        # apply to hit modifier to damage
        if hit_type == HitTypes.CRIT:
            modified_damage = mitigated_damage * HitTypes.CRIT_MODIFIER.value
        elif hit_type == HitTypes.HIT:
            modified_damage = mitigated_damage * HitTypes.HIT_MODIFIER.value
        else:
            modified_damage = mitigated_damage * HitTypes.GRAZE_MODIFIER.value

        # round down the dmg
        modified_damage = int(modified_damage)

        # log the info
        from scripts.core.global_data import game_manager
        log_string = f"-> Initial damage:{initial_damage}, Mitigated:{mitigated_damage},  Modified:{modified_damage}."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return modified_damage

    @staticmethod
    def apply_damage(attacker, defender, damage):
        """
        Apply damage to an entity

        Args:
            attacker(Entity):
            defender(Entity):
            damage(int):
        """
        defender.combatant.hp -= damage