from scripts.core.constants import EntityEventNames, LoggingEventNames
from scripts.core.global_data import world_manager, entity_manager, game_manager
from scripts.events.entity_events import AttackEvent, MoveEvent
from scripts.events.game_events import EndTurnEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber


class EntityHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "entity_handler", event_hub)

    def run(self, event):
        log_string = f"{self.name} received {event.name}"
        game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

        if event.name == EntityEventNames.MOVE:
            entity = event.entity
            destination_x = entity.x + event.destination_x
            destination_y = entity.y + event.destination_y
            tile_is_blocked = world_manager.game_map.is_tile_blocking_movement(destination_x, destination_y)
            map_height = world_manager.game_map.height
            map_width = world_manager.game_map.width

            # if the tile is accessible check if there is someone else there
            if not tile_is_blocked and 0 <= destination_x <= map_width and 0 <= destination_y <= map_height:
                target = entity_manager.get_blocking_entities_at_location(destination_x, destination_y)

                # someone is in the way, attack them!
                if target:
                    game_manager.create_event(AttackEvent(entity, target))

                # no one is in the way, move!
                else:
                    entity.actor.move(destination_x, destination_y)
                    world_manager.player_fov_is_dirty = True
                    log_string = f"{entity.name} ({entity}) moved to [{destination_x},{destination_y}]"
                    game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

                    game_manager.create_event(EndTurnEvent(10))  # TODO abstract magic number

            else:
                log_string = f"Target location blocked and {entity.name} did not move."
                game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

        if event.name == EntityEventNames.GET_MOVE_TARGET:
            entity = event.moving_entity
            target = event.target_entity
            log_string = f"{entity.name} ({entity}) looked for a path to {target.name} [{target.x},{target.y}] with a*"
            game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

            # get destination to move to and then move
            dx, dy = entity_manager.get_direction_between_entities(entity, target)
            game_manager.create_event(MoveEvent(entity, dx, dy))

        if event.name == EntityEventNames.ATTACK:
            attacker = event.values[0]
            target = event.values[1]

            log_string = f"{attacker.name} ({attacker}) tries to attack {target.name} [{target.x},{target.y}] "
            game_manager.create_event(LoggingEvent(LoggingEventNames.MUNDANE, log_string))

            # attacker.living.attack(target)
            game_manager.create_event(EndTurnEvent(10))  # TODO abstract magic number
