import pygame

from scripts.core.constants import InputModes, GameStates, TILE_SIZE, MessageEventTypes, LoggingEventTypes, MouseButtons
from scripts.events.entity_events import UseSkillEvent, MoveEvent
from scripts.events.game_events import ChangeGameStateEvent, ExitEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.events.ui_events import ClickUIEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher


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
            "skill0": False,
            "skill1": False,
            "skill2": False,
            "skill3": False,
            "skill4": False,
            "refresh_data": False

        }

        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, f"InputManager initialised."))

    def update(self):
        """
        Get the input and process it
        """
        self.update_input_values()

        # log input for debug
        input_received = ""
        for key, value in self.input_values.items():
            if key != "mouse_moved":
                if value:
                    input_received += key + ", "

        if input_received != "":
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"Input received: {input_received}"))

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
            self.input_values["skill0"] = True
        elif event.key == pygame.K_2:
            self.input_values["skill1"] = True
        elif event.key == pygame.K_3:
            self.input_values["skill2"] = True
        elif event.key == pygame.K_4:
            self.input_values["skill3"] = True
        elif event.key == pygame.K_5:
            self.input_values["skill4"] = True

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
        elif event.key == pygame.K_F5:
            self.input_values["refresh_data"] = True

    def process_input(self):
        """
        Process all input from input_values. Calls multiple sub methods based on current GameState.
        """
        from scripts.global_singletons.managers import game_manager
        game_state = game_manager.game_state

        self.process_generic_input()

        if game_state == GameStates.PLAYER_TURN:
            self.process_player_turn_input()

        elif game_state == GameStates.TARGETING_MODE:
            self.process_targeting_mode_input()

        elif game_state == GameStates.PLAYER_DEAD:
            pass

    def process_generic_input(self):
        """
        Interpret none GameState-specific actions
        """
        if self.input_values["debug_toggle"]:
            from scripts.global_singletons.managers import debug_manager
            if debug_manager.visible:
                debug_manager.set_visibility(False)
            else:
                debug_manager.set_visibility(True)

        if self.input_values["refresh_data"]:
            library.load_data_into_library()
            from scripts.global_singletons.managers import ui_manager
            ui_manager.skill_bar.update_skill_icons_to_show()

    def process_player_turn_input(self):
        """
        Interpret Player Turn actions
        """
        from scripts.global_singletons.managers import world_manager
        player = world_manager.player

        # general actions
        if self.input_values["cancel"]:
            publisher.publish(ExitEvent())

        # UI interactions
        mouse_button = self.get_pressed_mouse_button()

        if mouse_button:
            publisher.publish(ClickUIEvent(mouse_button))

        # movement
        direction_x, direction_y = self.get_pressed_direction()

        # if destination isn't 0 then we need to move player
        if direction_x != 0 or direction_y != 0:
            target_x, target_y = direction_x + player.x, direction_y + player.y
            publisher.publish(MoveEvent(player, (target_x, target_y)))

        # SKILLS usage
        skill_number = self.get_pressed_skill_number()

        # has a skill input been pressed?
        if skill_number != -1:

            # get the skill at the relevant number
            skill = player.actor.known_skills[skill_number]

            # do we have a skill in the slot?
            if skill:
                skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)

                # check who we are moused over
                from scripts.global_singletons.managers import ui_manager
                mouse_x, mouse_y = ui_manager.get_relative_scaled_mouse_pos("game_map")
                target_x, target_y = world_manager.Map.convert_xy_to_tile(mouse_x, mouse_y)

                # create a skill with a target, or activate targeting mode
                if world_manager.Skill.can_use_skill(player, (target_x, target_y), skill):
                    publisher.publish((UseSkillEvent(player, (target_x, target_y), skill)))
                else:
                    # can't use skill, is it due to being too poor?
                    if world_manager.Skill.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost):
                        # can afford so must be picking wrong target
                        msg = f"You can't do that there!"
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

                        publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))

                    else:
                        msg = f"It seems you're too poor to do that."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
            else:
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, "There is nothing in that skill slot."))

    def process_targeting_mode_input(self):
        """
        Interpret Targeting Mode actions
        """
        from scripts.global_singletons.managers import world_manager
        player = world_manager.player

        from scripts.global_singletons.managers import ui_manager
        selected_tile = ui_manager.targeting_overlay.selected_tile

        # UI interactions
        mouse_button = self.get_pressed_mouse_button()

        if mouse_button:
            publisher.publish(ClickUIEvent(mouse_button))

        mouse_x, mouse_y = ui_manager.get_scaled_mouse_pos()
        mouse_tile_x, mouse_tile_y = world_manager.Map.convert_xy_to_tile(mouse_x, mouse_y)

        # cancel out
        if self.input_values["cancel"] or self.input_values["right_click"]:
            from scripts.global_singletons.managers import game_manager
            previous_state = game_manager.previous_game_state
            publisher.publish(ChangeGameStateEvent(previous_state))

        # if direction isn't 0 then we need to move selected_tile
        # TODO - move logic to event
        direction_x, direction_y = self.get_pressed_direction()

        if direction_x != 0 or direction_y != 0:
            tile_x, tile_y = direction_x + selected_tile.x, direction_y + selected_tile.y
            tile = world_manager.Map.get_tile(tile_x, tile_y)
            ui_manager.targeting_overlay.set_selected_tile(tile)
            entity = world_manager.Entity.get_blocking_entity_at_location(tile.x, tile.y)
            ui_manager.entity_info.set_selected_entity(entity)

        # if mouse moved update selected tile
        # TODO - move logic to event
        if self.input_values["mouse_moved"]:
            tile = world_manager.Map.get_tile(mouse_tile_x, mouse_tile_y)
            ui_manager.targeting_overlay.set_selected_tile(tile)
            entity = world_manager.Entity.get_blocking_entity_at_location(tile.x, tile.y)
            ui_manager.entity_info.set_selected_entity(entity)

        #  SKILL USAGE
        skill_number = self.get_pressed_skill_number()
        skill_being_targeted = ui_manager.targeting_overlay.skill_being_targeted

        # have we confirmed skill use on selected tile?
        if self.input_values["confirm"]:
            if world_manager.Skill.can_use_skill(player, (selected_tile.x, selected_tile.y), skill_being_targeted):
                publisher.publish((UseSkillEvent(player, (selected_tile.x, selected_tile.y),
                                                 skill_being_targeted)))
            else:
                # we already checked player can afford when triggering targeting mode so must be wrong target
                msg = f"You can't do that there!"
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

        # has a skill input been pressed?
        if skill_number != -1:
            skill_selected = player.actor.known_skills[skill_number]

            # if we chose a skill check if it is same one, or if we otherwise confirmed
            if skill_being_targeted == skill_selected:

                skill_data = library.get_skill_data(skill_being_targeted.skill_tree_name, skill_being_targeted.name)

                # confirm can use skill
                if world_manager.Skill.can_use_skill(player, (selected_tile.x, selected_tile.y), skill_being_targeted):
                    publisher.publish((UseSkillEvent(player, (selected_tile.x, selected_tile.y),
                                                     skill_being_targeted)))
                else:
                    # can't use skill, is it due to being too poor?
                    if world_manager.Skill.can_afford_cost(player, skill_data.resource_type,
                                                           skill_data.resource_cost):
                        publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill_being_targeted))
                    else:
                        # we already checked player can afford when triggering targeting mode so must be wrong target
                        msg = f"You can't do that there!"
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

            # pressed another skill so should we swap to that one?
            elif skill_selected != player.actor.known_skills.index(skill_being_targeted):

                skill_data = library.get_skill_data(skill_selected.skill_tree_name, skill_selected.name)

                # can we afford the new skill selected?
                if world_manager.Skill.can_afford_cost(player, skill_data.resource_type,
                                                       skill_data.resource_cost):
                    # can afford so swap
                    publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill_selected))

                # can't afford so cancel targeting?
                else:
                    msg = f"It seems you're too poor to do that."
                    publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

                    publisher.publish(ChangeGameStateEvent(GameStates.PLAYER_TURN))

    def get_pressed_mouse_button(self):
        """
        Get which mouse button has been pressed.

        Returns:
            MouseButtons: Mouse buttons enum or None if no button pressed.

        """
        if self.input_values["right_click"]:
            return MouseButtons.RIGHT_BUTTON
        elif self.input_values["left_click"]:
            return MouseButtons.LEFT_BUTTON
        elif self.input_values["middle_click"]:
            return MouseButtons.MIDDLE_BUTTON
        else:
            return None

    def get_pressed_direction(self):
        """
        Get the intended direction based on input values.

        Returns:
            tuple: tuple of ints showing direction as (dir_x, dir_y). (0,0) if nothing pressed.
        """
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

        return direction_x, direction_y

    def get_pressed_skill_number(self):
        """
        Get the pressed skill number based on input values.

        Returns:
            int: value of skill number pressed. Returns -1 if none.
        """
        if self.input_values["skill0"]:
            return 0
        elif self.input_values["skill1"]:
            return 1
        elif self.input_values["skill2"]:
            return 2
        elif self.input_values["skill3"]:
            return 3
        elif self.input_values["skill4"]:
            return 4
        else:
            return -1