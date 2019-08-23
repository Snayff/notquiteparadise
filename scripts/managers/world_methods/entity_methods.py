import logging
import math
import pygame
import tcod
import scipy.spatial

from scripts.components.actor import Actor
from scripts.components.combatant import Combatant
from scripts.components.homeland import Homeland
from scripts.components.race import Race
from scripts.components.savvy import Savvy
from scripts.core.constants import TILE_SIZE

from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.world.entity import Entity
from scripts.world.tile import Tile


class EntityMethods:
    """
    Queries relating to entities.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """
    def __init__(self, manager):
        from scripts.managers.world import WorldManager
        self.manager = manager  # type: WorldManager

    def get_blocking_entity_at_location(self, tile_x, tile_y):
        """

        Args:
            tile_x:
            tile_y:

        Returns:
            Entity: returns entity if there is one, else None.
        """
        tile = self.manager.Map.get_tile(tile_x, tile_y)
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
        tile = self.manager.Map.get_tile(tile_x, tile_y)
        entity = tile.entity

        if entity:
            if self.manager.FOV.is_tile_in_fov(tile_x, tile_y):
                return entity

        return None

    @staticmethod
    def get_euclidean_distance_between_entities(start_entity, target_entity):
        """
        get distance from an entity towards another entity`s location

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
    def get_chebyshev_distance_between_tiles(start_tile, end_tile):
        """
        get distance from a Tile towards another Tile`s location

        Args:
            start_tile (Tile):
            end_tile (Tile):

        Returns:
            int: distance in tiles

        """
        start_tile_position = [start_tile.x, start_tile.y]
        target_tile_position = [end_tile.x, end_tile.y]
        return scipy.spatial.distance.chebyshev(start_tile_position, target_tile_position)

    def get_direct_direction_between_entities(self, start_entity, target_entity):
        """
        get direction from an entity towards another entity`s location

        Args:
            start_entity (Entity):
            target_entity (Entity):

        """
        log_string = f"{start_entity.name} is looking for a direct path to {target_entity.name}."
        logging.debug(log_string)

        direction_x = target_entity.x - start_entity.x
        direction_y = target_entity.y - start_entity.y
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)

        direction_x = int(round(direction_x / distance))
        direction_y = int(round(direction_y / distance))

        tile_is_blocked = self.manager.Map.is_tile_blocking_movement(start_entity.x + direction_x,
                                                                                start_entity.y + direction_y)

        if not (tile_is_blocked or self.get_blocking_entity_at_location(start_entity.x + direction_x,
                                                                          start_entity.y + direction_y)):
            log_string = f"{start_entity.name} found a direct path to {target_entity.name}."
            logging.debug(log_string)

            return direction_x, direction_y
        else:
            log_string = f"{start_entity.name} did NOT find a direct path to {target_entity.name}."
            logging.debug(log_string)

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
        from scripts.global_singletons.managers import world_manager
        game_map = world_manager.game_map
        entities = world_manager.Entity.get_all_entities()
        entity_to_move = start_entity
        target = target_entity

        log_string = f"{entity_to_move.name} is looking for a path to {target.name} with a*"
        logging.debug(log_string)

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

        # Compute the path between self`s coordinates and the target`s coordinates
        tcod.path_compute(my_path, entity_to_move.x, entity_to_move.y, target.x, target.y)

        # Check if the path exists, and in this case, also the path is shorter than max_path_length
        # The path size matters if you want the monster to use alternative longer paths (for example through
        # other rooms) if for example the player is in a corridor
        # It makes sense to keep path size relatively low to keep the monsters from running around the map if
        # there`s an alternative path really far away
        if not tcod.path_is_empty(my_path) and tcod.path_size(my_path) < max_path_length:
            # Find the next coordinates in the computed full path
            x, y = tcod.path_walk(my_path, True)

            # convert to direction
            direction_x = x - entity_to_move.x
            direction_y = y - entity_to_move.y

            log_string = f"{entity_to_move.name} found an a* path to {target.name}..."
            log_string2 = f"-> will move from [{entity_to_move.x},{entity_to_move.y}] towards [{x},{y}] in direction "\
                f"[{direction_x},{direction_y}]"
            logging.debug(log_string)
            logging.debug( log_string2)

        else:
            # no path found return no movement direction
            direction_x, direction_y = 0, 0
            log_string = f"{entity_to_move.name} did NOT find an a* path to {target.name}."
            logging.debug(log_string)

        # Delete the path to free memory
        tcod.path_delete(my_path)
        return direction_x, direction_y

    def get_all_entities(self):
        """
        Get the list of all entities

        Returns:
            list: list of entities

        """
        return self.manager.entities

    def get_player(self):
        """
        Get the player.

        Returns:
            Entity
        """
        return self.manager.player

    def add_entity(self, tile_x, tile_y, entity):
        """
        Add entity to game map

        Args:
            tile_x:
            tile_y:
            entity:
        """
        self.manager.entities.append(entity)
        tile = self.manager.Map.get_tile(tile_x, tile_y)
        self.manager.Map.set_entity_on_tile(tile, entity)

    def add_player(self, tile_x, tile_y, entity):
        """

        Args:
            tile_x:
            tile_y:
            entity:
        """
        # TODO - fold into create actor, use player arg default to false
        self.manager.player = entity
        self.manager.Entity.add_entity(tile_x, tile_y, entity)

    def remove_entity(self, entity):
        """
        Remove entity from entities list and current tile.

        Args:
            entity:
        """
        # remove from tile
        tile = self.manager.Map.get_tile(entity.x, entity.y)
        self.manager.Map.remove_entity(tile)

        # remove from entities list
        self.manager.entities.remove(entity)

    def create_actor_entity(self, tile_x, tile_y, actor_name, player=False):
        """

        Args:
            tile_x:
            tile_y:
            actor_name:
            player (bool):
        """
        actor_template = library.get_actor_template_data(actor_name)

        actor_name = actor_template.name

        sprite = pygame.image.load("assets/actor/" + actor_template.spritesheet).convert_alpha()
        icon = pygame.image.load("assets/actor/" + actor_template.icon).convert_alpha()

        # catch any images not resized and resize them
        if icon.get_size() != (TILE_SIZE, TILE_SIZE):
            icon = pygame.transform.smoothscale(icon, (TILE_SIZE, TILE_SIZE))

        combatant_component = Combatant()
        savvy_component = Savvy(actor_template.savvy_component)
        homeland_component = Homeland(actor_template.homeland_component)
        race_component = Race(actor_template.race_component)
        actor_component = Actor()

        # get the AI value and convert to relevant class
        ai_value = actor_template.ai_component
        from scripts.components.ai import BasicMonster
        if ai_value == "basic_monster":
            ai_component = BasicMonster()
        else:
            ai_component = None

        # create the Entity
        actor = Entity(sprite, actor_name, blocks_movement=True, combatant=combatant_component, race=race_component,
                       savvy=savvy_component, homeland=homeland_component, ai=ai_component,
                       actor=actor_component, player=player, icon=icon)

        actor.combatant.hp = actor.combatant.secondary_stats.max_hp
        actor.combatant.stamina = actor.combatant.secondary_stats.max_stamina

        if player:
            self.add_player(tile_x, tile_y, actor)
        else:
            self.manager.Entity.add_entity(tile_x, tile_y, actor)

