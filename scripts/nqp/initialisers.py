from __future__ import annotations

from scripts.engine.core.constants import EventTopics, GameStates
from scripts.nqp.god_handler import GodHandler
from scripts.nqp.map_handler import MapHandler
from scripts.nqp.entity_handler import EntityHandler
from scripts.engine.events import ChangeGameStateEvent
from scripts.nqp.game_handler import GameHandler
from scripts.engine.core.event_core import publisher, event_hub

from scripts.managers.world_manager.world_manager import world
from scripts.managers.input_manager.input_manager import input
from scripts.nqp.ui_handler import UiHandler



