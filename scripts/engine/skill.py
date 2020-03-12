from __future__ import annotations

import logging
import random
from typing import TYPE_CHECKING
from scripts.engine import entity, world, utility
from scripts.engine.component import Position, Resources, Aspect, HasCombatStats, Identity, Affliction
from scripts.engine.core.constants import MessageType, SecondaryStat, ProjectileExpiry, \
    ProjectileTerrainCollision, ProjectileTravel, TargetTag, EffectType, AfflictionCategory, HitType, HitModifier, \
    PrimaryStat, HitValue, SecondaryStatType, PrimaryStatType, HitTypeType, EffectTypeType, HitValueType, \
    ProjectileTravelType
from scripts.engine.core.definitions import EffectData
from scripts.engine.core.event_core import publisher
from scripts.engine.event import MessageEvent, DieEvent
from scripts.engine.library import library
from scripts.engine.utility import create_shape
from scripts.engine.world_objects.combat_stats import CombatStats
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import List, Tuple, Type

#########################################################################################
########################   SKILL  & EFFECTS REQS. #######################################
# all skills create a projectile, use that to specify conditions such as speed and sprite. <-
    # TODO - create the projectile
    # TODO - fix the directions
# use a standardised collection of triggers
# allow for conditional criteria
# each effect is unique so each effect must be able to accept multiple params e.g. damage types
# there should be Active and Passive Skills
# passive skills, when learnt, apply the relevant affliction with an infinite duration and cannot be dispelled.
# the effects must be ordered and apply in order
# have the ability to create entities, e.g. summons, traps, etc.
# ability to target automatically based on condition, e.g. nearest, lowest health etc.
# cooldowns applied and respected
# can only spend resource types, which map to secondary stats, not secondary stats directly

########################################################################################


######################################## CHECKS ######################################

def can_use(ent: int, target_pos: Tuple[int, int], skill_name: str):
    """
    Confirm entity can use skill on targeted position. True if can use the skill. Else False.
    """
    start_tile = target_tile = None

    position = entity.get_entitys_component(ent, Position)
    if position:
        target_x, target_y = target_pos
        start_tile = world.get_tile((position.x, position.y))
        target_tile = world.get_tile((target_x, target_y))

    skill_data = library.get_skill_data(skill_name)

    # check we have everything we need and if so use the skill
    if start_tile and target_tile:
        if world.tile_has_tags(target_tile, skill_data.required_tags, ent):
            resource_type = skill_data.resource_type
            resource_cost = skill_data.resource_cost
            if resource_type:
                if can_afford_cost(ent, resource_type, resource_cost):
                    distance = utility.get_chebyshev_distance((start_tile.x, start_tile.y), target_pos)
                    skill_range = skill_data.range
                    if distance <= skill_range:
                        return True
                    else:
                        logging.debug(f"Target out of skill range, range:{skill_range} < distance:{distance}.")

            else:
                msg = f"You can't afford the cost."
                publisher.publish(MessageEvent(MessageType.LOG, msg))

    return False


def can_afford_cost(ent: int, resource: SecondaryStatType, cost: int):
    """
    Check if entity can afford the resource cost
    """
    resources = entity.get_entitys_component(ent, Resources)
    name = entity.get_name(ent)

    # Check if cost can be paid
    value = getattr(resources, resource.lower())
    if value - cost >= 0:
        logging.debug(f"'{name}' can afford cost.")
        return True
    else:
        logging.debug(f"'{name}' cannot afford cost.")
        return False


########################################### ACTIONS ################################

def pay_resource_cost(ent: int, resource: SecondaryStatType, cost: int):
    """
    Remove the resource cost from the using entity
    """
    resources = entity.get_entitys_component(ent, Resources)
    name = entity.get_name(ent)

    if resources:
        resource_value = getattr(resources, resource.lower())
        resource_left = resource_value - cost

        setattr(resources, resource.lower(), resource_left)

        log_string = f"'{name}' paid {cost} {resource} and has {resource_left} left."
        logging.debug(log_string)
    else:
        logging.warning(f"'{name}' tried to pay {cost} {resource} but Resources component not found.")


