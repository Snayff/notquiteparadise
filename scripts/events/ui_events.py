from scripts.core.constants import UIEventTypes, EventTopics
from scripts.event_handlers.pub_sub_hub import Event


class ClickUIEvent(Event):
    """
    Event for clicking the UI

    Args:
        mouse_pos(tuple):
        button_pressed (MouseButtons):
    """
    def __init__(self, button_pressed):
        Event.__init__(self, UIEventTypes.CLICK_UI, EventTopics.UI)

        from scripts.global_singletons.managers import ui_manager
        mouse_pos = ui_manager.get_scaled_mouse_pos()
        self.mouse_x = mouse_pos[0]
        self.mouse_y = mouse_pos[1]
        self.button_pressed = button_pressed