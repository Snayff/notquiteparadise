import dataclasses
import pygame
from scripts.core.constants import InputIntents, Directions, GameStates, MessageTypes
from scripts.core.event_hub import publisher
from scripts.core.library import library
from scripts.events.entity_events import MoveEvent, UseSkillEvent
from scripts.events.game_events import ExitGameEvent, ChangeGameStateEvent, EndTurnEvent
from scripts.events.ui_events import ClickTile, MessageEvent
from scripts.managers.game_manager import game
from scripts.managers.world_manager import world


class ControlMethods:
    """
    Methods for handling Input values and converting them to intents

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.input_manager import InputManager
        self.manager = manager  # type: InputManager

    ############### INPUT CHECKS ####################

    def check_directions(self, event):
        """
        get directional input from the keyboard

        Args:
            event (pygame.event):
        """
        # TODO - refer to key mapping to enable key rebinding

        # handle key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_KP8 or event.key == pygame.K_k:
                self.set_intent(InputIntents.UP)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2 or event.key == pygame.K_j:
                self.set_intent(InputIntents.DOWN)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4 or event.key == pygame.K_h:
                self.set_intent(InputIntents.LEFT)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6 or event.key == pygame.K_l:
                self.set_intent(InputIntents.RIGHT)
            elif event.key == pygame.K_KP7 or event.key == pygame.K_y:
                self.set_intent(InputIntents.UP_LEFT)
            elif event.key == pygame.K_KP9 or event.key == pygame.K_u:
                self.set_intent(InputIntents.UP_RIGHT)
            elif event.key == pygame.K_KP1 or event.key == pygame.K_b:
                self.set_intent(InputIntents.DOWN_LEFT)
            elif event.key == pygame.K_KP3 or event.key == pygame.K_n:
                self.set_intent(InputIntents.DOWN_RIGHT)

    def check_actions(self, event):
        """
        get actions such as confirm or cancel, or skill usage.

        Args:
            event (pygame.event):
        """
        # TODO - refer to key mapping to enable key rebinding
        # handle key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.set_intent(InputIntents.SKILL0)
            elif event.key == pygame.K_2:
                self.set_intent(InputIntents.SKILL1)
            elif event.key == pygame.K_3:
                self.set_intent(InputIntents.SKILL2)
            elif event.key == pygame.K_4:
                self.set_intent(InputIntents.SKILL3)
            elif event.key == pygame.K_5:
                self.set_intent(InputIntents.SKILL4)
            elif event.key == pygame.K_RETURN:
                self.set_intent(InputIntents.CONFIRM)
            elif event.key == pygame.K_ESCAPE:
                self.set_intent(InputIntents.CANCEL)

        # handle mouse click events
        if event.type == pygame.USEREVENT:
            self.set_intent(InputIntents.BUTTON_PRESSED)

    def check_dev_actions(self, event):
        """
        get any dev actions

        Args:
            event (pygame.event):
        """
        # handle key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.set_intent(InputIntents.DEBUG_TOGGLE)
            elif event.key == pygame.K_F5:
                self.set_intent(InputIntents.REFRESH_DATA)

    ############### GET INFO ABOUT AN INPUT #########
    @staticmethod
    def get_pressed_ui_button(event):
        """
        Process input of a gui button

        Args:
            event ():

        Returns:
            Tuple: (str) button name, button values
        """
        if event.ui_object_id[:-1] == "#skill_button":
            print(f"button clicked(skill{event.ui_object_id[-1:]})")
            return "skill", event.ui_object_id[-1:]

        elif event.ui_object_id[:len("#tile")] == "#tile":
            print(f"button clicked(grid.tile{event.ui_object_id[len('#tile'):]})")
            return "tile", event.ui_object_id[len('#tile'):]

    def get_pressed_direction(self):
        """
        Get the value of the directions pressed.

        Returns:
            Tuple: (x, y). Values are ints between -1 and 1.
        """
        get_intent = self.get_intent
        intent = InputIntents

        if get_intent(intent.UP):
            dir_x, dir_y = Directions.UP.value
        elif get_intent(intent.UP_RIGHT):
            dir_x, dir_y = Directions.UP_RIGHT.value
        elif get_intent(intent.UP_LEFT):
            dir_x, dir_y = Directions.UP_LEFT.value
        elif get_intent(intent.RIGHT):
            dir_x, dir_y = Directions.RIGHT.value
        elif get_intent(intent.LEFT):
            dir_x, dir_y = Directions.LEFT.value
        elif get_intent(intent.DOWN):
            dir_x, dir_y = Directions.DOWN.value
        elif get_intent(intent.DOWN_RIGHT):
            dir_x, dir_y = Directions.DOWN_RIGHT.value
        elif get_intent(intent.DOWN_LEFT):
            dir_x, dir_y = Directions.DOWN_LEFT.value
        else:
            dir_x, dir_y = 0, 0

        return dir_x, dir_y

    def get_pressed_skills_number(self):
        """
        Get the pressed skill number.

        Returns:
            int: value of skill number pressed. Returns -1 if none.
        """
        get_intent = self.get_intent
        intent = InputIntents

        if get_intent(intent.SKILL0):
            skill_number = 0
        elif get_intent(intent.SKILL1):
            skill_number = 1
        elif get_intent(intent.SKILL2):
            skill_number = 2
        elif get_intent(intent.SKILL3):
            skill_number = 3
        elif get_intent(intent.SKILL4):
            skill_number = 4
        else:
            skill_number = -1

        return skill_number

    ############### INTENT AMENDMENTS ###############

    def set_intent(self, intent: InputIntents):
        """
        Set an intent to true. Intents must exist in InputIntents and name must match (except case).

        Args:
            intent ():
        """
        setattr(self.manager.Intents, intent.name.lower(), True)
        # print(f"Set {intent.name.lower()} Intent to True")

    def get_intent(self, intent: InputIntents):
        """
        Get an intent. Intents must exist in InputIntents and name must match (except case).

        Args:
            intent ():

        Returns:
            bool: True if intent is True.
        """
        return getattr(self.manager.Intents, intent.name.lower())

    def reset_intents(self):
        """
        Reset all input intents to false
        """
        for field in dataclasses.fields(self.manager.Intents):
            if field.type is bool:
                setattr(self.manager.Intents, field.name, False)

    ############### PROCESS INTENT ###############

    def process_stateless_intents(self, event):
        """
        Process intents that don't rely on game state.

        Args:
            event ():
        """
        get_intent = self.get_intent
        intent = InputIntents

        if get_intent(intent.DEBUG_TOGGLE):
            # TODO - create event to toggle debug
            pass

        if get_intent(intent.REFRESH_DATA):
            # TODO - create event to refresh data
            pass

    def process_player_turn_intents(self, event):
        """
        Process intents for the player turn game state.

        Args:
            event ():
        """
        get_intent = self.get_intent
        intent = InputIntents
        player = world.Entity.get_player()

        # Exit game
        if get_intent(intent.CANCEL):
            publisher.publish(ExitGameEvent())

        # Button press
        if get_intent(intent.BUTTON_PRESSED):
            button = self.get_pressed_ui_button(event)
            # Click tile
            if button[0] == "tile":
                publisher.publish(ClickTile(tile_pos_string=button[1]))

        # Player movement
        dir_x, dir_y = self.get_pressed_direction()
        if dir_x != 0 or dir_y != 0:
            publisher.publish(MoveEvent(player, (dir_x, dir_y)))
            publisher.publish(EndTurnEvent(player, 10))  # TODO - replace magic number with cost to move

        # Use a skill
        skill_number = self.get_pressed_skills_number()
        if skill_number != -1:
            skill = player.actor.known_skills[skill_number]
            skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)

            if world.Skill.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost):
                publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))

    def process_targeting_mode_intents(self, event):
        """
        Process intents for the player turn game state.

        Args:
            event ():
        """
        get_intent = self.get_intent
        intent = InputIntents
        player = world.Entity.get_player()
        skill = game.active_skill

        # Use skill on tile
        if get_intent(intent.BUTTON_PRESSED):
            button = self.get_pressed_ui_button(event)
            if button[0] == "tile":
                direction = world.Map.get_direction((player.x, player.y), button[1])
                publisher.publish(UseSkillEvent(player, skill, direction))
                skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)
                publisher.publish(EndTurnEvent(player, skill_data.time_cost))

        # Cancel use
        if get_intent(intent.CANCEL):
            publisher.publish(ChangeGameStateEvent(game.previous_game_state))

        # Use another skill
        skill_number = self.get_pressed_skills_number()
        if skill_number != -1:
            skill_pressed = player.actor.known_skills[skill_number]
            # confirm skill pressed doesn't match skill already pressed
            if skill_pressed != skill:
                skill = player.actor.known_skills[skill_number]
                skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)

                if world.Skill.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost):
                    publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))