from scripts.core.constants import HitTypes, LoggingEventTypes, DamageTypes, HitModifiers, MessageEventTypes
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.affliction_effects.affliction_effect import AfflictionEffect


class DamageAfflictionEffect(AfflictionEffect):
    """
    AfflictionEffect to damage an Entity

    Attributes:
        owner(Affliction): The Affliction containing this effect
        affliction_effect_type(AfflictionEffectTypes): The type of affliction
    """

    def __init__(self, owner, affliction_effect_type):
        super().__init__(owner, "damage", affliction_effect_type,  "This is the damage effect")

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

        data = library.get_affliction_effect_data(self.owner.name, self.affliction_effect_type)
        damage_type = data.damage_type
        initial_damage = data.damage

        # get resistance value
        resist_value = 0
        if damage_type == DamageTypes.PIERCE:
            resist_value = defending_entity.combatant.secondary_stats.resist_pierce
        elif damage_type == DamageTypes.BLUNT:
            resist_value = defending_entity.combatant.secondary_stats.resist_blunt
        elif damage_type == DamageTypes.ELEMENTAL:
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