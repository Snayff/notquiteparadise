
import logging

from scripts.core.constants import EffectTypes

from scripts.global_singletons.event_hub import publisher


class Effect:
    """
    Base class for  effects that make up the basis of skills.
    """

    def __init__(self, owner, name, description, effect_type):
        self.owner = owner
        self.name = name
        self.description = description
        self.effect_type = effect_type  # type:EffectTypes

    def trigger(self):
        """
        Trigger the effect
        """
        log_string = f"Applying {self.name} skill effect from '{self.owner.name}'."
        logging.debug(log_string)


