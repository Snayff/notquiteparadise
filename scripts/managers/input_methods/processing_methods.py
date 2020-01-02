

class ProcessingMethods:
    """
    Methods for handling intents and creating events to carry out the actions

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.new_input_manager import InputManager
        self.manager = manager  # type: InputManager