from __future__ import annotations

import pygame

from scripts.engine.core.ui import ui
from scripts.engine.internal.constant import GameEvent, GameStateType, InputIntent, UIElement
from scripts.nqp import command
from scripts.nqp.processors.intent import process_intent

__all__ = ["process_event"]


def process_event(event: pygame.event, game_state: GameStateType):
    intent = None

    if event.type == GameEvent.EXIT_MENU:
        ## Exit Actor Info
        if event.menu == UIElement.ACTOR_INFO:
            intent = InputIntent.ACTOR_INFO_TOGGLE

    elif event.type == GameEvent.NEW_GAME:
        ui.set_element_visibility(UIElement.TITLE_SCREEN, False)
        command.goto_character_select()

    elif event.type == GameEvent.START_GAME:
        ui.set_element_visibility(UIElement.CHARACTER_SELECTOR, False)
        command.start_game(event.player_data)

    elif event.type == GameEvent.LOAD_GAME:
        ui.set_element_visibility(UIElement.TITLE_SCREEN, False)
        command.load_game()

    elif event.type == GameEvent.EXIT_GAME:
        command.exit_game()

    elif event.type == GameEvent.WIN_CONDITION_MET:
        command.win_game()

    # if we have an intent we need to process, do so
    if intent:
        process_intent(intent, game_state)
