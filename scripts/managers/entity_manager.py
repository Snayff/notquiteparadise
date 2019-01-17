import math

import pygame

from scripts.components.actor import Actor
from scripts.components.adulthood import Adulthood
from scripts.components.combatant import Combatant
from scripts.components.youth import Youth
from scripts.core import global_data
from scripts.data_loaders.getters import get_value_from_actor_json
from scripts.entities.entity import Entity


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

        tile_is_blocked = game_map.tile_is_blocking_movement(entity1.x + dx, entity1.y + dy)

        if not (tile_is_blocked or self.get_blocking_entities_at_location(entity1.x + dx, entity1.y + dy)):
            return dx, dy
        else:
            return entity1.x, entity1.y

    def distance_between_entities(self, entity1, entity2):
        dx = entity2.x - entity1.x
        dy = entity2.y - entity1.y
        return math.sqrt(dx ** 2 + dy ** 2)