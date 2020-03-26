from __future__ import annotations

import logging
import random
from typing import TYPE_CHECKING, Any, Union, Optional
from snecs.typedefs import EntityID
from scripts.engine import existence, world, utility
from scripts.engine.component import Position, Resources, Aspect, HasCombatStats, Identity, Afflictions, Knowledge
from scripts.engine.core.constants import MessageType, TravelMethod, TargetTag, Effect, AfflictionCategory, HitType, \
    HitModifier, PrimaryStat, HitValue, SecondaryStatType, PrimaryStatType, HitTypeType, TravelMethodType, Direction, \
    ResourceType, INFINITE
from scripts.engine.core.definitions import EffectData, UseSkillEffectData, RemoveAspectEffectData, \
    AddAspectEffectData, ApplyAfflictionEffectData, DamageEffectData, AffectStatEffectData, ActivateSkillEffectData
from scripts.engine.core.event_core import publisher
from scripts.engine.event import MessageEvent, DieEvent, UseSkillEvent, WantToUseSkillEvent
from scripts.engine.library import library
from scripts.engine.world_objects.combat_stats import CombatStats
from scripts.engine.world_objects.tile import Tile
from importlib import import_module

if TYPE_CHECKING:
    from typing import List, Tuple


#############################################################################################
####################### HOW DO SKILLS WORK? #################################################
# TODO - rewrite and update
# something triggers a WantToUseSkillEvent
# entity handler picks this up and:
#   checks affordability, pays skill costs, get's target/s and creates a UseSkillEvent
# entity handler picks this up and:
#   calls skills.use
# skills.use calls the "use" method of the relevant {skill_name} in nqp.skills which may:
#   create a projectile
#       projectile given turn, as any other entity travels in a direction until it activates or expires
#       on collision with another entity the projectile calls the  "activate" method {skill_name} in nqp.skills
#           create ActivateSkillEvent and pass effects
#   else call "activate"
########################################################################################

# TODO - have the ability to create entities, e.g. summons, traps, etc.
# TODO - ability to specify target/ target automatically based on condition, e.g. nearest, lowest health etc.

######################################## CHECKS ######################################

def can_use_skill(entity: int, target_pos: Tuple[int, int], skill_name: str):
    """
    Confirm entity can use skill on targeted position. True if can use the skill. Else False.
    """
    start_tile = target_tile = None

    position = existence.get_entitys_component(entity, Position)
    if position:
        target_x, target_y = target_pos
        start_tile = world.get_tile((position.x, position.y))
        target_tile = world.get_tile((target_x, target_y))

    skill_data = library.get_skill_data(skill_name)

    # check we have everything we need and if so use the skill
    if start_tile and target_tile:
        if world.tile_has_tags(target_tile, skill_data.required_tags, entity):
            resource_type = skill_data.resource_type
            resource_cost = skill_data.resource_cost
            if resource_type:
                if can_afford_cost(entity, resource_type, resource_cost):
                    distance = utility.get_chebyshev_distance((start_tile.x, start_tile.y), target_pos)
                    skill_range = skill_data.range
                    if distance <= skill_range:
                        return True
                    else:
                        logging.debug(f"Target out of skill range, range:{skill_range} < distance:{distance}.")

            else:
                msg = f"I can't afford the cost."
                publisher.publish(MessageEvent(MessageType.LOG, msg))

    return False


def can_afford_cost(entity: int, resource: ResourceType, cost: int):
    """
    Check if entity can afford the resource cost
    """
    resources = existence.get_entitys_component(entity, Resources)
    name = existence.get_name(entity)

    # Check if cost can be paid
    value = getattr(resources, resource.lower())
    if value - cost >= 0:
        logging.debug(f"'{name}' can afford cost.")
        return True
    else:
        logging.info(f"'{name}' cannot afford cost.")
        return False


########################################### ACTIONS ################################

