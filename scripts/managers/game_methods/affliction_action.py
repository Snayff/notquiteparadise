
from scripts.core.constants import AfflictionTypes, AfflictionCategory, AfflictionTriggers
from scripts.skills.affliction import Affliction
from scripts.skills.affliction_effects.damage import DamageAfflictionEffect


class AfflictionAction:
    """
    Methods for taking actions with Afflictions
    """
    def __init__(self, manager):
        self.manager = manager

    def create_affliction(self, affliction_name, duration):
        affliction = Affliction(affliction_name, duration)

        return affliction

    def create_damage_effect(self, affliction,  effect):
        owner = affliction
        damage = effect["base_damage"]
        damage_type = effect["damage_type"]
        stat_to_target = effect["stat_to_target"]

        created_effect = DamageAfflictionEffect(owner, damage, damage_type, stat_to_target)

        return created_effect

    def get_affliction_type_from_string(self, affliction_name):

        # TODO - add remaining afflictions
        if affliction_name == "flaming":
            return AfflictionTypes.FLAMING

    def get_affliction_category_from_string(self, affliction_category):

        if affliction_category == "bane":
            return AfflictionCategory.BANE
        elif affliction_category == "boon":
            return AfflictionCategory.BOON

    @staticmethod
    def get_affliction_name(affliction):
        """
        Get affliction name from AfflictionTypes
        Args:
            affliction (AfflictionTypes):

        Returns:
            string: Name of affliction
        """
        # TODO - add remaining types
        if affliction == AfflictionTypes.MYOPIC:
            name = "Myopic"
        elif affliction == AfflictionTypes.SLUGGISH:
            name = "Sluggish"
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""

        return name

    def get_trigger_event_from_string(self, trigger_event):

        # TODO - add remaining afflictions
        if trigger_event == "passive":
            return AfflictionTriggers.PASSIVE
        elif trigger_event == "end_turn":
            return AfflictionTriggers.END_TURN