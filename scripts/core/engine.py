import pygame
import tcod

from scripts.core.constants import TILE_SIZE, GameStates, DEBUG_FONT
from scripts.core.global_data import world_manager, game_manager, entity_manager, turn_manager, ui_manager
from scripts.core.input import get_input, handle_input
from scripts.core.intialisers import initialise_game

main_surface = None


def main():
    """The container for the game init and game loop"""

    global main_surface

    main_surface = initialise_game()
    game_loop()

    # we've left the game loop so now leave the game
    pygame.quit()  # clean up pygame resources
    raise SystemExit  # exit window and python


def game_loop():

    # TODO enforce loop timestep
    while not game_manager.game_state == GameStates.EXIT_GAME:

        if game_manager.game_state == GameStates.PLAYER_TURN:
            # HANDLE INPUT
            # determine the action to take from the input with the context of the game state
            input_values = get_input()
            handle_input(input_values)

        elif game_manager.game_state == GameStates.ENEMY_TURN:
            turn_manager.turn_holder.ai.take_turn()

        # HANDLE UPDATE
        game_manager.event_hub.update()

        if world_manager.player_fov_is_dirty:
            player = entity_manager.player
            world_manager.recompute_player_fov(player.x, player.y, player.sight_range)

        # DRAW
        draw_game()


def draw_game():
    global main_surface

    main_surface.fill((0,0,0)) # TODO remove magic number

    draw_map(world_manager.game_map)
    draw_entities(world_manager.game_map)
    draw_debug_info()

    # update the display
    pygame.display.flip()


def draw_map(game_map):

    for x in range(0, game_map.width):
        for y in range(0, game_map.height):

            if game_map.is_tile_visible(x, y):
                tile_position = (x * TILE_SIZE, y * TILE_SIZE)
                main_surface.blit(game_map.tiles[x][y].sprite, tile_position)


def draw_entities(game_map):
    for entity in entity_manager.entities:
        if game_map.is_tile_visible(entity.x, entity.y):
            main_surface.blit(entity.sprite, (entity.x * TILE_SIZE, entity.y * TILE_SIZE))


def draw_debug_info():
    info_to_display = f"The current time is:{turn_manager.time}"
    DEBUG_FONT.render_to(main_surface, (0, 0), info_to_display, ui_manager.palette.debug_font_colour)


if __name__ == "__main__":  # prevents being run from other modules
    main()
