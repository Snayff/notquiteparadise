from __future__ import annotations
from typing import TYPE_CHECKING

import cProfile
import datetime
import gc
import io
import logging
import os
import pstats
import time
import timeit

from scripts.engine import state
from scripts.engine.core.constants import INFINITE, VERSION

if TYPE_CHECKING:
    from typing import Callable, TYPE_CHECKING, List, Optional, Tuple, Union

__all__ = [
    "update",
    "initialise_logging",
    "kill_logging",
    "is_logging",
    "enable_profiling",
    "disable_profiling",
    "kill_profiler",
    "performance_test",
    "is_profiling",
    "print_values_to_console",
    "set_fps_visibility",
    "get_visible_values",
]


class Debugger:
    def __init__(self):
        # objects
        self.profiler: Optional[cProfile.Profile] = None

        # counters
        self.current_fps: int = 0
        self.recent_average_fps: int = 0
        self.average_fps: int = 0
        self._frames: int = 0
        self.profile_duration_remaining: int = INFINITE

        # flags
        self.is_fps_visible: bool = False
        self.is_profiling: bool = True
        self.is_logging: bool = True

        # values
        self._num_frames_considered_recent: int = 600

    def update(self):

        self._frames += 1
        self.current_fps = state.get_internal_clock().get_fps()
        self.average_fps += (self.current_fps - self.average_fps) / self._frames

        # count down profiler duration, if it isnt running temporarily
        if self.profile_duration_remaining != INFINITE:
            self.profile_duration_remaining -= 1

        # check if profiler needs to turn off
        if self.profile_duration_remaining == 0:
            disable_profiling(True)

        # get recent fps
        if self._frames >= self._num_frames_considered_recent:
            frames_to_count = self._num_frames_considered_recent
        else:
            frames_to_count = self._frames
        self.recent_average_fps += (self.current_fps - self.average_fps) / frames_to_count


if "GENERATING_SPHINX_DOCS" not in os.environ:  # when building in CI these fail
    _debugger = Debugger()
else:
    _debugger = ""  # type: ignore


########################## UPDATE #####################################


def update():
    _debugger.update()


########################## LOGGING  #####################################


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

    _debugger.is_logging = True

    log_file_name = "logs/" + "game.log"

    # Creating directory "logs/" if it does not exist, as logging.basicConfig() appears
    # to be unable to create the directory itself, resulting in FileNotFoundError
    if not os.path.isdir("logs/"):
        os.mkdir("logs")

    log_level = logging.DEBUG
    file_mode = "w"

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # 8 adds space for 8 characters (# CRITICAL)
    log_format = "%(asctime)s| %(levelname)-8s| %(message)s"
    logging.basicConfig(filename=log_file_name, filemode=file_mode, level=log_level, format=log_format)

    # format into uk time
    logging.Formatter.converter = time.gmtime


def kill_logging():
    """
    Kill logging resources
    """
    logging.shutdown()
    _debugger.is_logging = False


def is_logging() -> bool:
    """
    Returns true if logging is active
    """
    return _debugger.is_logging


########################## PROFILING  #####################################


def _create_profiler():
    """
    Create the profiler.
    """
    _debugger.profiler = cProfile.Profile()


def enable_profiling(duration: int = INFINITE):
    """
    Enable profiling. Create profiler if one doesnt exist
    """
    # if we dont have a profiler create one
    if not _debugger.profiler:
        _create_profiler()

    # enable, set flag and set duration
    assert isinstance(_debugger.profiler, cProfile.Profile)
    _debugger.profiler.enable()
    _debugger.is_profiling = True
    _debugger.profile_duration_remaining = duration


def disable_profiling(dump_data: bool = False):
    """
    Turn off current profiling. Dump data to file if required.
    """
    if _debugger.profiler:
        if dump_data:
            _dump_profiling_data()

        _debugger.profiler.disable()
        _debugger.is_profiling = False


def kill_profiler():
    """
    Kill profiling resource
    """
    if _debugger.profiler:
        disable_profiling(True)
        _debugger.profiler = None


def _dump_profiling_data():
    """
    Dump data to a readable file
    """
    if not _debugger.is_profiling:
        return

    _ = _debugger.profiler.create_stats()

    # dump the profiler stats
    s = io.StringIO()
    ps = pstats.Stats(_debugger.profiler, stream=s).sort_stats("cumulative")
    ps.dump_stats("logs/profiling/profile.dump")

    # convert profiling to human readable format
    date_and_time = datetime.datetime.utcnow()
    out_stream = open("logs/profiling/" + date_and_time.strftime("%Y%m%d@%H%M") + "_" + VERSION + ".profile", "w")
    ps = pstats.Stats("logs/profiling/profile.dump", stream=out_stream)
    ps.strip_dirs().sort_stats("cumulative").print_stats()


def performance_test(
    method_descs: List[str],
    old_methods: List[Tuple[Union[str, Callable], str]],
    new_methods: List[Tuple[Union[str, Callable], str]],
    num_runs: int = 1000,
    repeats: int = 3,
) -> str:
    """
    Run performance testing on a collection of methods/functions. Returns a formatted string detailing performance of
     old, new and % change between them.

    method_descs are used as descriptions only.
    old_methods/new_methods expects a list of tuples that are (method_to_test, setup). Setup can be an empty string
    but is usually an import.
    Index in each list much match, i.e. method_name[0] is the alias of the methods in old_methods[0] and
    new_methods[0].

    Outputs as "Access Trait: 0.00123 -> 0.00036(71.00033%)".

    example usage:
    method_descs = ["Set Var", "Access Skill"]
    old_methods = [("x = 1", ""),("library.get_skill_data('lunge')", "")]
    new_methods = [("x = 'one'", ""), ("library2.SKILLS.get('lunge')", "from scripts.engine import library2")]
    print( performance_test(method_descs, old_methods, new_methods) )
    """
    result = f"== Performance Test ==\n(Run {num_runs} * {repeats})"
    gc.disable()

    for x in range(0, len(method_descs)):
        name = method_descs[x]
        old = min(timeit.repeat(old_methods[x][0], setup=old_methods[x][1], number=num_runs, repeat=repeats))
        new = min(timeit.repeat(new_methods[x][0], setup=new_methods[x][1], number=num_runs, repeat=repeats))
        result += (
            f"\n{name}: {format(old, '0.5f')} -> {format(new, '0.5f')}"
            f"({format(((old - new) / old) * 100, '0.2f')}%)"
        )

    gc.enable()
    return result


def is_profiling() -> bool:
    """
    Returns true if profiling is active
    """
    return _debugger.is_profiling


########################## FPS #####################################


def is_fps_visible() -> bool:
    """
    Returns true if fps stats are visible
    """
    return _debugger.is_fps_visible


########################## GET OR SET VALUES #####################################


def print_values_to_console():
    """
    Print the debuggers stats.
    """
    print(f"Avg FPS: {format(_debugger.average_fps, '.2f')}, " f"R_Avg: {format(_debugger.recent_average_fps, '.2f')}")


def set_fps_visibility(is_visible: bool = True):
    """
    Set whether the FPS is visible
    """
    _debugger.is_fps_visible = is_visible


def get_visible_values() -> List[str]:
    """
    Get all visible values from the debugger
    """
    values = []
    if _debugger.is_fps_visible:
        values.append(
            f"FPS: C={format(_debugger.current_fps, '.2f')}, "
            f"R_Avg={format(_debugger.recent_average_fps, '.2f')}, "
            f"Avg={format(_debugger.average_fps, '.2f')}"
        )

    return values
