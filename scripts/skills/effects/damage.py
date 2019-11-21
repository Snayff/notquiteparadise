import logging
from typing import List

from scripts.core.constants import TargetTags, MessageEventTypes, HitTypes, DamageTypes, PrimaryStatTypes, HitModifiers, EffectTypes
from scripts.events.entity_events import DieEvent

from scripts.events.message_events import MessageEvent
from scripts.core.data_library import library
from scripts.core.event_hub import publisher
from scripts.skills.effects.effect import Effect
from scripts.world.aspect import Aspect
from scripts.world.entity import Entity
from scripts.world.tile import Tile


class DamageEffect(Effect):
    """
    Effect to damage an Entity

    """

    def __init__(self, owner):
        super().__init__(owner, "damage", "This is the damage effect", EffectTypes.DAMAGE)

    def trigger(self, tiles):
        """
        Trigger the effect

        Args:
            tiles (List[Tile]):
        """
        super().trigger()

        # determine if the damage is from an Affliction or a Skill
        from scripts.skills.skill import Skill
        from scripts.skills.affliction import Affliction
        if isinstance(self.owner, Skill):
            attacker = self.owner.owner.owner  # entity:actor:skill:skill_effect
            data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name,
                                                 self.effect_type)
            is_guaranteed_hit = False
        elif isinstance(self.owner, Affliction):
            attacker = None
            data = library.get_affliction_effect_data(self.owner.name, self.effect_type)
            is_guaranteed_hit = True
        elif isinstance(self.owner, Aspect):
            attacker = None
            data = library.get_aspect_effect_data(self.owner.name, self.effect_type)
            is_guaranteed_hit = False

        # loop all tiles in list
        for tile in tiles:
            defender = tile.entity

            # check that the tags match
            from scripts.managers.world_manager import world
            if world.Skill.has_required_tags(tile, data.required_tags, attacker):
                # if it needs to be another entity then it can't be looking at itself
                if TargetTags.OTHER_ENTITY in data.required_tags:
                    if attacker != defender:

                        # get the hit type
                        if is_guaranteed_hit:
                            hit_type = HitTypes.HIT
                        else:
                            to_hit_score = world.Skill.calculate_to_hit_score(defender,
                                                                data.accuracy, data.stat_to_target, attacker)
                            hit_type = world.Skill.get_hit_type(to_hit_score)

                        # calculate damage
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

                            # who did the damage?
                            if attacker:
                                attacker_name = attacker.name
                            else:
                                attacker_name = self.owner.name
                            msg = f"{attacker_name} {hit_type_desc} {defender.name} for {damage}."
                            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                            # TODO - add the damage type to the text and replace the type with an icon
                            # TODO - add the explanation of the damage roll to a tooltip

                            # trigger tile interactions caused by damage type
                            from scripts.events.map_events import TileInteractionEvent
                            # make lower case to compare to unconverted json string
                            damage_type_name = data.damage_type.name.lower()
                            publisher.publish(TileInteractionEvent(tiles, damage_type_name))

                            # check if defender died
                            if defender.combatant.hp <= 0:
                                publisher.publish(DieEvent(defender))

                        else:
                            msg = f" {defender.name} resists damage from {self.owner.name}."
                            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

                else:
                    msg = f"{attacker.name} uses {self.owner.name} and deals no damage to {defender.name}."
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
        logging.debug(f"Calculate damage...")
        data = effect_data

        initial_damage = data.damage  # TODO - add skill dmg modifier to allow dmg growth
        damage_from_stats = 0

        # get damage from stats of attacker
        if attacking_entity:
            stat_amount = 0
            # get the stat
            for stat in PrimaryStatTypes:
                if stat == data.mod_stat:
                    stat_amount = getattr(attacking_entity.combatant.primary_stats, stat.name.lower())
                    break

            damage_from_stats = stat_amount * data.mod_amount

        # get resistance value
        resist_value = 0

        for dmg_type in DamageTypes:
            if dmg_type == data.damage_type:
                resist_value = getattr(defending_entity.combatant.secondary_stats, "resist_" + dmg_type.name.lower())
                break
        # if data.damage_type == DamageTypes.PIERCE:
        #     resist_value = defending_entity.combatant.secondary_stats.resist_pierce
        # elif data.damage_type == DamageTypes.BLUNT:
        #     resist_value = defending_entity.combatant.secondary_stats.resist_blunt
        # elif data.damage_type == DamageTypes.ELEMENTAL:
        #     resist_value = defending_entity.combatant.secondary_stats.resist_elemental

        # mitigate damage with defence
        mitigated_damage = (initial_damage + damage_from_stats) - resist_value

        # apply to hit modifier to damage
        if hit_type == HitTypes.CRIT:
            modified_damage = mitigated_damage * HitModifiers.CRIT.value
        elif hit_type == HitTypes.HIT:
            modified_damage = mitigated_damage * HitModifiers.HIT.value
        else:
            modified_damage = mitigated_damage * HitModifiers.GRAZE.value

        # round down the dmg
        int_modified_damage = int(modified_damage)

        # log the info
        log_string = f"-> Initial:{initial_damage}, Mitigated: {format(mitigated_damage,'.2f')},  Modified" \
                     f":{format(modified_damage,'.2f')}, Final: {int_modified_damage}"
        logging.debug(log_string)

        return int_modified_damage

    @staticmethod
    def apply_damage(defending_entity, damage):
        """
        Apply damage to an entity

        Args:
            defending_entity(Entity):
            damage(int):
        """
        defending_entity.combatant.hp -= damage