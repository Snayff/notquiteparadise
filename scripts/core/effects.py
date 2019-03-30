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
        # get start pos for log
        start_pos_x, start_pos_y = self.entity_to_move.x, self.entity_to_move.y

        # move the entity
        # TODO - loop through tiles on way to target to check for collisions and move as far as can
        self.entity_to_move.x += self.target_tile[0]
        self.entity_to_move.y += self.target_tile[1]

        # get end pos for log
        end_pos_x, end_pos_y = self.entity_to_move.x, self.entity_to_move.y

        # update the fov if player moved
        from scripts.core.global_data import entity_manager
        if self.entity_to_move == entity_manager.player:
            from scripts.core.global_data import world_manager
            world_manager.player_fov_is_dirty = True

        # log the movement
        log_string = f"{self.entity_to_move.name} moved from [{start_pos_x},{start_pos_y}] to [{end_pos_x}," \
            f"{end_pos_y}]"
        from scripts.core.global_data import game_manager
        from scripts.events.logging_events import LoggingEvent
        from scripts.core.constants import LoggingEventTypes
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))