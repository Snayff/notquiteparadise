from scripts.core.constants import SkillEffectTypes
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.skill_effects.skill_effect import SkillEffect


class MoveSkillEffect(SkillEffect):
    """
    SkillEffect to move an entity towards target tile
    """

    def __init__(self, owner):
        super().__init__(owner, "move", "This is the Move effect", SkillEffectTypes.MOVE)

    def trigger(self, entity_to_move, target):
        """
        Trigger the effect
        """
        # FIXME - handle target and destination
        #  destination held in inherent values? e.g. distance to move AWAY = 1 ?
        from scripts.global_singletons.managers import world_manager

        data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.skill_effect_type)

        # get required info
        start_pos_x, start_pos_y = entity_to_move.x, entity_to_move.y
        target_tile_x, target_tile_y = target.x, target.y
        direction_x, direction_y = world_manager.Entity.get_a_star_direction_between_entities(entity_to_move,
                                                                                              target)
        # move towards target up to move_distance
        for move in range(1, data.move_distance):
            # check target tile is valid
            in_bounds = world_manager.Map.is_tile_in_bounds(target_tile_x, target_tile_y)
            tile_blocking_movement = world_manager.Map.is_tile_blocking_movement(target_tile_x,
                                                               target_tile_y)
            entity_blocking_movement = world_manager.Entity.get_blocking_entity_at_location(target_tile_x,
                                                                                            target_tile_y)
            if in_bounds and not tile_blocking_movement and not entity_blocking_movement:
                # move the entity
                entity_to_move.x += direction_x
                entity_to_move.y += direction_y

        # update the fov if player moved
        from scripts.global_singletons.managers import world_manager
        if entity_to_move == world_manager.player:
            world_manager.player_fov_is_dirty = True

        # log the movement
        log_string = f"{entity_to_move.name} moved from [{start_pos_x},{start_pos_y}] to " \
            f"[{entity_to_move.x},{entity_to_move.y}]"
        from scripts.events.logging_events import LoggingEvent
        from scripts.core.constants import LoggingEventTypes
        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))