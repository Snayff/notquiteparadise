from scripts.core.constants import AfflictionTypes, AfflictionCategory, AfflictionTriggers, LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.affliction import Affliction
from scripts.skills.affliction_effects.damage import DamageAfflictionEffect
from scripts.world.entity import Entity


class AfflictionAction:
    """
    Methods for taking actions with Afflictions

    Attributes:
        manager ():
        active_afflictions (): list of all active afflictions
        expired_afflictions (): list containing the expired afflictions to be deleted. empties at end of GameLoop
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

    @staticmethod
    def create_affliction(affliction_name, duration, affected_entity):
        """
        Create an Affliction object

        Args:
            affliction_name (str): the string name of the affliction
            duration (int): amount of activations before expiry
            affected_entity (Entity): the entity to be affected

        Returns:
            Affliction:
        """
        affliction = Affliction(affliction_name, duration, affected_entity)

        return affliction

    @staticmethod
    def create_damage_effect(affliction, effect):
        """
        Create the Damage Affliction Effect for the Affliction

        Args:
            affliction (Affliction): the Affliction to contain the damage effect
            effect (): affliction effect json data

        Returns:
            DamageAfflictionEffect
        """
        owner = affliction
        damage = effect["damage"]
        damage_type = effect["damage_type"]
        stat_to_target = effect["stat_to_target"]

        created_effect = DamageAfflictionEffect(owner, damage, damage_type, stat_to_target)

        return created_effect

    @staticmethod
    def get_affliction_type_from_string(affliction_name):
        """
        Convert a string to the appropriate AfflictionTypes (Enum) value

        Args:
            affliction_name (str): string name of affliction

        Returns:
            AfflictionTypes
        """
        # TODO - add remaining afflictions
        if affliction_name == "flaming":
            return AfflictionTypes.FLAMING

    @staticmethod
    def get_affliction_category_from_string(affliction_category):
        """
        Convert a string to the appropriate AfflictionCategory (Enum) value

        Args:
            affliction_category (str): string name of affliction category

        Returns:
            AfflictionCategory
        """
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

    @staticmethod
    def get_trigger_event_from_string(trigger_event):
        """
        Convert a string to the appropriate AfflictionTriggers (Enum) value

        Args:
            trigger_event (str): string name of trigger event

        Returns:
            AfflictionTriggers
        """
        # TODO - add remaining afflictions
        if trigger_event == "passive":
            return AfflictionTriggers.PASSIVE
        elif trigger_event == "end_turn":
            return AfflictionTriggers.END_TURN

    def register_active_affliction(self, affliction):
        """
        Register an affliction with the central list. Without this they exist in the ether and do nothing.

        Args:
            affliction (Affliction):
        """
        self.active_afflictions.append(affliction)

    def trigger_afflictions_on_entity(self, affliction_trigger, entity):
        """
        Cause all afflictions of a specified AfflictionTrigger to trigger on an Entity
        Args:
            affliction_trigger (AfflictionTriggers):
            entity (Entity):
        """
        for affliction in self.active_afflictions:
            if affliction.trigger_event == affliction_trigger and affliction.affected_entity == entity:
                affliction.trigger()

    def get_afflictions_for_entity(self, entity):
        """
        Get all Afflictions for an Entity

        Args:
            entity (Entity):

        Returns:
            list: list of Afflictions
        """
        entitys_afflictions = []

        for affliction in self.active_afflictions:
            if affliction.affected_entity == entity:
                entitys_afflictions.append(affliction)

        return entitys_afflictions

    def affliction_exists(self, entity, affliction_type):
        """
        Check if a specific Affliction exists on an Entity

        Args:
            entity (Entity):
            affliction_type (AfflictionTypes):

        Returns:
            bool:
        """
        for affliction in self.active_afflictions:
            if affliction.affected_entity == entity and affliction.affliction_type == affliction_type:
                return True

        return False

    def get_affliction_type_for_entity(self, entity, affliction_type):
        """
        Get the specified Affliction for an Entity

        Args:
            entity (Entity):
            affliction_type (AfflictionTypes):

        Returns:
            Affliction: the requested affliction, or None if nothing found

        """
        for affliction in self.active_afflictions:
            if affliction.affected_entity == entity and affliction.affliction_type == affliction_type:
                return affliction

        return None