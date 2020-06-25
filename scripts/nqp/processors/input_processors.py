from __future__ import annotations

from typing import Optional, TYPE_CHECKING, Type
from snecs.typedefs import EntityID
from scripts.engine import debug, state, world
from scripts.engine.component import Knowledge, Position
from scripts.engine.core.constants import Direction, DirectionType, GameState, GameStateType, InputIntent, \
    InputIntentType, TargetingMethod, UIElement
from scripts.engine.library import library
from scripts.engine.ui.manager import ui
from scripts.engine.world_objects.tile import Tile
from scripts.nqp.processors import ai_processors
from scripts.nqp.actions.skills import Move, Skill

if TYPE_CHECKING:
    from typing import Optional


def process_intent(intent: InputIntentType, game_state: GameStateType):
    """
    Process the intent in the context of the game state
    """
    _process_stateless_intents(intent)

    if game_state == GameState.GAMEMAP:
        _process_player_turn_intents(intent)
    elif game_state == GameState.TARGETING:
        _process_targeting_mode_intents(intent)


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

    return skill_name


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
        library.refresh_library_data()

    ## Exit game
    elif intent == InputIntent.EXIT_GAME:
        state.set_new(GameState.EXIT_GAME)

    ## activate the data editor
    # TODO - have this trigger dev console and move skill editor to a command in the console.
    elif intent == InputIntent.DEV_TOGGLE:
        if ui.get_element(UIElement.DATA_EDITOR):
            ui.kill_element(UIElement.DATA_EDITOR)
            state.set_new(state.get_previous())
        else:
            ui.create_element(UIElement.DATA_EDITOR)
            state.set_new(GameState.DEVELOPER)


def _process_player_turn_intents(intent: InputIntentType):
    """
    Process intents for the player turn game state.
    """
    player = world.get_player()

    position = world.get_entitys_component(player, Position)
    if position:
        tile = world.get_tile((position.x, position.y))
        if tile:

            ## Player movement
            direction = _get_pressed_direction(intent)
            possible_moves = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
            if direction in possible_moves:
                _process_skill_use(player, Move, tile, direction)

            ## Use a skill
            skill_name = _get_pressed_skills_name(intent)

            # is skill ready to use
            if world.can_use_skill(player, skill_name):
                skill = world.get_known_skill(player, skill_name)

                if skill:
                    # if auto targeting use the skill
                    if skill.targeting_method == TargetingMethod.AUTO:
                        _process_skill_use(player, skill, tile, direction)
                    else:
                        state.set_new(GameState.TARGETING)
                        state.set_active_skill(skill_name)


def _process_targeting_mode_intents(intent):
    """
    Process intents for the player turn game state.
    """
    player = world.get_player()
    position = world.get_entitys_component(player, Position)
    active_skill_name = state.get_active_skill()

    ## Cancel use
    if intent == InputIntent.CANCEL:
        # go back to previous state
        state.set_new(state.get_previous())

    ## Select new skill
    pressed_skill_name = _get_pressed_skills_name(intent)
    if pressed_skill_name:

        # if skill pressed doesn't match skill already being targeted
        if pressed_skill_name != active_skill_name:
            # reactivate targeting mode with the new skill
            if world.can_use_skill(player, pressed_skill_name):
                state.set_active_skill(pressed_skill_name)

    ## Use skill
    direction = _get_pressed_direction(intent)
    skill = world.get_known_skill(player, active_skill_name)
    possible_moves = skill.target_directions
    if direction in possible_moves and position and skill:
        tile = world.get_tile((position.x, position.y))
        if tile:
            if world.pay_resource_cost(player, skill.resource_type, skill.resource_cost):
                if world.use_skill(player, skill, tile, direction):
                    world.end_turn(player, skill.time_cost)


def _process_skill_use(player: EntityID, skill: Type[Skill], current_tile: Tile, direction: DirectionType):
    """
    Process the use of specified skill. Wrapper for actions needed to handle a full skill use. Assumed
    'can_use_skill' already completed.
     """
    if world.use_skill(player, skill, current_tile, direction):
        world.pay_resource_cost(player, skill.resource_type, skill.resource_cost)
        world.judge_action(player, skill.name)
        ai_processors.process_interventions()
        world.end_turn(player, skill.time_cost)
        new_tile = world.get_tile((current_tile.x + direction[0], current_tile.y + direction[1]))
        ui.set_player_tile(new_tile)

