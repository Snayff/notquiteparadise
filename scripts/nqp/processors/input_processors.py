from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Optional, Type

import pygame
from pygame_gui import UI_WINDOW_CLOSE
from snecs.typedefs import EntityID

import scripts.engine.chronicle
from scripts.engine import debug, key, state, world
from scripts.engine.component import IsActor, Knowledge, Position
from scripts.engine.core.constants import (
    Direction, DirectionType, EventType, GameState, GameStateType, InputIntent,
    InputIntentType, TargetingMethod, UIElement)
from scripts.engine.library import library
from scripts.engine.ui.manager import ui
from scripts.engine.ui.elements.actor_info import ActorInfo
from scripts.engine.world_objects.tile import Tile
from scripts.nqp.actions.skills import Move, Skill
from scripts.nqp.processors import ai_processors

if TYPE_CHECKING:
    from typing import Optional


########################## OUTER LAYER PROCESSORS - EXTERNAL FACING #####################################

def process_event(event: pygame.event, game_state: GameStateType):
    """
    Extract the intent from the event and process them in the context of the game state
    """
    intent = None
    # some events only apply to certain GameStates, we need to process them and separate them
    if event.type == EventType.TILE_CLICK:

        if game_state == GameState.TARGETING:
            ## Activate skill on mouse click while in targeting mode
            player = world.get_player()
            position = world.get_entitys_component(player, Position)
            if position:
                event_x, event_y = event.tile_pos
                direction = (max(-1, min(1, event_x - position.x)), max(-1, min(1, position.y - event_y)))
                intent = key.convert_vector_to_intent(direction)

        elif game_state == GameState.GAMEMAP:
            ## Activate Actor Info Menu
            x, y = event.tile_pos
            # get entity on tile
            for entity, (position, *other) in world.get_components([Position, IsActor]): # type: ignore
                if (x, y) in position: # type: ignore
                    # found entity, set to selected
                    actor_info: ActorInfo = ui.get_element(UIElement.ACTOR_INFO)
                    actor_info.set_entity(entity)
                    intent = InputIntent.ACTOR_INFO_TOGGLE

    elif event.type == EventType.SKILL_BAR_CLICK:
        intent = event.skill_intent

    elif event.type == EventType.EXIT_MENU:
        ## Exit Actor Info
        if event.menu == UIElement.ACTOR_INFO:
            intent = InputIntent.ACTOR_INFO_TOGGLE

    else:
        intent = key.convert_to_intent(event)

    # if we have an intent we need to process, do so
    if intent:
        process_intent(intent, game_state)


def process_intent(intent: InputIntentType, game_state: GameStateType):
    """
    Process the intent in the context of the game state
    """
    _process_stateless_intents(intent)

    if game_state == GameState.GAMEMAP:
        _process_gamemap_intents(intent)
    elif game_state == GameState.TARGETING:
        _process_targeting_mode_intents(intent)
    elif game_state == GameState.MENU:
        _process_menu_intents(intent)


############################### INNER PROCESSORS - LOCAL ONLY ################################

def _process_stateless_intents(intent: InputIntentType):
    """
    Process intents that don't rely on game state.
    """
    ## Activate Debug
    if intent == InputIntent.DEBUG_TOGGLE:
        if debug.is_fps_visible():
            debug.set_fps_visibility(False)
        else:
            debug.set_fps_visibility(True)

    ## Refresh Library Data
    elif intent == InputIntent.REFRESH_DATA:
        # TODO - have this trigger dev console and move skill editor to a command in the console.
        library.refresh_library_data()

    ## Activate data editor
    # TODO - have this trigger dev console and move skill editor to a command in the console.
    elif intent == InputIntent.DEV_TOGGLE:
        if ui.get_element(UIElement.DATA_EDITOR):
            ui.set_element_visibility(UIElement.DATA_EDITOR, False)
            state.set_new(state.get_previous())
        else:
            ui.create_element(UIElement.DATA_EDITOR)
            state.set_new(GameState.DEVELOPER)


def _process_gamemap_intents(intent: InputIntentType):
    """
    Process intents for the player turn game state.
    """
    player = world.get_player()
    position = world.get_entitys_component(player, Position)

    possible_move_intents = [InputIntent.DOWN, InputIntent.UP, InputIntent.LEFT, InputIntent.RIGHT]
    possible_skill_intents = [InputIntent.SKILL0, InputIntent.SKILL1, InputIntent.SKILL2, InputIntent.SKILL3,
    InputIntent.SKILL4, InputIntent.SKILL5]

    ## Player movement
    if intent in possible_move_intents and position:
        direction = _get_pressed_direction(intent)
        target_tile = world.get_tile((position.x, position.y))
        possible_moves = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        if direction in possible_moves:
            _process_skill_use(player, Move, target_tile, direction)


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

    ## Exit game
    elif intent == InputIntent.EXIT:
        state.set_new(GameState.EXIT_GAME)


def _process_targeting_mode_intents(intent):
    """
    Process intents for the player turn game state.
    """
    player = world.get_player()
    position = world.get_entitys_component(player, Position)
    active_skill_name = state.get_active_skill()
    skill = world.get_known_skill(player, active_skill_name)

    possible_skill_intents = [InputIntent.SKILL0, InputIntent.SKILL1, InputIntent.SKILL2, InputIntent.SKILL3,
        InputIntent.SKILL4, InputIntent.SKILL5]

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
    elif intent in skill.target_directions:
        direction = _get_pressed_direction(intent)
        if position and skill and direction:
            outmost = position.get_outmost(direction)
            tile = world.get_tile((outmost[0] + direction[0], outmost[1] + direction[1]))
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
    if world.use_skill(player, skill, target_tile, direction):
        world.pay_resource_cost(player, skill.resource_type, skill.resource_cost)
        world.judge_action(player, skill.name)
        ai_processors.process_interventions()
        scripts.engine.chronicle.end_turn(player, skill.time_cost)
        if skill.name == "move":
            ui.set_player_tile(target_tile)


######################### GET ##########################

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
