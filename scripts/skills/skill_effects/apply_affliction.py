from scripts.core.constants import TargetTags, AfflictionCategory, HitTypes, MessageEventTypes, HitModifiers, \
    LoggingEventTypes, SkillEffectTypes
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.affliction import Affliction
from scripts.skills.skill_effects.skill_effect import SkillEffect
from scripts.world.entity import Entity


class ApplyAfflictionSkillEffect(SkillEffect):
    """
    SkillEffect to apply an Affliction to an Entity
    """

    def __init__(self, owner):
        super().__init__(owner, "apply affliction", "This is the affliction effect", SkillEffectTypes.APPLY_AFFLICTION)

    def trigger(self, attacking_entity, defending_entity):
        """
        Trigger the effect. Attacking Entity can be None.

        Args:
            attacking_entity(Entity):
            defending_entity(Entity):
        """

        super().trigger()

        skill_data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.skill_effect_type)
        affliction_data = library.get_affliction_data(skill_data.affliction_name)

        attacker = attacking_entity
        defender = defending_entity

        from scripts.global_singletons.managers import world_manager
        target_type = world_manager.Skill.get_target_type(defender)

        # check the type is correct, then that the tags match
        if target_type == skill_data.required_target_type:

            # create var to hold the modified duration, if it does change, or the base duration
            base_duration = skill_data.affliction_duration
            modified_duration = base_duration

            # get the tile to check the tags
            from scripts.global_singletons.managers import world_manager
            tile = world_manager.Map.get_tile(defender.x, defender.y)

            if world_manager.Skill.has_required_tags(tile, skill_data.required_tags):

                # Roll for BANE application
                if affliction_data.affliction_category == AfflictionCategory.BANE:
                    to_hit_score = world_manager.Skill.calculate_to_hit_score(defender,
                                                                skill_data.base_accuracy, skill_data.stat_to_target,
                                                                              attacker)
                    hit_type = world_manager.Skill.get_hit_type(to_hit_score)

                    # check if affliction applied
                    if hit_type == HitTypes.GRAZE:
                        msg = f"{defender.name} resisted {skill_data.affliction_name}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                    else:
                        hit_msg = ""

                        # check if there was a crit and if so modify the duration of the affliction
                        if hit_type == HitTypes.CRIT:
                            modified_duration = int(base_duration * HitModifiers.CRIT.value)
                            hit_msg = f"a critical "

                        msg = f"{defender.name} succumbed to {hit_msg}{skill_data.affliction_name}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

                        self.apply_affliction(defender, modified_duration)

                # Just apply the BOON
                elif affliction_data.affliction_category == AfflictionCategory.BOON:
                    self.apply_affliction(defender, modified_duration)

    def apply_affliction(self, defending_entity, modified_duration):
        """
        Apply the affliction to the target entity

        Args:
            modified_duration (int):
            defending_entity (Entity):
        """
        skill_data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.skill_effect_type)

        from scripts.global_singletons.managers import world_manager
        action = world_manager.Affliction
        active_affliction = action.get_affliction_for_entity(defending_entity, skill_data.affliction_name)

        # check if entity already has the affliction
        if active_affliction:
            # if so compare durations
            active_duration = active_affliction.duration

            log_string = f"{defending_entity.name} already has {skill_data.affliction_name}:{active_duration}..."
            publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))

            # alter the duration of the current affliction if the new one will last longer
            if active_duration < modified_duration:
                active_affliction.duration = modified_duration

                log_string = f"-> Active duration {active_duration} is less than new duration " \
                    f"{modified_duration} so updated the duration on the active affliction."

            else:
                log_string = f"-> Active duration {active_duration} is greater than or equal to new duration " \
                    f"{modified_duration} so no action taken."
            # log the outcome of the duration comparison
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        # no current affliction of same type so apply new one
        else:
            log_string = f"Applying {skill_data.affliction_name} affliction to {defending_entity.name} with duration " \
                f"of {modified_duration}."
            publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))

            # create the affliction
            affliction = action.create_affliction(skill_data.affliction_name, modified_duration, defending_entity)

            # add affliction to the central list
            action.register_active_affliction(affliction)
