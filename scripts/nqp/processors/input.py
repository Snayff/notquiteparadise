from __future__ import annotations

import pygame

import scripts.engine.core.matter
from scripts.engine.core import hourglass, key, query, world
from scripts.engine.core.component import Position
from scripts.engine.core.ui import ui
from scripts.engine.internal.constant import EventType, GameState, InputEventType, InputIntent, UIElement
from scripts.nqp import command
from scripts.nqp.processors.intent import process_intent

__all__ = ["process_input_event"]

from scripts.nqp.ui_elements.actor_info import ActorInfo


def process_input_event(event: pygame.event, game_state: GameState):
    """
    Extract the intent from the event and process them in the context of the game state. If an event can only be
    called in one way then no intent is generated and the event will directly go to the relevant action.

    This covers the custom InputEventType and pygame pygame.KEYDOWN events.
    """
    intent = None

    # some events only apply to certain GameStates, we need to process them and separate them
    if event.type == EventType.INPUT:
        if event.subtype == InputEventType.TILE_CLICK:

            if game_state == GameState.TARGETING:
                # Activate skill on mouse click while in targeting mode
                player = scripts.engine.core.matter.get_player()
                position = scripts.engine.core.matter.get_entitys_component(player, Position)
                event_x, event_y = event.tile_pos
                direction = (max(-1, min(1, event_x - position.x)), max(-1, min(1, position.y - event_y)))
                intent = key.convert_vector_to_intent(direction)

            elif (
                game_state == GameState.GAME_MAP
                and hourglass.get_turn_holder() == scripts.engine.core.matter.get_player()
            ):
                # Activate Actor Info Menu
                x, y = event.tile_pos
                # get entity on tile
                for entity, (position,) in query.position:  # type: ignore
                    assert isinstance(position, Position)
                    if (x, y) in position.coordinates:
                        # found entity, set to selected
                        if ui.has_element(UIElement.ACTOR_INFO):
                            ui.kill_element(UIElement.ACTOR_INFO)

                        actor_info: ActorInfo = ActorInfo(
                            command.get_element_rect(UIElement.ACTOR_INFO), ui.get_gui_manager()
                        )
                        ui.register_element(UIElement.ACTOR_INFO, actor_info)
                        actor_info.set_entity(entity)
                        intent = InputIntent.ACTOR_INFO_TOGGLE

        elif event.subtype == InputEventType.SKILL_BAR_CLICK:
            intent = event.skill_intent

    else:
        intent = key.convert_to_intent(event)

    # if we have an intent we need to process, do so
    if intent:
        process_intent(intent, game_state)
