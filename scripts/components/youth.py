from scripts.data_loaders.getters import get_value_from_youth_json


class Youth:
    """
    [Component] Derives some stats from the Youth type.

    Attributes:
        name (str): Adulthood type's name
        power (int) = Power value
        defence (int) = Defence value
        xp_given_on_death (int) = Amount of XP to give on death
    """
    def __init__(self, youth_name):
        """
        Args:
            youth_name (str): Name of the Youth type.
        """
        values = get_value_from_youth_json(youth_name)

        self.name = values["name"]
        self.max_hp = values["max_hp"]
        self.power = values["power"]
        self.defence = values["defence"]
        self.xp_given_on_death = values["xp_given_on_death"]
