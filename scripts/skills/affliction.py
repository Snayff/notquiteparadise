
from scripts.core.constants import AfflictionCategory, AfflictionTriggers, LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
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
        from scripts.global_singletons.managers import world_manager
        action = world_manager.Affliction
        affliction = library.get_affliction_data(affliction_name)

        self.name = affliction_name
        self.description = affliction.description
        self.icon = affliction.icon
        self.affliction_category = action.get_affliction_category_from_string(affliction.category)
        self.duration = duration
        self.trigger_event = action.get_trigger_event_from_string(affliction.trigger_event)
        self.affected_entity = affected_entity  # set at time of allocation to an entity
        self.affliction_effects = []

        # get the affliction skill_effects
        affliction_effects_values = affliction.affliction_effects

        # unpack all affliction_effects
        for effect in affliction_effects_values:
            created_effect = None
            effect_name = effect["name"]

            created_effect = world_manager.Affliction.create_affliction_effect(self, effect["type"])

            if effect_name == "damage":
                created_effect = world_manager.Affliction.create_damage_effect(self, effect)

            if effect_name == "affect_stat":
                created_effect = world_manager.Affliction.create_affect_stat_effect(self, effect)

            # if we have an effect add it to internal list
            if created_effect:
                self.affliction_effects.append(created_effect)

    def trigger(self):
        """
        Trigger all affliction effects and decrement duration by 1
        """
        log_string = f"Triggering effects in {self.name}"
        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))

        for effect in self.affliction_effects:
            effect.trigger(self.affected_entity)

        # reduce duration on all effects other than Passive
        if self.trigger_event != AfflictionTriggers.PASSIVE:
            self.duration -= 1
            log_string = f"Duration reduced to: {self.duration}"
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

