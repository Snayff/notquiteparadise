import math
import random

import pygame

from scripts.components.actor import Actor
from scripts.components.adulthood import Adulthood
from scripts.components.combatant import Combatant
from scripts.components.youth import Youth
from scripts.core import global_data
from scripts.core.constants import TILE_SIZE, GAME_FPS, ENTITY_SPRITE_FRAME_DURATION
from scripts.data_loaders.getters import get_value_from_actor_json
from scripts.entities.entity import Entity


class EntityManager:
    def __init__(self):
        self.entities = []
        self.player = None

    def update(self, game_map):
        """
        Update all entity info that requires per frame changes

        Args:
            game_map (GameMap): The current game map
        """
        self.update_entity_sprites(game_map)

    def update_entity_sprites(self, game_map):
        """
        Loop all visible entities and update their sprites based on current sprite

        Args:
            game_map (GameMap): The current game map
        """
        # update entity sprites, if they're visible to player
        for entity in self.entities:
            if game_map.is_tile_visible(entity.x, entity.y):
                time_increment = 1 / GAME_FPS
                entity.delay_until_idle_animation -= time_increment

                #  if we aren't in the still sprite
                if entity.current_sprite_name != "still":

                    entity.animation_timer += time_increment

                    # is it time to move to a new frame?
                    if entity.animation_timer > ENTITY_SPRITE_FRAME_DURATION:

                        # reset the timer
                        entity.animation_timer = 0

                        # are we finished with the animation?
                        if entity.current_sprite_frame >= len(entity.current_sprite) - 1:

                            self.set_entity_current_sprite(entity, "still")
                        else:
                            entity.current_sprite_frame += 1

                # we are in still, so are we ready for idle?
                elif entity.delay_until_idle_animation <= 0:
                    self.set_entity_current_sprite(entity, "idle")

    def set_entity_current_sprite(self, entity, sprite_name):
        """
        Set the current sprite to the named one
        Args:
            entity (Entity): the entity to update the sprite on
            sprite_name (str): the name of the sprite
        """
        if entity.current_sprite_name != sprite_name:
            entity.current_sprite_frame = 0
            entity.current_sprite = entity.spritesheet.get(sprite_name)
            entity.current_sprite_name = sprite_name
            self.set_delay_on_idle_animation(entity)

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def add_player(self, entity):
        # TODO - fold into create actor, use player arg default to false
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

    def get_entity_in_fov_at_tile(self, target_tile):
        """
        Get the entity at a target tile

        Args:
            target_tile(tuple): x y of tile

        Returns:
            entity: Entity or None if no entity found
        """

        for entity in self.entities:
            if entity.x == target_tile[0] and entity.y == target_tile[1]:
                from scripts.core.global_data import world_manager
                if world_manager.is_tile_in_fov(target_tile):
                    return entity

        return None

    def create_actor_entity(self, x, y, actor_name):
        values = get_value_from_actor_json(actor_name)

        actor_name = values["name"]
        sprite = pygame.image.load("assets/actor/" + values["spritesheet"] + ".png").convert()
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

        tile_is_blocked = game_map.is_tile_blocking_movement(entity1.x + dx, entity1.y + dy)

        if not (tile_is_blocked or self.get_blocking_entities_at_location(entity1.x + dx, entity1.y + dy)):
            return dx, dy
        else:
            return entity1.x, entity1.y

    def distance_between_entities(self, entity1, entity2):
        dx = entity2.x - entity1.x
        dy = entity2.y - entity1.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def create_actor_sprite_dict(self, spritesheet_name):
        """
        Build a sprites dictionary for the actor. Spritesheet must be in assets/actor
        Args:
            spritesheet_name (str): name of actor's spritesheet

        Returns:
            Dict: Contains all sprites animations.
        """

        file_path = "assets/actor/"
        spritesheet = pygame.image.load(file_path + spritesheet_name + ".png").convert_alpha()

        # define start and end points for image strips
        still_image_info = (0, 0, 1)  # col, row, number of frames to get
        idle_image_info = (0, 1, 5)
        move_image_info = (0, 2, 5)
        attack_image_info = (0, 2, 5)

        sprite_dict = {}

        # TODO - change strings into enums
        sprite_dict["still"] = self.extract_images_from_spritesheet(spritesheet, still_image_info)
        sprite_dict["idle"] = self.extract_images_from_spritesheet(spritesheet, idle_image_info)
        sprite_dict["move"] = self.extract_images_from_spritesheet(spritesheet, move_image_info)
        sprite_dict["attack"] = self.extract_images_from_spritesheet(spritesheet, attack_image_info)

        return sprite_dict

    def extract_images_from_spritesheet(self, spritesheet, images_info):
        """
        Extract a set of images from a spritesheet into a list.

        Args:
            spritesheet (pygame.image):
            images_info(tuple):

        Returns:
            List: List of image strip frames
        """
        image_list = []

        starting_image_col = images_info[0]
        starting_image_row = images_info[1]
        number_of_sprites = images_info[2]

        for sprite in range(number_of_sprites):
            adjusted_image_col = (starting_image_col + sprite) * TILE_SIZE
            adjusted_image_row = starting_image_row * TILE_SIZE
            frame = spritesheet.subsurface(pygame.Rect(adjusted_image_col, adjusted_image_row, TILE_SIZE, TILE_SIZE))
            image_list.append(frame)

        return image_list

    def get_entity_current_frame(self, entity):
        """
        Get entity's current sprite frame

        Args:
            entity (Entity): The entity to get the frame from

        Returns:
            pygame.image: image of the current frame
        """
        sprite = entity.current_sprite
        frame = entity.current_sprite_frame

        return sprite[frame]

    def set_delay_on_idle_animation(self, entity):
        """
        Set new delay timer for idle animation

        Args:
            entity (Entity): the entity to get new delay
        """
        entity.delay_until_idle_animation = random.uniform(3.0, 5.0)  # add delay of 3 to 5 seconds