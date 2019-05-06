import pygame

from scripts.core.constants import GameStates, TILE_SIZE, MessageEventTypes
from scripts.core.global_data import entity_manager, game_manager, ui_manager, world_manager, debug_manager
from scripts.events.entity_events import UseSkillEvent, MoveEvent
from scripts.events.game_events import ExitEvent, ChangeGameStateEvent
from scripts.events.message_events import MessageEvent


def get_input():
    """
    Get the pygame event, update the input_values dictionary and return input_values.

    Returns:
        Dict[] : `input_values` containing True for all appropriate inputs, and Tuple[int,int] for the `mouse_xy`.

    """
    # gets mouse and key input as list of events
    input_events = pygame.event.get()

    # init input values
    input_values = {
        "left_click": False,
        "right_click": False,
        "middle_click": False,
        "mouse_moved": False,
        "up": False,
        "down": False,
        "left": False,
        "right": False,
        "up_right": False,
        "up_left": False,
        "down_right": False,
        "down_left": False,
        "wait": False,
        "interact": False,
        "inventory": False,
        "drop": False,
        "character": False,
        "fullscreen": False,
        "confirm": False,
        "cancel": False,
        "new_game": False,
        "load_game": False,
        "debug_toggle": False,
        "skill": -1

    }

    # check all input events
    for input in input_events:

        # update MOUSE input values based on input
        if input.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_input(input_values)

        if input.type == pygame.MOUSEMOTION:
            input_values["mouse_moved"] = True

        # is a key pressed?
        if input.type == pygame.KEYDOWN:

            # movement
            if input.key == pygame.K_UP or input.key == pygame.K_KP8 or input.key == pygame.K_k:
                input_values["up"] = True
            elif input.key == pygame.K_DOWN or input.key == pygame.K_KP2 or input.key == pygame.K_j:
                input_values["down"] = True
            elif input.key == pygame.K_LEFT or input.key == pygame.K_KP4 or input.key == pygame.K_h:
                input_values["left"] = True
            elif input.key == pygame.K_RIGHT or input.key == pygame.K_KP6 or input.key == pygame.K_l:
                input_values["right"] = True
            elif input.key == pygame.K_KP7 or input.key == pygame.K_y:
                input_values["up_left"] = True
            elif input.key == pygame.K_KP9 or input.key == pygame.K_u:
                input_values["up_right"] = True
            elif input.key == pygame.K_KP1 or input.key == pygame.K_b:
                input_values["down_left"] = True
            elif input.key == pygame.K_KP3 or input.key == pygame.K_n:
                input_values["down_right"] = True
            elif input.key == pygame.K_z or input.key == pygame.K_KP5:
                input_values["wait"] = True

            # interactions
            if input.key == pygame.K_RETURN:
                input_values["confirm"] = True
            elif input.key == pygame.K_1:
                input_values["skill"] = 0
            elif input.key == pygame.K_2:
                input_values["skill"] = 1
            elif input.key == pygame.K_3:
                input_values["skill"] = 2
            elif input.key == pygame.K_4:
                input_values["skill"] = 3
            elif input.key == pygame.K_5:
                input_values["skill"] = 4

            # game functions
            if input.key == pygame.K_RETURN and pygame.K_LALT:
                # Alt+Enter: toggle full screen
                input_values["fullscreen"] = True
            elif input.key == pygame.K_ESCAPE:
                input_values["cancel"] = True
            elif input.key == pygame.K_TAB:
                input_values["debug_toggle"] = True

    return input_values


def check_mouse_input(input_values):
    """

    Args:
        input_values:
    """

    if pygame.mouse.get_pressed()[0]:
        input_values["left_click"] = True
    elif pygame.mouse.get_pressed()[1]:
        input_values["middle_click"] = True
    elif pygame.mouse.get_pressed()[2]:
        input_values["right_click"] = True


def handle_input(values):
    """
    Process the user input into game action by interpreting the value in relation to the `GameState`.

    Args:
        values (Dict[]): User input events.

    """
    game_state = game_manager.game_state

    # game state agnostic
    if game_state:
        if values["debug_toggle"]:
            if debug_manager.visible:
                debug_manager.set_visibility(False)
            else:
                debug_manager.set_visibility(True)

    if game_state == GameStates.PLAYER_TURN:
        handle_player_turn_input(values)

    if game_state == GameStates.TARGETING_MODE:
        handle_targeting_mode_input(values)

    if game_state == GameStates.PLAYER_DEAD:
        if values["inventory"]:
            return {"show_inventory": True}
        elif values["fullscreen"]:
            return {"fullscreen": True}
        elif values["cancel"]:
            return {"exit": True}


