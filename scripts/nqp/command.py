from __future__ import annotations

import logging
import os
from threading import Timer
from typing import List

import pygame
import snecs
from snecs import Component

from scripts.engine.core import chronicle, state, system, utility, world
from scripts.engine.core.ui import ui
from scripts.engine.internal import library
from scripts.engine.internal.action import register_action
from scripts.engine.core.component import Aesthetic, Position, WinCondition
from scripts.engine.internal.constant import (
    ASSET_PATH,
    DEBUG_START,
    GameState,
    GAP_SIZE,
    Height,
    MAX_SKILLS,
    RenderLayer,
    SAVE_PATH,
    SKILL_BUTTON_SIZE,
    UIElement,
)
from scripts.engine.internal.data import store
from scripts.engine.internal.definition import ActorData, TraitSpritePathsData
from scripts.engine.world_objects.game_map import GameMap
from scripts.nqp.actions.affliction import BoggedDown, Flaming
from scripts.nqp.actions.behaviour import FollowPlayer, SearchAndAttack, SkipTurn
from scripts.nqp.actions.skill import BasicAttack, Lunge, Move, Splash, TarAndFeather
from scripts.nqp.processors.game import GameEventSubscriber
from scripts.nqp.ui_elements.camera import camera
from scripts.nqp.ui_elements.character_selector import CharacterSelector
from scripts.nqp.ui_elements.skill_bar import SkillBar
from scripts.nqp.ui_elements.title_screen import TitleScreen

__all__ = [
    "initialise_game",
    "goto_character_select",
    "load_game",
    "exit_game",
    "win_game",
    "register_actions",
    "get_element_rect",
]


def initialise_game():
    """
    Init the game`s required info
    """
    register_actions()
    init_subscribers()

    if DEBUG_START:
        _start_debug_game()
    else:
        state.set_new(GameState.MENU)

        goto_to_title()


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
        height=Height.MIDDLING,
    )
    game_map.generate_new_map(player_data)
    logging.info(game_map.generation_info)

    # init the player
    player = world.get_player()

    # tell places about the player
    chronicle.set_turn_holder(player)

    # create actor near to player
    player_pos = world.get_entitys_component(player, Position)
    actor_data = library.ACTORS["crocturion"]
    world.create_actor(actor_data, (player_pos.x, player_pos.y - 2))

    # create god
    god_data = library.GODS["the_small_gods"]
    world.create_god(god_data)

    # update draw position for all entities
    for entity, (aesthetic, position) in world.get_components([Aesthetic, Position]):
        assert isinstance(aesthetic, Aesthetic)
        assert isinstance(position, Position)
        aesthetic.draw_x, aesthetic.draw_y = (position.x, position.y)
        aesthetic.target_draw_x = aesthetic.draw_x
        aesthetic.target_draw_y = aesthetic.draw_y

    # entities load with a blank fov, update them now
    system.process_light_map()
    system.process_fov()
    system.process_tile_visibility()

    # point the camera at the player, now that FOV is updated
    camera.set_target((player_pos.x, player_pos.y), True)

    # create terrain next to the player
    world.create_terrain(library.TERRAIN["bog"], (player_pos.x + 1, player_pos.y))

    # loading finished, give player control
    state.set_new(GameState.GAME_MAP)

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
    god_data = library.GODS["the_small_gods"]
    world.create_god(god_data)

    # show the in game screens
    # message_log = MessageLog(get_element_rect(UIElement.MESSAGE_LOG), ui.get_gui_manager())
    # ui.register_element(UIElement.MESSAGE_LOG, message_log)
    # ui.set_element_visibility(UIElement.MESSAGE_LOG, True)

    skill_bar = SkillBar(get_element_rect(UIElement.SKILL_BAR), ui.get_gui_manager())
    ui.register_element(UIElement.SKILL_BAR, skill_bar)
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
    system.process_light_map()
    system.process_fov()
    system.process_tile_visibility()

    # point the camera at the player, now that FOV is updated
    pos = world.get_entitys_component(player, Position)
    camera.set_target((pos.x, pos.y), True)

    # loading finished, give player control
    state.set_new(GameState.GAME_MAP)

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

    # move camera to player
    player_pos = world.get_entitys_component(world.get_player(), Position)
    camera.set_target((player_pos.x, player_pos.y), True)

    # show UI
    skill_bar = SkillBar(get_element_rect(UIElement.SKILL_BAR), ui.get_gui_manager())
    ui.register_element(UIElement.SKILL_BAR, skill_bar)
    ui.set_element_visibility(UIElement.SKILL_BAR, True)

    # welcome message
    ui.create_screen_message("Welcome back to Not Quite Paradise")

    # loading finished, give player control
    state.set_new(GameState.GAME_MAP)


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
    character_select = CharacterSelector(get_element_rect(UIElement.CHARACTER_SELECTOR), ui.get_gui_manager())
    ui.register_element(UIElement.CHARACTER_SELECTOR, character_select)
    ui.set_element_visibility(UIElement.CHARACTER_SELECTOR, True)


