import logging
import math

from scripts.core.constants import SkillExpiryTypes, Directions, SkillTravelTypes, TargetTags, \
    SkillTerrainCollisions
from scripts.events.game_events import EndTurnEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher


class Skill:
    """
    A skill to be used by an actor

    Attributes:
            name(str):
            owner():
            skill_tree_name():
    """

    def __init__(self, owner, skill_tree_name, skill_name):
        self.owner = owner
        self.skill_tree_name = skill_tree_name
        self.name = skill_name


