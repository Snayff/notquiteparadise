from scripts.core.constants import MessageEventTypes, TargetTags, LoggingEventTypes, TargetTypes
from scripts.core.effects import MoveEffect, DamageEffect
from scripts.data_loaders.getters import get_value_from_skill_json
from scripts.events.game_events import EndTurnEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent


class Skill:
    """
    A skill to be used by an actor

    Args:
            name:
    """
    def __init__(self, name):
        self.name = name

        skill_values = get_value_from_skill_json(name)

        # aesthetic info
        self.description = skill_values["description"]  # the description of the skill
        self.icon = skill_values["icon"]  # icon showing the skill

        # target info
        self.range = skill_values["range"]  # how far away the skill can be used
        self.target_type = self.get_target_type_from_type_string(skill_values["target_type"])
        target_tags = skill_values["target_tags"]
        self.target_tags = []

        for tag in target_tags:
            self.target_tags.append(self.get_target_tags_from_tag_string(tag))

        # resource info
        self.resource_type = skill_values["resource_type"]
        self.resource_cost = skill_values["resource_cost"]  # base value of resource spent to complete action
        self.time_cost = skill_values["time_cost"]  # base value of time spent to complete action
        self.cooldown = skill_values["cooldown"]  # how many rounds to wait between uses

        # effects info
        effects = skill_values["effects"]  # list of effects to process
        self.effects = []

        for effect in effects:
            if effect["name"] == "damage":

                # get tags from effects
                target_tags = []
                for tag in effect["target_tags"]:
                    target_tags.append(self.get_target_tags_from_tag_string(tag))

                target_type = self.get_target_type_from_type_string(effect["target_type"])
                # add effect object to skill
                self.effects.append(DamageEffect(effect["amount"], target_type, target_tags))

    def is_valid_target_type(self, tile_target_type, entity_target_type):
        """
        Check if the skill can be used on the target

        Args:
            tile_target_type(TargetTags): the type of the target
            entity_target_type(TargetTags): the type of the target

        Returns:
             bool: True for success, False otherwise.

        """
        tile_target_ok = False
        entity_target_ok = False

        from scripts.core.global_data import game_manager
        log_string = f"Checking if target is valid type for skill..."
        log_string2 = f"-> looking for {self.target_tags}"
        log_string3 = f"-> got {tile_target_type} and {entity_target_type}"
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string2))
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string3))

        # check tags match
        if tile_target_type != TargetTags.OUT_OF_BOUNDS:
            for tag in self.target_tags:
                if tag == tile_target_type:
                    tile_target_ok = True
                elif tag == entity_target_type:
                    entity_target_ok = True

            # return result
            if self.target_type == TargetTypes.ENTITY:
                if entity_target_ok:
                    log_string = f"Target type is OK!"
                    game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                    return True
            elif self.target_type == TargetTypes.TILE:
                if tile_target_ok:
                    log_string = f"Target type is OK!"
                    game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                    return True

        # inform player of wrong target type
        from scripts.core.global_data import game_manager
        msg = f"You can't do that there!"
        game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

        # log it
        log_string = f"Target type is wrong; tile:{tile_target_ok}, entity:{entity_target_ok}"
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

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
        target_x, target_y = target_pos
        target = self.get_target(target_pos)  # get the tile or entity

        # apply any effects
        if self.effects:
            for effect in self.effects:

                if type(effect) is DamageEffect:
                    effect.trigger(entity, target)

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
        log_string = f"{entity.name} paid {self.resource_cost} hp."
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
    def get_target_type_from_type_string(target_type):
        """
        Get the target type enum from the tag string

        Args:
            target_type(str): the type as in the json

        Returns:
            enum
        """
        if target_type == "entity":
            return TargetTypes.ENTITY
        elif target_type == "tile":
            return TargetTypes.TILE

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

        if self.target_type == TargetTypes.ENTITY:
            from scripts.core.global_data import entity_manager
            target = entity_manager.query.get_blocking_entity_at_location(target_x, target_y)

        elif self.target_type == TargetTypes.TILE:
            from scripts.core.global_data import world_manager
            target = world_manager.get_tile(target_x, target_y)

        log_string = f"Got target {target.name} for the skill."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return target