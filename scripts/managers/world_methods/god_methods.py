import logging
from enum import Enum
from typing import List

from scripts.global_singletons.data_library import library
from scripts.world.god import God
from scripts.world.god_dataclass import GodData


class GodMethods:
    """
    Methods for querying and managing god related actions and info

    Attributes:
        manager(WorldManager): the manager containing this class.
    """

    def __init__(self, manager):
        from scripts.managers.world import WorldManager
        self.manager = manager  # type: WorldManager

    def create_god(self, god_name):
        """

        Args:
            god_name ():
        """
        data = library.get_god_data(god_name)

        from scripts.world.god import God
        god = God(god_name)
        self.add_god_to_central_list(god)

    def add_god_to_central_list(self, god):
        """
        Add a god to the world_manager list

        Args:
            god (God):
        """

        self.manager.gods.append(god)

    def get_gods(self):
        """
        Get all gods

        Returns:
            List[God]:
        """

        return self.manager.gods

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
