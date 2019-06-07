from scripts.data_loaders.getters import get_value_from_race_json


class Race:
    """
    [Component]  Derives some stats from the Race type.
    """

    def __init__(self, race_name):
        """
        Args:
            race_name (str): Name of the Race type.
        """
        values = get_value_from_race_json(race_name)

        self.name = values["name"]
        self.description = values["description"]
        self.vigour = values["vigour"]
        self.clout = values["clout"]
        self.skullduggery = values["SKULLDUGGERY"]
        self.bustle = values["bustle"]
        self.exactitude = values["exactitude"]

