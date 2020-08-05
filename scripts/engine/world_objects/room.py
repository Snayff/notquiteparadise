from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Type

from scripts.engine.core.constants import TileCategory

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List

# 0 - floor
# 1 = wall
#



@dataclass
class Room:
    """
    Details of a room. Used for world generation.
    """
    tile_categories: List[List[TileCategory]]  # what to place in a tile
    design: str  # type of room places

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
        return len(self.tile_categories[0])

    @property
    def generation_info(self) -> str:
        """
        Return the generation information about the room
        """
        gen_info = f"{self.design} | (w:{self.width}, h:{self.height}) " \
                   f"| a:{self.available_area}/ t:{self.total_area}."

        return gen_info