def pay_resource_cost(entity: int, resource: SecondaryStatType, cost: int):
    """
    Remove the resource cost from the using entity
    """
    resources = existence.get_entitys_component(entity, Resources)
    name = existence.get_name(entity)

    if resources:
        resource_value = getattr(resources, resource.lower())

        if resource_value != INFINITE:
            resource_left = resource_value - cost

            setattr(resources, resource.lower(), resource_left)

            logging.info(f"'{name}' paid {cost} {resource} and has {resource_left} left.")
        else:
            logging.info(f"'{name}' paid nothing as they have infinite {resource}.")
    else:
        logging.warning(f"'{name}' tried to pay {cost} {resource} but Resources component not found.")


def use_skill(using_entity: int, skill_name: str, target_tiles: List[Tile]):
    """
    Calls the skills "use" function. N.B. target_tiles are the tiles the skill we be used on.
    """
    knowledge = existence.get_entitys_component(using_entity, Knowledge)
    knowledge.skills[skill_name].use(target_tiles)
    name = existence.get_name(using_entity)
    tiles = [(tile.x, tile.y) for tile in target_tiles]
    logging.info(f"'{name}' used {skill_name} on {tiles}.")


def create_skill_instance(skill_class_name: str, **kwargs):
    """
    Create an instance of the skill class
    """
    module_name = "skills"
    module = import_module(module_name)
    cls = getattr(module, skill_class_name)
    return cls(**kwargs)


########################################## GET ####################################

def get_target_tiles(using_entity: EntityID, skill_name: str, start_position: Tuple[int, int],
        target_position: Tuple[int, int]) -> List[Optional[Tile]]:
    """
    Call the skills "get_target_tiles" method. Checks for appropriate tiles based on target position and the skill
    """
    knowledge = existence.get_entitys_component(using_entity, Knowledge)
    return knowledge.skills[skill_name].get_target_tiles(start_position, target_position)


def _get_furthest_free_position(start_position: Tuple[int, int], target_direction: Tuple[int, int],
        max_distance: int, travel_type: TravelMethodType) -> Tuple[int, int]:
    """
    Checks each position in a line and returns the last position that doesnt block movement. If no position in
    range blocks movement then the last position checked is returned. If all positions in range block movement
    then starting position is returned.
    """
    start_x = start_position[0]
    start_y = start_position[1]
    dir_x = target_direction[0]
    dir_y = target_direction[1]
    current_x = start_x
    current_y = start_y
    free_x = start_x
    free_y = start_y
    check_for_target = False

    # determine travel method
    if travel_type == TravelMethod.STANDARD:
        # standard can hit a target at any point during travel
        check_for_target = True
    elif travel_type == TravelMethod.ARC:
        # throw can only hit target at end of travel
        check_for_target = False

    # determine impact location N.B. +1 to make inclusive as starting from 1
    for distance in range(1, max_distance + 1):

        # allow throw to hit target
        if travel_type == TravelMethod.ARC:
            if distance == max_distance + 1:
                check_for_target = True

        # get current position
        current_x = start_x + (dir_x * distance)
        current_y = start_y + (dir_y * distance)
        tile = world.get_tile((current_x, current_y))

        if tile:
            # did we hit something causing standard to stop
            if world.tile_has_tag(tile, TargetTag.BLOCKED_MOVEMENT):
                # if we're ready to check for a target, do so
                if check_for_target:
                    # we hit something, go back to last free tile
                    current_x = free_x
                    current_y = free_y
                    break
            else:
                free_x = current_x
                free_y = current_y

    return current_x, current_y


def _get_hit_type(to_hit_score: int) -> HitTypeType:
    """
    Get the hit type from the to hit score
    """
    if to_hit_score >= HitValue.CRIT:
        return HitType.CRIT
    elif to_hit_score >= HitValue.HIT:
        return HitType.HIT
    else:
        return HitType.GRAZE


########################################## EFFECTS ####################################

