from __future__ import annotations

from typing import TYPE_CHECKING
from scripts.engine.core.constants import InputModes

if TYPE_CHECKING:
    from scripts.managers.input_manager.input_manager import InputManager


class ConfigMethods:
    """
    Methods for handling configuration of the Input

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        self._manager: InputManager = manager

        self.mode = None

        self.set_input_mode(InputModes.MOUSE_AND_KB)

    def set_input_mode(self, mode: InputModes):
        """
        Set the input mode being used.

        Args:
            mode ():
        """
        self.mode = mode