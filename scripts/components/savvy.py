
from scripts.global_singletons.data_library import library


class Savvy:
    """
    [Component] Adds some stats from the Trade.

    """
    def __init__(self, savvy_name):
        """
        Args:
            savvy_name (str): Name of the Trade type.
        """
        savvy = library.get_savvy_data(savvy_name)

        self.name = savvy.name
        self.description = savvy.description
        self.vigour = savvy.vigour
        self.clout = savvy.clout
        self.skullduggery = savvy.skullduggery
        self.bustle = savvy.bustle
        self.exactitude = savvy.exactitude
