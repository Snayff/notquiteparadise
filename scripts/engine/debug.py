from __future__ import annotations

import cProfile
import datetime
import io
import logging
import pstats
import time
from typing import Optional, TYPE_CHECKING, List
from snecs import Component
from snecs.typedefs import EntityID
from scripts.engine import state, world
from scripts.engine.core.constants import INFINITE, VERSION

if TYPE_CHECKING:
    from typing import Type

# objects
PROFILER: Optional[cProfile.Profile] = None

# counters
CURRENT_FPS: int = 0
RECENT_AVERAGE_FPS: int = 0
AVERAGE_FPS: int = 0
_FRAMES: int = 0
_PROFILE_DURATION_REMAINING: int = 0

# flags
IS_FPS_VISIBLE: bool = True
IS_PROFILING: bool = False
IS_LOGGING: bool = True

# values
_NUM_FRAMES_CONSIDERED_RECENT: int = 600


########################## UPDATE #####################################

def update():
    global _FRAMES
    global CURRENT_FPS
    global _PROFILE_DURATION_REMAINING
    global AVERAGE_FPS
    global RECENT_AVERAGE_FPS

    _FRAMES += 1
    CURRENT_FPS = state.get_internal_clock().get_fps()
    AVERAGE_FPS += (CURRENT_FPS - AVERAGE_FPS) / _FRAMES

    # count down profiler duration, if it isnt running temporarily
    if _PROFILE_DURATION_REMAINING != INFINITE:
        _PROFILE_DURATION_REMAINING -= 1

    # check if profiler needs to turn off
    if _PROFILE_DURATION_REMAINING == 0:
        disable_profiling(True)

    # get recent fps
    if _FRAMES >= _NUM_FRAMES_CONSIDERED_RECENT:
        frames_to_count = _NUM_FRAMES_CONSIDERED_RECENT
    else:
        frames_to_count = _FRAMES
    RECENT_AVERAGE_FPS += (CURRENT_FPS - AVERAGE_FPS) / frames_to_count


########################## LOGGING AND PROFILING #####################################

def initialise_logging():
    """
    Initialise logging.
    """
    # Logging levels:
    #     CRITICAL - A serious error, indicating that may be unable to continue running.
    #     ERROR - A more serious problem, has not been able to perform some function.
    #     WARNING - An indication that something unexpected happened, but otherwise still working as expected.
    #     INFO - Confirmation that things are working as expected.
    #     DEBUG - Detailed information, typically of interest only when diagnosing problems
    #
    # File mode options:
    #     'r' - open for reading(default)
    #     'w' - open for writing, truncating the file first
    #     'x' - open for exclusive creation, failing if the file already exists
    #     'a' - open for writing, appending to the end of the file if it exists

    global IS_LOGGING
    IS_LOGGING = True

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
    global PROFILER
    if not PROFILER:
        PROFILER = cProfile.Profile()


def enable_profiling(duration: int = INFINITE):
    """
    Enable profiling. Create profiler if one doesnt exist
    """
    global IS_PROFILING
    global _PROFILE_DURATION_REMAINING

    # if we dont have a profiler create one
    if not PROFILER:
        create_profiler()

    # enable, set flag and set duration
    assert isinstance(PROFILER, cProfile.Profile)
    PROFILER.enable()
    IS_PROFILING = True
    _PROFILE_DURATION_REMAINING = duration


def disable_profiling(dump_data: bool = False):
    """
    Turn off current profiling. Dump data to file if required.
    """
    global PROFILER
    global IS_PROFILING

    if PROFILER:
        assert isinstance(PROFILER, cProfile.Profile)
        PROFILER.disable()
        IS_PROFILING = False

        if dump_data:
            _dump_profiling_data()


def kill_profiler():
    """
    Kill profiling resource
    """
    global PROFILER

    if PROFILER:
        disable_profiling(False)
        PROFILER = None


def kill_logging():
    """
    Kill logging resources
    """
    global IS_LOGGING

    logging.shutdown()
    IS_LOGGING = False


def _dump_profiling_data():
    """
    Dump data to a readable file
    """
    # dump the profiler stats
    s = io.StringIO()
    ps = pstats.Stats(PROFILER, stream=s).sort_stats("cumulative")
    ps.dump_stats("logs/profiling/profile.dump")

    # convert profiling to human readable format
    date_and_time = datetime.datetime.utcnow()
    out_stream = open("logs/profiling/" + date_and_time.strftime("%Y%m%d@%H%M") + "_" + VERSION + ".profile", "w")
    ps = pstats.Stats("logs/profiling/profile.dump", stream=out_stream)
    ps.strip_dirs().sort_stats("cumulative").print_stats()


########################## GET OR SET VALUES #####################################

def print_values_to_console():
    """
    Print the debuggers stats.
    """
    print(f"Avg FPS: {format(AVERAGE_FPS, '.2f')}, "
          f"R_Avg: {format(RECENT_AVERAGE_FPS, '.2f')}")


def set_fps_visibility(is_visible: bool = True):
    """
    Set whether the FPS is visible
    """
    global IS_FPS_VISIBLE
    IS_FPS_VISIBLE = is_visible


def get_visible_values() -> List[str]:
    """
    Get all visible values from the debugger
    """
    values = []
    if IS_FPS_VISIBLE:
        values.append(f"FPS: C={format(CURRENT_FPS, '.2f')}, "
                      f"R_Avg={format(RECENT_AVERAGE_FPS, '.2f')}, "
                      f"Avg={format(AVERAGE_FPS, '.2f')}")

    return values


########################## DEBUG FUNCTIONS #####################################

def log_component_not_found(entity: EntityID, component: Type[Component]):
    """
    Use if component not found. Log the error as a warning in the format '{entity} tried to get {component} but it was
    not found.'
    """
    name = world.get_name(entity)
    logging.warning(f"'{name}'({entity}) tried to get {component.__name__}, but it was not found.")




