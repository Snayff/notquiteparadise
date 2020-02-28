from __future__ import annotations

import dataclasses
import logging
import pygame
from typing import TYPE_CHECKING
from scripts.core.constants import InputIntents, Directions, GameStates, MessageTypes, EffectTypes
from scripts.core.event_hub import publisher
from scripts.core.library import library
from scripts.events.entity_events import MoveEvent, UseSkillEvent
from scripts.events.game_events import ExitGameEvent, ChangeGameStateEvent, EndTurnEvent
from scripts.managers.game_manager.game_manager import game
from scripts.managers.world_manager.world_manager import world
from scripts.world.components import Knowledge, Position

if TYPE_CHECKING:
    from scripts.managers.input_manager.input_manager import InputManager


class ControlMethods:
    """
    Methods for handling Input values and converting them to intents

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        self._manager = manager  # type: InputManager

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
                self.set_intent(InputIntents.EXIT_GAME)

    def check_dev_actions(self, event):
        """
        get any dev actions

        Args:
            event (pygame.event):
        """
        # handle key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.set_intent(InputIntents.DEBUG_TOGGLE)
            elif event.key == pygame.K_F5:
                self.set_intent(InputIntents.REFRESH_DATA)
            elif event.key == pygame.K_F2:
                self.set_intent(InputIntents.DEV_TOGGLE)

    ############### GET INFO ABOUT AN INPUT #########

    def get_pressed_direction(self):
        """
        Get the value of the directions pressed.

        Returns:
            Tuple: (x, y). Values are ints between -1 and 1.
        """
        get_intent = self.get_intent
        intent = InputIntents

        if get_intent(intent.UP):
            dir_x, dir_y = Directions.UP
        elif get_intent(intent.UP_RIGHT):
            dir_x, dir_y = Directions.UP_RIGHT
        elif get_intent(intent.UP_LEFT):
            dir_x, dir_y = Directions.UP_LEFT
        elif get_intent(intent.RIGHT):
            dir_x, dir_y = Directions.RIGHT
        elif get_intent(intent.LEFT):
            dir_x, dir_y = Directions.LEFT
        elif get_intent(intent.DOWN):
            dir_x, dir_y = Directions.DOWN
        elif get_intent(intent.DOWN_RIGHT):
            dir_x, dir_y = Directions.DOWN_RIGHT
        elif get_intent(intent.DOWN_LEFT):
            dir_x, dir_y = Directions.DOWN_LEFT
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
        Set an intent to true. IntentsData must exist in InputIntents and name must match (except case).
        """
        setattr(self._manager.Intents, intent, True)
        #print(f"Set {intent} Intent to True")

    def get_intent(self, intent: InputIntents) -> bool:
        """
        Get an intent. IntentsData must exist in InputIntents and name must match.
        """
        return getattr(self._manager.Intents, intent)

    def reset_intents(self):
        """
        Reset all input intents to false
        """
        for field in dataclasses.fields(self._manager.Intents):
            if field.type is "bool":
                setattr(self._manager.Intents, field.name, False)

    ############### PROCESS INTENT ###############

    def process_stateless_intents(self, event):
        """
        Process intents that don't rely on game state.

        Args:
            event ():
        """
        get_intent = self.get_intent
        intent = InputIntents

        # Activate Debug
        if get_intent(intent.DEBUG_TOGGLE):
            # TODO - create event to toggle debug
            pass

        # Refresh Library Data
        if get_intent(intent.REFRESH_DATA):
            # TODO - create event to refresh data
            pass

        # Exit game
        if get_intent(intent.EXIT_GAME):
            publisher.publish(ExitGameEvent())

    def process_player_turn_intents(self, event):
        """
        Process intents for the player turn game state.

        Args:
            event ():
        """
        get_intent = self.get_intent
        intent = InputIntents
        player = world.Entity.get_player()

        # Player movement
        dir_x, dir_y = self.get_pressed_direction()
        if dir_x != 0 or dir_y != 0:
            position = world.Entity.get_entitys_component(player, Position)
            publisher.publish(MoveEvent(player, (position.x, position.y), (dir_x, dir_y)))

        # Use a skill
        skill_number = self.get_pressed_skills_number()
        if skill_number != -1:
            knowledge = world.Entity.get_entitys_component(player, Knowledge)
            skill_name = knowledge.skills[skill_number]
            skill_data = library.get_skill_data(skill_name)

            if world.Skill.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost):
                publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill_name))

        # activate the skill editor
        if get_intent(intent.DEV_TOGGLE):
            publisher.publish(ChangeGameStateEvent(GameStates.DEV_MODE))

    def process_targeting_mode_intents(self, event):
        """
        Process intents for the player turn game state.

        Args:
            event ():
        """
        get_intent = self.get_intent
        intent = InputIntents
        player = world.Entity.get_player()
        skill_name = game.State.get_active_skill()

        # Cancel use
        if get_intent(intent.CANCEL):
            publisher.publish(ChangeGameStateEvent(game.State.get_previous()))

        # Use another skill
        skill_number = self.get_pressed_skills_number()
        if skill_number != -1:
            skill_pressed = player.actor.known_skills[skill_number]
            # confirm skill pressed doesn't match skill already pressed
            if skill_pressed != skill_name:
                knowledge = world.Entity.get_entitys_component(player, Knowledge)
                skill_name = knowledge.skills[skill_number]
                skill_data = library.get_skill_data(skill_name)

                if world.Skill.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost):
                    publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill_name))

    def process_dev_mode_intents(self, event):
        """
        Process intents for the dev mode game state.

        Args:
            event ():
        """
        get_intent = self.get_intent
        intent = InputIntents

        if get_intent(intent.DEV_TOGGLE):

            publisher.publish(ChangeGameStateEvent(game.State.get_previous()))
