from __future__ import annotations

__all__ = ["process_event"]

import pygame

from scripts.engine.core.constants import GameEvent, GameStateType, InputIntent, UIElement
from scripts.engine.ui.manager import ui
from scripts.nqp import command
from scripts.nqp.processors.intent import process_intent


def process_event(event: pygame.event, game_state: GameStateType):
    intent = None

    if event.type == GameEvent.EXIT_MENU:
        ## Exit Actor Info
        if event.menu == UIElement.ACTOR_INFO:
            intent = InputIntent.ACTOR_INFO_TOGGLE

    elif event.type == GameEvent.NEW_GAME:
        ui.set_element_visibility(UIElement.TITLE_SCREEN, False)
        command.new_game()

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
