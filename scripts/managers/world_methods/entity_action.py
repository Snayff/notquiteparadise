import pygame

from scripts.components.actor import Actor
from scripts.components.homeland import Homeland
from scripts.components.combatant import Combatant
from scripts.components.player import Player
from scripts.components.trade import Trade
from scripts.core.constants import TILE_SIZE
from scripts.data_loaders.getters import get_value_from_actor_json
from scripts.world.entity import Entity


class EntityAction:
    """
    Entity existence related methods and info.

    Attributes:
        manager(WorldManager): the containing manager
        entities(List): list of entities
    """
    def __init__(self, manager):
        self.manager = manager

    def add_entity(self, tile_x, tile_y, entity):
        """

        Args:
            tile_x:
            tile_y:
            entity:
        """
        self.manager.entities.append(entity)
        tile = self.manager.game_map.get_tile(tile_x, tile_y)
        tile.set_entity(entity)

    def add_player(self, tile_x, tile_y, entity):
        """

        Args:
            tile_x:
            tile_y:
            entity:
        """
        # TODO - fold into create actor, use player arg default to false
        self.manager.player = entity
        self.add_entity(tile_x, tile_y, entity)

    def remove_entity(self, entity):
        """
        Remove entity from entities list and current tile.

        Args:
            entity:
        """
        # remove from tile
        tile = self.manager.game_map.get_tile(entity.x, entity.y)
        tile.remove_entity()

        # remove from entities list
        self.manager.entities.remove(entity)

    def create_actor_entity(self, tile_x, tile_y, actor_name):
        """

        Args:
            tile_x:
            tile_y:
            actor_name:
        """
        values = get_value_from_actor_json(actor_name)

        actor_name = values["name"]

        sprite = pygame.image.load("assets/actor/" + values["spritesheet"]).convert_alpha()
        icon = pygame.image.load("assets/actor/" + values["icon"]).convert_alpha()

        # catch any images not resized and resize them
        if icon.get_size() != (TILE_SIZE, TILE_SIZE):
            icon = pygame.transform.smoothscale(icon, (TILE_SIZE, TILE_SIZE))

        combatant_component = Combatant()
        youth_component = Trade(values["trade_component"])
        adulthood_component = Homeland(values["homeland_component"])
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

        # create the Entity
        actor = Entity(sprite, actor_name, blocks_movement=True, combatant=combatant_component,
                       trade=youth_component, homeland=adulthood_component, ai=ai_component,
                       actor=actor_component, sight_range=sight_range, player=player, icon=icon)

        actor.combatant.hp = actor.combatant.secondary_stats.max_hp

        if player:
            self.add_player(tile_x, tile_y, actor)
        else:
            self.add_entity(tile_x, tile_y, actor)
