import random

from scripts.core.constants import LoggingEventTypes, TargetTypes, TargetTags, MessageEventTypes, SecondaryStatTypes, \
    HitTypes, DamageTypes, PrimaryStatTypes, HitValues, HitModifiers
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.skill_effects.skill_effect import SkillEffect
from scripts.world.entity import Entity


class DamageSkillEffect(SkillEffect):
    """
    SkillEffect to damage an Entity

    Attributes:
        damage(int):
        damage_type(int):
        required_target_type(TargetTypes):
        required_tags(list): list of TargetType enums
        accuracy(int):
        stat_to_target(PrimaryStatTypes):
    """

    def __init__(self, owner, required_target_type, required_tags, damage, damage_type,  accuracy, stat_to_target):
        super().__init__(owner, "damage", "This is the damage effect", required_target_type, required_tags)
        self.base_damage = damage
        self.damage_type = damage_type
        self.base_accuracy = accuracy
        self.stat_to_target = stat_to_target

    def trigger(self, attacking_entity, defending_entity):
        """
        Trigger the effect

        Args:
            attacking_entity (Entity):
            defending_entity (Entity):
        """
        super().trigger()

        attacker = attacking_entity
        defender = defending_entity

        from scripts.global_instances.managers import world_manager
        target_type = world_manager.Skill.get_target_type(defender)

        # check the type is correct, then that the tags match
        if target_type == self.required_target_type:
            # if it needs to be another entity then it can't be looking at itself
            if TargetTags.OTHER_ENTITY in self.required_tags:
                if attacker != defender:
                    to_hit_score = world_manager.Skill.calculate_to_hit_score(defender,
                                                            self.base_accuracy, self.stat_to_target, attacker)
                    hit_type = world_manager.Skill.get_hit_type(to_hit_score)
                    damage = self.calculate_damage(defender, hit_type, attacker)

                    # apply damage
                    if damage > 0:
                        self.apply_damage(defender, damage)

                        if hit_type == HitTypes.GRAZE:
                            hit_type_desc = "grazes"
                        elif hit_type == HitTypes.HIT:
                            hit_type_desc = "hits"
                        elif hit_type == HitTypes.CRIT:
                            hit_type_desc = "crits"
                        else:
                            hit_type_desc = "does something unknown" # catch all

                        msg = f"{attacker.name} {hit_type_desc} {defender.name} for {damage}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                        # TODO - add the damage type to the message and replace the type with an icon
                        # TODO - add the explanation of the damage roll to a tooltip

                        # check if defender died
                        if defender.combatant.hp <= 0:
                            publisher.publish(DieEvent(defender))

                    else:
                        msg = f" {defender.name} resists damage from {self.owner.name}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

            else:
                msg = f"{attacker.name} uses {self.owner.name} and deals no damage to {defender.name}."
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

        else:
            msg = f"You can't do that there!"
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

            # log why
            log_string = f"-> target type incorrect; selected:{target_type}, needed:{self.required_target_type}"
            publisher.publish(LoggingEvent(LoggingEventTypes.WARNING, log_string))

    def calculate_damage(self, defending_entity, hit_type, attacking_entity=None):
        """
        Work out the damage to be dealt. if attacking entity is None then value used is 0.
        Args:
            attacking_entity(Entity):
            defending_entity(Entity):
            hit_type(HitTypes):
        Returns:
            int: damage to be dealt
        """
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"Calculate damage..."))

        initial_damage = self.base_damage  # TODO - add skill dmg modifier to allow dmg growth

        # get resistance value
        resist_value = 0
        if self.damage_type == DamageTypes.PIERCE:
            resist_value = defending_entity.combatant.secondary_stats.resist_pierce
        elif self.damage_type == DamageTypes.BLUNT:
            resist_value = defending_entity.combatant.secondary_stats.resist_blunt
        elif self.damage_type == DamageTypes.ELEMENTAL:
            resist_value = defending_entity.combatant.secondary_stats.resist_elemental

        # mitigate damage with defence
        mitigated_damage = initial_damage - resist_value

        # apply to hit modifier to damage
        if hit_type == HitTypes.CRIT:
            modified_damage = mitigated_damage * HitModifiers.CRIT.value
        elif hit_type == HitTypes.HIT:
            modified_damage = mitigated_damage * HitModifiers.HIT.value
        else:
            modified_damage = mitigated_damage * HitModifiers.GRAZE.value

        # round down the dmg
        modified_damage = int(modified_damage)

        # log the info
        log_string = f"-> Initial damage:{initial_damage}, Mitigated:{mitigated_damage},  Modified:{modified_damage}."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return modified_damage

    @staticmethod
    def apply_damage(defending_entity, damage):
        """
        Apply damage to an entity

        Args:
            defending_entity(Entity):
            damage(int):
        """
        defending_entity.combatant.hp -= damage