from __future__ import annotations

import pygame

from scripts.engine import key, world
from scripts.engine.component import Position
from scripts.engine.core import queries
from scripts.engine.core.constants import GameState, GameStateType, InputEvent, InputIntent, UIElement
from scripts.engine.ui.elements.actor_info import ActorInfo
from scripts.engine.ui.manager import ui
from scripts.nqp.processors.intent import process_intent

__all__ = ["process_event"]


def process_event(event: pygame.event, game_state: GameStateType):
    """
    Extract the intent from the event and process them in the context of the game state. If an event can only be
    called in one way then no intent is generated and the event will directly go to the relevant action.
    """
    intent = None

    # some events only apply to certain GameStates, we need to process them and separate them
    if event.type == InputEvent.TILE_CLICK:

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
            for entity, (position, _) in queries.position_and_actor:  # type: ignore
                if (x, y) in position:
                    # found entity, set to selected
                    actor_info: ActorInfo = ui.get_element(UIElement.ACTOR_INFO)
                    actor_info.set_entity(entity)
                    intent = InputIntent.ACTOR_INFO_TOGGLE

    elif event.type == InputEvent.SKILL_BAR_CLICK:
        intent = event.skill_intent

    else:
        intent = key.convert_to_intent(event)

    # if we have an intent we need to process, do so
    if intent:
        process_intent(intent, game_state)