def use(using_entity: int, skill_name: str, start_position: Tuple[int, int],
        target_direction: Tuple[int, int]):
    """
    Use the skill in the target direction from the start position.
    """
    # initial values
    skill_data = library.get_skill_data(skill_name)
    skill_range = skill_data.range
    terrain_collision = skill_data.terrain_collision
    travel_type = skill_data.travel_type
    expiry_type = skill_data.expiry_type
    name = entity.get_name(using_entity)
    start_x, start_y = start_position
    current_x, current_y = start_position
    dir_x, dir_y = target_direction
    direction = (target_direction[0], target_direction[1])

    # flags
    activate = False
    fizzle = False

    logging.info(f"{name} used {skill_name} at ({start_x},{start_y}) in {direction}...")

    # do we have everything we need?
    if terrain_collision and travel_type and expiry_type:
        # continue finding the position to use the skill on until we fizzle or activate
        while not activate and not fizzle:

            # get last free position in direction
            current_x, current_y = _get_furthest_free_position(start_position, (dir_x, dir_y), skill_range,
                                                               travel_type)

            # determine how far we've travelled
            distance = max(abs(start_x) - abs(current_x), abs(start_y) - abs(current_y))

            # are we at max distance?
            if distance >= skill_range:
                # handle expiry type
                if expiry_type == ProjectileExpiry.FIZZLE:
                    fizzle = True
                    logging.info(f"-> and hit nothing. Skill fizzled at ({current_x},{current_y}).")
                elif expiry_type == ProjectileExpiry.ACTIVATE:
                    activate = True
                    logging.debug(f"-> and hit nothing. Skill will activate at ({current_x},{current_y}).")
            else:
                # we arent at max so we must have hit something one space further along
                current_x, current_y = current_x + dir_x, current_y + dir_y
                tile = world.get_tile((current_x, current_y))

                if tile:
                    # did we hit something that has the tags we need?
                    if world.tile_has_tags(tile, skill_data.required_tags, using_entity):
                        activate = True
                        logging.debug(f"-> and found suitable target at ({current_x},{current_y}).")
                    else:
                        # we didnt hit the right thing so what happens now?
                        if terrain_collision == ProjectileTerrainCollision.ACTIVATE:
                            activate = True
                            logging.debug(f"-> and hit something. Skill will activate at "
                                          f"({current_x},{current_y}).")
                        elif terrain_collision == ProjectileTerrainCollision.REFLECT:
                            dir_x, dir_y = _get_reflected_direction((current_x, current_y), direction)
                            logging.info(f"-> and hit something. Skill`s direction changed to ({dir_x},{dir_y}).")
                        elif terrain_collision == ProjectileTerrainCollision.FIZZLE:
                            activate = False
                            logging.info(f"-> and hit something. Skill fizzled at ({current_x},{current_y}).")
                else:
                    activate = False
                    logging.warning(f"-> and went out of bounds at ({current_x},{current_y}).")

    # deal with activation
    if activate:
        if skill_data.shape:
            coords = create_shape(skill_data.shape, skill_data.shape_size)
            effected_tiles = world.get_tiles(current_x, current_y, coords)

            # apply any effects
            for effect_name, effect_data in skill_data.effects.items():
                apply_effect(effect_data.effect_type, skill_name, effected_tiles, using_entity)


########################################## GET ####################################

def _get_furthest_free_position(start_position: Tuple[int, int], target_direction: Tuple[int, int],
        max_distance: int, travel_type: ProjectileTravelType) -> Tuple[int, int]:
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
    if travel_type == ProjectileTravel.DIRECT:
        # direct can hit a target at any point during travel
        check_for_target = True
    elif travel_type == ProjectileTravel.ARC:
        # throw can only hit target at end of travel
        check_for_target = False

    # determine impact location N.B. +1 to make inclusive as starting from 1
    for distance in range(1, max_distance + 1):

        # allow throw to hit target
        if travel_type == ProjectileTravel.ARC:
            if distance == max_distance + 1:
                check_for_target = True

        # get current position
        current_x = start_x + (dir_x * distance)
        current_y = start_y + (dir_y * distance)
        tile = world.get_tile((current_x, current_y))

        if tile:
            # did we hit something causing direct to stop
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


