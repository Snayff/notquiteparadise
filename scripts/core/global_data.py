from scripts.managers.debug import DebugManager
from scripts.managers.entity import EntityManager
from scripts.managers.game import GameManager
from scripts.managers.turn import TurnManager
from scripts.managers.ui import UIManager
from scripts.managers.world import WorldManager

entity_manager = EntityManager()
world_manager = WorldManager()
ui_manager = UIManager()
turn_manager = TurnManager()
game_manager = GameManager()
debug_manager = DebugManager()
