from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import esper


class MovementProcessor(esper.Processor):
    """Processor to handle the movement of entities"""

    def process(self):
        for ent, (vel, pos) in self.world.get_components(Velocity, Position):
            pos.x += vel.x
            pos.y += vel.y