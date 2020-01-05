from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Position:
    """
    An entity's position on the map.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

