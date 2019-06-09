
from scripts.core.constants import AfflictionTypes, AfflictionCategory, AfflictionTriggers, LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.affliction import Affliction
from scripts.skills.affliction_effects.damage import DamageAfflictionEffect


class AfflictionAction:
    """
    Methods for taking actions with Afflictions
    """
    def __init__(self, manager):
        self.manager = manager
        self.active_afflictions = []
        self.expired_afflictions = []

    def cleanse_expired_afflictions(self):
        """
        Delete expired afflictions
        """
        removed_afflictions = []

        # check if affliction has expired
        for affliction in self.active_afflictions:
            if affliction.duration <= 0:
                # log on expired list. Not removing now to avoid amending the currently iterating list
                self.expired_afflictions.append(affliction)

        # remove all expired afflictions from the active list and delete each instance
        # pop removes the element so we keep looking at element 0 and popping it
        index = 0
        while index < len(self.expired_afflictions):
            # get the affliction
            affliction = self.expired_afflictions.pop(index)

            # remove from active list
            self.active_afflictions.remove(affliction)

            # add info to logging
            removed_afflictions.append(f"{affliction.affected_entity.name}:{affliction.name}")

            # delete the instance
            del affliction

        # if we removed anything log it
        if removed_afflictions:
            log_string = f"Removed the following afflictions: {removed_afflictions}"
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))


    def create_affliction(self, affliction_name, duration, affected_entity):
        affliction = Affliction(affliction_name, duration, affected_entity)

        return affliction

    def create_damage_effect(self, affliction,  effect):
        owner = affliction
        damage = effect["damage"]
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

    def register_active_affliction(self, affliction):
        self.active_afflictions.append(affliction)

    def trigger_afflictions_on_entity(self, affliction_trigger, entity):

        for affliction in self.active_afflictions:
            if affliction.trigger_event == affliction_trigger and affliction.affected_entity == entity:
                affliction.trigger()

    def get_afflictions_for_entity(self, entity):
        entitys_afflictions = []

        for affliction in self.active_afflictions:
            if affliction.affected_entity == entity:
                entitys_afflictions.append(affliction)

        return entitys_afflictions

    def affliction_exists(self, entity, affliction_type):
        for affliction in self.active_afflictions:
            if affliction.affected_entity == entity and affliction.affliction_type == affliction_type:
                return True

        return False

    def get_affliction_type_for_entity(self, entity, affliction_type):
        for affliction in self.active_afflictions:
            if affliction.affected_entity == entity and affliction.affliction_type == affliction_type:
                return affliction