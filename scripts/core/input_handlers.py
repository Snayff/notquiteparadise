import pygame

from scripts.core.constants import GameStates, EntityEventNames, EventTopics, GameEventNames
from scripts.core.events import Event
from scripts.core.global_data import entity_manager, game_manager


def get_input():

	# gets mouse and key input as list of events
	input_events = pygame.event.get()

	# init input values
	input_values = {
		"left_click": False,
		"right_click": False,
		"mouse_xy": (0, 0),
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
		"cancel": False,
		"new_game": False,
		"load_game": False

	}

	# check all input events
	for input in input_events:

		# is a key pressed?
		if input.type == pygame.KEYDOWN:

			# update MOUSE input values based on input
			if pygame.mouse.get_pressed()[0]:
				input_values["left_click"] = True
				input_values["mouse_xy"] = pygame.mouse.get_pos()
			elif pygame.mouse.get_pressed()[1]:
				input_values["right_click"] = True
				input_values["mouse_xy"] = pygame.mouse.get_pos()

			# update OTHER input values based on input
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
			elif input.key == pygame.K_i:
				input_values["inventory"] = True
			elif input.key == pygame.K_d:
				input_values["drop"] = True
			elif input.key == pygame.K_RETURN:
				input_values["interact"] = True
			elif input.key == pygame.K_c:
				input_values["character"] = True
			elif input.key == pygame.K_RETURN and pygame.K_LALT:
				# Alt+Enter: toggle full screen
				input_values["fullscreen"] = True
			elif input.key == pygame.K_ESCAPE:
				input_values["cancel"] = True
			elif input.key == pygame.K_a:
				# TODO remove this legacy when menu's can use kb+m
				input_values["new_game"] = True
			elif input.key == pygame.K_b:
				# TODO remove this legacy when menu's can use kb+m
				input_values["load_game"] = True

	return input_values


def handle_input(values):

	game_state = game_manager.game_state
	player = entity_manager.player

	game_state = GameStates.PLAYER_TURN # TODO remove once game_state is updated naturally
	if game_state == GameStates.PLAYER_TURN:
		dx = 0
		dy = 0

		if values["up"]:
			dx = 0
			dy = -1
		elif values["down"]:
			dx = 0
			dy = 1
		elif values["left"]:
			dx = -1
			dy = 0
		elif values["right"]:
			dx = 1
			dy = 0
		elif values["up_left"]:
			dx = -1
			dy = -1
		elif values["up_right"]:
			dx = 1
			dy = -1
		elif values["down_left"]:
			dx = -1
			dy = 1
		elif values["down_right"]:
			dx = 1
			dy = 1

		# if destination isnt 0 then we need to move an entity
		if dx != 0 or dy != 0:
			game_manager.create_event(Event(EntityEventNames.MOVE, EventTopics.ENTITY, [player, dx, dy]))

		if values["wait"]:
			return {"wait": True}
		elif values["inventory"]:
			return {"show_inventory": True}
		elif values["drop"]:
			return {"drop_inventory": True}
		elif values["interact"]:
			# TODO check if item on same tile
			return {"pickup": True}
			# TODO check if stairs on same tile
			return {"take_stairs": True}
		elif values["character"]:
			return {"show_character_screen": True}
		elif values["fullscreen"]:
			return {"fullscreen": True}
		elif values["cancel"]:
			print("About to create exit event")
			game_manager.create_event(Event(GameEventNames.EXIT, EventTopics.GAME, []))
			print("Exit event created")

	if game_state == GameStates.TARGETING:
		if values["cancel"]:
			return{"exit": True}

	if game_state == GameStates.PLAYER_DEAD:
		if values["inventory"]:
			return {"show_inventory": True}
		elif values["fullscreen"]:
			return {"fullscreen": True}
		elif values["cancel"]:
			return {"exit": True}

	if game_state == GameStates.SHOW_INVENTORY:
		# TODO add mouse and keyboard input
		# TODO change to generic Menu state; will need a var to hold which menu
		if values["fullscreen"]:
			return {"fullscreen": True}
		elif values["cancel"]:
			return {"exit": True}

	if game_state == GameStates.MAIN_MENU:
		pass
		# if values["new_game"]:
		# 	create_event(event_hub, Event(GameEventNames.NEW_GAME, EventTopics.GAME, []))
		# elif values["load_game"]:
		# 	return {"load_game": True}
		# elif values["cancel"]:
		# 	create_event(event_hub, Event(GameEventNames.EXIT, EventTopics.GAME, []))


