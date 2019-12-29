
import logging

from scripts.core.constants import AfflictionCategory, HitTypes, MessageEventTypes, HitModifiers, \
    EffectTypes
from scripts.events.message_events import MessageEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.skills.effects.effect import Effect
from scripts.world.entity import Entity



class ApplyAfflictionEffect(Effect):
    """
    Effect to apply an Affliction to an Entity
    """

    def __init__(self, owner):
        super().__init__(owner, "apply afflictions", "This is the afflictions effect", EffectTypes.APPLY_AFFLICTION)

    def trigger(self, tiles):
        """
        Trigger the effect

        Args:
            tiles (List[Tile]):
        """
        super().trigger()

        # determine who triggered this effect to articulate the attacker and get the effect data
        from scripts.skills.skill import Skill
        from scripts.world.aspect import Aspect
        from scripts.world.intervention import Intervention
        if isinstance(self.owner, Skill):
            attacker = self.owner.owner.owner  # entity:actor:skill:skill_effect
            effect_data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name,
                                                        self.effect_type)
        elif isinstance(self.owner, Aspect):
            attacker = None
            effect_data = library.get_aspect_effect_data(self.owner.name, self.effect_type)

        elif isinstance(self.owner, Intervention):
            attacker = None
            effect_data = library.get_god_intervention_effect_data(self.owner.owner.name, self.owner.name,
                                                                   self.effect_type)

        affliction_data = library.get_affliction_data(effect_data.affliction_name)

        # loop all tiles in list
        for tile in tiles:
            defender = tile.entity

            # create var to hold the modified duration, if it does change, or the base duration
            base_duration = effect_data.duration
            modified_duration = base_duration

            # check the tags match
            from scripts.managers.world_manager import world
            if world.Skill.has_required_tags(tile, effect_data.required_tags, attacker):

                # Roll for BANE application
                if affliction_data.category == AfflictionCategory.BANE:
                    to_hit_score = world.Skill.calculate_to_hit_score(defender, effect_data.accuracy,
                                                                              effect_data.stat_to_target,  attacker)
                    hit_type = world.Skill.get_hit_type(to_hit_score)

                    # check if afflictions applied
                    if hit_type == HitTypes.GRAZE:
                        msg = f"{defender.name} resisted {effect_data.affliction_name}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
                    else:
                        hit_msg = ""

                        # check if there was a crit and if so modify the duration of the afflictions
                        if hit_type == HitTypes.CRIT:
                            modified_duration = int(base_duration * HitModifiers.CRIT.value)
                            hit_msg = f"a critical "

                        msg = f"{defender.name} succumbed to {hit_msg}{effect_data.affliction_name}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

                        self.apply_affliction(defender, modified_duration)

                # Just apply the BOON
                elif affliction_data.affliction_category == AfflictionCategory.BOON:
                    self.apply_affliction(defender, modified_duration)

        # trigger tile interactions caused by affliction
        from scripts.events.map_events import TileInteractionEvent
        publisher.publish(TileInteractionEvent(tiles, effect_data.affliction_name))

    def apply_affliction(self, defending_entity, modified_duration):
        """
        Apply the afflictions to the target entity

        Args:
            modified_duration (int):
            defending_entity (Entity):
        """
        # determine who triggered this effect to articulate the attacker and get the effect data
        from scripts.skills.skill import Skill
        from scripts.world.aspect import Aspect
        from scripts.world.intervention import Intervention
        if isinstance(self.owner, Skill):
            effect_data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name,
                                                        self.effect_type)
        elif isinstance(self.owner, Aspect):
            effect_data = library.get_aspect_effect_data(self.owner.name, self.effect_type)
        elif isinstance(self.owner, Intervention):
            effect_data = library.get_god_intervention_effect_data(self.owner.owner.name, self.owner.name,
                                                                   self.effect_type)

        from scripts.managers.world_manager import world
        active_affliction = world.Affliction.get_affliction_for_entity(defending_entity,
                                                                               effect_data.affliction_name)

        # check if entity already has the afflictions
        if active_affliction:
            # if so compare durations
            active_duration = active_affliction.duration

            log_string = f"{defending_entity.name} already has {effect_data.affliction_name}:{active_duration}..."
            logging.debug(log_string)

            # alter the duration of the current afflictions if the new one will last longer
            if active_duration < modified_duration:
                active_affliction.duration = modified_duration

                log_string = f"-> Active duration {active_duration} is less than new duration " \
                    f"{modified_duration} so updated the duration on the active afflictions."

            # no action taken if duration already longer

            # log the outcome of the duration comparison
            logging.debug(log_string)

        # no current afflictions of same type so apply new one
        else:
            log_string = f"Applying {effect_data.affliction_name} afflictions to '{defending_entity.name}' with " \
                f"duration of {modified_duration}."
            logging.info(log_string)

            # create the afflictions
            affliction = world.Affliction.create_affliction(effect_data.affliction_name, modified_duration,
                                                                    defending_entity)

            # add afflictions to the central list
            world.Affliction.register_active_affliction(affliction)
