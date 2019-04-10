from scripts.data_loaders.getters import get_value_from_motive_json


class Motive:
    """
    [Component] Derives some stats from the Motive type.

    Attributes:
        name (str): Motive type's name
        power (int) = Power value
        defence (int) = Defence value
        xp_given_on_death (int) = Amount of XP to give on death
    """
    def __init__(self, motive_name):
        """
        Args:
            motive_name (str): Name of the Motive type.
        """
        values = get_value_from_motive_json(motive_name)

        self.name = values["name"]
        self.description = values["description"]
        self.vigour = values["vigour"]
        self.clout = values["clout"]
        self.subtlety = values["subtlety"]
        self.bustle = values["bustle"]
        self.exactitude = values["exactitude"]

