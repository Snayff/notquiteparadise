from scripts.data_loaders.getters import get_value_from_youth_json


class Youth:
    def __init__(self, youth_name):
        values = get_value_from_youth_json(youth_name)

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
        youth_name = json_data.get('name')

        youth = Youth(youth_name)

        return youth
