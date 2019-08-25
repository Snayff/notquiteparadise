
import logging

from scripts.core.constants import EventTopics, GameEventTypes, GameStates, EntityEventTypes, \
    UIEventTypes, MouseButtons, TILE_SIZE, MessageEventTypes
from scripts.events.entity_events import UseSkillEvent
from scripts.events.game_events import ChangeGameStateEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.event_hub import publisher
from scripts.global_singletons.managers import game_manager, ui_manager, world_manager
from scripts.event_handlers.pub_sub_hub import Subscriber


class UiHandler(Subscriber):
    """
    Handle events that effect the UI
    """

    def __init__(self, event_hub):
        Subscriber.__init__(self, "ui_handler", event_hub)
        # TODO - all UI functionality to watch events and update UI in response

    def run(self, event):
        """
        Process the events
        """

        # log that event has been received
        log_string = f"{self.name} received {event.topic}:{event.type}"
        logging.debug(log_string)

        if event.topic == EventTopics.UI:
            self.process_ui(event)

        if event.topic == EventTopics.ENTITY:
            self.process_entity(event)

        if event.topic == EventTopics.GAME:
            self.process_game(event)

    def process_entity(self, event):
        """
        Process Entity Events

        Args:
            event ():
        """

        # if an entity acts then hide the entity info
        if "entity_info" in ui_manager.visible_elements:
            self.hide_entity_info()

        if event.type == EntityEventTypes.LEARN:
            ui_manager.skill_bar.update_skill_icons_to_show()
        elif event.type == EntityEventTypes.DIE:
            ui_manager.entity_queue.update_entity_queue()

    @staticmethod
    def process_game(event):
        """
        Process Game Events

        Args:
            event ():
        """
        if event.type == GameEventTypes.CHANGE_GAME_STATE:

            # if changing to targeting mode then turn on targeting overlay
            if event.new_game_state == GameStates.TARGETING_MODE:
                # get info for initial selected tile
                player = world_manager.player
                tile = world_manager.Map.get_tile(player.x, player.y)

                # set the info needed to draw the overlay
                ui_manager.targeting_overlay.set_skill_being_targeted(event.skill_to_be_used)
                ui_manager.targeting_overlay.update_tiles_in_range_and_fov()
                ui_manager.targeting_overlay.set_selected_tile(tile)
                ui_manager.targeting_overlay.update_tiles_in_skill_effect_range()

                # show the entity info
                entity = world_manager.Entity.get_blocking_entity_at_location(tile.x, tile.y)
                ui_manager.entity_info.set_selected_entity(entity)

                # show the overlay
                ui_manager.targeting_overlay.set_visibility(True)

            elif game_manager.previous_game_state.TARGETING_MODE:
                ui_manager.targeting_overlay.set_visibility(False)

        elif event.type == GameEventTypes.END_TURN:
            ui_manager.entity_queue.update_entity_queue()

    def process_ui(self, event):
        """
        Process UI Events

        Args:
            event ():
        """

        if event.type == UIEventTypes.CLICK_UI:
            button = event.button_pressed
            mouse_x = event.mouse_x
            mouse_y = event.mouse_y
            clicked_rect = ui_manager.get_clicked_panels_rect(mouse_x, mouse_y)
            game_state = game_manager.game_state

            # handle right click actions
            # TODO - replace strings with enum
            # Selecting an entity
            if button == MouseButtons.RIGHT_BUTTON and clicked_rect == "game_map":
                self.attempt_to_set_selected_entity(clicked_rect, mouse_x, mouse_y)

            # Selecting a skill
            elif button == MouseButtons.LEFT_BUTTON and clicked_rect == "skill_bar":
                self.attempt_to_trigger_targeting_mode(clicked_rect, mouse_x, mouse_y)

            # using a selected skill
            elif button == MouseButtons.LEFT_BUTTON and clicked_rect == "game_map" and game_state == \
                    GameStates.TARGETING_MODE:
                selected_tile = ui_manager.targeting_overlay.selected_tile
                player = world_manager.player
                skill_being_targeted = ui_manager.targeting_overlay.skill_being_targeted

                if world_manager.Skill.can_use_skill(player, (selected_tile.x, selected_tile.y), skill_being_targeted):
                    publisher.publish((UseSkillEvent(player, (selected_tile.x, selected_tile.y),
                                                     skill_being_targeted)))
                else:
                    # we already checked player can afford when triggering targeting mode so must be wrong target
                    msg = f"You can't do that there!"
                    publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

    def attempt_to_set_selected_entity(self, clicked_rect, mouse_x, mouse_y):
        """
        Check if clicked location includes an entity and if so set it as selected to display its info.

        Args:
            mouse_x (int):
            mouse_y (int):
            clicked_rect (Rect): The clicked rect, from ui_elements.
        """
        tile_pos = ui_manager.get_relative_scaled_mouse_pos(clicked_rect, mouse_x, mouse_y)
        tile_x = tile_pos[0] // TILE_SIZE
        tile_y = tile_pos[1] // TILE_SIZE
        entity = world_manager.Entity.get_entity_in_fov_at_tile(tile_x, tile_y)

        if entity:
            ui_manager.entity_info.set_selected_entity(entity)
        else:
            self.hide_entity_info()

    @staticmethod
    def attempt_to_trigger_targeting_mode(clicked_rect, mouse_x, mouse_y):
        """
        Check if a skill was clicked in the skill bar and set targeting mode.

        Args:
            clicked_rect (Rect): The clicked rect, from ui_elements.
            mouse_x (int):
            mouse_y (int):
        """
        relative_mouse_pos = ui_manager.get_relative_scaled_mouse_pos(clicked_rect, mouse_x, mouse_y)
        skill_number = ui_manager.skill_bar.get_skill_index_from_skill_clicked(relative_mouse_pos[0],
                                                                               relative_mouse_pos[1])
        player = world_manager.player

        # if we clicked a skill in the skill bar create the targeting overlay
        skill = player.actor.known_skills[skill_number]

        if skill:
            publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))
        else:
            logging.debug( f"Left clicked skill bar but no skill found.")

    @staticmethod
    def hide_entity_info():
        """
        Hide the entity info panel
        """
        ui_manager.entity_info.set_visibility(False)
        log_string = f"Entity info hidden."
        logging.info( log_string)