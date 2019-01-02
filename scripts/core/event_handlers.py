from scripts.core.constants import EntityEventNames, EventTopics, LoggingEventNames, GameEventNames, GameStates
from scripts.core.events import Subscriber, Event
from scripts.core.global_data import world_manager, entity_manager, game_manager


class GameHandler(Subscriber):
	def __init__(self, event_hub):
		Subscriber.__init__(self, "game_handler", event_hub)

	def run(self, event):
		log_msg = f"{self.name} received {event.name}"
		game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_msg]))

		if event.name == GameEventNames.EXIT:
			game_manager.update_game_state(GameStates.EXIT_GAME)

		# if event.name == GameEventNames.NEW_GAME:
		# 	from Code.Core.initialisers import initialise_new_game
		# 	initialise_new_game()


class MessageHandler(Subscriber):
	def __init__(self, event_hub):
		Subscriber.__init__(self, "message_handler", event_hub)

	def run(self, event):
		log_msg = f"{self.name} received {event.name}"
		game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_msg]))

		# TODO add message to message log


class LoggingHandler(Subscriber):
	def __init__(self, event_hub):
		Subscriber.__init__(self, "logging_handler", event_hub)

	def run(self, event):
		# Note: Does not create a log entry. Doing so causes infinite loops. Don't do that.
		for value in event.values:
			print(value)


class EntityHandler(Subscriber):
	def __init__(self, event_hub):
		Subscriber.__init__(self, "entity_handler", event_hub)

	def run(self, event):
		log_msg = f"{self.name} received {event.name}"
		game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_msg]))

		if event.name == EntityEventNames.MOVE:
			entity = event.values[0]
			destination_x = entity.x + event.values[1]
			destination_y = entity.y + event.values[2]
			tile_is_blocked = world_manager.game_map[destination_x][destination_y].blocks_movement

			# if the tile is accessible check if there is someone else there
			if not tile_is_blocked:
				target = entity_manager.get_blocking_entities_at_location(destination_x, destination_y)

				# someone is in the way, attack them!
				if target:
					game_manager.create_event(Event(EntityEventNames.ATTACK, EventTopics.ENTITY, [entity,
						target]))

				# no one is in the way, move
				else:
					entity.move(destination_x, destination_y)
					world_manager.fov_is_dirty = True

				# turn_manager.next_turn()

		# if event.name == EntityEventNames.MOVE_ASTAR:
		# 	entity = event.values[0]
		# 	target = event.values[1]
		#
		# 	entity.move_astar(entity, target)
		# 	turn_manager.next_turn()
		#
		# if event.name == EntityEventNames.ATTACK:
		# 	attacker = event.values[0]
		# 	defender = event.values[1]
		#
		# 	attacker.living.attack(defender)
		# 	turn_manager.next_turn()
