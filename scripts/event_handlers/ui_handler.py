import logging
from typing import Tuple

from scripts.core.constants import EventTopics, GameEventTypes, GameStates, EntityEventTypes, \
    UIEventTypes, TILE_SIZE, MessageEventTypes, UIElementTypes
from scripts.events.entity_events import UseSkillEvent
from scripts.events.game_events import ChangeGameStateEvent
from scripts.events.message_events import MessageEvent
from scripts.core.event_hub import publisher
from scripts.managers.ui_manager import ui
from scripts.managers.world_manager import world
from scripts.managers.game_manager import game
from scripts.event_handlers.pub_sub_hub import Subscriber


class UiHandler(Subscriber):
    """
    Handle events that effect the UI. The UI handler watches and reacts.
    """

    def __init__(self, event_hub):
        Subscriber.__init__(self, "ui_handler", event_hub)

    def run(self, event):
        """
        Process the events
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}...")

        if event.topic == EventTopics.UI:
            if event.event_type == UIEventTypes.CLICK_UI:
                button = event.button_pressed
                mouse_x = event.mouse_x
                mouse_y = event.mouse_y
                clicked_element = ui.Mouse.get_colliding_ui_element_type(mouse_x, mouse_y)
                game_state = game.game_state

                # Selecting an entity
                # TODO - move to camera.handle_input
                # if button == MouseButtons.RIGHT_BUTTON and clicked_element == UIElementTypes.CAMERA:
                #     self.attempt_to_set_selected_entity(mouse_x, mouse_y)
                #
                # # Selecting a skill
                # TODO - move to skill_bar.handle_input
                # # elif button == MouseButtons.LEFT_BUTTON and clicked_element == UIElementTypes.SKILL_BAR:
                # #     self.attempt_to_trigger_targeting_mode(mouse_x, mouse_y)
                #
                # # using a selected skill
                # TODO - move to camera.handle_input
                # elif button == MouseButtons.LEFT_BUTTON and clicked_element == UIElementTypes.CAMERA and game_state \
                #         == GameStates.TARGETING_MODE:
                #     self.attempt_to_use_targeted_skill()

                # NEW APPROACH - remove once all migrated  ############
                # pass input to element
                if clicked_element == UIElementTypes.MESSAGE_LOG:
                    ui_element = ui.Element.get_ui_element(clicked_element)
                    ui_element.handle_input(button)
                elif clicked_element == UIElementTypes.SKILL_BAR:
                    ui_element = ui.Element.get_ui_element(clicked_element)
                    ui_element.handle_input(button)

        if event.topic == EventTopics.ENTITY:

            # if an entity acts then hide the entity info element
            ui.Element.set_element_visibility(UIElementTypes.ENTITY_INFO, False)

            # update UI based on entity action taken
            if event.event_type == EntityEventTypes.LEARN:
                ui.Element.update_skill_bars_icons()
            elif event.event_type == EntityEventTypes.DIE:
                ui.Element.update_entity_queue()
                self.update_camera()
            elif event.event_type == EntityEventTypes.MOVE:
                if event.entity == world.Entity.get_player():
                    self.update_camera(event.start_pos, event.target_pos)
                else:
                    self.update_camera()

        if event.topic == EventTopics.GAME:
            if event.event_type == GameEventTypes.CHANGE_GAME_STATE:

                if event.new_game_state == GameStates.GAME_INITIALISING:
                    self.init_ui()

                # if changing to targeting mode then turn on targeting overlay
                elif event.new_game_state == GameStates.TARGETING_MODE:
                    self.trigger_targeting_overlay_and_entity_info(event.skill_to_be_used)

                # new turn updates
                elif event.new_game_state == GameStates.NEW_TURN:
                    ui.Element.update_entity_queue()

                # if the previous game state was targeting mode we must be moving to something else, therefore the
                # overlay is no longer needed
                if game.previous_game_state == GameStates.TARGETING_MODE:
                    ui.Element.set_element_visibility(UIElementTypes.TARGETING_OVERLAY, False)

    @staticmethod
    def attempt_to_set_selected_entity(mouse_x, mouse_y):
        """
        Check if clicked location includes an entity and if so set it as selected to display its info.

        Args:
            mouse_x (int):
            mouse_y (int):
        """
        tile_pos = ui.Mouse.get_relative_scaled_mouse_pos(mouse_x, mouse_y)
        tile_x = tile_pos[0] // TILE_SIZE
        tile_y = tile_pos[1] // TILE_SIZE
        entity = world.Entity.get_entity_in_fov_at_tile(tile_x, tile_y)

        if entity:
            ui.Element.set_selected_entity(entity)
            ui.Element.set_element_visibility(UIElementTypes.ENTITY_INFO, True)
            ui.Element.set_element_visibility(UIElementTypes.MESSAGE_LOG, False)
        else:
            ui.Element.set_element_visibility(UIElementTypes.ENTITY_INFO, False)
            ui.Element.set_element_visibility(UIElementTypes.ENTITY_INFO, True)

    @staticmethod
    def attempt_to_trigger_targeting_mode(mouse_x, mouse_y):
        """
        Check if a skill was clicked in the skill bar and set targeting mode.

        Args:
            mouse_x (int):
            mouse_y (int):
        """
        relative_mouse_pos = ui.Mouse.get_relative_scaled_mouse_pos(mouse_x, mouse_y)
        # TODO - replace skill get
        skill_number = 0  # ui.Mouse.get_skill_index_from_skill_clicked(relative_mouse_pos[0], relative_mouse_pos[1])

        # if we clicked a skill in the skill bar create the targeting overlay
        player = world.player
        skill = player.actor.known_skills[skill_number]

        if skill:
            publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))
        else:
            logging.debug(f"Left clicked skill bar but no skill found.")

    def trigger_targeting_overlay_and_entity_info(self, skill_to_be_used):
        """
        Show the targeting overlay for the skill specified and update the entity info in line.

        Args:
            skill_to_be_used ():
        """
        # get info for initial selected tile
        # TODO - get nearest entity in range, use player only if nothing in range
        player = world.player
        tile = world.Map.get_tile(player.x, player.y)

        # set the info needed to draw the overlay
        # TODO - re add the overlay when set up using ui widgets
        # ui.Element.set_skill_being_targeted(skill_to_be_used)
        # ui.Element.update_targeting_overlays_tiles_in_range_and_fov()
        # ui.Element.set_selected_tile(tile)
        # ui.Element.update_targeting_overlays_tiles_in_skill_effect_range()

        # show the overlay
        # ui.Element.set_element_visibility(UIElementTypes.TARGETING_OVERLAY, True)

        # show the entity info
        self.trigger_entity_info(tile)

    @staticmethod
    def trigger_entity_info(tile):
        """
        Trigger the entity info element and update the selected entity based on the tile.

        Args:
            tile (Tile):
        """
        entity = world.Entity.get_blocking_entity(tile.x, tile.y)
        ui.Element.set_selected_entity(entity)
        ui.Element.set_element_visibility(UIElementTypes.ENTITY_INFO, True)

    @staticmethod
    def attempt_to_use_targeted_skill():
        """
        Check if player can use the selected skill on the selected target and if so trigger use.
        """
        selected_tile = ui.targeting_overlay.selected_tile
        player = world.player
        skill_being_targeted = ui.targeting_overlay.skill_being_targeted

        if world.Skill.can_use_skill(player, (selected_tile.x, selected_tile.y),
                                             skill_being_targeted):
            publisher.publish((UseSkillEvent(entity, skill_being_targeted, (selected_tile.x, selected_tile.y))))
        else:
            # we already checked player can afford when triggering targeting mode so must be wrong target
            msg = f"You can't do that there!"
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

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

            #ui.Element.set_player_pos_in_camera(target_x, target_y)
        ui.Element.update_cameras_tiles()
        ui.Element.update_camera_game_map()
        ui.Element.update_camera_grid()

    def init_ui(self):
        """
        Initialise the UI
        """
        # show ui
        ui.Element.set_element_visibility(UIElementTypes.CAMERA, True)
        ui.Element.set_element_visibility(UIElementTypes.MESSAGE_LOG, True)
        ui.Element.set_element_visibility(UIElementTypes.ENTITY_QUEUE, True)
        ui.Element.set_element_visibility(UIElementTypes.SKILL_BAR, True)

        # update camera
        self.update_camera()