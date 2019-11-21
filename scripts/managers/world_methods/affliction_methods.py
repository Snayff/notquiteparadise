
import logging
from typing import List

from scripts.core.constants import AfflictionTriggers, EffectTypes, AfflictionLifespan
from scripts.core.data_library import library
from scripts.skills.affliction import Affliction
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
        from scripts.managers.world_manager import WorldManager
        self.manager = manager  # type: WorldManager
        self.active_afflictions = []
        self.expired_afflictions = []

    def cleanse_expired_afflictions(self):
        """
        Delete expired afflictions
        """
        removed_afflictions = []

        # check if afflictions has expired
        for affliction in self.active_afflictions:
            if affliction.duration <= 0:
                # log on expired list. Not removing now to avoid amending the currently iterating list
                self.expired_afflictions.append(affliction)

        # remove all expired afflictions from the active list and delete each instance
        # pop removes the element so we keep looking at element 0 and popping it
        index = 0
        while index < len(self.expired_afflictions):
            # get the afflictions
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
            logging.debug(log_string)

    def create_effect(self, owner, effect_type):
        """
        Create an effect and assign an owner.
        Wrapper for the create effect under world.Skill.

        Args:
            owner (object): Skill or Affliction
            effect_type (EffectTypes):
        """
        self.manager.Skill.create_effect(owner, effect_type)

    @staticmethod
    def create_affliction(affliction_name, duration, affected_entity):
        """
        Create an Affliction object

        Args:
            affliction_name (str): the type of the afflictions
            duration (int): amount of activations before expiry
            affected_entity (Entity): the entity to be affected

        Returns:
            Affliction:
        """
        affliction = Affliction(affliction_name, duration, affected_entity)

        return affliction

    def register_active_affliction(self, affliction):
        """
        Register an afflictions with the central list. Without this they exist in the ether and do nothing.

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
            data = library.get_affliction_data(affliction.name)

            if data.trigger_event == affliction_trigger and affliction.affected_entity == entity:
                affliction.trigger()

    def get_afflictions_for_entity(self, entity):
        """
        Get all Afflictions for an Entity

        Args:
            entity (Entity):

        Returns:
            List[Affliction]: list of Afflictions
        """
        entitys_afflictions = []

        for affliction in self.active_afflictions:
            if affliction.affected_entity == entity:
                entitys_afflictions.append(affliction)

        return entitys_afflictions

    def get_affliction_for_entity(self, entity, affliction_name):
        """
        Get the specified Affliction for an Entity

        Args:
            entity (Entity):
            affliction_name (str):

        Returns:
            Affliction: the requested afflictions, or None if nothing found

        """
        for affliction in self.active_afflictions:
            if affliction.affected_entity == entity and affliction.name == affliction_name:
                return affliction

    def get_affliction_effects_for_entity(self, entity, effect_type):
        """
        Get all afflictions effects of specified type from a specified entity

        Args:
            entity (Entity):
            effect_type (EffectTypes):
        """
        afflictions = self.get_afflictions_for_entity(entity)
        affliction_effects = []

        # loop all afflictions effects in all afflictions and return specified type
        for affliction in afflictions:
            data = library.get_affliction_effect_data(affliction.name, effect_type)

            if data:
                affliction_effects.append(data)

        return affliction_effects

    def get_stat_change_from_afflictions_on_entity(self, entity, stat):
        """
        Get the change for a specified stat from all applied afflictions on an entity

        Args:
            entity (Entity):
            stat (): primary or secondary stat

        Returns:
            int: Amount of stat change
        """
        stat_change = 0

        affect_stat_effects = self.get_affliction_effects_for_entity(entity, EffectTypes.AFFECT_STAT)

        # if we have any afflictions get the modifiers to the specified stat
        if affect_stat_effects:
            for effect in affect_stat_effects:
                if effect.stat_to_affect == stat:
                    stat_change += effect.amount

        return stat_change

    def reduce_affliction_durations_on_entity(self, entity):
        """
        Reduce duration of all non-permanent afflictions on an entity.
        """
        entitys_afflictions = self.get_afflictions_for_entity(entity)
        for affliction in entitys_afflictions:
            # reduce duration on all effects if they're not meant to be permanent
            if affliction.duration != AfflictionLifespan.PERMANENT.value:
                affliction.duration -= 1
                log_string = f"{affliction.affected_entity.name}`s {affliction.name} duration reduced to " \
                             f" {affliction.duration}"
                logging.debug(log_string)