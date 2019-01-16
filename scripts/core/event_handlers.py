from scripts.core.constants import EntityEventNames, EventTopics, LoggingEventNames, GameEventNames, GameStates
from scripts.core.events import Subscriber, Event
from scripts.core.global_data import world_manager, entity_manager, game_manager, turn_manager


class GameHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "game_handler", event_hub)

    def run(self, event):
        log_msg = f"{self.name} received {event.name}"
        game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_msg]))

        if event.name == GameEventNames.EXIT:
            game_manager.update_game_state(GameStates.EXIT_GAME)

        elif event.name == GameEventNames.END_TURN:
            turn_manager.end_turn(event.values[0])

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
            map_height = len(world_manager.game_map)
            map_width = len(world_manager.game_map[0])

            # if the tile is accessible check if there is someone else there
            if not tile_is_blocked and 0 <= destination_x <= map_width and 0 <= destination_y <= map_height:
                target = entity_manager.get_blocking_entities_at_location(destination_x, destination_y)

                # someone is in the way, attack them!
                if target:
                    game_manager.create_event(Event(EntityEventNames.ATTACK, EventTopics.ENTITY, [entity,
                        target]))

                # no one is in the way, move!
                else:
                    entity.actor.move(destination_x, destination_y)
                    world_manager.player_fov_is_dirty = True
                    log_string = f"{entity.name} ({entity}) moved to [{destination_x},{destination_y}]"
                    game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))

                    game_manager.create_event(Event(GameEventNames.END_TURN, EventTopics.GAME, [10]))  # TODO abstract magic number

            else:
                log_string = f"Target location blocked and {entity.name} did not move."
                game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))

        if event.name == EntityEventNames.GET_MOVE_TARGET:
            entity = event.values[0]
            target = event.values[1]
            log_string = f"{entity.name} ({entity}) looked for a path to {target.name} [{target.x},{target.y}] with a*"
            game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))

            # get destination to move to and then move
            dx, dy = entity_manager.get_direction_between_entities(entity, target)
            game_manager.create_event(Event(EntityEventNames.MOVE, EventTopics.ENTITY, [entity, dx, dy]))

        if event.name == EntityEventNames.ATTACK:
            attacker = event.values[0]
            target = event.values[1]

            log_string = f"{attacker.name} ({attacker}) tries to attack {target.name} [{target.x},{target.y}] "
            game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))

            # attacker.living.attack(target)
            game_manager.create_event(Event(GameEventNames.END_TURN, EventTopics.GAME, [10]))  # TODO abstract magic number
