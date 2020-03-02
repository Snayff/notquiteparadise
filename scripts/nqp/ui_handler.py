from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Tuple

from scripts.engine.state import get_current
from scripts.engine.library import library



from scripts.engine.core.event_core import Subscriber, publisher
from scripts.engine.core.constants import EventTopics, GameStates, MessageTypes, UIElementTypes
from scripts.engine.component import Position, Aesthetic
from scripts.engine.event import MessageEvent, ClickTile, UseSkillEvent, DieEvent, MoveEvent, ChangeGameStateEvent

if TYPE_CHECKING:
    pass


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
        logging.debug(f"{self.name} received {event.topic}:{event.__class__.__name__}...")

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
        if isinstance(event, DieEvent):
            event: DieEvent
            # remove the entity from the camera
            self.update_camera()

        elif isinstance(event, MoveEvent):
            event: MoveEvent
            # show the entity in the new tile
            player = world.Entity.get_player()
            if event.entity == player:
                position = world.Entity.get_entitys_component(player, Position)
                self.update_camera(event.start_pos, (position.x, position.y))
            else:
                self.update_camera()

    ############# HANDLE GAME EVENTS ###############

    def process_game_event(self, event):
        """
        Process Game topic event
        """
        if isinstance(event, ChangeGameStateEvent):
            event: ChangeGameStateEvent
            if event.new_game_state == GameStates.GAME_INITIALISING:
                self.init_game_ui()

            elif game.State.get_previous() == GameStates.GAME_INITIALISING:
                # once everything is initialised present the welcome message
                ui_manager.Element.create_screen_message("Welcome to Not Quite Paradise", "", 6)

            elif event.new_game_state == GameStates.TARGETING_MODE:
                # turn on targeting overlay
                self.set_targeting_overlay(True, event.skill_to_be_used)

            # check if we are moving to player turn and we are either in, or were just in, targeting
            # this is due to processing order of events
            elif event.new_game_state == GameStates.PLAYER_TURN and (
                    get_current(game.State._current_game_state) == GameStates.TARGETING_MODE or
                    game.State.get_previous() == GameStates.TARGETING_MODE):

                # turn off the targeting overlay
                self.set_targeting_overlay(False)

            # new turn updates
            elif event.new_game_state == GameStates.NEW_TURN:
                # TODO - reflect new turn info
                pass

            elif event.new_game_state == GameStates.DEV_MODE:
                self.init_dev_ui()
                self.close_game_ui()

            elif game.State.get_previous() == GameStates.DEV_MODE:
                self.close_dev_ui()
                self.init_game_ui()

    def init_game_ui(self):
        """
        Initialise the UI elements
        """
        ui_manager.Element.init_camera()
        ui_manager.Element.init_skill_bar()
        ui_manager.Element.init_message_log()
        ui_manager.Element.init_entity_info()

        # Loop all entities with Position and Aesthetic and update their screen position
        for entity, (aesthetic, position) in world.Entity.get_components(Aesthetic, Position):
            aesthetic.screen_x, aesthetic.screen_y = ui_manager.Element.world_to_screen_position((position.x, position.y))
            aesthetic.target_screen_x = aesthetic.screen_x
            aesthetic.target_screen_y = aesthetic.screen_y

        # update camera
        self.update_camera()

    @staticmethod
    def close_game_ui():
        """
        Close all game ui_manager elements
        """
        ui_manager.Element.kill_element(UIElementTypes.MESSAGE_LOG)
        ui_manager.Element.kill_element(UIElementTypes.SKILL_BAR)
        ui_manager.Element.kill_element(UIElementTypes.CAMERA)
        ui_manager.Element.kill_element(UIElementTypes.ENTITY_INFO)

    @staticmethod
    def init_dev_ui():
        """
        Initialise all dev mode widgets
        """
        ui_manager.Element.init_skill_editor()

    @staticmethod
    def close_dev_ui():
        """
        Clear all dev mode elements
        """
        ui_manager.Element.kill_element(UIElementTypes.DATA_EDITOR)

    ############# HANDLE UI EVENTS #################

    def process_ui_event(self, event):
        """
        Process UI topic event
        """
        if isinstance(event, ClickTile):
            event: ClickTile
            if get_current(game.State._current_game_state) == GameStates.PLAYER_TURN:

                # Select an entity
                tile = world.Map.get_tile(event.tile_pos_string)

                # ensure there is a tile
                if tile:
                    entities = world.Entity.get_entities_and_components_in_area([tile])
                else:
                    entities = []

                # there should only be one entity, but just in case...
                for entity in entities:
                    self.select_entity(entity)
                    break
            elif get_current(game.State._current_game_state) == GameStates.TARGETING_MODE:
                # use the skill on the clicked tile
                player = world.Entity.get_player()
                position = world.Entity.get_entitys_component(player, Position)
                direction = world.Map.get_direction((position.x, position.y), event.tile_pos_string)
                publisher.publish(UseSkillEvent(player, game.State.get_active_skill(), (position.x, position.y), direction))

        if isinstance(event, MessageEvent):
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

        ui_manager.Element.set_overlay_directions(directions)
        ui_manager.Element.set_overlay_visibility(is_visible)
        ui_manager.Element.update_camera_grid()

    @staticmethod
    def update_camera(start_pos: Tuple = None, target_pos: Tuple = None):
        """
        Update tiles shown in camera.
        """
        if target_pos:
            should_move_camera = ui_manager.Element.should_camera_move(start_pos, target_pos)
            target_x, target_y = target_pos

            if should_move_camera:
                start_x, start_y = start_pos
                move_x = target_x - start_x
                move_y = target_y - start_y
                ui_manager.Element.move_camera(move_x, move_y)

            # update player's pos in camera
            tile = world.Map.get_tile((target_x, target_y))
            ui_manager.Element.set_player_tile(tile)

        ui_manager.Element.update_cameras_tiles()
        ui_manager.Element.update_camera_game_map()
        ui_manager.Element.update_camera_grid()

    @staticmethod
    def select_entity(entity: int):
        """
        Set the selected entity

        Args:
            entity ():
        """
        ui_manager.Element.set_selected_entity(entity)

    @staticmethod
    def process_message(event: MessageEvent):
        """
        Process a message event

        Args:
            event ():
        """
        if event.message_type == MessageTypes.LOG:
            ui_manager.Element.add_to_message_log(event.message)

        elif event.message_type == MessageTypes.SCREEN:
            ui_manager.Element.create_screen_message(event.message, event.colour, event.size)

        elif event.message_type == MessageTypes.ENTITY:
            # TODO - create message over entity
            #  can we reuse screen message but provide xy?
            pass


