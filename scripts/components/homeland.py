from scripts.data_loaders.getters import get_value_from_homeland_json


class Homeland:
    """
    [Component] Derives some stats from the Motive type.

    Attributes:
        name (str): Motive type's name
        power (int) = Power value
        defence (int) = Defence value
        xp_given_on_death (int) = Amount of XP to give on death
    """
    def __init__(self, homeland_name):
        """
        Args:
            homeland_name (str): Name of the Motive type.
        """
        values = get_value_from_homeland_json(homeland_name)

        self.name = values["name"]
        self.description = values["description"]
        self.vigour = values["vigour"]
        self.clout = values["clout"]
        self.skullduggery = values["skullduggery"]
        self.bustle = values["bustle"]
        self.exactitude = values["exactitude"]

