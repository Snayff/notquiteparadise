from __future__ import annotations

import logging

import pytweening
from scripts.engine import utility, entity
from scripts.engine.component import Aesthetic, Position, Knowledge
from typing import TYPE_CHECKING, Optional
from scripts.engine.core.constants import GameState, InputIntent, Direction, InputIntentType, GameStateType, \
    TravelMethod, BASE_MOVE_COST
from scripts.engine.core.event_core import publisher
from scripts.engine.event import ExitGameEvent, MoveEvent, WantToUseSkillEvent, ChangeGameStateEvent

if TYPE_CHECKING:
    from typing import Type, Tuple


def process_all(delta_time: float):
    """
    Process all processors. N.B. does not include processing intent.
    """
    _process_aesthetic_update(delta_time)


def _process_aesthetic_update(delta_time: float):
    """
    Update real-time timers on entities
    """
    # move entities screen position towards target
    for ent, (aesthetic, ) in entity.get_components([Aesthetic]):
        max_duration = 0.3

        # increment time
        aesthetic.current_sprite_duration += delta_time

        # do we need to show moving to a new position? Have we exceeded animation duration?
        if (aesthetic.screen_x != aesthetic.target_screen_x or aesthetic.screen_y != aesthetic.target_screen_y) \
                and aesthetic.current_sprite_duration <= max_duration:
            # are we close?
            if (aesthetic.screen_x - 1 < aesthetic.target_screen_x < aesthetic.screen_x + 1) and \
                    (aesthetic.screen_y - 1 < aesthetic.target_screen_y < aesthetic.screen_y + 1):
                # jump to target
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


def _get_pressed_direction(intent: InputIntentType) -> Tuple[int, int]:
    """
    Get the value of the directions pressed. Returns as (x, y). Values are ints between -1 and 1.
    """

    if intent == InputIntent.UP:
        dir_x, dir_y = Direction.UP
    elif intent == InputIntent.UP_RIGHT:
        dir_x, dir_y = Direction.UP_RIGHT
    elif intent == InputIntent.UP_LEFT:
        dir_x, dir_y = Direction.UP_LEFT
    elif intent == InputIntent.RIGHT:
        dir_x, dir_y = Direction.RIGHT
    elif intent == InputIntent.LEFT:
        dir_x, dir_y = Direction.LEFT
    elif intent == InputIntent.DOWN:
        dir_x, dir_y = Direction.DOWN
    elif intent == InputIntent.DOWN_RIGHT:
        dir_x, dir_y = Direction.DOWN_RIGHT
    elif intent == InputIntent.DOWN_LEFT:
        dir_x, dir_y = Direction.DOWN_LEFT
    else:
        dir_x, dir_y = 0, 0

    return dir_x, dir_y


def _get_pressed_skills_name(intent: InputIntentType) -> Optional[str]:
    """
    Get the pressed skill number. Returns value of skill number pressed. If not found returns None.
    """
    player = entity.get_player()
    skills = entity.get_entitys_component(player, Knowledge).skill_order

    if intent == InputIntent.SKILL0:
        skill_name = skills[0]
    elif intent == InputIntent.SKILL1:
        skill_name = skills[1]
    elif intent == InputIntent.SKILL2:
        skill_name = skills[2]
    elif intent == InputIntent.SKILL3:
        skill_name = skills[3]
    elif intent == InputIntent.SKILL4:
        skill_name = skills[4]
    else:
        skill_name = None

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
        publisher.publish(ExitGameEvent())


def _process_player_turn_intents(intent: InputIntentType):
    """
    Process intents for the player turn game state.
    """
    player = entity.get_player()

    # if player exists, which it should, because we're in PLAYER_TURN game state
    if player:
        # Player movement
        direction = _get_pressed_direction(intent)
        possible_moves = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        if direction in possible_moves:
            position = entity.get_entitys_component(player, Position)
            publisher.publish(MoveEvent(player, (position.x, position.y), direction, TravelMethod.STANDARD,
                                        BASE_MOVE_COST))

        # Use a skill
        skill_name = _get_pressed_skills_name(intent)
        if skill_name:
            position = entity.get_entitys_component(player, Position)
            # None to trigger targeting mode
            publisher.publish(WantToUseSkillEvent(player, skill_name, (position.y, position.x), None))

    # activate the skill editor
    if intent == InputIntent.DEV_TOGGLE:
        publisher.publish(ChangeGameStateEvent(GameState.DEV_MODE))


def _process_targeting_mode_intents(intent):
    """
    Process intents for the player turn game state.
    """
    player = entity.get_player()

    # Cancel use
    if intent == InputIntent.CANCEL:
        publisher.publish(ChangeGameStateEvent(GameState.PREVIOUS))

    # Use a skill
    skill_name = _get_pressed_skills_name(intent)
    if skill_name:
        position = entity.get_entitys_component(player, Position)
        # None to trigger targeting mode
        publisher.publish(WantToUseSkillEvent(player, skill_name, (position.y, position.x), None))


def _process_dev_mode_intents(intent):
    """
    Process intents for the dev mode game state.
    """
    if intent == InputIntent.DEV_TOGGLE:
        publisher.publish(ChangeGameStateEvent(GameState.PREVIOUS))