def process_effect(effect: EffectData, effected_tiles: List[Tile], causing_entity: EntityID,
        instigator: Optional[Union[EntityID, str]] = None) -> bool:
    """
    Apply an effect to all tiles in a list.
    """
    if isinstance(instigator, EntityID):
        name = existence.get_name(instigator)
    elif isinstance(instigator, str):
        name = instigator
    else:
        name = existence.get_name(causing_entity)

    if effect.effect_type is None:
        logging.critical(f"Processing effect, caused by '{name}', but effect_type is None.")
    elif len(effected_tiles) == 0:
        logging.critical(f"Processing effect, caused by '{name}', but no tiles provided.")
    else:
        logging.debug(f"Processing {effect.effect_type} effect, caused by '{name}'.")

    if isinstance(effect, DamageEffectData):
        return _process_damage_effect(effect, effected_tiles, causing_entity)
    elif isinstance(effect, ApplyAfflictionEffectData):
        return _process_apply_affliction_effect(effect, effected_tiles, causing_entity)
    elif isinstance(effect, AddAspectEffectData):
        return _process_add_aspect_effect(effect, effected_tiles)
    elif isinstance(effect, RemoveAspectEffectData):
        return _process_remove_aspect_effect(effect, effected_tiles)
    elif isinstance(effect, UseSkillEffectData):
        return _process_use_skill_effect(effect, effected_tiles, causing_entity)
    elif isinstance(effect, ActivateSkillEffectData):
        return _process_activate_skill_effect(effect, effected_tiles, causing_entity)
    elif isinstance(effect, AffectStatEffectData):
        logging.warning("Trying to process affect stat. This applies passively. What are you doing?")


def _process_use_skill_effect(effect: UseSkillEffectData, effected_tiles: List[Tile],
        attacker: EntityID) -> bool:
    skill_name = effect.skill_name

    position = existence.get_entitys_component(attacker, Position)
    start_pos = (position.x, position.y)

    # uses first tile in list for target direction. Should only be one tile when triggering trigger skill.
    target_pos = (effected_tiles[0].x, effected_tiles[0].y)
    direction = world.get_direction(start_pos, target_pos)

    publisher.publish(WantToUseSkillEvent(attacker, skill_name, start_pos, direction))
    return True


def _process_activate_skill_effect(effect: ActivateSkillEffectData, target_tiles: List[Tile],
        attacker: EntityID) -> bool:
    """
    Activate the skill by calling the skill's activate function.
    """
    name = existence.get_name(attacker)
    skill_name = effect.skill_name
    logging.info(f"'{name}' about to activate {skill_name}.")
    knowledge = existence.get_entitys_component(attacker, Knowledge)
    knowledge.skills[effect.skill_name].activate(target_tiles)
    return True


def _process_remove_aspect_effect(effect: RemoveAspectEffectData, effected_tiles: List[Tile]) -> bool:
    """
    Success on removing aspect
    """
    success = False
    aspect_name = effect.aspect_name
    entities = existence.get_entities_and_components_in_area(effected_tiles, [Aspect])

    # loop all relevant aspects and if one is matching delete the entity
    for entity, (position, aspect) in entities.items():
        if aspect_name in aspect.aspects:
            existence.delete(entity)
            success = True

    return success


def _process_add_aspect_effect(effect: AddAspectEffectData, effected_tiles: List[Tile]) -> bool:
    """
    Success on adding aspect
    """
    success = False
    for tile in effected_tiles:
        _create_aspect(effect.aspect_name, tile)
        success = True
    return success

def _create_aspect(aspect_name: str, tile: Tile):
    data = library.get_aspect_data(aspect_name)
    position: Position
    aspect: Aspect
    entities = existence.get_entities_and_components_in_area([tile], [Aspect])

    for entity, (position, aspect) in entities.items():
        # if there is an active version of the same aspect already
        if aspect:
            # increase duration to initial value
            aspect.aspects[aspect_name] = data.duration
        else:
            existence.create([Position(position.x, position.y), Aspect({aspect_name: data.duration})])


