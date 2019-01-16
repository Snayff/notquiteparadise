import math
import tcod

from scripts.core import global_data



class Entity:
    """ A generic object to represent players, enemies, items, etc. """

    def __init__(self, x, y, sprite, name, blocks_movement=False, blocks_sight=False,
            living=False, race=None, youth=None, adulthood=None, ai=None, ):

        # item=None, inventory=None, stairs=None, level=None, equipment=None, equippable=None, sight_range=None
        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name
        self.blocks_movement = blocks_movement
        self.blocks_sight = blocks_sight
        self.time_of_next_action = 0
        # self.sight_range = sight_range

        # components
        self.race = race
        self.living = living
        self.youth = youth
        self.adulthood = adulthood
        self.ai = ai
        # self.item = item
        # self.inventory = inventory
        # self.stairs = stairs
        # self.level = level
        # self.equipment = equipment
        # self.equippable = equippable

        # Create owners so all components can refer to the owning entity
        if self.living:
            self.living.owner = self

        if self.race:
            self.race.owner = self

        if self.youth:
            self.youth.owner = self

        if self.adulthood:
            self.adulthood.owner = self

        if self.ai:
            self.ai.owner = self

    # if self.item:
    # 	self.item.owner = self
    #
    # if self.inventory:
    # 	self.inventory.owner = self
    #
    # if self.stairs:
    # 	self.stairs.owner = self
    #
    # if self.level:
    # 	self.level.owner = self
    #
    # if self.equipment:
    # 	self.equipment.owner = self
    #
    # if self.equippable:
    # 	self.equippable.owner = self
    #
    # 	if not self.item:
    # 		item = Item()
    # 		self.item = item
    # 		self.item.owner = self

    def move(self, dx, dy):
        # Move the entity to a specified tile
        self.x = dx
        self.y = dy

    def spend_time(self, time_spent):
        self.time_of_next_action += time_spent

    def get_nearest_position_towards_target_direct(self, target_x, target_y):
        """
        move an entity towards a specified location
        :param self:
        :param target_x:
        :param target_y:
        """
        game_map = global_data.world_manager.game_map

        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        tile_is_blocked = game_map[self.x + dx][self.y + dy].blocks_movement

        from scripts.core.global_data import entity_manager

        if not (tile_is_blocked or entity_manager.get_blocking_entities_at_location(self.x + dx, self.y + dy)):
            return dx, dy
        else:
            return self.x, self.y

    def distance(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def get_nearest_position_towards_target_astar(self, target):
        entities = global_data.entity_manager.entities
        game_map = global_data.world_manager.game_map
        game_map_width = len(game_map)
        game_map_height = len(game_map[0])


        # Create a FOV map that has the dimensions of the map
        fov = tcod.map_new(game_map_height, game_map_width)

        # Scan the current map each turn and set all the walls as unwalkable
        for y1 in range(game_map_height):
            for x1 in range(game_map_width):
                tcod.map_set_properties(fov, x1, y1, not game_map[x1][y1].blocks_sight,
                                        not game_map[x1][y1].blocks_movement)

        # Scan all the objects to see if there are objects that must be navigated around
        # Check also that the object isn't self or the target (so that the start and the end points are free)
        # The AI class handles the situation if self is next to the target so it will not use this A* function anyway
        for entity in entities:
            if entity.blocks_movement and entity != self and entity != target:
                # Set the tile as a wall so it must be navigated around
                tcod.map_set_properties(fov, entity.x, entity.y, True, False)

        # Allocate a A* path
        # The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited
        my_path = tcod.path_new_using_map(fov, 1.41)

        # Compute the path between self's coordinates and the target's coordinates
        tcod.path_compute(my_path, self.x, self.y, target.x, target.y)

        # Check if the path exists, and in this case, also the path is shorter than 25 tiles
        # The path size matters if you want the monster to use alternative longer paths (for example through other
        # rooms) if for example the player is in a corridor. It makes sense to keep path size relatively low to keep
        # the monsters from running around the map if there's an alternative path really far away
        if not tcod.path_is_empty(my_path) and tcod.path_size(my_path) < 25:
            # Find the next coordinates in the computed full path
            dx, dy = tcod.path_walk(my_path, True)

        else:
            # Keep the old move function as a backup so that if there are no paths  (for example another monster
            # blocks a corridor)it will still try to move towards the player (closer to the corridor opening)
            dx, dy = self.get_nearest_position_towards_target_direct(target.x, target.y)

        # Delete the path to free memory
        tcod.path_delete(my_path)

        return dx, dy
