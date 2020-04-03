from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Tuple

from snecs.typedefs import EntityID

from scripts.engine import world, state
from scripts.engine.library import library
from scripts.engine.core.event_core import Subscriber, publisher
from scripts.engine.core.constants import EventTopic, GameState, MessageType, UIElement, Direction
from scripts.engine.component import Position, Aesthetic
from scripts.engine.event import MessageEvent, ClickTile, UseSkillEvent, DieEvent, MoveEvent, ChangeGameStateEvent, \
    WantToUseSkillEvent
from scripts.engine.ui.manager import ui

if TYPE_CHECKING:
    pass


class UIHandler(Subscriber):
    """
    Handle events that effect the UI. The UI handler watches and reacts.
    """

    def __init__(self, event_hub):
        super().__init__("ui_handler", event_hub)

    def process_event(self, event):
        """
        Control the events
        """
        if event.topic == EventTopic.UI:
            self._process_ui_event(event)
        elif event.topic == EventTopic.ENTITY:
            self._process_entity_event(event)
        elif event.topic == EventTopic.GAME:
            self._process_game_event(event)

    ############# HANDLE ENTITY EVENTS ##############

    def _process_entity_event(self, event):
        """
        Process entity topic event
        """
        if isinstance(event, DieEvent):
            # remove the entity from the camera
            self._update_camera(entity=event.entity)

        elif isinstance(event, MoveEvent):
            # show the entity in the new tile
            player = world.get_player()
            if event.entity == player:
                position = world.get_entitys_component(player, Position)
                self._update_camera(event.start_pos, (position.x, position.y), entity=event.entity)
            else:
                self._update_camera()

    ############# HANDLE GAME EVENTS ###############

    def _process_game_event(self, event):
        """
        Process game topic event
        """
        if isinstance(event, ChangeGameStateEvent):
            event: ChangeGameStateEvent
            if event.new_game_state == GameState.GAME_INITIALISING:
                self._init_game_ui()

            elif state.get_previous() == GameState.GAME_INITIALISING:
                # once everything is initialised present the welcome message
                ui.create_screen_message("Welcome to Not Quite Paradise", "", 6)

            elif event.new_game_state == GameState.TARGETING_MODE:
                # turn on targeting overlay
                self._set_targeting_overlay(True, event.skill_to_be_used)

            # check if we are moving to player turn and we are either in, or were just in, targeting
            # this is due to processing order of events
            elif event.new_game_state == GameState.PLAYER_TURN and (
                    state.get_current() == GameState.TARGETING_MODE or
                    state.get_previous() == GameState.TARGETING_MODE):

                # turn off the targeting overlay
                self._set_targeting_overlay(False)

            # new turn updates
            elif event.new_game_state == GameState.NEW_TURN:
                # TODO - reflect new turn info
                pass

            elif event.new_game_state == GameState.DEV_MODE:
                self._init_dev_ui()
                self._close_game_ui()

            elif state.get_previous() == GameState.DEV_MODE:
                self._close_dev_ui()
                self._init_game_ui()

    def _init_game_ui(self):
        """
        Initialise the UI elements
        """
        ui.init_camera()
        ui.init_skill_bar()
        ui.init_message_log()
        ui.init_entity_info()

        # Loop all entities with Position and Aesthetic and update their screen position
        for entity, (aesthetic, position) in world.get_components([Aesthetic, Position]):
            aesthetic.screen_x, aesthetic.screen_y = ui.world_to_screen_position((position.x, position.y))
            aesthetic.target_screen_x = aesthetic.screen_x
            aesthetic.target_screen_y = aesthetic.screen_y

        # update camera
        self._update_camera()

    @staticmethod
    def _close_game_ui():
        """
        Close all game ui_manager elements
        """
        ui.kill_element(UIElement.MESSAGE_LOG)
        ui.kill_element(UIElement.SKILL_BAR)
        ui.kill_element(UIElement.CAMERA)
        ui.kill_element(UIElement.ENTITY_INFO)

    @staticmethod
    def _init_dev_ui():
        """
        Initialise all dev mode widgets
        """
        ui.init_skill_editor()

    @staticmethod
    def _close_dev_ui():
        """
        Clear all dev mode elements
        """
        ui.kill_element(UIElement.DATA_EDITOR)

    ############# HANDLE UI EVENTS #################

    def _process_ui_event(self, event, entity=None):
        """
        Process UI topic event
        """
        if isinstance(event, ClickTile):
            game_state = state.get_current()
            tile = event.tile
            if game_state == GameState.PLAYER_TURN:
                # there should only be one entity, but just in case...
                for entity, (pos, ) in world.get_components([Position]):
                    if pos.x == tile.x and pos.y == tile.y:
                        self._select_entity(entity)
                        break

            elif game_state == GameState.TARGETING_MODE:
                # use the skill on the clicked tile
                player = world.get_player()
                position = world.get_entitys_component(player, Position)
                direction = world.get_direction((position.x, position.y), tile)
                skill_name = state.get_active_skill()
                publisher.publish(WantToUseSkillEvent(player, skill_name, (position.x, position.y), direction))

        elif isinstance(event, MessageEvent):
            # process a message
            self._process_message(event)

    @staticmethod
    def _set_targeting_overlay(is_visible: bool, skill_name: str = None):
        """
        Show or hide targeting overlay, using Direction possible in the skill.
        """
        # update directions to either clear or use info from skill
        if is_visible and skill_name:
            data = library.get_skill_data(skill_name)
            _directions = data.target_directions
        else:
            _directions = []

        # ensure all directions are of type Direction
        directions = []
        for direction in _directions:
            if not isinstance(direction, Direction):
                directions.append(getattr(Direction, direction.upper()))
            else:
                directions.append(direction)

        ui.set_overlay_directions(directions)
        ui.set_overlay_visibility(is_visible)
        ui.update_camera_grid()

    @staticmethod
    def _update_camera(start_pos: Tuple = None, target_pos: Tuple = None, entity: EntityID = None):
        """
        Update tiles shown in camera.
        """
        if start_pos and target_pos:
            should_move_camera = ui.should_camera_move(start_pos, target_pos)
            target_x, target_y = target_pos

            if should_move_camera:
                start_x, start_y = start_pos
                move_x = target_x - start_x
                move_y = target_y - start_y
                ui.move_camera(move_x, move_y)

            # update player's pos in camera
            if entity == world.get_player():
                target_tile = world.get_tile((target_x, target_y))
                ui.set_player_tile(target_tile)

        ui.update_cameras_tiles()
        ui.update_camera_game_map()
        ui.update_camera_grid()

    @staticmethod
    def _select_entity(entity: EntityID):
        """
        Set the selected entity
        """
        ui.set_selected_entity(entity)

    @staticmethod
    def _process_message(event: MessageEvent):
        """
        Process a message event
        """
        # TODO - grab all other message events in the current stack and join the messages for each type.
        #  TODO - Process message event last. Ensures they are as accurate as possible.

        if event.message_type == MessageType.LOG:
            ui.add_to_message_log(event.message)

        elif event.message_type == MessageType.SCREEN:
            ui.create_screen_message(event.message, event.colour, event.size)

        elif event.message_type == MessageType.ENTITY:
            # TODO - create message over entity
            #  can we reuse screen message but provide xy?
            pass


