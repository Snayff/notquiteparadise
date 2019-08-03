import random
from typing import List

from scripts.core.constants import LoggingEventTypes, MessageEventTypes, TargetTags, DamageTypes, \
    PrimaryStatTypes, SecondaryStatTypes, HitValues, HitTypes, EffectTypes
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.effects.affect_stat import AffectStatEffect
from scripts.skills.skill import Skill
from scripts.skills.effects.apply_affliction import ApplyAfflictionEffect
from scripts.skills.effects.change_terrain import ChangeTerrainEffect
from scripts.skills.effects.damage import DamageEffect
from scripts.skills.effects.move import MoveEffect
from scripts.world.entity import Entity
from scripts.world.terrain.terrain import Terrain
from scripts.world.tile import Tile


class SkillMethods:
    """
    Methods for querying skills and skill related info and taking skill actions.
    """
    def __init__(self, manager):
        self.manager = manager  # type: WorldManager

    def can_use_skill(self, entity, target_pos, skill):
        """
        Confirm entity can use skill on targeted position

        Args:
            entity (Entity):
            target_pos (tuple(int, int)):
            skill (Skill):

        Returns:
            bool: True if can use the skill. Else False.
        """
        from scripts.global_singletons.managers import world_manager

        start_tile = world_manager.Map.get_tile(entity.x, entity.y)
        target_x, target_y = target_pos
        target_tile = world_manager.Map.get_tile(target_x, target_y)
        skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)

        # check we have everything we need and if so use the skill
        if self.has_required_tags(target_tile, skill_data.required_tags):
            resource_type = skill_data.resource_type
            resource_cost = skill_data.resource_cost
            if self.can_afford_cost(entity, resource_type, resource_cost):
                distance = world_manager.Entity.get_chebyshev_distance_between_tiles(start_tile, target_tile)
                skill_range = skill_data.range
                if distance <= skill_range:
                    return True
                else:
                    publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"Target out of skill range, "
                    f"range {skill_range} > distance {distance}"))

            else:
                msg = f"You can't afford the cost."
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

        return False

    def has_required_tags(self, tile, required_tags):
        """
        Check a tile has all required tags

        Args:
            tile(Tile):
            required_tags(List):

        Returns:
            bool: True if tile has all tags
        """
        log_string = f"Checking target for tags {required_tags}..."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        tags_checked = {}

        # assess all tags
        for tag in required_tags:
            tags_checked[tag.name] = self.manager.Map.tile_has_tag(tile, tag)

        # if all tags came back true return true
        if all(value for value in tags_checked.values()):
            log_string = f"-> All tags OK! Tags checked are {tags_checked}"
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            return True
        else:
            log_string = f"-> Some tags WRONG! Tags checked are {tags_checked}"
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

            msg = f"That's not the right target!"
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
            return False

    @staticmethod
    def can_afford_cost(entity, resource, cost):
        """
        Check if entity can afford the resource cost

        Args:
            entity ():
            resource ():
            cost ():

        Returns:
            bool: True for success, False otherwise.
        """

        # Check if cost can be paid
        # TODO - take different resources for cost, not just hp
        if entity.combatant.hp - cost > 0:
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"'{entity.name}' can afford cost."))
            return True
        else:
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"'{entity.name}' cannot afford cost."))
            return False

    @staticmethod
    def get_hit_type(to_hit_score):
        """
        Get the hit type from the to hit score
        Args:
            to_hit_score:

        Returns:
            HitTypes:
        """
        if to_hit_score >= HitValues.CRIT.value:
            return HitTypes.CRIT
        elif to_hit_score >= HitValues.HIT.value:
            return HitTypes.HIT
        else:
            return HitTypes.GRAZE

    @staticmethod
    def create_effect(owner, effect_type):
        """
        Create an effect and assign the owner.

        Args:
            owner (object): Skill or Affliction
            effect_type(EffectTypes):
        """
        created_effect = None

        if effect_type == EffectTypes.DAMAGE:
            created_effect = DamageEffect(owner)
        elif effect_type == EffectTypes.APPLY_AFFLICTION:
            created_effect = ApplyAfflictionEffect(owner)
        elif effect_type == EffectTypes.MOVE:
            created_effect = MoveEffect(owner)
        elif effect_type == EffectTypes.CHANGE_TERRAIN:
            created_effect = ChangeTerrainEffect(owner)
        elif effect_type == EffectTypes.AFFECT_STAT:
            created_effect = AffectStatEffect(owner)

        return created_effect

    @staticmethod
    def calculate_to_hit_score(defender, skill_accuracy, stat_to_target, attacker=None):
        """
        Get the to hit score from the stats of both entities. If Attacker is None then 0 is used for attacker values.
        Args:

            defender ():
            skill_accuracy ():
            stat_to_target ():
            attacker ():
        """
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"Get to hit scores..."))

        roll = random.randint(1, 100)

        # check if attacker provided
        if attacker:
            attacker_value = attacker.combatant.secondary_stats.accuracy
        else:
            attacker_value = 0

        modified_to_hit_score = attacker_value + skill_accuracy + roll

        # TODO -  mitigate to hit using stat to target

        # mitigate the to hit
        mitigated_to_hit_score = modified_to_hit_score

        # log the info
        log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return mitigated_to_hit_score

    @staticmethod
    def create_skill(actor, skill_tree_name, skill_name):
        """
        Create a SKill object
        Args:
            actor ():
            skill_tree_name ():
            skill_name ():

        Returns:
            Skill: The created skill
        """
        skill = Skill(actor, skill_tree_name, skill_name)

        return skill

    @staticmethod
    def pay_resource_cost(entity, resource, cost):
        """
        Remove the resource cost from the using entity
        """
        entity.combatant.hp -= cost

        log_string = f"'{entity.name}' paid {cost} hp and has {entity.combatant.hp} left."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))