from __future__ import annotations

import logging

import pytweening
from scripts.engine import state, utility, world
from scripts.engine.component import Aesthetic, Position, Knowledge
from typing import TYPE_CHECKING, Optional, cast
from scripts.engine.core.constants import GameState, InputIntent, Direction, InputIntentType, GameStateType, \
    TargetingMethod, DirectionType, UIElement
from scripts.engine.core.event_core import publisher
from scripts.engine.utility import is_close
from scripts.nqp.skills import Move

if TYPE_CHECKING:
    from typing import Type, Tuple


def process_realtime_updates(delta_time: float):
    """
    Fire realtime processors.
    """
    _process_camera_update(delta_time)
    _process_aesthetic_update(delta_time)


def _process_camera_update(delta_time: float):
    """
    Update realtime camera timers, such as the camera scrolling to reveal new tiles.
    """
    camera = world.ui.get_element(UIElement.CAMERA)

    if not camera:
        return

    max_duration = 1

    # increment time
    camera.current_sprite_duration += delta_time

    if not camera.has_reached_target():

        # time for animation exceeded
        time_exceeded = camera.current_sprite_duration > max_duration

        # time for animation exceeded or animation very close to end
        if time_exceeded or is_close((camera.start_tile_col, camera.start_tile_row),
                                     (camera.target_tile_col, camera.target_tile_row)):

            # set start_tile to target
            camera.set_start_to_target()

        # keep moving:
        else:

            lerp_amount = pytweening.easeOutCubic(min(1.0, camera.current_sprite_duration / max_duration))
            col_ = utility.lerp(camera.start_tile_col, camera.target_tile_col, lerp_amount)
            row_ = utility.lerp(camera.start_tile_row, camera.target_tile_row, lerp_amount)

            camera.set_start_col_row((col_, row_))

    # not moving
    else:
        camera.current_sprite_duration = 0


def _process_aesthetic_update(delta_time: float):
    """
    Update real-time timers on entities, such as entity animations.
    """
    # move entities screen position towards target
    for entity, (aesthetic, ) in world.get_components([Aesthetic]):
        # cast for typing
        aesthetic = cast(Aesthetic, aesthetic)

        max_duration = 0.3

        # increment time
        aesthetic.current_sprite_duration += delta_time

        # do we need to show moving to a new position?
        if aesthetic.screen_x != aesthetic.target_screen_x or aesthetic.screen_y != aesthetic.target_screen_y:

            # Have we exceeded animation duration?
            time_exceeded = aesthetic.current_sprite_duration > max_duration

            # time for animation exceeded or animation very close to end
            if time_exceeded or is_close((aesthetic.screen_x, aesthetic.screen_y),
                                         (aesthetic.target_screen_x, aesthetic.target_screen_y)):

                # set to target
                aesthetic.screen_x = aesthetic.target_screen_x
                aesthetic.screen_y = aesthetic.target_screen_y


            # keep moving:
            else:
                lerp_amount = pytweening.easeOutCubic(min(1.0, aesthetic.current_sprite_duration * 2))
                aesthetic.screen_x = utility.lerp(aesthetic.screen_x, aesthetic.target_screen_x, lerp_amount)
                aesthetic.screen_y = utility.lerp(aesthetic.screen_y, aesthetic.target_screen_y, lerp_amount)

        # not moving so reset to idle
        else:
            aesthetic.current_sprite = aesthetic.sprites.idle
            aesthetic.current_sprite_duration = 0


########################### INPUT ###########################

def process_intent(intent: InputIntentType, game_state: GameStateType):
    """
    Process the intent in the context of the game state
    """
    _process_stateless_intents(intent)

    if game_state == GameState.PLAYER_TURN:
        _process_player_turn_intents(intent)
    elif game_state == GameState.TARGETING_MODE:
        _process_targeting_mode_intents(intent)
    elif game_state == GameState.DEV_MODE:
        _process_dev_mode_intents(intent)


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

    # Activate Debug
    if intent == InputIntent.DEBUG_TOGGLE:
        # TODO - create event to toggle debug
        pass

    # Refresh Library Data
    if intent == InputIntent.REFRESH_DATA:
        # TODO - create event to refresh data
        pass

    # Exit game
    if intent == InputIntent.EXIT_GAME:
        state.set_new(GameState.EXIT_GAME)


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
                if world.pay_resource_cost(player, Move.resource_type, Move.resource_cost):
                    if world.use_skill(player, Move, tile, direction):
                        world.end_turn(player, Move.time_cost)

            ## Use a skill
            skill_name = _get_pressed_skills_name(intent)

            # is skill ready to use
            if world.can_use_skill(player, skill_name):
                skill = world.get_known_skill(player, skill_name)

                if skill:
                    # if auto targeting use the skill
                    if skill.targeting_method == TargetingMethod.AUTO:
                        if world.pay_resource_cost(player, skill.resource_type, skill.resource_cost):
                            if world.use_skill(player, skill, tile, direction):
                                world.end_turn(player, skill.time_cost)
                    else:
                        state.set_new(GameState.TARGETING_MODE)
                        state.set_active_skill(skill_name)

    ## activate the skill editor
    if intent == InputIntent.DEV_TOGGLE:
        publisher.publish(ChangeGameStateEvent(GameState.DEV_MODE))


def _process_targeting_mode_intents(intent):
    """
    Process intents for the player turn game state.
    """
    player = world.get_player()
    position = world.get_entitys_component(player, Position)
    active_skill_name = state.get_active_skill()

    ## Cancel use
    if intent == InputIntent.CANCEL:
        publisher.publish(ChangeGameStateEvent(state.get_previous()))

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


def _process_dev_mode_intents(intent):
    """
    Process intents for the dev mode game state.
    """
    if intent == InputIntent.DEV_TOGGLE:
        publisher.publish(ChangeGameStateEvent(state.get_previous()))
