import logging

from scripts.core.constants import AfflictionCategory, AfflictionTriggers
from scripts.global_singletons.data_library import library
from scripts.world.entity import Entity


class Affliction:
    """
    Affliction, either Bane or Boon. Applies a periodic effect to an Entity, dictated by its AfflictionTrigger.

    Attributes:
        name (str):  string name of the Affliction
        description (str): description of the Affliction
        icon (pygame.Image): pygame image to symbolise the Affliction
        affliction_category (AfflictionCategory): Bane or Boon
        duration (int): amount of applications before expiry
        trigger_event (AfflictionTriggers): the event that triggers the Affliction to activate
        affected_entity (Entity): the Entity being impacted by the Affliction
        affliction_effects (list(AfflictionEffect)): list of AfflictionEffects
    """

    def __init__(self, affliction_name, duration, affected_entity):

        self.name = affliction_name
        self.duration = duration
        self.affected_entity = affected_entity  # set at time of allocation to an entity

    def trigger(self):
        """
        Trigger all afflictions effects and decrement duration by 1
        """
        log_string = f"Triggering effects in {self.name}"
        logging.info( log_string)

        from scripts.global_singletons.managers import world_manager
        data = library.get_affliction_data(self.name)

        # apply any effects
        for effect_name, effect_data in data.effects.items():
            effect = world_manager.Skill.create_effect(self, effect_data.effect_type)
            effected_tile = world_manager.Map.get_tile(self.affected_entity.x, self.affected_entity.y)
            effect.trigger([effected_tile])

    # reduce duration on all effects other than Passive
        if data.trigger_event != AfflictionTriggers.PASSIVE:
            self.duration -= 1
            log_string = f"{self.affected_entity.name}`s {self.name} duration reduced to {self.duration}"
            logging.debug(log_string)