def _process_apply_affliction_effect(effect: ApplyAfflictionEffectData, effected_tiles: List[Tile],
        attacker: EntityID) -> bool:
    """
    Success on applying affliction
    """
    success = False
    affliction_data = library.get_affliction_data(effect.affliction_name)
    attackers_stats = existence.get_combat_stats(attacker)

    # get relevant entities
    entities = existence.get_entities_and_components_in_area(effected_tiles, [Resources, HasCombatStats, Identity])

    # loop all relevant entities
    for defender, (position, resources, has_stats, identity) in entities.items():

        # create var to hold the modified duration, if it does change, or the base duration
        base_duration = effect.duration
        modified_duration = base_duration
        defender_stats = existence.get_combat_stats(defender)
        tile = world.get_tile((position.x, position.y))

        if tile:
            # check we have all tags
            if world.tile_has_tags(tile, effect.required_tags, attacker):
                # Roll for BANE application
                if affliction_data.category == AfflictionCategory.BANE:
                    # if we havent targeted a stat then default to 0
                    if effect.stat_to_target:
                        to_hit_score = _calculate_to_hit_score(defender_stats, effect.accuracy,
                                                               effect.stat_to_target, attackers_stats)
                    else:
                        to_hit_score = 0
                    hit_type = _get_hit_type(to_hit_score)

                    name = existence.get_name(attacker)

                    # check if afflictions applied
                    if hit_type == HitType.GRAZE:
                        msg = f"{name} resisted {effect.affliction_name}."
                        # TODO - ensure if player involved it shows as "You"
                        publisher.publish(MessageEvent(MessageType.LOG, msg))
                    else:
                        hit_msg = ""

                        # check if there was a crit and if so modify the duration of the afflictions
                        if hit_type == HitType.CRIT:
                            modified_duration = int(base_duration * HitModifier.CRIT)
                            hit_msg = f"a critical "

                        msg = f"{name} succumbed to {hit_msg}{effect.affliction_name}."
                        # TODO - ensure if player involved it shows as "You"
                        publisher.publish(MessageEvent(MessageType.LOG, msg))

                        _create_affliction(defender, effect.affliction_name, modified_duration)
                        success = True

                # Just process the BOON
                elif affliction_data.category == AfflictionCategory.BOON:
                    _create_affliction(defender, effect.affliction_name, modified_duration)
                    success = True

    return success


def _create_affliction(entity: int, affliction_name: str, duration: int):
    data = library.get_affliction_data(affliction_name)
    name = existence.get_name(entity)
    affliction = existence.get_entitys_component(entity, Afflictions)

    # check if entity already has the afflictions component
    if affliction:
        # one exists so do we have an active version of the same affliction
        if affliction[affliction_name]:
            active_affliction_duration = affliction[affliction_name]
        else:
            active_affliction_duration = None

        # if affliction exists
        if active_affliction_duration:
            logging.debug(f"'{name}' already has {affliction_name}:{active_affliction_duration}...")

            # alter the duration of the current afflictions if the new one will last longer
            affliction[affliction_name] = duration

            log_string = f"-> Active duration {active_affliction_duration} is less than new duration " \
                         f"{duration} so duration updated."
            logging.debug(log_string)
        else:
            # no action taken if duration already longer
            log_string = f"-> Active duration {active_affliction_duration} is less than new duration " \
                         f" {duration} so duration remains the same."
            logging.debug(log_string)

    # no current afflictions of same type so process new one
    else:
        logging.info(f"Applying {affliction_name} afflictions to '{name}' with duration of {duration}.")
        existence.add_component(entity, Afflictions({affliction_name: duration}))


