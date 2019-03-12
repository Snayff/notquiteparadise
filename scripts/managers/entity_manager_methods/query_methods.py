import math

from scripts.core import global_data

class EntityQuery:
    def __init__(self, manager):
        self.manager = manager

    def get_blocking_entities_at_location(self, destination_x, destination_y):
        """
        :type destination_x: int
        :type destination_y: int
        :return entity
        """
        for entity in self.manager.entities:
            if entity.blocks_movement and entity.x == destination_x and entity.y == destination_y:
                return entity

        return None

    def get_entity_in_fov_at_tile(self, target_tile):
        """
        Get the entity at a target tile

        Args:
            target_tile(tuple): x y of tile

        Returns:
            entity: Entity or None if no entity found
        """

        for entity in self.manager.entities:
            if entity.x == target_tile[0] and entity.y == target_tile[1]:
                from scripts.core.global_data import world_manager
                if world_manager.is_tile_in_fov(target_tile):
                    return entity

        return None

    def get_direction_between_entities(self, entity1, entity2):
        """
        get direction from an entity towards another entity's location
        :param self:
        :param entity1:
        :param entity2:
        """
        game_map = global_data.world_manager.game_map

        dx = entity2.x - entity1.x
        dy = entity2.y - entity1.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        tile_is_blocked = game_map.is_tile_blocking_movement(entity1.x + dx, entity1.y + dy)

        if not (tile_is_blocked or self.get_blocking_entities_at_location(entity1.x + dx, entity1.y + dy)):
            return dx, dy
        else:
            return entity1.x, entity1.y

    def distance_between_entities(self, entity1, entity2):
        dx = entity2.x - entity1.x
        dy = entity2.y - entity1.y
        return math.sqrt(dx ** 2 + dy ** 2)