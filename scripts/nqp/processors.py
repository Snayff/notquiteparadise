from __future__ import annotations

import pytweening
from scripts.engine import utility, entity
from scripts.engine.component import Aesthetic
from typing import TYPE_CHECKING
from scripts.engine.core.constants import GameStates, InputIntents, Directions
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
    for ent, aesthetic in entity.get_component(Aesthetic):
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

def process_intent(intent: Type[InputIntents], game_state: GameStates):
    """
    Process the intent in the context of the game state
    """
    _process_stateless_intents(intent)

    if game_state == GameStates.PLAYER_TURN:
        _process_player_turn_intents(intent)
    elif game_state == GameStates.TARGETING_MODE:
        _process_targeting_mode_intents(intent)
    elif game_state == GameStates.DEV_MODE:
        _process_dev_mode_intents(intent)


def _get_pressed_direction(intent: Type[InputIntents]) -> Tuple[int, int]:
    """
    Get the value of the directions pressed. Returns as (x, y). Values are ints between -1 and 1.
    """

    if intent == InputIntents.UP:
        dir_x, dir_y = Directions.UP
    elif intent == InputIntents.UP_RIGHT:
        dir_x, dir_y = Directions.UP_RIGHT
    elif intent == InputIntents.UP_LEFT:
        dir_x, dir_y = Directions.UP_LEFT
    elif intent == InputIntents.RIGHT:
        dir_x, dir_y = Directions.RIGHT
    elif intent == InputIntents.LEFT:
        dir_x, dir_y = Directions.LEFT
    elif intent == InputIntents.DOWN:
        dir_x, dir_y = Directions.DOWN
    elif intent == InputIntents.DOWN_RIGHT:
        dir_x, dir_y = Directions.DOWN_RIGHT
    elif intent == InputIntents.DOWN_LEFT:
        dir_x, dir_y = Directions.DOWN_LEFT
    else:
        dir_x, dir_y = 0, 0

    return dir_x, dir_y


def _get_pressed_skills_number(intent: Type[InputIntents]) -> int:
    """
    Get the pressed skill number. Returns value of skill number pressed. Returns -1 if none.
    """
    if intent == InputIntents.SKILL0:
        skill_number = 0
    elif intent == InputIntents.SKILL1:
        skill_number = 1
    elif intent == InputIntents.SKILL2:
        skill_number = 2
    elif intent == InputIntents.SKILL3:
        skill_number = 3
    elif intent == InputIntents.SKILL4:
        skill_number = 4
    else:
        skill_number = -1

    return skill_number


def _process_stateless_intents(intent):
    """
    Process intents that don't rely on game state.
    """

    # Activate Debug
    if intent == InputIntents.DEBUG_TOGGLE:
        # TODO - create event to toggle debug
        pass

    # Refresh Library Data
    if intent == InputIntents.REFRESH_DATA:
        # TODO - create event to refresh data
        pass

    # Exit game
    if intent == InputIntents.EXIT_GAME:
        publisher.publish(ExitGameEvent())


def _process_player_turn_intents(intent):
    """
    Process intents for the player turn game state.
    """
    player = entity.get_player()

    # Player movement
    dir_x, dir_y = _get_pressed_direction(intent)
    if dir_x != 0 or dir_y != 0:
        publisher.publish(MoveEvent(player, (dir_x, dir_y)))

    # Use a skill
    skill_number = _get_pressed_skills_number(intent)
    if skill_number != -1:
        publisher.publish(WantToUseSkillEvent(skill_number))

    # activate the skill editor
    if intent.DEV_TOGGLE:
        publisher.publish(ChangeGameStateEvent(GameStates.DEV_MODE))


def _process_targeting_mode_intents(intent):
    """
    Process intents for the player turn game state.
    """
    # Cancel use
    if intent == InputIntents.CANCEL:
        publisher.publish(ChangeGameStateEvent(GameStates.PREVIOUS))

    # Consider using the skill, handle if different skill pressed
    skill_number = _get_pressed_skills_number(intent)
    if skill_number != -1:
        publisher.publish(WantToUseSkillEvent(skill_number))


def _process_dev_mode_intents(intent):
    """
    Process intents for the dev mode game state.
    """
    if intent == InputIntents.DEV_TOGGLE:
        publisher.publish(ChangeGameStateEvent(GameStates.PREVIOUS))