def goto_to_title():
    """
    Quit out of the game back to the title screen
    """
    state.set_new(GameState.MENU)

    # remove any existing ui
    ui.kill_all_elements()

    # clear existing resource
    store.current_game_map = None  # TODO - add better clearing method.

    # show the title screen
    title_screen = TitleScreen(get_element_rect(UIElement.TITLE_SCREEN), ui.get_gui_manager())
    ui.register_element(UIElement.TITLE_SCREEN, title_screen)
    ui.set_element_visibility(UIElement.TITLE_SCREEN, True)


################## INIT ##########################


def register_actions():
    """
    Register all Actions with the engine
    """
    # afflictions
    register_action(BoggedDown)
    register_action(Flaming)

    # behaviour
    register_action(SkipTurn)
    register_action(FollowPlayer)
    register_action(SearchAndAttack)

    # skills
    register_action(Move)
    register_action(BasicAttack)
    register_action(Lunge)
    register_action(TarAndFeather)
    register_action(Splash)


def init_subscribers():
    """
    Initialise event subscribers.

    N.B. When init'd they are held in reference by the event hub and do not need to be referred to directly.
    """
    game_subscriber = GameEventSubscriber()


##################### UI ######################


def get_element_rect(element_type: UIElement) -> pygame.Rect:
    """
    Get the predefined rect for the specified element.
    """
    desired_width = ui.desired_width
    desired_height = ui.desired_height

    # Message Log
    message_width = int(desired_width * 0.31)
    message_height = int(desired_height * 0.28)
    message_x = 0
    message_y = -message_height

    # Skill Bar
    skill_width = (MAX_SKILLS * (SKILL_BUTTON_SIZE + GAP_SIZE)) + (GAP_SIZE * 2)  # gap * 2 for borders
    skill_height = SKILL_BUTTON_SIZE + (GAP_SIZE * 2)
    skill_x = (desired_width // 2) - (skill_width // 2)
    skill_y = -SKILL_BUTTON_SIZE

    # Title Screen
    title_screen_width = desired_width
    title_screen_height = desired_height
    title_screen_x = 0
    title_screen_y = 0

    # Dungeon dev view
    dungen_viewer_width = desired_width
    dungen_viewer_height = desired_height
    dungen_viewer_x = 0
    dungen_viewer_y = 0

    # Tile Info
    tile_info_width = int(desired_width * 0.19)
    tile_info_height = int(desired_height * 0.22)
    tile_info_x = -tile_info_width
    tile_info_y = -tile_info_height

    # Npc info
    npc_info_width = desired_width / 2
    npc_info_height = desired_height - (desired_height / 4)
    npc_info_x = 5
    npc_info_y = 10

    # character selector
    char_selector_width = desired_width
    char_selector_height = desired_height
    char_selector_x = 0
    char_selector_y = 0

    layout = {
        UIElement.MESSAGE_LOG: pygame.Rect((message_x, message_y), (message_width, message_height)),
        UIElement.TILE_INFO: pygame.Rect((tile_info_x, tile_info_y), (tile_info_width, tile_info_height)),
        UIElement.SKILL_BAR: pygame.Rect((skill_x, skill_y), (skill_width, skill_height)),
        UIElement.DUNGEN_VIEWER: pygame.Rect(
            (dungen_viewer_x, dungen_viewer_y), (dungen_viewer_width, dungen_viewer_height)
        ),
        UIElement.ACTOR_INFO: pygame.Rect((npc_info_x, npc_info_y), (npc_info_width, npc_info_height)),
        UIElement.TITLE_SCREEN: pygame.Rect(
            (title_screen_x, title_screen_y), (title_screen_width, title_screen_height)
        ),
        UIElement.CHARACTER_SELECTOR: pygame.Rect(
            (char_selector_x, char_selector_y), (char_selector_width, char_selector_height)
        ),
    }

    return layout[element_type]
