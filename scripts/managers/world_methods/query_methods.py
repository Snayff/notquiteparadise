import math
import tcod
import scipy.spatial

from scripts.core.constants import LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher


class EntityQuery:
    """
    Queries relating to entities.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """
    def __init__(self, manager):
        self.manager = manager

    def get_blocking_entity_at_location(self, tile_x, tile_y):
        """

        Args:
            tile_x:
            tile_y:

        Returns:
            Entity: returns entity if there is one, else None.
        """
        tile = self.manager.game_map.get_tile(tile_x, tile_y)
        entity = tile.entity

        if entity:
            if entity.blocks_movement:
                return entity

        return None

    def get_entity_in_fov_at_tile(self, tile_x, tile_y):
        """
        Get the entity at a target tile

        Args:
            tile_x: x of tile
            tile_y: y of tile

        Returns:
            entity: Entity or None if no entity found
        """
        tile = self.manager.game_map.get_tile(tile_x, tile_y)
        entity = tile.entity

        if entity:
            if self.manager.is_tile_in_fov(tile_x, tile_y):
                return entity

        return None

    @staticmethod
    def get_euclidean_distance_between_entities(start_entity, target_entity):
        """
        get distance from an entity towards another entity's location

        Args:
            start_entity (Entity):
            target_entity (Entity):

        Returns:
            float: straight line distance

        """
        dx = target_entity.x - start_entity.x
        dy = target_entity.y - start_entity.y
        return math.sqrt(dx ** 2 + dy ** 2)

    @staticmethod
    def get_chebyshev_distance_between_entities(start_entity, target_entity):
        """
        get distance from an entity towards another entity's location

        Args:
            start_entity (Entity):
            target_entity (Entity):

        Returns:
            int: distance in terrain

        """
        start_entity_position = [start_entity.x, start_entity.y]
        target_entity_position = [target_entity.x, target_entity.y]
        return scipy.spatial.distance.chebyshev(start_entity_position, target_entity_position)

    def get_direct_direction_between_entities(self, start_entity, target_entity):
        """
        get direction from an entity towards another entity's location

        Args:
            start_entity (Entity):
            target_entity (Entity):

        """
        log_string = f"{start_entity.name} is looking for a direct path to {target_entity.name}."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        game_map = self.manager.game_map

        direction_x = target_entity.x - start_entity.x
        direction_y = target_entity.y - start_entity.y
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)

        direction_x = int(round(direction_x / distance))
        direction_y = int(round(direction_y / distance))

        tile_is_blocked = game_map.is_tile_blocking_movement(start_entity.x + direction_x, start_entity.y +
                                                                                           direction_y)

        if not (tile_is_blocked or self.get_blocking_entity_at_location(start_entity.x + direction_x,
                                                                          start_entity.y + direction_y)):
            log_string = f"{start_entity.name} found a direct path to {target_entity.name}."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

            return direction_x, direction_y
        else:
            log_string = f"{start_entity.name} did NOT find a direct path to {target_entity.name}."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

            return start_entity.x, start_entity.y

    @staticmethod
    def get_a_star_direction_between_entities(start_entity, target_entity):
        """
        Use a* pathfinding to get a direction from one entity to another
        Args:
            start_entity:
            target_entity:

        Returns:

        """
        max_path_length = 25
        from scripts.global_instances.managers import world_manager
        game_map = world_manager.game_map
        entities = world_manager.entity_existence.get_all_entities()
        entity_to_move = start_entity
        target = target_entity

        log_string = f"{entity_to_move.name} is looking for a path to {target.name} with a*"
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        # Create a FOV map that has the dimensions of the map
        fov = tcod.map_new(game_map.width, game_map.height)

        # Scan the current map each turn and set all the walls as unwalkable
        for y1 in range(game_map.height):
            for x1 in range(game_map.width):
                tcod.map_set_properties(fov, x1, y1, not game_map.tiles[x1][y1].blocks_sight,
                                           not game_map.tiles[x1][y1].blocks_movement)

        # Scan all the objects to see if there are objects that must be navigated around
        # Check also that the object isn't self or the target (so that the start and the end points are free)
        # The AI class handles the situation if self is next to the target so it will not use this A* function
        # anyway
        for entity in entities:
            if entity.blocks_movement and entity != entity_to_move and entity != target:
                # Set the tile as a wall so it must be navigated around
                tcod.map_set_properties(fov, entity.x, entity.y, True, False)

        # Allocate a A* path
        # The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited
        my_path = tcod.path_new_using_map(fov, 1.41)

        # Compute the path between self's coordinates and the target's coordinates
        tcod.path_compute(my_path, entity_to_move.x, entity_to_move.y, target.x, target.y)

        # Check if the path exists, and in this case, also the path is shorter than max_path_length
        # The path size matters if you want the monster to use alternative longer paths (for example through
        # other rooms) if for example the player is in a corridor
        # It makes sense to keep path size relatively low to keep the monsters from running around the map if
        # there's an alternative path really far away
        if not tcod.path_is_empty(my_path) and tcod.path_size(my_path) < max_path_length:
            # Find the next coordinates in the computed full path
            x, y = tcod.path_walk(my_path, True)

            # convert to direction
            direction_x = x - entity_to_move.x
            direction_y = y - entity_to_move.y

            log_string = f"{entity_to_move.name} found an a* path to {target.name}..."
            log_string2 = f"-> will move from [{entity_to_move.x},{entity_to_move.y}] towards [{x},{y}] in direction "\
                f"[{direction_x},{direction_y}]"
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string2))

        else:
            # no path found return no movement direction
            direction_x, direction_y = 0, 0
            log_string = f"{entity_to_move.name} did NOT find an a* path to {target.name}."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        # Delete the path to free memory
        tcod.path_delete(my_path)
        return direction_x, direction_y
