import logging

from scripts.core.constants import EffectTypes
from scripts.core.data_library import library
from scripts.skills.effects.effect import Effect


class MoveEffect(Effect):
    """
    Effect to move an entity towards target tile
    """

    def __init__(self, owner):
        super().__init__(owner, "move", "This is the Move effect", EffectTypes.MOVE)

    def trigger(self, entity_to_move, target):
        """
        Trigger the effect
        """
        # FIXME - handle target and destination
        #  destination held in inherent values? e.g. distance to move AWAY = 1 ?
        from scripts.managers.world_manager import world

        data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.effect_type)

        # get required info
        start_pos_x, start_pos_y = entity_to_move.x, entity_to_move.y
        target_tile_x, target_tile_y = target.x, target.y
        direction_x, direction_y = world.Entity.get_a_star_direction_between_entities(entity_to_move,
                                                                                              target)
        # move towards target up to move_distance
        for move in range(1, data.move_distance):
            # check target tile is valid
            in_bounds = world.Map.is_tile_in_bounds(target_tile_x, target_tile_y)
            tile_blocking_movement = world.Map.is_tile_blocking_movement(target_tile_x,
                                                               target_tile_y)
            entity_blocking_movement = world.Entity.get_blocking_entity(target_tile_x,
                                                                        target_tile_y)
            if in_bounds and not tile_blocking_movement and not entity_blocking_movement:
                # move the entity
                entity_to_move.x += direction_x
                entity_to_move.y += direction_y

        # update the fov if player moved
        from scripts.managers.world_manager import world
        if entity_to_move == world.player:
            world.player_fov_is_dirty = True

        # log the movement
        log_string = f"{entity_to_move.name} moved from [{start_pos_x},{start_pos_y}] to " \
            f"[{entity_to_move.x},{entity_to_move.y}]"
        logging.info( log_string)