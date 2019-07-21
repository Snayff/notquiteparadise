
from scripts.core.constants import LoggingEventTypes, TargetTags, MessageEventTypes, SecondaryStatTypes, \
    HitTypes, DamageTypes, PrimaryStatTypes, HitValues, HitModifiers, EffectTypes
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.effects.effect import Effect
from scripts.world.entity import Entity
from scripts.world.tile import Tile


class DamageEffect(Effect):
    """
    Effect to damage an Entity

    """

    def __init__(self, owner):
        super().__init__(owner, "damage", "This is the damage effect", EffectTypes.DAMAGE)

    def trigger(self, tile):
        """
        Trigger the effect

        Args:
            tile (Tile):
        """
        super().trigger()

        # determine if the damage is from an Affliction or a Skill
        from scripts.skills.skill import Skill
        from scripts.skills.affliction import Affliction
        if isinstance(self.owner, Skill):
            self.process_skill_damage(tile)
        elif isinstance(self.owner, Affliction):
            self.process_affliction_damage(tile)

    def process_skill_damage(self, tile):
        """
        Process damage caused by a Skill. It is affected by the attacker.

        Args:
            tile (Tile):
        """
        attacker = self.owner.owner.owner  # entity:actor:skill:skill_effect
        defender = tile.entity
        data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.skill_effect_type.name)

        # check that the tags match
        from scripts.global_singletons.managers import world_manager
        if world_manager.Skill.has_required_tags(tile, data.required_tags):
            # if it needs to be another entity then it can't be looking at itself
            if TargetTags.OTHER_ENTITY in data.required_tags:
                if attacker != defender:
                    to_hit_score = world_manager.Skill.calculate_to_hit_score(defender,
                                                            data.accuracy, data.stat_to_target, attacker)
                    hit_type = world_manager.Skill.get_hit_type(to_hit_score)
                    damage = self.calculate_damage(defender, hit_type, data, attacker)

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
            # N.B. the reason why is logged in has_required_tags
            msg = f"You can't do that there!"
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

    def process_affliction_damage(self, tile):
        """
        Process damage caused by an Affliction

        Args:
            tile (Tile):
        """
        defender = tile.entity
        data = library.get_affliction_effect_data(self.owner.name, self.skill_effect_type.name)

        # check that the tags match
        from scripts.global_singletons.managers import world_manager
        if world_manager.Skill.has_required_tags(tile, data.required_tags):
            damage = self.calculate_damage(defender, HitTypes.HIT, data)

            # apply damage
            if damage > 0:
                self.apply_damage(defender, damage)

                msg = f"{self.owner.name} damaged {defender.name} for {damage}."
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

                # check if defender died
                if defender.combatant.hp <= 0:
                    publisher.publish(DieEvent(defender))

            else:
                # N.B. the reason why is logged in has_required_tags
                msg = f" {defender.name} resists damage from {self.owner.name}."
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

        else:
            msg = f" {defender.name} can't be effected by damage from {self.owner.name}."
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

    @staticmethod
    def calculate_damage(defending_entity, hit_type, effect_data, attacking_entity=None):
        """
        Work out the damage to be dealt. if attacking entity is None then value used is 0.
        Args:
            defending_entity(Entity):
            hit_type(HitTypes):
            effect_data (EffectData):
            attacking_entity(Entity): Optional. Defaults to None.

        Returns:
            int: damage to be dealt
        """
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"Calculate damage..."))
        data = effect_data

        initial_damage = data.damage  # TODO - add skill dmg modifier to allow dmg growth

        # get resistance value
        resist_value = 0
        if data.damage_type == DamageTypes.PIERCE:
            resist_value = defending_entity.combatant.secondary_stats.resist_pierce
        elif data.damage_type == DamageTypes.BLUNT:
            resist_value = defending_entity.combatant.secondary_stats.resist_blunt
        elif data.damage_type == DamageTypes.ELEMENTAL:
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