import logging

from scripts.core.constants import EntityEventTypes, EffectTypes, EventTopics
from scripts.event_handlers.pub_sub_hub import Subscriber
from scripts.global_singletons.data_library import library
from scripts.global_singletons.managers import world


class GodHandler(Subscriber):
    """
    Handle events affecting entities
    """

    def __init__(self, event_hub):
        Subscriber.__init__(self, "god_handler", event_hub)

    def run(self, event):
        """
        Process god actions from events

        Args:
            event(Event): the event in need of processing
        """
        # TODO -
        #  create events for receiving afflictions
        #  create events for receiving damage types
        #  create events for causing and receiving hit type
        #  create events for being the cause of death

        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}...")

        if event.topic == EventTopics.ENTITY:
            self.process_interventions(event)

        if event.event_type == EntityEventTypes.SKILL:
            self.process_judgements(event)

    @staticmethod
    def process_judgements(event):
        """
        Pass any actions taken to be judged by the gods.

        Args:
            event ():
        """
        tree_name = event.skill.skill_tree_name
        skill_name = event.skill.name
        entity = event.entity
        skill_data = library.get_skill_data(tree_name, skill_name)

        # check effect types used
        for effect_name, effect_data in skill_data.effects.items():
            world.God.judge_action(entity, effect_data.effect_type)

        # check damage type used
        if EffectTypes.DAMAGE.name in skill_data.effects:
            damage_type = skill_data.effects[EffectTypes.DAMAGE.name].damage_type
            world.God.judge_action(entity, damage_type)

        # check afflictions applied
        # TODO - this should apply to each instance applied
        if EffectTypes.APPLY_AFFLICTION.name in skill_data.effects:
            affliction_name = skill_data.effects[EffectTypes.APPLY_AFFLICTION.name].affliction_name
            world.God.judge_action(entity, affliction_name)

    @staticmethod
    def process_interventions(event):
        """
        Consider taking possible interventions and then take them.

        Args:
            event ():
        """
        # TODO - update to pass action to consider_intervening
        chosen_interventions = world.God.consider_intervening(event.entity)

        for god, intervention, entity in chosen_interventions:
            world.God.intervene(god, intervention, entity)

