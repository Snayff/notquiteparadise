from Code.Core.json_loaders import get_value_from_race_json


class Race:
	def __init__(self, race_name):
		values = get_value_from_race_json(race_name)

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
		race_name = json_data.get('name')

		race = Race(race_name)

		return race