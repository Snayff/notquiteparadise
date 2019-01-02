from scripts.core.constants import LoggingEventNames, EventTopics
from scripts.core.events import Event
from scripts.core.global_data import game_manager


class Entity:

	""" A generic object to represent players, enemies, items, etc. """

	def __init__(self, x, y, sprite, name):
		self.x = x
		self.y = y
		self.sprite = sprite
		self.name = name
		self.blocks_movement = True

	def move(self, dx, dy):
		# Move the entity to a specified tile
		self.x = dx
		self.y = dy

		log_string = f"{self.name} ({self}) moved to [{dx},{dy}]"
		game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))