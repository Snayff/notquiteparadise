from __future__ import annotations

import logging
import random
from typing import TYPE_CHECKING
from enum import Enum
from scripts.core.library import library
from scripts.world.god import God

if TYPE_CHECKING:
    from scripts.managers.world_manager import WorldManager
    from typing import List, Tuple


class GodMethods:
    """
    Methods for querying and managing god related actions and info

    Attributes:
        manager(WorldManager): the manager containing this class.
    """

    def __init__(self, manager):
        self._manager = manager  # type: WorldManager

    def create_god(self, god_name):
        """

        Args:
            god_name ():
        """
        from scripts.world.god import God
        god = God(god_name)

        self.add_god_to_central_list(god)

    def add_god_to_central_list(self, god):
        """
        Add a god to the world list

        Args:
            god (God):
        """

        self._manager.gods.append(god)

    def get_gods(self):
        """
        Get all gods

        Returns:
            List[God]:
        """

        return self._manager.gods

    def judge_action(self, entity, action):
        """
        Have all gods alter opinion of entity based on an action taken, if they have an attitude towards that action.

        Args:
            entity (Entity):
            action (object): Can be str if matching name, e.g. affliction name, or Enum name, e.g. Hit Type name.

        """

        gods = self.get_gods()

        # loop all gods and get their attitudes
        for god in gods:
            attitudes = library.get_god_attitudes_data(god.name)

            # handle enums and str being passed in
            if isinstance(action, Enum):
                action_name = action.name
            else:
                action_name = action

            # check if the god has an attitude towards the action and apply the opinion change, adding the entity to
            # the dict if necessary
            if action_name in attitudes:
                if entity in god.opinions:
                    god.opinions[entity] += attitudes[action].opinion_change
                else:
                    god.opinions[entity] = attitudes[action].opinion_change

                logging.debug(f"'{god.name}' reacted to '{entity.name}' using {action_name}. New opinion ="
                              f" {god.opinions[entity]}")

    def consider_intervening(self, entity, action=None):
        """
        Loop all gods and check if they will intervene

        Args:
            entity (Entity):
            action (object): Can be str if matching name, e.g. affliction name, or Enum name, e.g. Hit Type name.

        Returns:
            List[Tuple]: List of tuples containing (God.name, intervention, entity) as strings.
        """

        gods = self.get_gods()

        all_interventions_taken = []

        if action:
            # handle enums and str being passed in
            if isinstance(action, Enum):
                action_name = action.name
            else:
                action_name = action
        else:
            action_name = "None"

        # action taken by an entity so start consideration
        for god in gods:

            # does the god care about the entity?
            if entity in god.opinions:
                # what are the possible interventions
                interventions = god.interventions
                attitudes = library.get_god_attitudes_data(god.name)
                possible_interventions = []
                intervention_weightings = []
                base_inaction_value = 75  # weighting for doing nothing # TODO - move magic number to config
                inaction_modifier = 1  # TODO - move magic number to config

                for name, intervention in interventions.items():
                    intervention_data = library.get_god_intervention_data(intervention.owner.name, name)

                    # is the god willing to intervene (meet required opinion)
                    if abs(god.opinions[entity]) >= abs(intervention_data.required_opinion):
                        possible_interventions.append(intervention)
                        intervention_weightings.append(abs(intervention_data.required_opinion))

                # make no intervention less likely if god cares about action taken by entity
                if action_name in attitudes:
                    inaction_modifier = 0.5
                # add inaction to list of choices
                possible_interventions.append("None")
                intervention_weightings.append(base_inaction_value * inaction_modifier)

                # which intervention, if any,  shall the god consider using?
                chosen_intervention_list = random.choices(possible_interventions)
                chosen_intervention = chosen_intervention_list.pop()

                # if god has chosen to take an action then add to list
                if chosen_intervention != "None":
                    all_interventions_taken.append((god, chosen_intervention, entity))

            return all_interventions_taken

    @staticmethod
    def intervene(god, intervention, entity):
        """
        God to use intervention on entity.

        Args:
            god (God):
            intervention (Intervention):
            entity (Entity):
        """
        god.interventions[intervention.name].use((entity.x, entity.y))

