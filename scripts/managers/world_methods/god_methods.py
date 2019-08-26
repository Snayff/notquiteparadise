
from scripts.global_singletons.data_library import library


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
        god_data = library.get_god_data(god_name)

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