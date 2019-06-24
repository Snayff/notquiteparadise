from scripts.core.constants import AfflictionTypes, AfflictionCategory, AfflictionTriggers, LoggingEventTypes, \
    AfflictionEffectTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.affliction import Affliction
from scripts.skills.affliction_effects.affect_stat import AffectStatAfflictionEffect
from scripts.skills.affliction_effects.damage import DamageAfflictionEffect
from scripts.world.entity import Entity


class AfflictionMethods:
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
    def create_affliction(affliction_type, duration, affected_entity):
        """
        Create an Affliction object

        Args:
            affliction_type (AfflictionTypes): the type of the affliction
            duration (int): amount of activations before expiry
            affected_entity (Entity): the entity to be affected

        Returns:
            Affliction:
        """
        affliction = Affliction(affliction_type, duration, affected_entity)

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
    def create_affect_stat_effect(affliction, effect):
        """
        Create the Affect Stat Affliction Effect for the Affliction

        Args:
            affliction (Affliction): the Affliction to contain the damage effect
            effect (): affliction effect json data

        Returns:
            AffectStatAfflictionEffect
        """
        owner = affliction
        stat_to_affect = effect["stat_to_affect"]
        amount = effect["amount"]

        created_effect = AffectStatAfflictionEffect(owner, stat_to_affect, amount)

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
        elif affliction_name == "bogged_down":
            return AfflictionTypes.BOGGED_DOWN

        log_string = f"{affliction_name} not found in 'get_affliction_type_from_string'"
        publisher.publish(LoggingEvent(LoggingEventTypes.CRITICAL, log_string))

    @staticmethod
    def get_affliction_effect_type_from_string(affliction_effect_name):
        """
        Convert a string to the appropriate AfflictionEffectTypes (Enum) value

        Args:
            affliction_effect_name (str): string name of affliction effect

        Returns:
            AfflictionEffectTypes
        """
        if affliction_effect_name == "damage":
            return AfflictionEffectTypes.DAMAGE
        elif affliction_effect_name == "affect_stat":
            return AfflictionEffectTypes.AFFECT_STAT

        log_string = f"{affliction_effect_name} not found in 'get_affliction_effect_type_from_string'"
        publisher.publish(LoggingEvent(LoggingEventTypes.CRITICAL, log_string))

    @staticmethod
    def get_affliction_string_from_type(affliction_type):
        """
        Convert an AfflictionTypes (Enum) to appropriate string

        Args:
            affliction_type (AfflictionTypes): type of affliction

        Returns:
            str: name of the affliction
        """
        # TODO - add remaining afflictions
        if affliction_type == AfflictionTypes.FLAMING:
            return "flaming"
        elif affliction_type == AfflictionTypes.BOGGED_DOWN:
            return "bogged_down"

        log_string = f"{affliction_type} not found in 'get_affliction_string_from_type'"
        publisher.publish(LoggingEvent(LoggingEventTypes.CRITICAL, log_string))

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

        log_string = f"{affliction_category} not found in 'get_affliction_category_from_string'"
        publisher.publish(LoggingEvent(LoggingEventTypes.CRITICAL, log_string))

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
            return "Myopic"
        elif affliction == AfflictionTypes.BOGGED_DOWN:
            return "Sluggish"

        log_string = f"{affliction} not found in 'get_affliction_name'"
        publisher.publish(LoggingEvent(LoggingEventTypes.CRITICAL, log_string))

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

        log_string = f"{trigger_event} not found in 'get_trigger_event_from_string'"
        publisher.publish(LoggingEvent(LoggingEventTypes.CRITICAL, log_string))

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

    def get_affliction_effects_for_entity(self, entity, affliction_effect):
        """
        Get all affliction effects of specified type from a specified entity

        Args:
            entity (Entity):
            affliction_effect (AfflictionEffectTypes):
        """
        afflictions = self.get_afflictions_for_entity(entity)
        affliction_effects = []

        # loop all affliction effects in all afflictions and return specified type
        for affliction in afflictions:
            for effect in affliction.affliction_effects:
                if effect.effect_type == affliction_effect:
                    affliction_effects.append(effect)

        return affliction_effects

    def get_stat_modifier_from_afflictions_on_entity(self, entity, stat):
        """
        Get the modifier for a specified stat from all applied afflictions on an entity

        Args:
            entity (Entity):
            stat (): primary or secondary stat
        """
        modifier = 0

        affect_stat_effects = self.get_affliction_effects_for_entity(entity, AfflictionEffectTypes.AFFECT_STAT)

        # if we have any afflictions get the modifiers to the specified stat
        if affect_stat_effects:
            for effect in affect_stat_effects:
                if effect.stat_to_affect == stat:
                    modifier += effect.amount

        return modifier