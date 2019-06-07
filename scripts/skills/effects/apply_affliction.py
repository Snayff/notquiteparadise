from scripts.core.constants import TargetTags, AfflictionCategory, HitTypes, MessageEventTypes, HitModifiers, \
    LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.affliction import Affliction
from scripts.skills.effects.skill_effect import SkillEffect
from scripts.world.entity import Entity


class ApplyAfflictionEffect(SkillEffect):
    """
    SkillEffect to apply an Affliction to an Entity
    """

    def __init__(self, owner, required_target_type, required_tags, affliction, accuracy,
            stat_to_target):
        super().__init__(owner, "Apply_Affliction", "This is the affliction effect", required_target_type,
                         required_tags)
        self.base_accuracy = accuracy
        self.stat_to_target = stat_to_target
        self.affliction = affliction # type: Affliction

    def trigger(self, attacking_entity, defending_entity):
        """
        Trigger the effect

        Args:
            attacking_entity(Entity):
            defending_entity(Entity):
        """

        super().trigger()

        attacker = attacking_entity
        defender = defending_entity

        from scripts.global_instances.managers import game_manager
        target_type = game_manager.skill_query.get_target_type(defender)

        # check the type is correct, then that the tags match
        if target_type == self.required_target_type:

            # get the tile to check the tags
            from scripts.global_instances.managers import world_manager
            tile = world_manager.game_map.get_tile(defender.x, defender.y)

            if game_manager.skill_query.has_required_tags(tile, self.required_tags):

                # Roll for BANE application
                if self.affliction.affliction_category == AfflictionCategory.BANE:
                    to_hit_score = game_manager.skill_action.calculate_to_hit_score(attacker, defender,
                                                                self.base_accuracy, self.stat_to_target)
                    hit_type = game_manager.skill_query.get_hit_type(to_hit_score)

                    # check if affliction applied
                    if hit_type == HitTypes.GRAZE:
                        msg = f"{defender.name} resisted {self.affliction.name}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                    else:
                        # check if there was a crit and if so modify the duration of the affliction
                        if hit_type == HitTypes.CRIT:
                            self.affliction.duration *= HitModifiers.CRIT.value

                        self.apply_affliction(defender)

                # Just apply the BOON
                elif self.affliction.affliction_category == AfflictionCategory.BOON:
                    self.apply_affliction(defender)

    def apply_affliction(self, defending_entity):
        """
        Apply the affliction to the target entity

        Args:
            defending_entity (Entity):
        """
        log_string = f"Applying {self.affliction.name} affliction to {defending_entity.name}."
        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))

        defending_entity.afflictions.append(self.affliction)