def _process_damage_effect(effect: DamageEffectData, effected_tiles: List[Tile], attacker: int) -> bool:
    """
    Success determined by doing >0 damage
    """
    success = False
    attackers_stats = existence.get_combat_stats(attacker)
    entities = existence.get_entities_and_components_in_area(effected_tiles, [Resources, HasCombatStats])
    effect_creator = effect.creator

    # loop all relevant entities
    for defender, (position, resources, has_stats) in entities.items():
        tile = world.get_tile((position.x, position.y))
        if tile:
            if world.tile_has_tags(tile, effect.required_tags, attacker):
                # get the info to process the damage
                defenders_stats = existence.get_combat_stats(defender)

                # check we have a stat to target, else default to 0
                if effect.stat_to_target:
                    to_hit_score = _calculate_to_hit_score(defenders_stats, effect.accuracy, effect.stat_to_target,
                                                           attackers_stats)
                else:
                    to_hit_score = 0

                hit_type = _get_hit_type(to_hit_score)
                damage = _calculate_damage(defenders_stats, hit_type, effect, attackers_stats)

                # who did the damage? (for informing the player)
                if attacker:
                    attacker_name = existence.get_name(attacker)
                else:
                    attacker_name = "???"

                defender_name = existence.get_name(defender)

                # resolve the damage
                if damage > 0:
                    success = True
                    resources.health -= damage

                    # log the outcome
                    if hit_type == HitType.GRAZE:
                        hit_type_desc = "grazed"
                    elif hit_type == HitType.HIT:
                        hit_type_desc = "hit"
                    elif hit_type == HitType.CRIT:
                        hit_type_desc = "crit"
                    else:
                        hit_type_desc = "does something unknown"  # catch all

                    # confirm to the player that they damaged someone
                    if attacker_name == "player":
                        attacker_name = "I"
                    msg = f"{attacker_name} {hit_type_desc} {defender_name} with {effect_creator} for {damage}."
                    publisher.publish(MessageEvent(MessageType.LOG, msg))

                    # TODO - add the damage type to the text and replace the type with an icon
                    # TODO - add the explanation of the damage roll to a tooltip
                    # TODO - ensure if player involved it shows as "You/I"

                    if resources.health <= 0:
                        publisher.publish(DieEvent(defender))

                else:
                    # inform player of no damage
                    # TODO - doesnt read properly for afflictions
                    if attacker_name == "player":
                        msg = f"{defender_name} resisted damage from my {effect_creator}."
                    else:
                        msg = f"{defender_name} resisted damage from {attacker_name}'s {effect_creator}."

                    publisher.publish(MessageEvent(MessageType.LOG, msg))

                return success


############################################### CALCULATE ####################################


def _calculate_damage(defenders_stats: CombatStats, hit_type: HitTypeType, effect_data: EffectData,
        attackers_stats: CombatStats = None) -> int:
    """
    Work out the damage to be dealt. if attacking entity is None then value used is 0.
    """
    logging.debug(f"Calculate damage...")
    data = effect_data

    initial_damage = data.damage
    damage_from_stats = 0

    # get damage from stats of attacker
    if attackers_stats:
        stat_amount = 0

        # get the stat
        all_stats = utility.get_class_members(PrimaryStat)
        for stat in all_stats:
            if stat == data.mod_stat:
                stat_amount = getattr(attackers_stats, stat.lower())
                break

        damage_from_stats = stat_amount * data.mod_amount

    # get resistance value
    if data.damage_type:
        resist_value = getattr(defenders_stats, "resist_" + data.damage_type.lower())
    else:
        resist_value = 0

    # mitigate damage with defence
    mitigated_damage = (initial_damage + damage_from_stats) - resist_value

    # apply to hit modifier to damage
    if hit_type == HitType.CRIT:
        modified_damage = mitigated_damage * HitModifier.CRIT
    elif hit_type == HitType.HIT:
        modified_damage = mitigated_damage * HitModifier.HIT
    else:
        modified_damage = mitigated_damage * HitModifier.GRAZE

    # round down the dmg
    int_modified_damage = int(modified_damage)

    # log the info
    log_string = f"-> Initial:{initial_damage}, Mitigated: {format(mitigated_damage, '.2f')},  Modified" \
                 f":{format(modified_damage, '.2f')}, Final: {int_modified_damage}"
    logging.debug(log_string)

    return int_modified_damage


def _calculate_to_hit_score(defenders_stats: CombatStats, skill_accuracy: int, stat_to_target: PrimaryStatType,
        attackers_stats: CombatStats = None) -> int:
    """
    Get the to hit score from the stats of both entities. If Attacker is None then 0 is used for attacker values.
    """
    logging.debug(f"Get to hit scores...")

    roll = random.randint(-3, 3)  # TODO - move hit variance to somewhere more easily configurable

    # if attacker get their accuracy
    if attackers_stats:
        attacker_accuracy = attackers_stats.accuracy
    else:
        attacker_accuracy = 0

    modified_to_hit_score = attacker_accuracy + skill_accuracy + roll

    # mitigate the to hit
    defender_value = getattr(defenders_stats, stat_to_target.lower())

    mitigated_to_hit_score = modified_to_hit_score - defender_value

    # log the info
    log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
    logging.debug(log_string)

    return mitigated_to_hit_score
