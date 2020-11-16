from __future__ import annotations

import logging
from typing import Optional, Type

import numpy as np
import tcod
from snecs.typedefs import EntityID

from scripts.engine import chronicle, debug, library, state, utility, world
from scripts.engine.action import Skill
from scripts.engine.component import Knowledge, Position
from scripts.engine.core.constants import (
    Direction,
    DirectionType,
    GameState,
    GameStateType,
    InputIntent,
    InputIntentType,
    SAVE_PATH,
    TargetingMethod,
    UIElement,
)
from scripts.engine.ui.manager import ui
from scripts.engine.world_objects.tile import Tile
from scripts.nqp import command

__all__ = ["process_intent"]


def process_intent(intent: InputIntentType, game_state: GameStateType):
    """
    Process the intent in the context of the game state. Intents are game state sensitive.
    """
    _process_stateless_intents(intent)

    if game_state == GameState.GAMEMAP:
        _process_game_map_intents(intent)
    elif game_state == GameState.TARGETING:
        _process_targeting_mode_intents(intent)
    elif game_state == GameState.MENU:
        _process_menu_intents(intent)


def _process_stateless_intents(intent: InputIntentType):
    """
    Process intents that don't rely on game state.
    """
    ## Activate Debug
    if intent == InputIntent.DEBUG_TOGGLE:
        # F1
        if debug.is_fps_visible():
            debug.set_fps_visibility(False)
        else:
            debug.set_fps_visibility(True)

    ## Refresh Library Data
    elif intent == InputIntent.REFRESH_DATA:
        # TODO - move to a command in the console.
        library.refresh_library()

    ## Activate data editor
    # TODO - have this trigger dev console and move skill editor to a command in the console.
    elif intent == InputIntent.DUNGEON_DEV_VIEW:
        # F5
        if ui.element_is_visible(UIElement.DUNGEN_VIEWER):
            ui.set_element_visibility(UIElement.DUNGEN_VIEWER, False)
            state.set_new(state.get_previous())
        else:
            ui.get_element(UIElement.DUNGEN_VIEWER).refresh_viewer()
            ui.set_element_visibility(UIElement.DUNGEN_VIEWER, True)
            state.set_new(GameState.MENU)

    elif intent == InputIntent.DEV_TOGGLE:
        # F2
        if ui.get_element(UIElement.DATA_EDITOR):
            ui.set_element_visibility(UIElement.DATA_EDITOR, False)
            state.set_new(state.get_previous())
        else:
            ui.set_element_visibility(UIElement.DATA_EDITOR, True)
            state.set_new(GameState.DEVELOPER)

    elif intent == InputIntent.BURST_PROFILE:
        # F3
        debug.enable_profiling(120)

    elif intent == InputIntent.TOGGLE_UI:
        # F6
        if ui.element_is_visible(UIElement.MESSAGE_LOG):
            ui.set_element_visibility(UIElement.MESSAGE_LOG, False)
            ui.set_element_visibility(UIElement.SKILL_BAR, False)
        else:
            ui.set_element_visibility(UIElement.MESSAGE_LOG, True)
            ui.set_element_visibility(UIElement.SKILL_BAR, True)

    elif intent == InputIntent.TEST:
        # F12
        breakpoint()


def _process_game_map_intents(intent: InputIntentType):
    """
    Process intents for the player turn game state.
    """
    player = world.get_player()
    position = world.get_entitys_component(player, Position)

    possible_move_intents = [InputIntent.DOWN, InputIntent.UP, InputIntent.LEFT, InputIntent.RIGHT]
    possible_skill_intents = [
        InputIntent.SKILL0,
        InputIntent.SKILL1,
        InputIntent.SKILL2,
        InputIntent.SKILL3,
        InputIntent.SKILL4,
        InputIntent.SKILL5,
    ]

    ## Player movement
    if intent in possible_move_intents and position:
        direction = _get_pressed_direction(intent)
        target_tile = world.get_tile((position.x, position.y))
        move = world.get_known_skill(player, "Move")
        if direction in move.target_directions:
            _process_skill_use(player, move, target_tile, direction)

    ## Use a skill
    elif intent in possible_skill_intents and position:
        skill_name = _get_pressed_skills_name(intent)
        current_tile = world.get_tile((position.x, position.y))

        if skill_name:
            # is skill ready to use
            if world.can_use_skill(player, skill_name):
                skill = world.get_known_skill(player, skill_name)

                if skill:
                    # if auto targeting use the skill
                    if skill.targeting_method == TargetingMethod.AUTO:
                        # pass centre as it doesnt matter, the skill will pick the right direction
                        _process_skill_use(player, skill, current_tile, Direction.CENTRE)
                    else:
                        # trigger targeting overlay
                        state.set_new(GameState.TARGETING)
                        state.set_active_skill(skill_name)
                        ui.update_targeting_overlay(True, skill_name)

    ## Show actor info - we're in GAMEMAP so it cant be visible
    elif intent == InputIntent.ACTOR_INFO_TOGGLE:
        # show
        state.set_new(GameState.MENU)
        ui.set_element_visibility(UIElement.ACTOR_INFO, True)

    elif intent == InputIntent.EXIT:
        command.exit_game()


