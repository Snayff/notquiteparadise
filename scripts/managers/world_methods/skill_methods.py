import random

from scripts.core.constants import TargetTypes, LoggingEventTypes, MessageEventTypes, TargetTags, DamageTypes, \
    PrimaryStatTypes, SecondaryStatTypes, HitValues, HitTypes, SkillEffectTypes
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.skill import Skill
from scripts.skills.skill_effects.apply_affliction import ApplyAfflictionSkillEffect
from scripts.skills.skill_effects.change_terrain import ChangeTerrainSkillEffect
from scripts.skills.skill_effects.damage import DamageSkillEffect
from scripts.skills.skill_effects.move import MoveSkillEffect
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

        target_x, target_y = target_pos
        blocking_entity_at_location = world_manager.Entity.get_blocking_entity_at_location(target_x, target_y)
        tile = world_manager.Map.get_tile(target_x, target_y)

        skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)
        required_target = skill_data.required_target_type
        skill_range = skill_data.range
        resource_type = skill_data.resource_type
        resource_cost = skill_data.resource_cost

        # do we need an entity?
        if required_target == TargetTypes.ENTITY:
            # is there an entity to target?
            if blocking_entity_at_location:
                # is the entity within range?
                distance_to_entity = world_manager.Entity.get_chebyshev_distance_between_entities(entity,
                                            blocking_entity_at_location)
                if distance_to_entity > skill_range:
                    return False
            else:
                return False

        # get info about the tile and the skill requirements
        is_required_type = self.is_required_target_type(tile, required_target)
        has_tags = self.has_required_tags(tile, skill_data.required_tags)

        # check we have everything we need and if so use the skill
        if is_required_type and has_tags:
            if self.can_afford_cost(entity, resource_type, resource_cost):
                return True

        return False

    def is_required_target_type(self, tile, required_target_type):
        """
        Check if the tile has the required target type

        Args:
            required_target_type ():
            tile(Tile): tile to check for a target

        Returns:
             bool: True if required target type found, else False.

        """
        log_string = f"Checking target for type {required_target_type}..."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        # if we need a terrain type then pass the tiles terrain and get its type
        if required_target_type == TargetTypes.TERRAIN:
            target_type = self.get_target_type(tile.terrain)
            if target_type == TargetTypes.TERRAIN:
                log_string = f"-> Target type OK! Type is {target_type}"
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                return True
            else:
                log_string = f"-> Target type WRONG! Type is {target_type}"
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

                return False

        # if we need an entity type then pass the tiles entity and get its type
        elif required_target_type == TargetTypes.ENTITY:
            target_type = self.get_target_type(tile.entity)
            if target_type == TargetTypes.ENTITY:
                log_string = f"-> Target type OK! Type is {target_type}"
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                return True
            else:
                log_string = f"-> Target type WRONG! Type is {target_type}"
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

                return False

        return False  # catch all

    def has_required_tags(self, tile, required_tags):
        """
        Check a tile has all required tags

        Args:
            required_tags ():
            tile (Tile):

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

            msg = f"You can't do that there!"
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
    def get_target(target_pos, required_target_type):
        """
        Get target at xy based on target type

        Args:
            required_target_type ():
            target_pos (tuple): x y of the target
        """
        # TODO - extend to target an area
        from scripts.global_singletons.managers import world_manager
        target_x, target_y = target_pos
        target = None

        if required_target_type == TargetTypes.ENTITY:
            target = world_manager.Entity.get_blocking_entity_at_location(target_x, target_y)

        elif required_target_type == TargetTypes.TERRAIN:
            target_tile = world_manager.Map.get_tile(target_x, target_y)
            target = target_tile.terrain

        log_string = f"Got target {target.name} of type {required_target_type}."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return target

    @staticmethod
    def get_target_type(target):
        """
        Get the type of the required target

        Args:
            target: the target; terrain or entity

        Returns:
            TargetTypes:
        """

        if isinstance(target, Terrain):
            return TargetTypes.TERRAIN
        elif isinstance(target, Entity):
            return TargetTypes.ENTITY

        log_string = f"Type no found for {target} in 'get_target_type'"
        publisher.publish(LoggingEvent(LoggingEventTypes.CRITICAL, log_string))

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
    def create_skill_effect(skill, skill_effect_type):
        """
        Create a skill effect and assign skill as the owner.

        Args:
            skill (Skill):
            skill_effect_type(SkillEffectTypes):
        """
        created_effect = None

        if skill_effect_type == SkillEffectTypes.DAMAGE:
            created_effect = DamageSkillEffect(skill)
        elif skill_effect_type == SkillEffectTypes.APPLY_AFFLICTION:
            created_effect = ApplyAfflictionSkillEffect(skill)
        elif skill_effect_type == SkillEffectTypes.MOVE:
            created_effect = MoveSkillEffect(skill)
        elif skill_effect_type == SkillEffectTypes.CHANGE_TERRAIN:
            created_effect = ChangeTerrainSkillEffect(skill)

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
            attacker_value = attacker.combatant.secondary_stats.chance_to_hit
        else:
            attacker_value = 0

        modified_to_hit_score = attacker_value + skill_accuracy + roll

        # get dodge score
        dodge_value = 0
        if stat_to_target == SecondaryStatTypes.DODGE_SPEED:
            dodge_value = defender.combatant.secondary_stats.dodge_speed
        elif stat_to_target == SecondaryStatTypes.DODGE_TOUGHNESS:
            dodge_value = defender.combatant.secondary_stats.dodge_toughness
        elif stat_to_target == SecondaryStatTypes.DODGE_INTELLIGENCE:
            dodge_value = defender.combatant.secondary_stats.dodge_intelligence

        # mitigate the to hit
        mitigated_to_hit_score = modified_to_hit_score - dodge_value

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