

class DebugManager:
    def __init__(self):
        self.active = True
        self.messages = []

        self.show_game_time = True
        self.show_fps = True

    def update_debug_message(self):
        self.messages = []

        if self.show_game_time:
            from scripts.core.global_data import turn_manager
            msg = f"The game time is: {turn_manager.time}"
            self.messages.append(msg)

        if self.show_fps:
            from scripts.core.global_data import game_manager
            clock = game_manager.internal_clock
            fps = str(int(clock.get_fps()))
            msg = f"The FPS is: {fps}"
            self.messages.append(msg)

    def update(self):
        if self.active:
            self.update_debug_message()