def _get_reflected_direction(current_position: Tuple[int, int], target_direction: Tuple[int, int]) -> Tuple[int, int]:
    """
    Use surrounding walls to understand how the object should be reflected.
    """
    current_x, current_y = current_position
    dir_x, dir_y = target_direction

    # work out position of adjacent walls
    adj_tile = world.get_tile((current_x, current_y - dir_y))
    if adj_tile:
        collision_adj_y = world.tile_has_tag(adj_tile, TargetTag.BLOCKED_MOVEMENT)
    else:
        # found no tile
        collision_adj_y = True

    adj_tile = world.get_tile((current_x - dir_x, current_y))
    if adj_tile:
        collision_adj_x = world.tile_has_tag(adj_tile, TargetTag.BLOCKED_MOVEMENT)
    else:
        # found no tile
        collision_adj_x = True

    # where did we collide?
    if collision_adj_x:
        if collision_adj_y:
            # hit a corner, bounce back towards entity
            dir_x *= -1
            dir_y *= -1
        else:
            # hit horizontal wall, reverse y direction
            dir_y *= -1
    else:
        if collision_adj_y:
            # hit a vertical wall, reverse x direction
            dir_x *= -1
        else:  # not collision_adj_x and not collision_adj_y:
            # hit a single piece, on the corner, bounce back towards entity
            dir_x *= -1
            dir_y *= -1

    return dir_x, dir_y


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

def apply_effect(effect_type: EffectTypeType, skill_name: str, effected_tiles: List[Tile], using_entity: int):
    """
    Apply an effect to all tiles in a list.:
    """
    name = entity.get_name(using_entity)
    log_string = f"Applying {effect_type} effect; caused by '{skill_name}' from '{name}'."
    logging.info(log_string)

    if effect_type == EffectType.DAMAGE:
        _apply_damage_effect(skill_name, effected_tiles, using_entity)
    elif effect_type == EffectType.APPLY_AFFLICTION:
        _apply_affliction_effect(skill_name, effected_tiles, using_entity)
    elif effect_type == EffectType.ADD_ASPECT:
        _apply_aspect_effect(skill_name, effected_tiles)


def _apply_aspect_effect(skill_name: str, effected_tiles: List[Tile]):
    data = library.get_skill_effect_data(skill_name, EffectType.ADD_ASPECT)

    for tile in effected_tiles:
        _create_aspect(data.aspect_name, tile)


def _create_aspect(aspect_name: str, tile: Tile):
    data = library.get_aspect_data(aspect_name)
    position: Position
    aspect: Aspect
    entities = entity.get_entities_and_components_in_area([tile], Aspect)

    for ent, (position, aspect) in entities.items():
        # if there is an active version of the same aspect already
        # TODO - should probably move this check outside of this func
        if aspect:
            # increase duration to initial value
            aspect.aspects[aspect_name] = data.duration
        else:
            entity.create([Position(position.x, position.y), Aspect({aspect_name: data.duration})])


def _apply_affliction_effect(skill_name: str, effected_tiles: List[Tile], attacker: int):
    effect_data = library.get_skill_effect_data(skill_name, EffectType.APPLY_AFFLICTION)
    affliction_data = library.get_affliction_data(effect_data.affliction_name)
    attackers_stats = entity.get_combat_stats(attacker)

    # get relevant entities
    entities = entity.get_entities_and_components_in_area(effected_tiles, Resources, HasCombatStats, Identity)

    # loop all relevant entities
    for defender, (position, resources, has_stats, identity) in entities.items():

        # create var to hold the modified duration, if it does change, or the base duration
        base_duration = effect_data.duration
        modified_duration = base_duration
        defender_stats = entity.get_combat_stats(defender)
        tile = world.get_tile((position.x, position.y))

        if tile:
            # check we have all tags
            if world.tile_has_tags(tile, effect_data.required_tags, attacker):
                # Roll for BANE application
                if affliction_data.category == AfflictionCategory.BANE:
                    # if we havent targeted a stat then default to 0
                    if effect_data.stat_to_target:
                        to_hit_score = _calculate_to_hit_score(defender_stats, effect_data.accuracy,
                                                           effect_data.stat_to_target, attackers_stats)
                    else:
                        to_hit_score = 0
                    hit_type = _get_hit_type(to_hit_score)

                    name = entity.get_name(attacker)

                    # check if afflictions applied
                    if hit_type == HitType.GRAZE:
                        msg = f"{name} resisted {effect_data.affliction_name}."
                        publisher.publish(MessageEvent(MessageType.LOG, msg))
                    else:
                        hit_msg = ""

                        # check if there was a crit and if so modify the duration of the afflictions
                        if hit_type == HitType.CRIT:
                            modified_duration = int(base_duration * HitModifier.CRIT)
                            hit_msg = f"a critical "

                        msg = f"{name} succumbed to {hit_msg}{effect_data.affliction_name}."
                        publisher.publish(MessageEvent(MessageType.LOG, msg))

                        _create_affliction(defender, effect_data.affliction_name, modified_duration)

                # Just apply the BOON
                elif affliction_data.category == AfflictionCategory.BOON:
                    _create_affliction(defender, effect_data.affliction_name, modified_duration)


