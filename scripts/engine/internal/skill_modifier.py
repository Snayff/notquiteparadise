import random
from abc import ABC, abstractmethod
from typing import List, Set, Tuple, Dict, Any, TYPE_CHECKING

import scripts.engine.core.effect
from scripts.engine.core.effect import Effect

EFFECTS = {k : getattr(scripts.engine.core.effect, k) for k in dir(scripts.engine.core.effect)}

class SkillModifier(ABC):
    """
    The base class for blessings. Blessings modify skills through the effects applied.
    """

    name: str
    description: str

    level: str
    removable: bool
    conflicts: List[str]
    skill_types: List[str]

    # remove/add are applied when the blessing is applied
    remove_effects: List[str]
    add_effects: List[Dict[str, Any]]

    # modifications are applied when the effects are built
    modify_effects_set: List[Dict[str, Any]]
    modify_effects_tweak_flat: List[Dict[str, Any]]
    modify_effects_tweak_percent: List[Dict[str, Any]]

    # custom args (set by child if JSON doesn't cover the argument needs)
    custom_args: Dict[str, Any] = {}

    def __init__(self, owner):
        self.owner = owner

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
        cls.conflicts = cls.data['conflicts']
        cls.skill_types = cls.data['skill_types']

        cls.remove_effects = cls.data['base_effects']['remove_effects']
        cls.add_effects = cls.data['base_effects']['add_effects']
        cls.modify_effects_set = cls.data['base_effects']['modify_effects_set']
        cls.modify_effects_tweak_flat = cls.data['base_effects']['modify_effects_tweak_flat']
        cls.modify_effects_tweak_percent = cls.data['base_effects']['modify_effects_tweak_percent']

    @property
    def involved_effects(self) -> Set[str]:
        """
        Get the set of effects involved in the blessing.
        """
        return set([v['effect_id'] for v in self.add_effects + self.modify_effects_set] + self.remove_effects)

    def roll_level(self):
        """
        Runs the level selection algorithm and updates attributes with the applied level.
        """
        levels = []
        level_chances = []
        total = 0

        for level in self.data['levels']:
            levels.append(level)
            total += self.data['levels'][level]['rarity']
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
        self.level = level
        if 'remove_effects' in self.data['levels'][self.level]['effects']:
            self.remove_effects = self.data['levels'][self.level]['effects']['remove_effects']
        if 'add_effects' in self.data['levels'][self.level]['effects']:
            self.add_effects = self.data['levels'][self.level]['effects']['add_effects']
        if 'modify_effects_set' in self.data['levels'][self.level]['effects']:
            self.modify_effects_set = self.data['levels'][self.level]['effects']['modify_effects_set']
        if 'modify_effects_tweak_flat' in self.data['levels'][self.level]['effects']:
            self.modify_effects_tweak_flat = self.data['levels'][self.level]['effects']['modify_effects_tweak_flat']
        if 'modify_effects_tweak_percent' in self.data['levels'][self.level]['effects']:
            self.modify_effects_tweak_percent = self.data['levels'][self.level]['effects']['modify_effects_tweak_percent']

    def apply(self, effects: List[Effect], owner, target):
        """
        This is the core function of the blessing. It takes the effect stack and modifies it with the blessing.
        """

        # go through the effects backwards so that the .remove() doesn't mess up indexing
        for effect in effects[::-1]:
            effect_name = effect.__class__.__name__

            # flat config change
            for mod in self.modify_effects_tweak_flat:
                if mod['effect_id'] == effect_name:
                    for value in mod['values']:
                        current_value = getattr(effect, value)
                        setattr(effect, value, current_value + mod['values'][value])

            # set config change
            for mod in self.modify_effects_set:
                if mod['effect_id'] == effect_name:
                    for value in mod['values']:
                        setattr(effect, value, mod['values'][value])

            # percent config change
            for mod in self.modify_effects_tweak_percent:
                if mod['effect_id'] == effect_name:
                    for value in mod['values']:
                        current_value = getattr(effect, value)
                        setattr(effect, value, current_value * mod['values'][value])

            # remove effects from the stack if applicable
            if effect_name in self.remove_effects:
                effects.remove(effect)

        # add effects to the stack
        for add_effect in self.add_effects:
            # build the effect creation arguments from the config
            args = {'origin': owner, 'target': target, 'success_effects': [], 'failure_effects': []}
            args.update(add_effect['args'])
            if add_effect['effect_id'] in self.custom_args:
                args.update(self.custom_args)
            effects.append(EFFECTS[add_effect['effect_id']](**args))
