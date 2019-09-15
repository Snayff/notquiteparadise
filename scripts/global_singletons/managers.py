
from scripts.managers.debug_manager import DebugManager
from scripts.managers.game_manager import GameManager
from scripts.managers.input_manager import InputManager
from scripts.managers.turn_manager import TurnManager
from scripts.managers.ui_manager import UIManager
from scripts.managers.world_manager import WorldManager

game_manager2: GameManager

game_manager = GameManager()
world_manager = WorldManager()
turn_manager = TurnManager()
debug_manager = DebugManager()
ui_manager = UIManager()
input_manager = InputManager()


def start():
    # calling in a function like this prevents errors with importing
    global game_manager2
    game_manager2 = GameManager()  # type: GameManager

