from scripts.data_loaders.getters import get_value_from_adulthood_json


class Adulthood:
    def __init__(self, adulthood_name):
        values = get_value_from_adulthood_json(adulthood_name)

        self.name = values["name"]
        self.max_hp = values["max_hp"]
        self.power = values["power"]
        self.defense = values["defense"]
        self.xp_given_on_death = values["xp_given_on_death"]

    def to_json(self):
        # only name is required as all values are static in json
        json_data = {
            'name': self.name
        }

        return json_data

    @staticmethod
    def from_json(json_data):
        adulthood_name = json_data.get('name')

        adulthood = Adulthood(adulthood_name)

        return adulthood
