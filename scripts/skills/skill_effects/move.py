from scripts.managers.world_methods.game_map_query import is_tile_blocking_movement

from scripts.global_singletons.event_hub import publisher
from scripts.skills.skill_effects.skill_effect import SkillEffect
from scripts.world.Map import is_tile_blocking_movement


class MoveSkillEffect(SkillEffect):
    """
    SkillEffect to move an entity towards target tile
    """

    def __init__(self, target_type, tags, entity_to_move, target, move_distance):
        super().__init__("move", "This is the Move effect", target_type, tags)
        self.entity_to_move = entity_to_move
        self.target = target
        self.move_distance = move_distance

    def trigger(self):
        """
        Trigger the effect
        """
        from scripts.global_singletons.managers import world_manager

        # get required info
        start_pos_x, start_pos_y = self.entity_to_move.x, self.entity_to_move.y
        target_tile_x, target_tile_y = self.target.x, self.target.y
        direction_x, direction_y = world_manager.Entity.get_a_star_direction_between_entities(self.entity_to_move,
                                                                                              self.target)
        # move towards target up to move_distance
        for move in range(1, self.move_distance):
            # check target tile is valid
            in_bounds = world_manager.Map.is_tile_in_bounds(target_tile_x, target_tile_y)
            tile_blocking_movement = is_tile_blocking_movement(target_tile_x,
                                                               target_tile_y)
            entity_blocking_movement = world_manager.Entity.get_blocking_entity_at_location(target_tile_x,
                                                                                            target_tile_y)
            if in_bounds and not tile_blocking_movement and not entity_blocking_movement:
                # move the entity
                self.entity_to_move.x += direction_x
                self.entity_to_move.y += direction_y

        # update the fov if player moved
        from scripts.global_singletons.managers import world_manager
        if self.entity_to_move == world_manager.player:
            world_manager.player_fov_is_dirty = True

        # log the movement
        log_string = f"{self.entity_to_move.name} moved from [{start_pos_x},{start_pos_y}] to " \
            f"[{self.entity_to_move.x},{self.entity_to_move.y}]"
        from scripts.events.logging_events import LoggingEvent
        from scripts.core.constants import LoggingEventTypes
        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))