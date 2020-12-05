from __future__ import annotations

import pygame

from scripts.engine.core import chronicle, system
from scripts.engine.core.ui import ui
from scripts.engine.internal.constant import GameEvent, GameState, InputIntent, UIElement
from scripts.nqp import command
from scripts.nqp.processors.intent import process_intent

__all__ = ["process_game_event"]


def process_game_event(event: pygame.event, game_state: GameState):
    intent = None

    if event.subtype == GameEvent.EXIT_MENU:
        ## Exit Actor Info
        if event.menu == UIElement.ACTOR_INFO:
            intent = InputIntent.ACTOR_INFO_TOGGLE

    elif event.subtype == GameEvent.NEW_GAME:
        ui.set_element_visibility(UIElement.TITLE_SCREEN, False)
        command.goto_character_select()

    elif event.subtype == GameEvent.START_GAME:
        ui.set_element_visibility(UIElement.CHARACTER_SELECTOR, False)
        command.start_game(event.player_data)

    elif event.subtype == GameEvent.LOAD_GAME:
        ui.set_element_visibility(UIElement.TITLE_SCREEN, False)
        command.load_game()

    elif event.subtype == GameEvent.EXIT_GAME:
        command.exit_game()

    elif event.subtype == GameEvent.WIN_CONDITION_MET:
        command.win_game()

    elif event.subtype == GameEvent.NEW_TURN:
        pass

    elif event.subtype == GameEvent.END_TURN:
        _process_end_turn()

    elif event.subtype == GameEvent.NEW_ROUND:
        pass

    elif event.subtype == GameEvent.END_ROUND:
        pass

    # if we have an intent we need to process, do so
    if intent:
        process_intent(intent, game_state)


def _process_end_turn():
    """
    Update which entities are active and entity and map vision. Move to next turn.
    """
    system.process_activations()  # must be first otherwise wrong entities active
    system.process_light_map()
    system.process_fov()
    system.process_tile_visibility()

    # if player is current turn holder then save the game
    from scripts.engine.core import world
    if chronicle.get_turn_holder() == world.get_player():
        from scripts.engine.core import state
        state.save_game()

    chronicle.next_turn()


def _process_end_round():
    """
    Reduce durations and cooldowns. Move to next round.
    """
    system.reduce_skill_cooldowns()
    system.reduce_affliction_durations()
    system.reduce_lifespan_durations()

    chronicle.next_round()