def handle_player_turn_input(input_values):
    """

    Args:
        input_values:

    """
    values = input_values
    player = world_manager.player

    # UI interactions
    if values["right_click"] or values["left_click"]:
        pos = ui_manager.get_scaled_mouse_pos()
        for key, ui_object in ui_manager.visible_elements.items():
            if hasattr(ui_object, "panel"):
                if ui_object.panel.rect.collidepoint(pos):
                    clicked_rect = key

    if values["right_click"]:
        # right clicked on the map so give the selected tile to the ui manager to display info
        if clicked_rect == "game_map":
            tile_pos = ui_manager.get_relative_scaled_mouse_pos(clicked_rect)
            tile_x = tile_pos[0] // TILE_SIZE
            tile_y = tile_pos[1] // TILE_SIZE
            entity = world_manager.entity_query.get_entity_in_fov_at_tile(tile_x, tile_y)

            if entity:
                ui_manager.entity_info.set_selected_entity(entity)

    if values["left_click"]:

        # if we clicked the skill bar
        if clicked_rect == "skill_bar":
            relative_mouse_pos = ui_manager.get_relative_scaled_mouse_pos(clicked_rect)
            skill_number = ui_manager.skill_bar.get_skill_index_from_skill_clicked(relative_mouse_pos[0],
                                                                                   relative_mouse_pos[1])
            # if we clicked a skill in the skill bar create the targeting overlay
            if skill_number != -1:
                if len(player.actor.known_skills) > skill_number:
                    if player.actor.known_skills[skill_number]:
                        skill_name = player.actor.known_skills[skill_number].name
                        game_manager.create_event((UseSkillEvent(player, (0, 0), skill_name)))

    # movement
    direction_x = 0
    direction_y = 0

    if values["up"]:
        direction_x = 0
        direction_y = -1
    elif values["down"]:
        direction_x = 0
        direction_y = 1
    elif values["left"]:
        direction_x = -1
        direction_y = 0
    elif values["right"]:
        direction_x = 1
        direction_y = 0
    elif values["up_left"]:
        direction_x = -1
        direction_y = -1
    elif values["up_right"]:
        direction_x = 1
        direction_y = -1
    elif values["down_left"]:
        direction_x = -1
        direction_y = 1
    elif values["down_right"]:
        direction_x = 1
        direction_y = 1

    # if destination isn't 0 then we need to move player
    if direction_x != 0 or direction_y != 0:
        target_x, target_y = direction_x + player.x, direction_y + player.y

        # is there something in the way?
        in_bounds = world_manager.game_map.is_tile_in_bounds(target_x, target_y)
        tile_blocking_movement = world_manager.game_map.is_tile_blocking_movement(target_x, target_y)
        entity_blocking_movement = world_manager.entity_query.get_blocking_entity_at_location(target_x, target_y)

        if in_bounds:
            if not entity_blocking_movement and tile_blocking_movement:
                # no entity in way but tile is blocked
                msg = f"You can't do that there!"
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
            elif entity_blocking_movement:
                # entity blocking tile so attack
                skill_name = player.actor.known_skills[0].name
                game_manager.create_event((UseSkillEvent(player, (target_x, target_y), skill_name)))
            elif not entity_blocking_movement and not tile_blocking_movement:
                # nothing in the way, time to move!
                game_manager.create_event(MoveEvent(player, (target_x, target_y)))

    # Skill usage
    if values["skill"] != -1:
        skill_number = values["skill"]
        # check we actually have that skill
        # Note: this might bite me later if we can assign to any skill slot and not have preceding ones filled
        if len(player.actor.known_skills) > skill_number:
            skill = player.actor.known_skills[skill_number]
            if skill:

                mouse_x, mouse_y = ui_manager.get_relative_scaled_mouse_pos("game_map")
                target_x, target_y = world_manager.convert_xy_to_tile(mouse_x, mouse_y)
                blocking_entity_at_location = world_manager.entity_query.get_blocking_entity_at_location(target_x, target_y)

                # is there an entity to target?
                if blocking_entity_at_location:
                    # is the entity within range?
                    distance_to_entity = world_manager.entity_query.get_chebyshev_distance_between_entities(player,
                        blocking_entity_at_location)
                    if distance_to_entity <= skill.range:
                        target_x = blocking_entity_at_location.x
                        target_y = blocking_entity_at_location.y
                    else:
                        target_x, target_y = 0, 0
                else:
                    target_x, target_y = 0, 0
                # create a skill with a target, or not
                skill_name = player.actor.known_skills[skill_number].name
                game_manager.create_event((UseSkillEvent(player, (target_x, target_y), skill_name)))
            else:
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, "There is nothing in that skill slot."))
        else:
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, "You haven't learnt that many skills yet."))

    if values["wait"]:
        # TODO - add wait
        pass

    elif values["cancel"]:
        game_manager.create_event(ExitEvent())


