from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Tuple
from scripts.core.library import library
from scripts.events.entity_events import UseSkillEvent
from scripts.managers.game_manager import game
from scripts.managers.ui_manager import ui
from scripts.managers.world_manager import world
from scripts.core.event_hub import Subscriber, publisher
from scripts.core.constants import EventTopics, GameEventTypes, GameStates, EntityEventTypes, \
    UIEventTypes, MessageTypes, VisualInfo
from scripts.world.components import Position

if TYPE_CHECKING:
    from scripts.world.entity import Entity
    from scripts.events.ui_events import MessageEvent


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
            self.process_ui_event(event)

        if event.topic == EventTopics.ENTITY:
            self.process_entity_event(event)

        if event.topic == EventTopics.GAME:
            self.process_game_event(event)

    ############# HANDLE ENTITY EVENTS ##############

    def process_entity_event(self, event):
        """
        Process entity topic event

        Args:
            event ():
        """
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
                position = world.Entity.get_component(player, Position)
                self.update_camera(event.start_pos, (position.x, position.y))
            else:
                self.update_camera()

    ############# HANDLE GAME EVENTS ###############

    def process_game_event(self, event):
        """
        Process Game topic event

        Args:
            event ():
        """
        if event.event_type == GameEventTypes.CHANGE_GAME_STATE:
            if event.new_game_state == GameStates.GAME_INITIALISING:
                self.init_ui()

            elif game.previous_game_state == GameStates.GAME_INITIALISING:
                # once everything is initialised present the welcome message
                ui.Element.create_screen_message("Welcome to Not Quite Paradise", "", 6)

            elif event.new_game_state == GameStates.TARGETING_MODE:
                # turn on targeting overlay
                self.set_targeting_overlay(True, event.skill_to_be_used)

            # check if we are moving to player turn and we are either in, or were just in, targeting
            # this is due to processing order of events
            elif event.new_game_state == GameStates.PLAYER_TURN and (game.game_state == GameStates.TARGETING_MODE or
                game.previous_game_state == GameStates.TARGETING_MODE):

                # turn off the targeting overlay
                self.set_targeting_overlay(False)

            # new turn updates
            elif event.new_game_state == GameStates.NEW_TURN:
                # TODO - reflect new turn info
                pass

            elif event.new_game_state == GameStates.DEV_MODE:
                self.init_dev_mode()

            elif game.previous_game_state == GameStates.DEV_MODE:
                self.exit_dev_mode()

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
    def init_dev_mode():
        """
        Initialise all dev mode widgets
        """
        ui.Element.init_skill_editor()

    @staticmethod
    def exit_dev_mode():
        """
        Clear all dev mode widgets
        """
        ui.Element.kill_skill_editor()

    ############# HANDLE UI EVENTS #################

    def process_ui_event(self, event):
        """
        Process UI topic event

        Args:
            event ():
        """
        if event.event_type == UIEventTypes.CLICK_TILE:
            if game.game_state == GameStates.PLAYER_TURN:
                # Select an entity
                tile = world.Map.get_tile(event.tile_pos_string)
                entities = world.Entity.get_entities_and_components_in_area([tile])

                # there should only be one entity, but just in case...
                for entity in entities:
                    self.select_entity(entity)
                    break
            elif game.game_state == GameStates.TARGETING_MODE:
                # use the skill on the clicked tile
                player = world.Entity.get_player()
                position = world.Entity.get_component(player, Position)
                direction = world.Map.get_direction((position.x, position.y), event.tile_pos_string)
                publisher.publish(UseSkillEvent(player, game.active_skill, (position.x, position.y), direction))

        if event.event_type == UIEventTypes.MESSAGE:
            # process a message
            event: MessageEvent
            self.process_message(event)

    @staticmethod
    def set_targeting_overlay(is_visible: bool, skill_name: str = None):
        """
        Show or hide targeting overlay, using Directions possible in the skill.

        Args:
            skill_name ():
            is_visible ():
        """
        # update directions to either clear or use info from skill
        if is_visible:
            data = library.get_skill_data(skill_name)
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

    @staticmethod
    def select_entity(entity: Entity):
        """
        Set the selected entity

        Args:
            entity ():
        """
        ui.Element.set_selected_entity(entity)

    @staticmethod
    def process_message(event: MessageEvent):
        """
        Process a message event

        Args:
            event ():
        """
        if event.message_type == MessageTypes.LOG:
            ui.Element.add_to_message_log(event.message)

        elif event.message_type == MessageTypes.SCREEN:
            ui.Element.create_screen_message(event.message, event.colour, event.size)

        elif event.message_type == MessageTypes.ENTITY:
            # TODO - create message over entity
            #  can we reuse screen message but provide xy?
            pass


