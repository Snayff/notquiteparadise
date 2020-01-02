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

        from scripts.managers.ui_manager import ui
        mouse_pos = ui.Mouse.get_scaled_mouse_pos()
        self.mouse_x = mouse_pos[0]
        self.mouse_y = mouse_pos[1]
        self.button_pressed = button_pressed


class SelectEntity(Event):
    """
    Event for selecting an entity.
    """
    def __init__(self, entity):
        Event.__init__(self, UIEventTypes.SELECT_ENTITY, EventTopics.UI)

        self.selected_entity = entity
