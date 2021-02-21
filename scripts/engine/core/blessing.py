import random
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Any, TYPE_CHECKING

class Blessing(ABC):
    """
    The base class for blessings. Blessings modify skills through the effects applied.
    """

    name: str
    description: str

    level: str
    removable: bool

    # remove/add are applied when the blessing is applied
    remove_effects: List[str]
    add_effects: List[str]

    # modifications are applied when the effects are built
    modify_effects_set: List[Dict[str, Any]]
    modify_effects_tweak_flat: List[Dict[str, Any]]
    modify_effects_tweak_percent: List[Dict[str, Any]]

    def __init__(self):
        pass

    @classmethod
    def _init_properties(cls):
        """
        Sets the class properties of the blessing from the class key
        """
        from scripts.engine.internal import library

        cls.data = library.BLESSINGS[cls.__name__]
        cls.name = cls.__name__
        cls.description = cls.data['description']
        cls.level = 'Base' # assume common exists for now
        cls.removable = cls.data['removable']

        cls.remove_effects = cls.data['base_effects']['remove_effects']
        cls.add_effects = cls.data['base_effects']['add_effects']
        cls.modify_effects_set = cls.data['base_effects']['modify_effects_set']
        cls.modify_effects_tweak_flat = cls.data['base_effects']['modify_effects_tweak_flat']
        cls.modify_effects_tweak_percent = cls.data['base_effects']['modify_effects_tweak_percent']

    def roll_level(self):
        """
        Runs the level selection algorithm and updates attributes with the applied level.
        """
        levels = []
        level_chances = []
        total = 0

        for level in cls.data['levels']:
            rarities.append(level)
            total += cls.data['levels'][level]['rarity']
            level_chances.append(total)

        random_float = random.random()
        for i, chance in enumerate(level_chances):
            if random_float <= chance:
                break

        self.set_level(levels[i])

    def set_level(self, level):
        """
        Refreshes the class attributes with the data for the specific blessing level.
        """
        cls.level = level
        cls.remove_effects = cls.data['levels'][cls.level]['remove_effects']
        cls.add_effects = cls.data['levels'][cls.level]['add_effects']
        cls.modify_effects_set = cls.data['levels'][cls.level]['modify_effects_set']
        cls.modify_effects_tweak_flat = cls.data['levels'][cls.level]['modify_effects_tweak_flat']
        cls.modify_effects_tweak_percent = cls.data['levels'][cls.level]['modify_effects_tweak_percent']
