import json


def save_game(player, entities, game_map, message_log, game_state):
    data = {
        'player_index': entities.index(player),
        'entities': [entity.to_json() for entity in entities],
        'game_map': game_map.to_json(),
        'message_log': message_log.to_json(),
        'game_state': game_state.value
    }

    with open('Data/Save/save_game.json', 'w') as save_file:  # TODO move save path to global/config
        json.dump(data, save_file, indent=4)


def load_game():
    # imports enclosed in method to prevent ciruclar dependencies

    with open('Data/Save/save_game.json') as save_file:
        data = json.load(save_file)

    # player_index = data['player_index']
    # entities_json = data['entities']
    # game_map_json = data['game_map']
    # message_log_json = data['message_log']
    # game_state_json = data['game_state']
    #
    # from Code.Entities.entity import Entity
    # entities = [Entity.from_json(entity_json) for entity_json in entities_json]
    #
    # player = entities[player_index]
    #
    # from Code.Map.game_map import GameMap
    # game_map = GameMap.from_json(game_map_json)
    #
    # from Code.Core.game_messages import MessageLog
    # message_log = MessageLog.from_json(message_log_json)
    #
    # from Code.Core.constants import GameStates
    # game_state = GameStates(game_state_json)
    #
    # return player, entities, game_map, message_log, game_state
