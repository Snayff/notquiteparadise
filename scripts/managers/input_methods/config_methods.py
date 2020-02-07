from scripts.core.constants import InputModes


class ConfigMethods:
    """
    Methods for handling configuration of the Input

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.input_manager import InputManager
        self._manager = manager  # type: InputManager

        self.mode = None

        self.set_input_mode(InputModes.MOUSE_AND_KB)

    def set_input_mode(self, mode: InputModes):
        """
        Set the input mode being used.

        Args:
            mode ():
        """
        self.mode = mode