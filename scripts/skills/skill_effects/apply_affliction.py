from scripts.core.constants import TargetTags, AfflictionCategory, HitTypes, MessageEventTypes, HitModifiers, \
    LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.event_hub import publisher
from scripts.skills.affliction import Affliction
from scripts.skills.skill_effects.skill_effect import SkillEffect
from scripts.world.entity import Entity


class ApplyAfflictionSkillEffect(SkillEffect):
    """
    SkillEffect to apply an Affliction to an Entity
    """

    def __init__(self, owner, required_target_type, required_tags, accuracy, stat_to_target, affliction_name,
            affliction_category, affliction_duration):
        super().__init__(owner, "apply_affliction", "This is the affliction effect", required_target_type,
                         required_tags)
        self.base_accuracy = accuracy
        self.stat_to_target = stat_to_target
        self.affliction_name = affliction_name
        self.affliction_category = affliction_category
        self.affliction_duration = affliction_duration

    def trigger(self, attacking_entity, defending_entity):
        """
        Trigger the effect. Attacking Entity can be None.

        Args:
            attacking_entity(Entity):
            defending_entity(Entity):
        """

        super().trigger()

        attacker = attacking_entity
        defender = defending_entity

        from scripts.global_singletons.managers import world_manager
        target_type = world_manager.Skill.get_target_type(defender)

        # check the type is correct, then that the tags match
        if target_type == self.required_target_type:

            # create var to hold the modified duration, if it does change, or the base duration
            modified_duration = self.affliction_duration

            # get the tile to check the tags
            from scripts.global_singletons.managers import world_manager
            tile = world_manager.Map.get_tile(defender.x, defender.y)

            if world_manager.Skill.has_required_tags(tile, self.required_tags):

                # Roll for BANE application
                if self.affliction_category == AfflictionCategory.BANE:
                    to_hit_score = world_manager.Skill.calculate_to_hit_score(defender,
                                                                self.base_accuracy, self.stat_to_target, attacker)
                    hit_type = world_manager.Skill.get_hit_type(to_hit_score)

                    # check if affliction applied
                    if hit_type == HitTypes.GRAZE:
                        msg = f"{defender.name} resisted {self.affliction_name}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                    else:
                        hit_msg = ""

                        # check if there was a crit and if so modify the duration of the affliction
                        if hit_type == HitTypes.CRIT:
                            duration = self.affliction_duration
                            duration *= HitModifiers.CRIT.value
                            modified_duration= int(duration)
                            hit_msg = f"a critical "

                        msg = f"{defender.name} succumbed to {hit_msg}{self.affliction_name}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

                        self.apply_affliction(defender, modified_duration)

                # Just apply the BOON
                elif self.affliction_category == AfflictionCategory.BOON:
                    self.apply_affliction(defender, modified_duration)

    def apply_affliction(self, defending_entity, modified_duration):
        """
        Apply the affliction to the target entity

        Args:
            modified_duration (int):
            defending_entity (Entity):
        """

        from scripts.global_singletons.managers import world_manager
        action = world_manager.Affliction
        active_affliction = action.get_affliction_for_entity(defending_entity, self.affliction_name)

        # check if entity already has the affliction
        if active_affliction:
            # if so compare durations
            active_duration = active_affliction.duration

            log_string = f"{defending_entity.name} already has {self.affliction_name}:{active_duration}..."
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
            log_string = f"Applying {self.affliction_name} affliction to {defending_entity.name} with duration of " \
                f"{modified_duration}."
            publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))

            # create the affliction
            affliction = action.create_affliction(self.affliction_name, modified_duration, defending_entity)

            # add affliction to the central list
            action.register_active_affliction(affliction)
