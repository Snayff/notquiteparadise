from scripts.core.constants import HitTypes, LoggingEventTypes, DamageTypes, HitModifiers, MessageEventTypes
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.affliction_effects.affliction_effect import AfflictionEffect


class DamageAfflictionEffect(AfflictionEffect):
    """
    SkillEffect to damage an Entity

    Attributes:
        damage(int):
        damage_type(int):
        stat_to_target(PrimaryStatTypes):
    """

    def __init__(self, owner, damage, damage_type, stat_to_target):
        super().__init__(owner, "damage", "This is the damage effect")
        self.base_damage = damage
        self.damage_type = damage_type
        self.stat_to_target = stat_to_target

    def trigger(self, defending_entity):
        """
        Trigger the effect

        Args:
            defending_entity (Entity):
        """
        super().trigger()

        defender = defending_entity

        # affliction damage always Hits and is already on an appropriate target
        hit_type = HitTypes.HIT
        damage = self.calculate_damage(defender, hit_type)

        # apply damage
        if damage > 0:
            self.apply_damage(defender, damage)

            msg = f" {defender.name} takes {damage} damage from {self.owner.name}."
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
            # TODO - add the damage type to the message and replace the type with an icon
            # TODO - add the explanation of the damage roll to a tooltip

            # check if defender died
            if defender.combatant.hp <= 0:
                publisher.publish(DieEvent(defender))

        else:
            msg = f" {defender.name} resists damage from {self.owner.name}."
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

    def calculate_damage(self, defending_entity, hit_type):
        """
        Work out the damage to be dealt
        Args:
            defending_entity(Entity):
            hit_type(HitTypes):
        Returns:
            int: damage to be dealt
        """
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"Calculate damage..."))

        initial_damage = self.base_damage

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
        # NOTE: currently only Hit is used
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