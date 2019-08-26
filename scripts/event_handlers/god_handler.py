
import logging

from scripts.core.constants import EntityEventTypes, EffectTypes
from scripts.event_handlers.pub_sub_hub import Subscriber
from scripts.global_singletons.data_library import library
from scripts.global_singletons.managers import world_manager


class GodHandler(Subscriber):
    """
    Handle events affecting entities
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "god_handler", event_hub)

    def run(self, event):
        """
        Process entity events

        Args:
            event(Event): the event in need of processing
        """

        log_string = f"{self.name} received {event.type}..."
        logging.debug(log_string)

        if event.type == EntityEventTypes.SKILL:
            tree_name = event.skill.skill_tree_name
            skill_name = event.skill.name
            entity = event.entity
            skill_data = library.get_skill_data(tree_name, skill_name)

            # check effect types used
            for effect_name, effect_data in skill_data.effects.items():
                world_manager.God.judge_action(entity, effect_data.effect_type)

            # check damage type used
            if EffectTypes.DAMAGE.name in skill_data.effects:
                damage_type = skill_data.effects[EffectTypes.DAMAGE.name].damage_type
                world_manager.God.judge_action(entity, damage_type)

            # check afflictions applied
            if EffectTypes.APPLY_AFFLICTION.name in skill_data.effects:
                affliction_name = skill_data.effects[EffectTypes.APPLY_AFFLICTION.name].affliction_name
                world_manager.God.judge_action(entity, affliction_name)



        # TODO -
        #  create events for receiving afflictions
        #  create events for receiving damage types
        #  create events for causing and receiving hit type
        #  create events for being the cause of death
