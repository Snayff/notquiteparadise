from __future__ import annotations

import cProfile
import datetime
import io
import logging
import pstats
import time
from typing import TYPE_CHECKING, List

from snecs import Component
from snecs.typedefs import EntityID

from scripts.engine import state, world
from scripts.engine.core.constants import INFINITE, VERSION

if TYPE_CHECKING:
    from typing import Type


class _Debugger:
    def __init__(self):
        # objects
        self.profiler = None

        # counters
        self.current_fps = 0
        self.recent_average_fps = 0
        self.average_fps = 0
        self.frames = 0
        self.profile_duration_remaining = 0

        # flags
        self.fps_visible = True
        self.profiling = False
        self.logging = True

    def update(self):
        self.frames += 1
        self.current_fps = state.get_internal_clock().get_fps()
        self.average_fps += (self.current_fps - self.average_fps) / self.frames

        # count down profiler duration, if it isnt running temporarily
        if self.profile_duration_remaining != INFINITE:
            self.profile_duration_remaining -= 1

        # get recent fps
        if self.frames >= 600:
            frames_to_count = 600
        else:
            frames_to_count = self.frames
        self.recent_average_fps += (self.current_fps - self.average_fps) / frames_to_count

        # check if profiler needs to turn off
        if self.profile_duration_remaining == 0:
            disable_profiling(True)


########################## FUNCTIONS #####################################

def update():
    """
    Update all values held in the debugger.
    """
    _debugger.update()


def print_values_to_console():
    """
    Print the debuggers stats.
    """
    print(f"Avg FPS: {format(_debugger.average_fps, '.2f')}, "
          f"R_Avg: {format(_debugger.recent_average_fps, '.2f')}")


def set_fps_visibility(is_visible: bool):
    """
    Set whether the FPS is visible
    """
    _debugger.fps_visible = is_visible


def is_fps_visible() -> bool:
    if _debugger.fps_visible:
        return True
    else:
        return False


def get_visible_values() -> List[str]:
    """
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


def initialise_logging():
    """
    Configure logging

    Logging levels:
        CRITICAL - A serious error, indicating that may be unable to continue running.
        ERROR - A more serious problem, has not been able to perform some function.
        WARNING - An indication that something unexpected happened, but otherwise still working as expected.
        INFO - Confirmation that things are working as expected.
        DEBUG - Detailed information, typically of interest only when diagnosing problems

    File mode options:
        'r' - open for reading(default)
        'w' - open for writing, truncating the file first
        'x' - open for exclusive creation, failing if the file already exists
        'a' - open for writing, appending to the end of the file if it exists

    """
    _debugger.logging = True

    log_file_name = "logs/" + "game.log"
    log_level = logging.DEBUG
    file_mode = "w"

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # 8 adds space for 8 characters (# CRITICAL)
    log_format = "%(asctime)s| %(levelname)-8s| %(message)s"
    logging.basicConfig(filename=log_file_name, filemode=file_mode, level=log_level,
                        format=log_format)

    # format into uk time
    logging.Formatter.converter = time.gmtime


def create_profiler():
    """
    Create the profiler. If it exists does nothing.
    """
    if not _debugger.profiler:
        _debugger.profiler = cProfile.Profile()


def enable_profiling(duration: int = INFINITE):
    """
    Enable profiling. Create profiler if one doesnt exist
    """
    if not _debugger.profiler:
        create_profiler()

    _debugger.profiler.enable()
    _debugger.profiling = True
    _debugger.profile_duration_remaining = duration


def disable_profiling(dump_data: bool = False):
    """
    Turn off current profiling. Dump data to file if required.
    """
    if _debugger.profiler:
        _debugger.profiler.disable()
        _debugger.profiling = False

        if dump_data:
            _dump_profiling_data()


def kill_profiler():
    """
    Kill profiling resource
    """
    if _debugger.profiler:
        disable_profiling(False)
        _debugger.profiler = None


def kill_logging():
    """
    Kill logging resources
    """
    logging.shutdown()
    _debugger.logging = False


def _dump_profiling_data():
    """
    Dump data to a readable file
    """
    profiler = _debugger.profiler

    # dump the profiler stats
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
    ps.dump_stats("logs/profiling/profile.dump")

    # convert profiling to human readable format
    date_and_time = datetime.datetime.utcnow()
    out_stream = open("logs/profiling/" + date_and_time.strftime("%Y%m%d@%H%M") + "_" + VERSION + ".profile", "w")
    ps = pstats.Stats("logs/profiling/profile.dump", stream=out_stream)
    ps.strip_dirs().sort_stats("cumulative").print_stats()


def is_profiling() -> bool:
    return _debugger.profiling


def is_logging() -> bool:
    return _debugger.logging


########################## INIT DEBUGGER #####################################

_debugger = _Debugger()
