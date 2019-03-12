import random
import pygame

from scripts.core.constants import TILE_SIZE, GAME_FPS, ENTITY_SPRITE_FRAME_DURATION

class EntityAnimation:
    def __init__(self, manager):
        self.manager = manager

    def update_entity_sprites(self, game_map):
        """
        Loop all visible entities and update their sprites based on current sprite

        Args:
            game_map (GameMap): The current game map
        """
        # update entity sprites, if they're visible to player
        for entity in self.manager.entities:
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

                            self. set_entity_current_sprite(entity, "still")
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

    def set_delay_on_idle_animation(self, entity):
        """
        Set new delay timer for idle animation

        Args:
            entity (Entity): the entity to get new delay
        """
        entity.delay_until_idle_animation = random.uniform(3.0, 5.0)  # add delay of 3 to 5 seconds

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
            frame = spritesheet.subsurface(
                pygame.Rect(adjusted_image_col, adjusted_image_row, TILE_SIZE, TILE_SIZE))
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