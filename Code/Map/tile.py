class Tile:

	def __init__(self, blocked, block_sight=None):
		self.blocked = blocked

		# By default, if a tile is blocked, it also blocks sight
		if block_sight is None:
			block_sight = blocked

		self.block_sight = block_sight

		self.explored = False

	def to_json(self):
		json_data = {
			'blocked': self.blocked,
			'block_sight': self.block_sight,
			'explored': self.explored
		}

		return json_data

	@staticmethod
	def from_json(json_data):
		blocked = json_data.get('blocked')
		block_sight = json_data.get('block_sight')
		explored = json_data.get('explored')

		tile = Tile(blocked, block_sight)
		tile.explored = explored

		return Tile
