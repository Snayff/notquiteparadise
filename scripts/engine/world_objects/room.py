from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Type

from scripts.engine.core.constants import TileCategory

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


@dataclass
class Room:
    """
    Details of a room. Used for world generation.
    """
    tile_categories: List[List[TileCategory]]  # what to place in a tile
    design: str  # algorithm used to generate
    category: str  # the type of room placed
    start_x: int = -1
    start_y: int = -1
    entities: List[str] = field(default_factory=list)


    @property
    def available_area(self) -> int:
        """
        Number of unblocked tiles.
        """
        unblocked_count = 0
        for row in self.tile_categories:
            for tile_cat in row:
                if tile_cat == TileCategory.FLOOR:
                    unblocked_count += 1
        return unblocked_count

    @property
    def total_area(self) -> int:
        """
        Number of tiles in room.
        """
        count = 0
        for row in self.tile_categories:
            for tile_cat in row:
                count += 1
        return count

    @property
    def width(self) -> int:
        """
        Widest width.
        """
        return len(self.tile_categories)

    @property
    def height(self) -> int:
        """
        Tallest height
        """
        try:
            height = len(self.tile_categories[0])
        except IndexError:
            height = 0
            logging.error("Something referenced room height before the room had any tile categories.")

        return height

    @property
    def generation_info(self) -> str:
        """
        Return the generation information about the room
        """
        gen_info = f"{self.category} | {self.design} | (w:{self.width}, h:{self.height}) " \
                   f"| available:{self.available_area}/ total:{self.total_area}."

        return gen_info

    @property
    def end_x(self) -> int:
        return self.start_x + self.width

    @property
    def end_y(self) -> int:
        return self.start_y + self.height

    def intersects(self, room: Room) -> bool:
        """
        Check if this room intersects with another.
        """
        if (self.start_x <= room.end_x and self.end_x >= room.start_x) and \
                (self.start_y <= room.end_y and self.end_y >= room.start_y):
            return True
        else:
            return False
