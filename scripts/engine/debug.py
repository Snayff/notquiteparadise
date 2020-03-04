from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Type
from scripts.engine import entity
from scripts.engine.component import Component

if TYPE_CHECKING:
    pass

# TODO - show debug info
# TODO - approach to type commands to trigger actions e.g. spawn creature
# TODO - approach to show required info, e.g. rounds & time, FPS

########################  ###########################


# def set_visibility(self, visible: bool):
#     """
#     Set whether the debug info is visible
#     """


def log_component_not_found(ent: int, msg: str, component: Type[Component]):
    """
    Use if component not found. Log the error as a warning in the format "{ent} {msg} tried to but no {component]
    found."
    """
    name = entity.get_name(ent)
    logging.warning(f"'{name}({ent})' tried to {msg} but no {component.__class__} Component found.")


