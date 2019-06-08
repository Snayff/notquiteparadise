
from scripts.core.constants import AfflictionCategory, AfflictionTypes, AfflictionTriggers
from scripts.data_loaders.getters import get_value_from_afflictions_json


class Affliction:
    """
    Affliction, either Bane or Boon. Applies a periodic effect to an entity.
    """
    # TODO -
    #  Log the affliction on a central list
    #  create central method of managing afflictions
    #       Trigger the affliction's skill_effects (skill skill_effects) at required intervals
    #          decrement time remaining
    #          remove affliction if expired

    def __init__(self, name, duration):
        from scripts.global_instances.managers import game_manager
        action = game_manager.affliction_action
        values = get_value_from_afflictions_json(name)
        self.name = name
        self.description = values["description"]
        self.icon = values["icon"]
        self.affliction_category = action.get_affliction_category_from_string(values["category"])
        self.affliction_type = action.get_affliction_type_from_string(name)
        self.duration = duration
        self.trigger_event = action.get_trigger_event_from_string(values["trigger_event"])
        self.affected_entity = None  # set at time of allocation to an entity
        self.affliction_effects = []

        # get the affliction skill_effects
        affliction_effects_values = values["affliction_effects"]

        # unpack all affliction_effects
        for effect in affliction_effects_values:
            created_effect = None
            effect_name = effect["name"]

            if effect_name == "damage":
                created_effect = game_manager.affliction_action.create_damage_effect(self, effect)

            # if we have an effect add it to internal list
            if created_effect:
                self.affliction_effects.append(created_effect)

    def trigger(self):
        """
        Trigger all affliction effects and decrement duration by 1
        """
        for effect in self.affliction_effects:
            effect.trigger(self.affected_entity)

        self.duration -= 1