def _process_targeting_mode_intents(intent):
    """
    Process intents for the player turn game state.
    """
    player = world.get_player()
    position = world.get_entitys_component(player, Position)
    active_skill_name = state.get_active_skill()
    skill = world.get_known_skill(player, active_skill_name)

    possible_skill_intents = [
        InputIntent.SKILL0,
        InputIntent.SKILL1,
        InputIntent.SKILL2,
        InputIntent.SKILL3,
        InputIntent.SKILL4,
        InputIntent.SKILL5,
    ]

    ## Cancel use
    if intent == InputIntent.CANCEL:
        # go back to previous state
        state.set_new(state.get_previous())

    ## Select new skill
    elif intent in possible_skill_intents:
        pressed_skill_name = _get_pressed_skills_name(intent)

        if pressed_skill_name:

            # if skill pressed doesn't match skill already being targeted
            if pressed_skill_name != active_skill_name:
                # reactivate targeting mode with the new skill
                if world.can_use_skill(player, pressed_skill_name):
                    state.set_active_skill(pressed_skill_name)

    ## Use skill
    elif intent.upper() in utility.get_class_members(Direction):
        direction = _get_pressed_direction(intent)
        if position and skill and direction:
            outermost = position.get_outermost(direction)
            tile = world.get_tile((outermost[0] + direction[0], outermost[1] + direction[1]))
            if tile:
                # we already checked if we could use the skill before activating the targeting mode
                _process_skill_use(player, skill, tile, direction)

                # resume previous state
                state.set_new(state.get_previous())
                ui.update_targeting_overlay(False)


def _process_menu_intents(intent):
    ## Exit current menu
    if intent == InputIntent.ACTOR_INFO_TOGGLE:
        state.set_new(state.get_previous())
        ui.set_element_visibility(UIElement.ACTOR_INFO, False)


################## HELPER FUNCTIONS ############################


def _process_skill_use(player: EntityID, skill: Type[Skill], target_tile: Tile, direction: DirectionType):
    """
    Process the use of specified skill. Wrapper for actions needed to handle a full skill use. Assumed
    'can_use_skill' already completed.
    """
    # get players starting position for camera updates
    pos = world.get_entitys_component(player, Position)
    start_pos = pos.x, pos.y

    if world.use_skill(player, skill, target_tile, direction):
        world.pay_resource_cost(player, skill.resource_type, skill.resource_cost)
        world.judge_action(player, skill.__class__.__name__)
        chronicle.end_turn(player, skill.time_cost)

        state.save_game()

        # update camera if position changes
        try:
            if (pos.x, pos.y) != start_pos:
                ui.get_element(UIElement.CAMERA).set_target((pos.x, pos.y))
        except KeyError:
            logging.warning("Process skill use: tried to call camera but not init`d.")


def _get_pressed_direction(intent: InputIntentType) -> DirectionType:
    """
    Get the value of the directions pressed. Returns as (x, y). Values are ints between -1 and 1.
    """

    if intent == InputIntent.UP:
        direction = Direction.UP
    elif intent == InputIntent.UP_RIGHT:
        direction = Direction.UP_RIGHT
    elif intent == InputIntent.UP_LEFT:
        direction = Direction.UP_LEFT
    elif intent == InputIntent.RIGHT:
        direction = Direction.RIGHT
    elif intent == InputIntent.LEFT:
        direction = Direction.LEFT
    elif intent == InputIntent.DOWN:
        direction = Direction.DOWN
    elif intent == InputIntent.DOWN_RIGHT:
        direction = Direction.DOWN_RIGHT
    elif intent == InputIntent.DOWN_LEFT:
        direction = Direction.DOWN_LEFT
    else:
        direction = Direction.CENTRE

    return direction


def _get_pressed_skills_name(intent: InputIntentType) -> Optional[str]:
    """
    Get the pressed skill number. Returns value of skill number pressed. If not found returns None.
    """
    player = world.get_player()
    skill_name = None

    if player:
        skills = world.get_entitys_component(player, Knowledge)

        if skills:
            skill_order = skills.skill_order

            try:
                if intent == InputIntent.SKILL0:
                    skill_name = skill_order[0]
                elif intent == InputIntent.SKILL1:
                    skill_name = skill_order[1]
                elif intent == InputIntent.SKILL2:
                    skill_name = skill_order[2]
                elif intent == InputIntent.SKILL3:
                    skill_name = skill_order[3]
                elif intent == InputIntent.SKILL4:
                    skill_name = skill_order[4]
            except IndexError:
                logging.warning(f"_get_pressed_skills_name: Tried to use skill {intent} but no skill in that slot.")
    return skill_name
