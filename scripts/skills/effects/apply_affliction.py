from scripts.core.constants import TargetTags, AfflictionTypes, HitTypes, MessageEventTypes
from scripts.events.message_events import MessageEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.effects.skill_effect import SkillEffect


class ApplyAfflictionEffect(SkillEffect):
    """
    SkillEffect to apply an Affliction to an Entity
    """

    def __init__(self, owner, required_target_type, required_tags, affliction_type, affliction, accuracy,
            stat_to_target):
        super().__init__(owner, "Apply_Affliction", "This is the affliction effect", required_target_type,
                         required_tags)
        self.base_accuracy = accuracy
        self.stat_to_target = stat_to_target
        self.affliction_type = affliction_type  # type: AfflictionTypes
        self.affliction = affliction

    def trigger(self, attacking_entity, defending_entity):
        """
        Trigger the effect

        Args:
            attacking_entity:
            defending_entity:
        """

        super().trigger()

        attacker = attacking_entity
        defender = defending_entity

        from scripts.global_instances.managers import game_manager
        target_type = game_manager.skill_query.get_target_type(defender)

        # check the type is correct, then that the tags match
        if target_type == self.required_target_type:
            # if it needs to be another entity then it can't be looking at itself
            if TargetTags.OTHER_ENTITY in self.required_tags:
                if attacker != defender:
                    to_hit_score = game_manager.skill_action.calculate_to_hit_score(attacker, defender,
                                                                self.base_accuracy, self.stat_to_target)
                    hit_type = game_manager.skill_query.get_hit_type(to_hit_score)

                    # check if affliction applied
                    if hit_type == HitTypes.GRAZE:
                        msg = f"{defender.name} resisted "
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                    self.apply_affliction()

            elif TargetTags.SELF in self.required_tags:
                self.apply_affliction()

    def apply_affliction(self):
        """
        Apply the affliction to the target entity
        """
