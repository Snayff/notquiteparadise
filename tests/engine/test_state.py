import os

import pytest

from scripts.engine.core import state
from scripts.engine.internal.constant import GameState, Height, SAVE_PATH

# N.B. parametrize errors out with only 1 arg so add second unused arg.
test_set_state_parameters = [
    (GameState.LOADING, 0),
    (GameState.GAME_MAP, 0),
    (GameState.PLAYER_DEAD, 0),
    (GameState.TARGETING, 0),
    (GameState.EXITING, 0),
    (GameState.DEVELOPER, 0),
    (GameState.MENU, 0),
]


@pytest.mark.parametrize(["game_state", "_"], test_set_state_parameters)
def test_set_state(game_state: GameState, _):
    """
    Test changing the state
    """
    state.set_new(game_state)
    assert state.get_current() == game_state
    state.set_new(GameState.GAME_MAP)
    assert state.get_previous() == game_state


def _init_world():
    # create clean snecs.world
    import snecs
    empty_world = snecs.World()
    from scripts.engine.core import world
    world.move_world(empty_world)

    # init and save map
    from scripts.engine.world_objects.game_map import GameMap
    game_map = GameMap("debug", 10)
    from scripts.engine.internal.data import store
    store.current_game_map = game_map

    # populate the map
    from scripts.engine.internal.definition import ActorData
    player_data = ActorData(
        key="player",
        possible_names=["player"],
        description="Player desc",
        position_offsets=[(0, 0)],
        trait_names=["shoom", "soft_tops", "dandy"],
        height=Height.MIDDLING,
    )
    game_map.generate_new_map(player_data)

    # init the player
    player = world.get_player()

    # tell places about the player
    from scripts.engine.core import chronicle
    chronicle.set_turn_holder(player)

    # create actor near to player
    from scripts.engine.core.component import Position
    player_pos = world.get_entitys_component(player, Position)
    from scripts.engine.internal import library
    actor_data = library.ACTORS["crocturion"]
    world.create_actor(actor_data, (player_pos.x, player_pos.y - 2))

    # create god
    god_data = library.GODS["the_small_gods"]
    world.create_god(god_data)

    # create terrain next to the player
    world.create_terrain(library.TERRAIN["bog"], (player_pos.x + 1, player_pos.y))


def test_save_game(benchmark):
    _init_world()
    benchmark(state.save_game)


def test_dump_save_game(benchmark):
    _init_world()
    state.save_game()
    benchmark(state.dump_save_game)


def test_load_game(benchmark):
    full_save_path = str(SAVE_PATH)
    for save_name in os.listdir(full_save_path):
        save = save_name.replace(".json", "")
        benchmark(state.load_game, save)
        break


