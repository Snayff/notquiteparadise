from scripts.data_loaders.getters import get_value_from_adulthood_json


class Adulthood:
    def __init__(self, adulthood_name):
        values = get_value_from_adulthood_json(adulthood_name)

        self.name = values["name"]
        self.max_hp = values["max_hp"]
        self.power = values["power"]
        self.defence = values["defence"]
        self.xp_given_on_death = values["xp_given_on_death"]

