from scripts.core.constants import MessageEventTypes, TargetTypes
from scripts.core.effects import MoveEffect, DamageEffect
from scripts.data_loaders.getters import get_value_from_skill_json
from scripts.events.game_events import EndTurnEvent
from scripts.events.message_events import MessageEvent


class Skill:
    """A skill to be used by an actor"""
    def __init__(self, name):
        self.name = name

        skill_values = get_value_from_skill_json(name)

        self.description = skill_values["description"]  # the description of the skill
        self.targeting_required = skill_values["targeting_required"]   # need extra input after skill selection

        target_type = skill_values["target_type"]
        if target_type == "wall":
            self.target_type = TargetTypes.WALL
        elif target_type == "floor":
            self.target_type = TargetTypes.FLOOR
        elif target_type == "entity":
            self.target_type = TargetTypes.ENTITY

        self.effects = skill_values["effects"]  # list of effects to process
        self.base_time_cost = skill_values["base_time_cost"]  # base value of time spent to complete action
        self.base_resource_cost = skill_values["base_resource_cost"] # base value of resource spent to complete action
        self.icon = skill_values["icon"]  # icon showing the skill
        self.range = skill_values["range"]  # how far away the skill can be used
        self.base_cooldown = skill_values["base_cooldown"]  # how many rounds to wait between uses

    def is_valid_target(self, target=None, target_type=None):
        """
        Check if the skill can be used on the target
        Args:
            target (object): the tile or entity being targeted
            target_type(TargetTypes): the type of the target

        Returns:
             bool: True for success, False otherwise.

        """

        # check if it is a valid target
        if self.target_type == target_type:
            if target is None:
                return False

            else:
                return True

        else:
            # inform player of wrong target type
            from scripts.core.global_data import game_manager
            msg = f"You can't do that there!"
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
            return False

    def user_can_afford_cost(self):
        """
        Check if entity can afford the resource cost

        Returns:
            bool: True for success, False otherwise.
        """
        entity_using_skill = self.owner.owner  # owner is actor, actor's owner is entity

        # Check if cost can be paid
        # TODO - take different resources for cost, not just hp
        if entity_using_skill.combatant.hp - self.base_resource_cost > 0:
            return True
        else:
            from scripts.core.global_data import game_manager
            msg = f"It seems you're too poor to do that."
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
            return False

    def use(self,  target=None):
        """
        Use the skill

        Args:
            target (object): the tile or entity being targeted
        """
        entity_using_skill = self.owner.owner  # owner is actor, actor's owner is entity

        # apply any effects
        if self.effects:
            for effect_name in self.effects:
                effect = None

                if effect_name == "move_self":
                    target_tile = target[0], target[1]
                    effect = MoveEffect(entity_using_skill, target_tile)

                if effect_name == "damage_other":
                    target_tile = target[0], target[1]  #  TODO - change to take list of entities
                    effect = DamageEffect(entity_using_skill, target_tile)

                if effect:
                    effect.trigger()

        # end the turn
        from scripts.core.global_data import game_manager
        game_manager.create_event(EndTurnEvent(self.base_time_cost))

    def pay_the_resource_cost(self):
        """
        Remove the resource cost from the using entity
        """
        entity_using_skill = self.owner.owner  # owner is actor, actor's owner is entity
        entity_using_skill.combatant.hp -= self.base_resource_cost





