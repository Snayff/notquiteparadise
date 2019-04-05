import pygame

from scripts.components.actor import Actor
from scripts.components.adulthood import Adulthood
from scripts.components.combatant import Combatant
from scripts.components.player import Player
from scripts.components.youth import Youth
from scripts.core.constants import TILE_SIZE
from scripts.data_loaders.getters import get_value_from_actor_json
from scripts.core.entity import Entity

class EntityExistenceAmendment:
    def __init__(self, manager):
        self.manager = manager

    def add_entity(self, entity):
        self.manager.entities.append(entity)

    def add_player(self, entity):
        # TODO - fold into create actor, use player arg default to false
        self.manager.player = entity
        self.add_entity(entity)

    def remove_entity(self, entity):
        self.manager.entities.remove(entity)

    def create_actor_entity(self, x, y, actor_name):
        values = get_value_from_actor_json(actor_name)

        actor_name = values["name"]

        sprite = pygame.image.load("assets/actor/" + values["spritesheet"]).convert_alpha()
        # catch any images not resized and resize them
        if sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            sprite = pygame.transform.scale(sprite, (TILE_SIZE, TILE_SIZE))

        combatant_component = Combatant()
        youth_component = Youth(values["youth_component"])
        adulthood_component = Adulthood(values["adulthood_component"])
        actor_component = Actor()
        sight_range = values["sight_range"]

        # get then player value and convert to class if needed
        player_value = values["player_component"]
        if player_value:
            player = Player()
        else:
            player = None

        # get the AI value and convert to relevant class
        ai_value = values["ai_component"]
        from scripts.components.ai import BasicMonster
        if ai_value == "basic_monster":
            ai_component = BasicMonster()
        else:
            ai_component = None

        actor = Entity(x, y, sprite, actor_name, blocks_movement=True, combatant=combatant_component,
                       youth=youth_component, adulthood=adulthood_component, ai=ai_component,
                       actor=actor_component, sight_range=sight_range, player=player)

        actor.combatant.hp = actor.combatant.max_hp

        if player:
            self.add_player(actor)
        else:
            self.add_entity(actor)