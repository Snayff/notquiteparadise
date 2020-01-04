import logging
from typing import Tuple
from scripts.core.constants import EventTopics, GameEventTypes, GameStates, EntityEventTypes, \
    UIEventTypes
from scripts.core.library import library
from scripts.managers.ui_manager import ui
from scripts.managers.world_manager import world
from scripts.event_handlers.pub_sub_hub import Subscriber
from scripts.skills.skill import Skill
from scripts.world.entity import Entity


class UiHandler(Subscriber):
    """
    Handle events that effect the UI. The UI handler watches and reacts.
    """

    def __init__(self, event_hub):
        Subscriber.__init__(self, "ui_handler", event_hub)

    def process_event(self, event):
        """
        Control the events
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}...")

        if event.topic == EventTopics.UI:
            if event.event_type == UIEventTypes.CLICK_TILE:
                tile = world.Map.get_tile(event.tile_pos_string)
                entity = world.Map.get_entity_on_tile(tile)
                self.select_entity(entity)

        if event.topic == EventTopics.ENTITY:

            # update UI based on entity action taken
            if event.event_type == EntityEventTypes.LEARN:
                # TODO - update UI to reflect new skills
                pass

            elif event.event_type == EntityEventTypes.DIE:
                # remove the entity from the camera
                self.update_camera()

            elif event.event_type == EntityEventTypes.MOVE:
                # show the entity in the new tile
                player = world.Entity.get_player()
                if event.entity == player:
                    self.update_camera(event.start_pos, (player.x, player.y))
                else:
                    self.update_camera()

        if event.topic == EventTopics.GAME:
            if event.event_type == GameEventTypes.CHANGE_GAME_STATE:
                if event.new_game_state == GameStates.GAME_INITIALISING:
                    self.init_ui()

                elif event.new_game_state == GameStates.TARGETING_MODE:
                    # turn on targeting overlay
                    self.set_targeting_overlay(True, event.skill_to_be_used)

                # new turn updates
                elif event.new_game_state == GameStates.NEW_TURN:
                    # TODO - reflect new turn info
                    pass

    @staticmethod
    def set_targeting_overlay(is_visible: bool, skill: Skill = None):
        """
        Show or hide targeting overlay, using Directions possible in the skill.

        Args:
            is_visible ():
            skill ():
        """
        # update directions to either clear or use info from skill
        if is_visible:
            data = library.get_skill_data(skill.skill_tree_name, skill.name)
            directions = data.target_directions
        else:
            directions = []

        ui.Element.set_overlay_directions(directions)
        ui.Element.set_overlay_visibility(is_visible)
        ui.Element.update_camera_grid()

    @staticmethod
    def update_camera(start_pos: Tuple = None, target_pos: Tuple = None):
        """
        Update tiles shown in camera.

        Args:
            start_pos ():
            target_pos ():
        """
        if target_pos:
            should_move_camera = ui.Element.should_camera_move(start_pos, target_pos)
            target_x, target_y = target_pos

            if should_move_camera:
                start_x, start_y = start_pos
                move_x = target_x - start_x
                move_y = target_y - start_y
                ui.Element.move_camera(move_x, move_y)

            # update player's pos in camera
            tile = world.Map.get_tile((target_x, target_y))
            ui.Element.set_player_tile(tile)

        ui.Element.update_cameras_tiles()
        ui.Element.update_camera_game_map()
        ui.Element.update_camera_grid()

    def init_ui(self):
        """
        Initialise the UI elements
        """
        ui.Element.init_camera()
        ui.Element.init_skill_bar()
        ui.Element.init_message_log()
        ui.Element.init_entity_info()

        # update camera
        self.update_camera()

    @staticmethod
    def select_entity(entity: Entity):
        """
        Set the selected entity

        Args:
            entity ():
        """
        ui.Element.set_selected_entity(entity)