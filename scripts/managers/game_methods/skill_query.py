
from scripts.core.constants import TargetTypes, LoggingEventTypes, MessageEventTypes, TargetTags, DamageTypes, \
    PrimaryStatTypes, SecondaryStatTypes, HitValues, HitTypes
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_instances.event_hub import publisher
from scripts.world.entity import Entity
from scripts.world.terrain.terrain import Terrain
from scripts.world.tile import Tile


class SkillQuery():
    """
    Methods for querying skills and skill related info.
    """
    def __init__(self, manager):
        self.manager = manager

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
        from scripts.global_instances.managers import world_manager

        target_x, target_y = target_pos
        blocking_entity_at_location = world_manager.entity_query.get_blocking_entity_at_location(target_x,
                                                                                                 target_y)
        tile = world_manager.game_map.get_tile(target_x, target_y)

        # do we need an entity?
        if skill.required_target_type == TargetTypes.ENTITY:
            # is there an entity to target?
            if blocking_entity_at_location:
                # is the entity within range?
                distance_to_entity = world_manager.entity_query.get_chebyshev_distance_between_entities(entity,
                                            blocking_entity_at_location)
                if distance_to_entity > skill.range:
                    return False
            else:
                return False

        # get info about the tile and the skill requirements
        is_required_type = self.is_required_target_type(tile, skill.required_target_type)
        has_tags = self.has_required_tags(tile, skill.required_tags)

        # check we have everything we need and if so use the skill
        if is_required_type and has_tags:
            if self.can_afford_cost(skill.owner.owner, skill.resource_type, skill.resource_cost):
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
        log_string = f"Checking target for type '{required_target_type}'..."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        # if we need a terrain type then pass the tiles terrain and get its type
        if required_target_type == TargetTypes.TERRAIN:
            target_type = self.get_target_type(tile.terrain)
            if target_type == TargetTypes.TERRAIN:
                log_string = f"-> Target type OK! Type is '{target_type}'"
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                return True
            else:
                log_string = f"-> Target type WRONG! Type is '{target_type}'"
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

                msg = f"You can't do that there!"
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                return False

        # if we need an entity type then pass the tiles entity and get its type
        elif required_target_type == TargetTypes.ENTITY:
            target_type = self.get_target_type(tile.entity)
            if target_type == TargetTypes.ENTITY:
                log_string = f"-> Target type OK! Type is '{target_type}'"
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                return True
            else:
                log_string = f"-> Target type WRONG! Type is '{target_type}'"
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

                msg = f"You can't do that there!"
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                return False

        return False  # catch all

    @staticmethod
    def has_required_tags(tile, required_tags):
        """
        Check a tile has all required tags

        Args:
            required_tags ():
            tile (Tile):

        Returns:
            bool: True if tile has all tags
        """
        log_string = f"Checking target for tags '{required_tags}'..."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        tags_checked = {}


        # assess all tags
        for tag in required_tags:
            tags_checked[tag] = tile.has_tag(tag)

        # if all tags came back true return true
        if all(value for value in tags_checked.values()):
            log_string = f"-> All tags OK! Tags checked are '{tags_checked}'"
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            return True
        else:
            log_string = f"-> Some tags WRONG! Tags checked are '{tags_checked}'"
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
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"{entity.name} can afford cost."))
            return True
        else:
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"{entity.name} cannot afford cost."))
            return False

    @staticmethod
    def get_target_tags_from_tag_string(tag):
        """
        Get the tag enum from the tag string

        Args:
            tag(str): the tag as in the json

        Returns:
            enum
        """
        if tag == "wall":
            return TargetTags.WALL
        elif tag == "floor":
            return TargetTags.FLOOR
        elif tag == "self":
            return TargetTags.SELF
        elif tag == "other_entity":
            return TargetTags.OTHER_ENTITY
        elif tag == "no_entity":
            return TargetTags.NO_ENTITY

    @staticmethod
    def get_target_type_from_string(target_type):
        """
        Get the target type enum from the tag string

        Args:
            target_type(str): the type as in the json

        Returns:
            enum
        """
        if target_type == "entity":
            return TargetTypes.ENTITY
        elif target_type == "terrain":
            return TargetTypes.TERRAIN

    @staticmethod
    def get_damage_type_from_string(damage_type):
        """
        Get the damage type enum from a string
        Args:
            damage_type:

        Returns:

        """
        if damage_type == "pierce":
            return DamageTypes.PIERCE
        elif damage_type == "blunt":
            return DamageTypes.BLUNT
        elif damage_type == "elemental":
            return DamageTypes.ELEMENTAL

    @staticmethod
    def get_primary_stat_from_string(primary_stat):
        """
        Get the primary stat enum from a string
        Args:
            primary_stat:

        Returns:

        """
        if primary_stat == "vigour":
            return PrimaryStatTypes.VIGOUR
        elif primary_stat == "clout":
            return PrimaryStatTypes.CLOUT
        elif primary_stat == "SKULLDUGGERY":
            return PrimaryStatTypes.SKULLDUGGERY
        elif primary_stat == "bustle":
            return PrimaryStatTypes.BUSTLE
        elif primary_stat == "exactitude":
            return PrimaryStatTypes.EXACTITUDE

    @staticmethod
    def get_secondary_stat_from_string(secondary_stat):
        """
        Get the secondary stat enum from a string
        Args:
            secondary_stat:

        Returns:
            SecondaryStatTypes:
        """
        if secondary_stat == "dodge_speed":
            return SecondaryStatTypes.DODGE_SPEED
        elif secondary_stat == "dodge_toughness":
            return SecondaryStatTypes.DODGE_TOUGHNESS
        elif secondary_stat == "dodge_intelligence":
            return SecondaryStatTypes.DODGE_INTELLIGENCE

    @staticmethod
    def get_target(target_pos, required_target_type):
        """
        Get target at xy based on target type

        Args:
            required_target_type ():
            target_pos (tuple): x y of the target
        """
        # TODO - extend to target an area
        from scripts.global_instances.managers import world_manager
        target_x, target_y = target_pos
        target = None

        if required_target_type == TargetTypes.ENTITY:
            target = world_manager.entity_query.get_blocking_entity_at_location(target_x, target_y)

        elif required_target_type == TargetTypes.TERRAIN:
            target_tile = world_manager.game_map.get_tile(target_x, target_y)
            target = target_tile.terrain

        log_string = f"Got target '{target.name}' of type {required_target_type}."
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
        target_type = None

        if isinstance(target, Terrain):
            target_type = TargetTypes.TERRAIN
        elif isinstance(target, Entity):
            target_type = TargetTypes.ENTITY

        return target_type

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