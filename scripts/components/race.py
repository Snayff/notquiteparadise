
from scripts.global_singletons.data_library import library


class Race:
    """
    [Component]  Derives some stats from the Race type.
    """

    def __init__(self, race_name):
        """
        Args:
            race_name (str): Name of the Race type.
        """
        race = library.get_race_data(race_name)

        self.name = race.name
        self.description = race.description
        self.vigour = race.vigour
        self.clout = race.clout
        self.skullduggery = race.skullduggery
        self.bustle = race.bustle
        self.exactitude = race.exactitude

