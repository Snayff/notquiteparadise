from scripts.core.constants import MessageEventTypes, TargetTypes
from scripts.core.effects import MoveEffect
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

        target_type = skill_values["target_type"] # tile or entity or wall
        if target_type == "wall":
            self.target_type = TargetTypes.WALL
        elif target_type == "tile":
            self.target_type = TargetTypes.TILE
        elif target_type == "entity":
            self.target_type = TargetTypes.ENTITY

        self.effects = skill_values["effects"]  # list of effects to process
        self.base_time_cost = skill_values["base_time_cost"]  # base value of time spent to complete action
        self.icon = skill_values["icon"]  # icon showing the skill

    def use(self, target=None, target_type=None):
        """
        Use the skill

        Args:
            target_type (object):
            target (object):
        """
        if self.target_type == target_type:

            # if we need a target because we aren't targeting
            if target is None and not self.targeting_required:
                return False

            elif self.targeting_required:
                pass
                # TODO - trigger targeting system

            elif target is not None:

                # apply any effects
                if self.effects:
                    for effect_name in self.effects:
                        effect = None

                        if effect_name == "move_self":
                            target_tile = target[0], target[1]
                            effect = MoveEffect(self.owner.owner, target_tile)   # owner is Actor, actor's owner is
                                                                                    # Entity

                        if effect:
                            effect.trigger()
                from scripts.core.global_data import game_manager
                game_manager.create_event(EndTurnEvent(self.base_time_cost))
        else:
            # inform player of wrong target type
            from scripts.core.global_data import game_manager
            msg = f"You didn't actually target there, that would be silly."
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))






