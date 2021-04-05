from __future__ import annotations

import scripts.engine.core.matter
from scripts.engine.core import hourglass, system
from scripts.engine.core.ui import ui
from scripts.engine.core.component import Shrine
from scripts.engine.internal.constant import EventType, InputIntent, UIElement
from scripts.engine.internal.event import (
    ChangeMapEvent,
    ShrineEvent,
    EndRoundEvent,
    EndTurnEvent,
    ExitGameEvent,
    ExitMenuEvent,
    LoadGameEvent,
    LoseConditionMetEvent,
    NewGameEvent,
    NewRoundEvent,
    NewTurnEvent,
    StartGameEvent,
    Subscriber,
    WinConditionMetEvent,
    ShrineMenuEvent,
)
from scripts.nqp import command
from scripts.nqp.processors.intent import process_intent
from scripts.nqp.ui_elements.blessing_menu import BlessingMenu

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

        elif isinstance(event, ChangeMapEvent):
            command.change_map()

        elif isinstance(event, ShrineEvent):
            # not sure if this is where this should go...
            shrine = scripts.engine.core.matter.get_entitys_component(event.target_shrine, Shrine)
            shrine.interact()

        elif isinstance(event, LoseConditionMetEvent):
            command.lose_game()

        elif isinstance(event, NewTurnEvent):
            pass

        elif isinstance(event, EndTurnEvent):
            _process_end_turn()

        elif isinstance(event, NewRoundEvent):
            pass

        elif isinstance(event, EndRoundEvent):
            _process_end_round()

        elif isinstance(event, ShrineMenuEvent):
            blessing_menu: BlessingMenu = BlessingMenu(
                command.get_element_rect(UIElement.BLESSING_MENU), ui.get_gui_manager(), event.blessing_options
            )
            ui.register_element(UIElement.BLESSING_MENU, blessing_menu)


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

    if hourglass.get_turn_holder() == scripts.engine.core.matter.get_player():
        from scripts.engine.core import state

        state.save_game()

    hourglass.next_turn()


def _process_end_round():
    """
    Reduce durations and cooldowns. Move to next round.
    """
    system.reduce_skill_cooldowns()
    system.reduce_affliction_durations()
    system.reduce_lifespan_durations()
    system.reduce_immunity_durations()

    hourglass.next_round()