def _create_affliction(ent: int, affliction_name: str, duration: int):
    data = library.get_affliction_data(affliction_name)
    name = entity.get_name(ent)
    affliction = entity.get_entitys_component(ent, Affliction)
    active_affliction_duration = -1
    boon = {}
    bane = {}

    # check if entity already has the afflictions component
    if affliction:
        if data.category == AfflictionCategory.BANE:
            if affliction.banes[affliction_name]:
                active_affliction_duration = affliction.banes[affliction_name]
            else:
                active_affliction_duration = -1
        elif data.category == AfflictionCategory.BOON:
            if affliction.boons[affliction_name]:
                active_affliction_duration = affliction.boons[affliction_name]
            else:
                active_affliction_duration = -1

        # if affliction exists
        if active_affliction_duration:
            logging.debug(f"{name} already has {affliction_name}:{active_affliction_duration}...")

            # alter the duration of the current afflictions if the new one will last longer
            if active_affliction_duration < duration:
                if data.category == AfflictionCategory.BANE:
                    affliction.banes[affliction_name] = duration
                elif data.category == AfflictionCategory.BOON:
                    affliction.boons[affliction_name] = duration

                log_string = f"-> Active duration {active_affliction_duration} is less than new duration " \
                             f"{duration} so duration updated."
                logging.debug(log_string)
            else:
                # no action taken if duration already longer
                log_string = f"-> Active duration {active_affliction_duration} is less than new duration " \
                             f" {duration} so duration remains the same."
                logging.debug(log_string)

    # no current afflictions of same type so apply new one
    else:
        logging.info(f"Applying {affliction_name} afflictions to '{name}' with duration of {duration}.")

    if data.category == AfflictionCategory.BANE:
        bane = {affliction_name: duration}
    elif data.category == AfflictionCategory.BOON:
        boon = {affliction_name: duration}

    entity.add_component(ent, Affliction(boon, bane))


def _apply_damage_effect(skill_name: str, effected_tiles: List[Tile], attacker: int):
    data = library.get_skill_effect_data(skill_name, EffectType.DAMAGE)
    attackers_stats = entity.get_combat_stats(attacker)

    entities = entity.get_entities_and_components_in_area(effected_tiles, Resources, HasCombatStats)

    # loop all relevant entities
    for defender, (position, resources, has_stats) in entities.items():
        tile = world.get_tile((position.x, position.y))
        if tile:
            if world.tile_has_tags(tile, data.required_tags, attacker):
                # get the info to apply the damage
                entitys_stats = entity.get_combat_stats(defender)

                # check we have a stat to target, else default to 0
                if data.stat_to_target:
                    to_hit_score = _calculate_to_hit_score(entitys_stats, data.accuracy, data.stat_to_target,
                                                       attackers_stats)
                else:
                    to_hit_score = 0

                hit_type = _get_hit_type(to_hit_score)
                damage = _calculate_damage(entitys_stats, hit_type, data, attackers_stats)

                # who did the damage? (for informing the player)
                if attacker:
                    attacker_name = entity.get_name(attacker)
                else:
                    attacker_name = "???"

                defender_name = name = entity.get_name(defender)

                # resolve the damage
                if damage > 0:
                    resources.health -= damage

                    # log the outcome
                    if hit_type == HitType.GRAZE:
                        hit_type_desc = "grazes"
                    elif hit_type == HitType.HIT:
                        hit_type_desc = "hits"
                    elif hit_type == HitType.CRIT:
                        hit_type_desc = "crits"
                    else:
                        hit_type_desc = "does something unknown"  # catch all

                    msg = f"{attacker_name} {hit_type_desc} {defender_name} for {damage}."
                    publisher.publish(MessageEvent(MessageType.LOG, msg))

                    # TODO - add the damage type to the text and replace the type with an icon
                    # TODO - add the explanation of the damage roll to a tooltip

                    if resources.health <= 0:
                        publisher.publish(DieEvent(defender))

                else:
                    # log no damage
                    msg = f" {defender_name} resists damage from {attacker_name}."
                    publisher.publish(MessageEvent(MessageType.LOG, msg))


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
