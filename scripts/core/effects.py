class Effect:
    def __init__(self):
        self.owner = None


class MoveEffect(Effect):
    def __init__(self, entity_to_move, target_tile):
        Effect.__init__(self)
        self.description = "This is the move effect"
        self.entity_to_move = entity_to_move
        self.target_tile = target_tile

    def trigger(self):
        # move the entity
        self.entity_to_move.x += self.target_tile[0]
        self.entity_to_move.y += self.target_tile[1]

        # update the fov if player moved
        from scripts.core.global_data import entity_manager
        if self.entity_to_move == entity_manager.player:
            from scripts.core.global_data import world_manager
            world_manager.player_fov_is_dirty = True

        # log the movement
        destination_x = self.entity_to_move.x + self.target_tile[0]
        destination_y = self.entity_to_move.y + self.target_tile[1]
        # FIXME - logging negative positions
        log_string = f"{self.entity_to_move.name} ({self.entity_to_move}) moved to [{destination_x},{destination_y}]"
        from scripts.core.global_data import game_manager
        from scripts.events.logging_events import LoggingEvent
        from scripts.core.constants import LoggingEventTypes
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))