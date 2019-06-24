from scripts.managers.debug import DebugManager
from scripts.managers.game import GameManager
from scripts.managers.input import InputManager
from scripts.managers.turn import TurnManager
from scripts.managers.ui import UIManager
from scripts.managers.world import WorldManager

game_manager = GameManager()
world_manager = WorldManager()
turn_manager = TurnManager()
debug_manager = DebugManager()
ui_manager = UIManager()
input_manager = InputManager()
