from __future__ import annotations

import logging
from typing import TYPE_CHECKING, List
from snecs import Component
from snecs.typedefs import EntityID
from scripts.engine import state, world

if TYPE_CHECKING:
    from typing import Type


# TODO - approach to type commands to trigger actions e.g. spawn creature

########################  ###########################

class _Debugger:
    def __init__(self):
        self.current_fps = 0
        self.recent_average_fps = 0
        self.average_fps = 0
        self.frames = 0

        self.fps_visible = True

    def update(self):
        self.frames += 1
        self.current_fps = state.get_internal_clock().get_fps()
        self.average_fps += (self.current_fps - self.average_fps) / self.frames

        # get recent fps
        if self.frames >= 600:
            frames_to_count = 600
        else:
            frames_to_count = self.frames
        self.recent_average_fps += (self.current_fps - self.average_fps) / frames_to_count


def update():
    """
    Update all values held in the debugger.
    """
    _debugger.update()


def dump():
    """
    Print the debuggers stats.
    """
    print(f"Avg FPS: {format(_debugger.average_fps, '.2f')}, "
          f"R_Avg: {format(_debugger.recent_average_fps, '.2f')}")


def set_fps_visibility(is_visible: bool):
    """
    Set whether the FPS is visible
    """
    # TODO - this needs to be called from somewhere
    _debugger.fps_visible = is_visible


def is_fps_visible() -> bool:
    if _debugger.fps_visible:
        return True
    else:
        return False


def get_visible_values() -> List[str]:
    """"
    Get all visible values from the debugger
    """
    values = []
    if _debugger.fps_visible:
        values.append(f"FPS: C={format(_debugger.current_fps, '.2f')}, "
                      f"R_Avg={format(_debugger.recent_average_fps, '.2f')}, "
                      f"Avg={format(_debugger.average_fps, '.2f')}")

    return values


def log_component_not_found(entity: EntityID, component: Type[Component]):
    """
    Use if component not found. Log the error as a warning in the format '{entity} tried to get {component} but it was
    not found.'
    """
    name = world.get_name(entity)
    logging.warning(f"'{name}'({entity}) tried to get {component.__name__}, but it was not found.")


_debugger = _Debugger()
