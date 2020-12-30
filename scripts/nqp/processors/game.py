from __future__ import annotations

from scripts.engine.core import chronicle, system
from scripts.engine.core.event import (
    EndRoundEvent,
    EndTurnEvent,
    ExitGameEvent,
    ExitMenuEvent,
    LoadGameEvent,
    NewGameEvent,
    NewRoundEvent,
    NewTurnEvent,
    StartGameEvent,
    Subscriber,
    WinConditionMetEvent,
)
from scripts.engine.core.ui import ui
from scripts.engine.internal.constant import EventType, InputIntent, UIElement
from scripts.nqp import command
from scripts.nqp.processors.intent import process_intent

__all__ = ["GameEventSubscriber"]


class GameEventSubscriber(Subscriber):
    """
    Handle interaction events.
    """

    def __init__(self):
        super().__init__("game_subscriber")
        self.subscribe(EventType.GAME)

    def process_event(self, event):
        if isinstance(event, ExitMenuEvent):
            if event.menu == UIElement.ACTOR_INFO:
                process_intent(InputIntent.ACTOR_INFO_TOGGLE)

        elif isinstance(event, NewGameEvent):
            ui.set_element_visibility(UIElement.TITLE_SCREEN, False)
            command.goto_character_select()

        elif isinstance(event, StartGameEvent):
            ui.set_element_visibility(UIElement.CHARACTER_SELECTOR, False)
            command.start_game(event.player_data)

        elif isinstance(event, LoadGameEvent):
            ui.set_element_visibility(UIElement.TITLE_SCREEN, False)
            command.load_game()

        elif isinstance(event, ExitGameEvent):
            command.exit_game()

        elif isinstance(event, WinConditionMetEvent):
            command.win_game()

        elif isinstance(event, NewTurnEvent):
            pass

        elif isinstance(event, EndTurnEvent):
            _process_end_turn()

        elif isinstance(event, NewRoundEvent):
            pass

        elif isinstance(event, EndRoundEvent):
            _process_end_round()


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
