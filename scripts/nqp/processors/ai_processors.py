from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


__all__ = ["process_ai_updates"]


def process_ai_updates(time_delta: float):
    """
    Fire realtime processors.
    """
    process_interventions(time_delta)



