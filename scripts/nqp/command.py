from __future__ import annotations

import logging
import os
from threading import Timer
from typing import List

import snecs
from snecs import Component

from scripts.engine import chronicle, library, state, utility, world
from scripts.engine.component import Aesthetic, Position, WinCondition
from scripts.engine.core import systems
from scripts.engine.core.constants import ASSET_PATH, DEBUG_START, SAVE_PATH, GameState, RenderLayer, UIElement
from scripts.engine.core.data import store
from scripts.engine.core.definitions import ActorData, TraitSpritePathsData
from scripts.engine.ui.manager import ui
from scripts.engine.world_objects.game_map import GameMap

__all__ = ["initialise_game", "goto_character_select", "load_game", "exit_game", "win_game"]


def initialise_game():
    """
    Init the game`s required info
    """
    if DEBUG_START:
        _start_debug_game()
    else:
        state.set_new(GameState.MENU)
        ui.set_element_visibility(UIElement.TITLE_SCREEN, True)


def _start_debug_game():
    """
    Create a new game and show the gamemap
    """
    # create clean snecs.world
    empty_world = snecs.World()
    world.move_world(empty_world)

    # init and save map
    game_map = GameMap("debug", 10)
    store.current_game_map = game_map

    # populate the map
    player_data = ActorData(
        key="player",
        possible_names=["player"],
        description="Player desc",
        position_offsets=[(0, 0)],
        trait_names=["shoom", "soft_tops", "dandy"],
    )
    game_map.generate_new_map(player_data)
    logging.info(game_map.generation_info)

    # init the player
    player = world.get_player()

    # tell places about the player
    chronicle.set_turn_holder(player)

    # show the in game screens
    ui.set_element_visibility(UIElement.CAMERA, True)

    for entity, (aesthetic, position) in world.get_components([Aesthetic, Position]):
        assert isinstance(aesthetic, Aesthetic)
        assert isinstance(position, Position)
        aesthetic.draw_x, aesthetic.draw_y = (position.x, position.y)
        aesthetic.target_draw_x = aesthetic.draw_x
        aesthetic.target_draw_y = aesthetic.draw_y

    # entities load with a blank fov, update them now
    systems.process_light_map()
    systems.process_fov()
    systems.process_tile_visibility()

    # point the camera at the player, now that FOV is updated
    pos = world.get_entitys_component(player, Position)
    camera = ui.get_element(UIElement.CAMERA)
    camera.set_target((pos.x, pos.y), True)

    # create terrain next to the player
    world.create_terrain(library.TERRAIN["bog"], (pos.x + 1, pos.y))

    # loading finished, give player control
    state.set_new(GameState.GAMEMAP)

    # prompt turn actions
    chronicle.end_turn(player, 0)


def start_game(player_data: ActorData):
    """
    Create a new game and show the gamemap
    """
    # create clean snecs.world
    empty_world = snecs.World()
    world.move_world(empty_world)

    # init and save map
    game_map = GameMap("cave", 10)
    store.current_game_map = game_map

    # populate the map
    game_map.generate_new_map(player_data)

    # init the player
    player = world.get_player()

    # create win condition and place next to player
    player_pos = world.get_entitys_component(player, Position)

    win_x = player_pos.x + 1
    win_y = player_pos.y
    components: List[Component] = []
    components.append(Position((win_x, win_y)))  # lets hope this doesnt spawn in a wall
    components.append(WinCondition())
    traits_paths = [TraitSpritePathsData(idle=str(ASSET_PATH / "world/win_flag.png"))]
    sprites = utility.build_sprites_from_paths(traits_paths)
    components.append(Aesthetic(sprites.idle, sprites, traits_paths, RenderLayer.ACTOR, (win_x, win_y)))
    world.create_entity(components)

    # tell places about the player
    chronicle.set_turn_holder(player)

    # create a god
    world.create_god("the_small_gods")

    # show the in game screens
    ui.set_element_visibility(UIElement.CAMERA, True)
    ui.set_element_visibility(UIElement.MESSAGE_LOG, True)
    ui.set_element_visibility(UIElement.SKILL_BAR, True)

    # welcome message
    ui.create_screen_message("Welcome to Not Quite Paradise")

    # FIXME - entities load before camera so they cant get their screen position.
    #  If ui loads before entities then it fails due to player not existing. Below is a hacky fix.
    for entity, (aesthetic, position) in world.get_components([Aesthetic, Position]):
        assert isinstance(aesthetic, Aesthetic)
        assert isinstance(position, Position)
        aesthetic.draw_x, aesthetic.draw_y = (position.x, position.y)
        aesthetic.target_draw_x = aesthetic.draw_x
        aesthetic.target_draw_y = aesthetic.draw_y

    # entities load with a blank fov, update them now
    systems.process_light_map()
    systems.process_fov()
    systems.process_tile_visibility()

    # point the camera at the player, now that FOV is updated
    pos = world.get_entitys_component(player, Position)
    camera = ui.get_element(UIElement.CAMERA)
    camera.set_target((pos.x, pos.y), True)

    # loading finished, give player control
    state.set_new(GameState.GAMEMAP)

    # prompt turn actions
    chronicle.end_turn(player, 0)


def load_game():
    """
    Load existing game state
    """
    full_save_path = str(SAVE_PATH)
    for save_name in os.listdir(full_save_path):
        save = save_name.replace(".json", "")
        state.load_game(save)
        break

    # show the in game screens
    ui.set_element_visibility(UIElement.CAMERA, True)
    ui.set_element_visibility(UIElement.MESSAGE_LOG, True)
    ui.set_element_visibility(UIElement.SKILL_BAR, True)

    # welcome message
    ui.create_screen_message("Welcome back to Not Quite Paradise")

    # loading finished, give player control
    state.set_new(GameState.GAMEMAP)


def exit_game():
    """
    Exit the game
    """
    state.set_new(GameState.EXITING)


def win_game():
    """
    Trigger the win game actions
    """
    state.set_new(GameState.MENU)
    ui.create_screen_message("You wonned. Huzzah.")

    # quit to main menu after a few seconds
    timer = Timer(2.0, goto_to_title)
    timer.start()


############### NAVIGATION  #####################


def goto_character_select():
    """
    Create a new game
    """
    ui.set_element_visibility(UIElement.CHARACTER_SELECTOR, True)


def goto_to_title():
    """
    Quit out of the game back to the title screen
    """
    state.set_new(GameState.MENU)

    # hide the in game screens
    ui.set_element_visibility(UIElement.CAMERA, False)
    ui.set_element_visibility(UIElement.MESSAGE_LOG, False)
    ui.set_element_visibility(UIElement.SKILL_BAR, False)

    # clear existing resource
    store.current_game_map = None  # TODO - add better clearing method.

    # show the title screen
    ui.set_element_visibility(UIElement.TITLE_SCREEN, True)
