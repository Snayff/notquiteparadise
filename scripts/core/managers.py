import math

import pygame

from scripts.components.actor import Actor
from scripts.components.adulthood import Adulthood
from scripts.components.combatant import Combatant
from scripts.components.youth import Youth
from scripts.core import global_data
from scripts.core.constants import GameStates, LoggingEventNames, EventTopics
from scripts.core.events import Publisher, Event, EventHub
from scripts.data_loaders.getters import get_value_from_actor_json
from scripts.entities.entity import Entity
from scripts.world.tiles import Floor, Wall


class EntityManager:
    def __init__(self):
        self.entities = []
        self.player = None

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def add_player(self, entity):
        self.player = entity
        self.add_entity(entity)

    def get_blocking_entities_at_location(self, destination_x, destination_y):
        """
        :type destination_x: int
        :type destination_y: int
        :return entity
        """
        for entity in self.entities:
            if entity.blocks_movement and entity.x == destination_x and entity.y == destination_y:
                return entity

        return None

    def create_actor(self, x, y, actor_name):
        values = get_value_from_actor_json(actor_name)

        actor_name = values["name"]
        sprite = pygame.image.load("assets/actor/" + values["sprite"] + ".png")
        combatant_component = Combatant()
        youth_component = Youth(values["youth_component"])
        adulthood_component = Adulthood(values["adulthood_component"])
        actor_component = Actor()

        ai_value = values["ai_component"]

        from scripts.components.ai import BasicMonster
        if ai_value == "basic_monster":
            ai_component = BasicMonster()
        else:
            ai_component = None

        actor = Entity(x, y, sprite, actor_name, blocks_movement=True, combatant=combatant_component,
                       youth=youth_component, adulthood=adulthood_component, ai=ai_component, actor=actor_component)

        actor.combatant.hp = actor.combatant.max_hp

        self.add_entity(actor)

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

        tile_is_blocked = game_map[entity1.x + dx][entity1.y + dy].blocks_movement

        if not (tile_is_blocked or self.get_blocking_entities_at_location(entity1.x + dx, entity1.y + dy)):
            return dx, dy
        else:
            return entity1.x, entity1.y

    def distance_between_entities(self, entity1, entity2):
        dx = entity2.x - entity1.x
        dy = entity2.y - entity1.y
        return math.sqrt(dx ** 2 + dy ** 2)


class WorldManager:
    def __init__(self):
        self.game_map = []
        self.fov_map = None
        self.player_fov_is_dirty = False
        self.light_walls = True
        self.fov_algorithm = 0
    # TODO create game map class:
    #  To contain map tiles, fov map

    def create_new_map(self):
        """
        create a new game map
        """

        # get map size
        map_width = 40  # TODO abstract  magic numbers
        map_height = 32

        # populate map with floor tiles # N.B. the inner list should be the height
        # which would mean that the first referenced index in list[][] is y. Stop getting it wrong.
        self.game_map = [[Floor() for y in range(0, map_height)] for x in range(0, map_width)]

        self.game_map[0][5] = Wall()  # TODO remove - only for test
        self.game_map[10][2] = Wall()


# def create_fov_map(self):
#
# 	self.fov_map = tcod.map_new(self.game_map.width, self.game_map.height)
#
# 	for y in range(self.game_map.height):
# 		for x in range(self.game_map.width):
# 			tcod.map_set_properties(self.fov_map, x, y, not self.game_map.tiles[x][y].block_sight,
# 				not self.game_map.tiles[x][y].blocked)
#
# 	self.player_fov_is_dirty = True

# def recompute_fov(self, x, y, radius):
# 	tcod.map_compute_fov(self.fov_map, x, y, radius, self.light_walls, self.fov_algorithm)


class UIManager:
    """
    Manage the UI, such as windows, resource bars etc
    """

    def __init__(self):
        self.focused_window = None


class TurnManager:
    # TODO What do we need from the turn queue?
    #  Add all entities that are within X range of the player;
    #  Add new entities to the queue as they get into range;
    #  Amend an entities position in the queue;
    #  Keep track of rounds;

    def __init__(self):
        self.turn_holder = None
        self.turn_queue = []  # queue stores a tuple of the entity and their time to next action
        self.round = 0
        self.time = 0
        self.time_of_last_turn = 0

    def build_new_turn_queue(self):
        from scripts.core.global_data import game_manager, entity_manager
        log_string = f"Building a new turn queue."
        game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))

        # create a turn queue from the entities list
        for entity in entity_manager.entities:
            if entity.ai or entity == entity_manager.player:
                self.turn_queue.append((entity, entity.actor.time_of_next_action))

        # sort the queue
        self.turn_queue.sort(key=lambda x: x[1])

        # get the next entity in the queue
        self.turn_holder = self.turn_queue.pop(0)[0]

    def end_turn(self, spent_time):
        from scripts.core.global_data import game_manager
        entity = self.turn_holder

        log_string = f"Ending {entity.name}'s turn."
        game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))

        #  update actor's time spent
        entity.actor.spend_time(spent_time)

        self.next_turn()

    def next_turn(self):
        from scripts.core.global_data import game_manager

        if not self.turn_queue:
            self.build_new_turn_queue()

        # add current turn holder back into queue
        self.turn_queue.append((self.turn_holder, self.turn_holder.actor.time_of_next_action))

        # sort the queue so the next to act is top
        self.turn_queue.sort(key=lambda x: x[1])

        # get the next entity in the queue
        self.turn_holder = self.turn_queue.pop(0)[0]

        # update time using last action and when new turn holder can act
        self.time += self.turn_holder.actor.time_of_next_action - self.time_of_last_turn
        self.time_of_last_turn = self.time

        # if turn holder is the player then update to player turn
        if self.turn_holder == global_data.entity_manager.player:
            game_manager.update_game_state(GameStates.PLAYER_TURN)
        # if turn holder is not player and we aren't already in enemy turn then update to enemy turn
        elif game_manager.game_state != GameStates.ENEMY_TURN:
            game_manager.update_game_state(GameStates.ENEMY_TURN)

        log_string = f"It is now {self.turn_holder.name}'s turn."
        game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))


class GameManager:

    def __init__(self):
        self.game_state = GameStates.GAME_INITIALISING
        self.previous_game_state = GameStates.GAME_INITIALISING
       # self.message_log = None
        self.event_hub = EventHub()

    # def new_message_log(self, message_log):
    #     """
    #     :type message_log: MessageLog
    #     """
    #     self.message_log = message_log

    def update_game_state(self, new_game_state):
        """
        :type new_game_state: Code.Core.constants.GameStates
        """
        self.previous_game_state = self.game_state
        self.game_state = new_game_state

        log_string = f"game_state updated to {self.game_state} from {self.previous_game_state}"
        self.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING, [log_string]))

    def create_event(self, event):
        pub = Publisher(self.event_hub)
        pub.publish(event)
