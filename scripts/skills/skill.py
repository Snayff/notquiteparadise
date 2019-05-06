import pygame

from scripts.core.constants import MessageEventTypes, TargetTags, LoggingEventTypes, TargetTypes, DamageTypes, \
    PrimaryStatTypes, SecondaryStatTypes
from scripts.data_loaders.getters import get_value_from_skill_json
from scripts.events.game_events import EndTurnEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.skills.effects.change_terrain import ChangeTerrainSkillEffect
from scripts.skills.effects.damage import DamageSkillEffect
from scripts.world.entity import Entity
from scripts.world.terrain.terrain import Terrain
from scripts.world.tile import Tile


class Skill:
    """
    A skill to be used by an actor

    Args:
            name(str):
    """
    def __init__(self, skill_tree_name, skill_name):
        self.name = skill_name
        self.skill_tree_name = skill_tree_name

        skill_values = get_value_from_skill_json(skill_tree_name, skill_name)

        # aesthetic info
        self.description = skill_values["description"]  # the description of the skill
        self.icon = pygame.image.load("assets/skills/" + skill_values["icon"]).convert_alpha()  # icon showing theskill

        # target info
        self.range = skill_values["range"]  # how far away the skill can be used
        self.required_target_type = self.get_target_type_from_string(skill_values["required_target_type"])
        required_tags = skill_values["required_tags"]
        self.required_tags = []

        for tag in required_tags:
            self.required_tags.append(self.get_target_tags_from_tag_string(tag))

        # resource info
        self.resource_type = skill_values["resource_type"]
        self.resource_cost = skill_values["resource_cost"]  # base value of resource spent to complete action
        self.time_cost = skill_values["time_cost"]  # base value of time spent to complete action
        self.cooldown = skill_values["cooldown"]  # how many rounds to wait between uses

        # effects info
        effects = skill_values["effects"]  # list of effects to process
        self.effects = []

        for effect in effects:
            created_effect = None
            effect_name = effect["name"]

            if effect_name == "damage":
                created_effect = self.create_damage_effect(effect)

            elif effect_name == "change_terrain":
                created_effect = self.create_change_terrain_effect(effect)

            # if we have an effect add it to internal list
            if created_effect:
                self.effects.append(created_effect)

    def create_damage_effect(self, effect):
        """
        Create the damage effect object

        Args:
            effect (dict): dict of effect values, from json

        Returns:
            DamageSkillEffect: The created effect object
        """
        # get tags from effects
        target_tags = []
        for tag in effect["required_tags"]:
            target_tags.append(self.get_target_tags_from_tag_string(tag))

        target_type = self.get_target_type_from_string(effect["required_target_type"])
        damage_type = self.get_damage_type_from_string(effect["damage_type"])
        stat_to_target = self.get_secondary_stat_from_string(effect["stat_to_target"])

        # add effect object to skill
        created_effect = DamageSkillEffect(effect["damage"], damage_type, target_type, target_tags,
                                           effect["accuracy"], stat_to_target)
        created_effect.owner = self

        return created_effect

    def create_change_terrain_effect(self, effect):
        """
        Create the change terrain effect object

        Args:
            effect (dict): dict of effect values, from json

        Returns:
            ChangeTerrainSkillEffect: The created effect object
        """
        # get tags from effects
        target_tags = []
        for tag in effect["required_tags"]:
            target_tags.append(self.get_target_tags_from_tag_string(tag))

        target_type = self.get_target_type_from_string(effect["required_target_type"])
        new_terrain = self.get_target_tags_from_tag_string(effect["new_terrain"])

        # add effect object to skill
        created_effect = ChangeTerrainSkillEffect(target_type, target_tags, new_terrain)
        created_effect.owner = self

        return created_effect

    def is_required_target_type(self, tile):
        """
        Check if the stile has the required target type

        Args:
            tile(Tile): tile to check for a target

        Returns:
             bool: True if required target type found, else False.

        """
        from scripts.core.global_data import game_manager
        log_string = f"Checking target for type '{self.required_target_type}'..."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        # if we need a terrain type then pass the tiles terrain and get its type
        if self.required_target_type == TargetTypes.TERRAIN:
            target_type = self.get_target_type(tile.terrain)
            if target_type == TargetTypes.TERRAIN:
                log_string = f"-> Target type OK! Type is '{target_type}'"
                game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                return True
            else:
                log_string = f"-> Target type WRONG! Type is '{target_type}'"
                game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

                msg = f"You can't do that there!"
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
                return False

        # if we need an entity type then pass the tiles entity and get its type
        elif self.required_target_type == TargetTypes.ENTITY:
            target_type = self.get_target_type(tile.entity)
            if target_type == TargetTypes.ENTITY:
                log_string = f"-> Target type OK! Type is '{target_type}'"
                game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                return True
            else:
                log_string = f"-> Target type WRONG! Type is '{target_type}'"
                game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

                msg = f"You can't do that there!"
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
                return False

        return False  # catch all

    def has_required_tags(self, tile):
        """
        Check a tile has all required tags

        Args:
            tile (Tile):

        Returns:
            bool: True if tile has all tags
        """
        from scripts.core.global_data import game_manager
        log_string = f"Checking target for tags '{self.required_tags}'..."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        tags_checked = {}

        # assess all tags
        for tag in self.required_tags:
            tags_checked[tag] = tile.has_tag(tag)

        # if all tags came back true return true
        if all(value for value in tags_checked.values()):
            log_string = f"-> All tags OK! Tags checked are '{tags_checked}'"
            game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            return True
        else:
            log_string = f"-> Some tags WRONG! Tags checked are '{tags_checked}'"
            game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

            msg = f"You can't do that there!"
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
            return False

    def user_can_afford_cost(self):
        """
        Check if entity can afford the resource cost

        Returns:
            bool: True for success, False otherwise.
        """
        entity = self.owner.owner  # owner is actor, actor's owner is entity

        # Check if cost can be paid
        # TODO - take different resources for cost, not just hp
        if entity.combatant.hp - self.resource_cost > 0:
            return True
        else:
            from scripts.core.global_data import game_manager
            msg = f"It seems you're too poor to do that."
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
            return False

    def use(self, target_pos):
        """
        Use the skill

        Args:
            target_pos (tuple): x y of the target
        """
        entity = self.owner.owner  # owner is actor, actor's owner is entity
        target = self.get_target(target_pos)  # get the tile or entity

        # apply any effects
        if self.effects:
            for effect in self.effects:

                if type(effect) is DamageSkillEffect:
                    effect.trigger(entity, target)

                elif type(effect) is ChangeTerrainSkillEffect:
                    effect.trigger(target)

        # end the turn
        from scripts.core.global_data import game_manager
        game_manager.create_event(EndTurnEvent(self.time_cost))

    def pay_the_resource_cost(self):
        """
        Remove the resource cost from the using entity
        """
        entity = self.owner.owner  # owner is actor, actor's owner is entity
        entity.combatant.hp -= self.resource_cost

        from scripts.core.global_data import game_manager
        log_string = f"{entity.name} paid {self.resource_cost} hp and has {entity.combatant.hp} left."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

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
        elif primary_stat == "subtlety":
            return PrimaryStatTypes.SUBTLETY
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

    def get_target(self, target_pos):
        """
        Get target at xy based on target type

        Args:
            target_pos (tuple): x y of the target
        """
        # TODO - extend to target an area
        target_x, target_y = target_pos

        from scripts.core.global_data import game_manager
        target = None

        if self.required_target_type == TargetTypes.ENTITY:
            from scripts.core.global_data import world_manager
            target = world_manager.entity_query.get_blocking_entity_at_location(target_x, target_y)

        elif self.required_target_type == TargetTypes.TERRAIN:
            from scripts.core.global_data import world_manager
            target_tile = world_manager.game_map.get_tile(target_x, target_y)
            target = target_tile.terrain

        log_string = f"Got target '{target.name}' for {self.name}."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

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
            target_type = TargetTypes.TERRAIN
        elif isinstance(target, Entity):
            target_type = TargetTypes.ENTITY

        return target_type
