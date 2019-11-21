
from scripts.core.data_library import library


class Homeland:
    """
    [Component] Derives some stats from the Motive type.

    Attributes:
        name (str): Motive type`s name
        power (int) = Power value
        defence (int) = Defence value
        xp_given_on_death (int) = Amount of XP to give on death
    """
    def __init__(self, homeland_name):
        """
        Args:
            homeland_name (str): Name of the Motive type.
        """
        homeland = library.get_homeland_data(homeland_name)

        self.name = homeland.name
        self.description = homeland.description
        self.vigour = homeland.vigour
        self.clout = homeland.clout
        self.skullduggery = homeland.skullduggery
        self.bustle = homeland.bustle
        self.exactitude = homeland.exactitude

