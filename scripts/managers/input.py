import pygame

from scripts.core.constants import InputModes, GameStates, TILE_SIZE, MessageEventTypes
from scripts.events.entity_events import UseSkillEvent, MoveEvent
from scripts.events.game_events import ChangeGameStateEvent, ExitEvent
from scripts.events.message_events import MessageEvent
from scripts.global_instances.event_hub import publisher


class InputManager:
    """
    Manager of Input Functions and data, such as which input method and recent key presses
    """
    def __init__(self):
        self.input_mode = InputModes.MOUSE_AND_KB
        self.input_values = {
            "left_click": False,
            "right_click": False,
            "middle_click": False,
            "mouse_moved": False,
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "up_right": False,
            "up_left": False,
            "down_right": False,
            "down_left": False,
            "confirm": False,
            "cancel": False,
            "debug_toggle": False,
            "skill": []
        }

    def update(self):
        """
        Get the input and process it
        """
        self.update_input_values()
        self.process_input()

    def update_input_values(self):
        """
        Get the pygame event and update the input_values dictionary

        Returns:
            dict: `self.input_values` containing True for all appropriate inputs.

        """
        # gets mouse and key input as list of events
        input_events = pygame.event.get()

        # reset all input values
        for key in self.input_values:
            self.input_values[key] = False

        # check all input events
        for event in input_events:

            self.check_mouse_input(event)

            # is a KB KEY pressed?
            if event.type == pygame.KEYDOWN:
                self.check_kb_directional_input(event)
                self.check_kb_interaction_input(event)
                self.check_kb_general_input(event)
    
    def check_mouse_input(self, event):
        """
        Check for mouse input

        Args:
            event (pygame.event):
        """
        # update MOUSE input values based on event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                self.input_values["left_click"] = True
            elif pygame.mouse.get_pressed()[1]:
                self.input_values["middle_click"] = True
            elif pygame.mouse.get_pressed()[2]:
                self.input_values["right_click"] = True

        if event.type == pygame.MOUSEMOTION:
            self.input_values["mouse_moved"] = True

    def check_kb_directional_input(self, event):
        """
        get directional input from the keyboard

        Args:
            event (pygame.event):
        """
        if event.key == pygame.K_UP or event.key == pygame.K_KP8 or event.key == pygame.K_k:
            self.input_values["up"] = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2 or event.key == pygame.K_j:
            self.input_values["down"] = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4 or event.key == pygame.K_h:
            self.input_values["left"] = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6 or event.key == pygame.K_l:
            self.input_values["right"] = True
        elif event.key == pygame.K_KP7 or event.key == pygame.K_y:
            self.input_values["up_left"] = True
        elif event.key == pygame.K_KP9 or event.key == pygame.K_u:
            self.input_values["up_right"] = True
        elif event.key == pygame.K_KP1 or event.key == pygame.K_b:
            self.input_values["down_left"] = True
        elif event.key == pygame.K_KP3 or event.key == pygame.K_n:
            self.input_values["down_right"] = True

    def check_kb_interaction_input(self, event):
        """
        get interaction input, such as skills,  from the keyboard

        Args:
            event (pygame.event):
        """
        if event.key == pygame.K_1:
            self.input_values["skill"][0] = True
        elif event.key == pygame.K_2:
            self.input_values["skill"][1] = True
        elif event.key == pygame.K_3:
            self.input_values["skill"][2] = True
        elif event.key == pygame.K_4:
            self.input_values["skill"][3] = True
        elif event.key == pygame.K_5:
            self.input_values["skill"][4] = True

    def check_kb_general_input(self, event):
        """
        get general input, such as confirm and cancel, from the keyboard

        Args:
            event (pygame.event):
        """
        if event.key == pygame.K_RETURN:
            self.input_values["confirm"] = True
        elif event.key == pygame.K_ESCAPE:
            self.input_values["cancel"] = True
        elif event.key == pygame.K_TAB:
            self.input_values["debug_toggle"] = True

    def process_input(self):
        """
        Process all input from input_values. Calls multiple sub methods based on current GameState.
        """
        from scripts.global_instances.managers import game_manager
        game_state = game_manager.game_state

        self.process_generic_input()

        if game_state == GameStates.PLAYER_TURN:
            self.process_player_turn_input()

        elif game_state == GameStates.TARGETING_MODE:
            # handle_targeting_mode_input()
            pass

        elif game_state == GameStates.PLAYER_DEAD:
            pass

    def process_generic_input(self):
        """
        Interpret none GameState-specific actions
        """
        if self.input_values["debug_toggle"]:
            from scripts.global_instances.managers import debug_manager
            if debug_manager.visible:
                debug_manager.set_visibility(False)
            else:
                debug_manager.set_visibility(True)

        # UI interactions
        if self.input_values["right_click"] or self.input_values["left_click"]:
            from scripts.global_instances.managers import ui_manager
            clicked_rect = ui_manager.get_clicked_panels_rect()

            if self.input_values["right_click"]:
                # right clicked on the map so give the selected tile to the ui manager to display info
                if clicked_rect == "game_map":
                    # TODO - convert to input event and move logic to event processing
                    tile_pos = ui_manager.get_relative_scaled_mouse_pos(clicked_rect)
                    tile_x = tile_pos[0] // TILE_SIZE
                    tile_y = tile_pos[1] // TILE_SIZE
                    from scripts.global_instances.managers import world_manager
                    entity = world_manager.Entity.get_entity_in_fov_at_tile(tile_x, tile_y)

                    if entity:
                        ui_manager.entity_info.set_selected_entity(entity)

    def process_player_turn_input(self):

        from scripts.global_instances.managers import world_manager
        player = world_manager.player

        # general actions
        if self.input_values["cancel"]:
            publisher.publish(ExitEvent())

        # UI interactions
        if self.input_values["right_click"] or self.input_values["left_click"]:
            from scripts.global_instances.managers import ui_manager
            clicked_rect = ui_manager.get_clicked_panels_rect()

            if self.input_values["right_click"]:
                # right clicked on the map so give the selected tile to the ui manager to display info
                if clicked_rect == "game_map":
                    tile_pos = ui_manager.get_relative_scaled_mouse_pos(clicked_rect)
                    tile_x = tile_pos[0] // TILE_SIZE
                    tile_y = tile_pos[1] // TILE_SIZE
                    from scripts.global_instances.managers import world_manager
                    entity = world_manager.Entity.get_entity_in_fov_at_tile(tile_x, tile_y)

                    if entity:
                        ui_manager.entity_info.set_selected_entity(entity)

            if self.input_values["left_click"]:

                # if we clicked the skill bar
                if clicked_rect == "skill_bar":
                    relative_mouse_pos = ui_manager.get_relative_scaled_mouse_pos(clicked_rect)
                    skill_number = ui_manager.skill_bar.get_skill_index_from_skill_clicked(relative_mouse_pos[0],
                                                                                           relative_mouse_pos[1])
                    # if we clicked a skill in the skill bar create the targeting overlay
                    if self.input_values["skill"][skill_number]:
                        if player.actor.known_skills[skill_number]:
                            skill = player.actor.known_skills[skill_number]
                            publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))

        # movement
        direction_x = 0
        direction_y = 0

        if self.input_values["up"]:
            direction_x = 0
            direction_y = -1
        elif self.input_values["down"]:
            direction_x = 0
            direction_y = 1
        elif self.input_values["left"]:
            direction_x = -1
            direction_y = 0
        elif self.input_values["right"]:
            direction_x = 1
            direction_y = 0
        elif self.input_values["up_left"]:
            direction_x = -1
            direction_y = -1
        elif self.input_values["up_right"]:
            direction_x = 1
            direction_y = -1
        elif self.input_values["down_left"]:
            direction_x = -1
            direction_y = 1
        elif self.input_values["down_right"]:
            direction_x = 1
            direction_y = 1

        # if destination isn't 0 then we need to move player
        if direction_x != 0 or direction_y != 0:
            target_x, target_y = direction_x + player.x, direction_y + player.y

            # is there something in the way?
            in_bounds = world_manager.Map.is_tile_in_bounds(target_x, target_y)
            tile_blocking_movement = world_manager.Map.is_tile_blocking_movement(target_x, target_y)
            entity_blocking_movement = world_manager.Entity.get_blocking_entity_at_location(target_x, target_y)

            if in_bounds:
                if not entity_blocking_movement and tile_blocking_movement:
                    # no entity in way but tile is blocked
                    msg = f"There`s something in the way!"
                    publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                elif entity_blocking_movement:
                    # entity blocking tile so attack
                    skill = player.actor.known_skills[0]
                    publisher.publish((UseSkillEvent(player, (target_x, target_y), skill)))
                elif not entity_blocking_movement and not tile_blocking_movement:
                    # nothing in the way, time to move!
                    publisher.publish(MoveEvent(player, (target_x, target_y)))