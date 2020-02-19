from __future__ import annotations

import cProfile
import logging
import time
import io
import pstats
from typing import TYPE_CHECKING

from scripts.core.constants import VERSION

if TYPE_CHECKING:
    from scripts.managers.game_manager.game_manager import GameManager


# TODO - approach to type commands to trigger actions e.g. spawn creature
# TODO - approach to show required info, e.g. rounds & time, FPS

class DebugMethods:
    """
    Methods for taking actions with the state of the game
    """

    def __init__(self, manager):
        self._manager = manager  # type: GameManager
        self._profiler = None
        self._is_visible = False

    ######################## SET ###########################

    def set_visibility(self, visible: bool):
        """
        Set whether the debug info is visible
        """
        self._is_visible = visible

    ##################### INIT #############################

    def initialise_logging(self):
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

        log_file_name = "logs/" + "game.log"
        log_level = logging.INFO
        file_mode = "w"

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        # 8 adds space for 8 characters (# CRITICAL)
        log_format = "%(asctime)s| %(levelname)-8s| %(message)s"
        logging.basicConfig(filename=log_file_name, filemode=file_mode, level=log_level,
                            format=log_format)

        # format into uk time
        logging.Formatter.converter = time.gmtime

    def initialise_profiling(self):
        """
        Initialise and enable the profiler
        """
        self._profiler = cProfile.Profile()
        self._profiler.enable()

    ##################### CLOSE ##############################
    def disable_logging(self):
        """
        Turn off current logging and clear logging resources
        """
        logging.shutdown()

    def disable_profiling(self):
        """
        Turn off current profiling
        """
        if self._profiler:
            self._profiler.disable()

    ################## ACTIONS ##########################

    def dump_profiling_data(self):
        """
        Dump data to a readable file
        """
        # dump the profiler stats
        s = io.StringIO()
        ps = pstats.Stats(self._profiler, stream=s).sort_stats("cumulative")
        ps.dump_stats("logs/profiling/profile.dump")

        # convert profiling to human readable format
        import datetime
        date_and_time = datetime.datetime.utcnow()

        out_stream = open("logs/profiling/" + date_and_time.strftime("%y%m%d@%H%M") + "_" + VERSION + ".profile", "w")
        ps = pstats.Stats("logs/profiling/profile.dump", stream=out_stream)
        ps.strip_dirs().sort_stats("cumulative").print_stats()