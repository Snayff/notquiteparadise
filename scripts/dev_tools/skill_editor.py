from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from scripts.core.library import library
from scripts.skills.skill import SkillData

if TYPE_CHECKING:
    pass


class SkillEditor:
    """
    Dev tool to allow creating and editing skills.
    """
    def __init__(self):
        self.current_skill = SkillData()
        self.all_skills = library.skills