def handle_targeting_mode_input(input_values):
    """

    Args:
        input_values:
    """
    values = input_values
    player = world_manager.player
    mouse_x, mouse_y = ui_manager.get_scaled_mouse_pos()
    mouse_tile_x, mouse_tile_y = world_manager.convert_xy_to_tile(mouse_x, mouse_y)

    # cancel out
    if values["cancel"]:
        previous_state = game_manager.previous_game_state
        game_manager.create_event(ChangeGameStateEvent(previous_state))

    # Selected tile
    direction_x = 0
    direction_y = 0

    if values["up"]:
        direction_x = 0
        direction_y = -1
    elif values["down"]:
        direction_x = 0
        direction_y = 1
    elif values["left"]:
        direction_x = -1
        direction_y = 0
    elif values["right"]:
        direction_x = 1
        direction_y = 0
    elif values["up_left"]:
        direction_x = -1
        direction_y = -1
    elif values["up_right"]:
        direction_x = 1
        direction_y = -1
    elif values["down_left"]:
        direction_x = -1
        direction_y = 1
    elif values["down_right"]:
        direction_x = 1
        direction_y = 1

    # get selected tile from ui
    selected_tile = ui_manager.targeting_overlay.selected_tile

    # if direction isn't 0 then we need to move selected_tile
    if direction_x != 0 or direction_y != 0:
        tile_x, tile_y = direction_x + selected_tile.x, direction_y + selected_tile.y
        tile = world_manager.game_map.get_tile(tile_x, tile_y)
        ui_manager.targeting_overlay.set_selected_tile(tile)
        entity = world_manager.entity_query.get_blocking_entity_at_location(tile.x, tile.y)
        ui_manager.entity_info.set_selected_entity(entity)

    # if mouse moved update selected tile
    if values["mouse_moved"]:
        tile = world_manager.game_map.get_tile(mouse_tile_x, mouse_tile_y)
        ui_manager.targeting_overlay.set_selected_tile(tile)
        entity = world_manager.entity_query.get_blocking_entity_at_location(tile.x, tile.y)
        ui_manager.entity_info.set_selected_entity(entity)

    # confirm usage
    skill_being_targeted = ui_manager.targeting_overlay.skill_being_targeted
    skill_number = values["skill"]
    # check the skill value has been set
    if values["skill"] != -1:

        if values["skill"] == player.actor.known_skills.index(skill_being_targeted) or values["confirm"]:

            # if entity selected then use skill
            if world_manager.entity_query.get_blocking_entity_at_location(selected_tile.x, selected_tile.y):
                skill_name = player.actor.known_skills[skill_number].name
                game_manager.create_event((UseSkillEvent(player, (selected_tile.x, selected_tile.y), skill_name)))

        # pressed another skill so swap to that one
        elif values["skill"] != player.actor.known_skills.index(skill_being_targeted) :
            skill_name = player.actor.known_skills[skill_number].name
            game_manager.create_event((UseSkillEvent(player, (0, 0), skill_name)))

    if values["left_click"]:
        # if entity selected then use skill
        if world_manager.entity_query.get_blocking_entity_at_location(selected_tile.x, selected_tile.y):
            game_manager.create_event((UseSkillEvent(player, (selected_tile.x, selected_tile.y),
                                                     skill_being_targeted.name)))