from __future__ import annotations

import logging
import random
from typing import TYPE_CHECKING
from scripts.core.constants import MessageTypes, PrimaryStatTypes, SecondaryStatTypes, HitValues, HitTypes, \
    EffectTypes, SkillShapes, Directions, TargetTags, SkillTerrainCollisions, SkillTravelTypes, SkillExpiryTypes, \
    HitModifiers, AfflictionCategory
from scripts.events.entity_events import DieEvent
from scripts.events.ui_events import MessageEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.world.data_classes.effect_dataclass import EffectData
from scripts.world.combat_stats import CombatStats
from scripts.world.components import Resources, Position, HasCombatStats, Affliction, Aspect, Identity

from scripts.world.tile import Tile

if TYPE_CHECKING:
    from scripts.managers.world_manager.world_manager import WorldManager
    from typing import List, Tuple


class SkillMethods:
    """
    Methods for querying skills and skill related info and taking skill actions.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """

    def __init__(self, manager):
        self._manager = manager  # type: WorldManager

    ############## CHECKS ###############

    def can_use(self, entity: int, target_pos: Tuple[int, int], skill_name: str):
        """
        Confirm entity can use skill on targeted position

        Args:
            entity ():
            target_pos ():
            skill_name ():

        Returns:
            bool: True if can use the skill. Else False.
        """
        world = self._manager
        position = world.Entity.get_entitys_component(entity, Position)
        start_tile = world.Map.get_tile((position.x, position.y))
        target_x, target_y = target_pos
        target_tile = world.Map.get_tile((target_x, target_y))
        skill_data = library.get_skill_data(skill_name)

        # check we have everything we need and if so use the skill
        if start_tile and target_tile:
            if world.Map.tile_has_tags(target_tile, skill_data.required_tags, entity):
                resource_type = skill_data.resource_type
                resource_cost = skill_data.resource_cost
                if self.can_afford_cost(entity, resource_type, resource_cost):
                    distance = world.Map.get_chebyshev_distance((start_tile.x, start_tile.y), target_pos)
                    skill_range = skill_data.range
                    if distance <= skill_range:
                        return True
                    else:
                        logging.debug(f"Target out of skill range, "
                                      f"range {skill_range} < distance {distance}")

                else:
                    msg = f"You can't afford the cost."
                    publisher.publish(MessageEvent(MessageTypes.LOG, msg))

        return False

    def can_afford_cost(self, entity: int, resource: SecondaryStatTypes, cost: int):
        """
        Check if entity can afford the resource cost

        Args:
            entity (int):
            resource (SecondaryStatTypes): HP or Stamina
            cost (int):

        Returns:
            bool: True for success, False otherwise.
        """
        resources = self._manager.Entity.get_entitys_component(entity, Resources)
        identity = self._manager.Entity.get_identity(entity)

        # Check if cost can be paid
        value = getattr(resources, resource.lower())
        if value - cost >= 0:
            logging.debug(f"'{identity.name}' can afford cost.")
            return True
        else:
            logging.debug(f"'{identity.name}' cannot afford cost.")
            return False

    ################ ACTIONS #############

    def pay_resource_cost(self, entity, resource, cost):
        """
        Remove the resource cost from the using entity

        Args:
            entity (Entity):
            resource (SecondaryStatTypes): HP or STAMINA
            cost (int):
        """
        resources = self._manager.Entity.get_entitys_component(entity, Resources)
        identity = self._manager.Entity.get_identity(entity)

        resource_value = getattr(resources, resource.name.lower())
        resource_left = resource_value - cost

        setattr(resources, resource.name.lower(), resource_left)

        log_string = f"'{identity.name}' paid {cost} {resource.name} and has {resource_left} left."
        logging.debug(log_string)

    @staticmethod
    def create_shape(shape, size):
        """
        Get a list of coords from a shape and size.

        Args:
            shape (SkillShapes):
            size (int):

        Returns:
            List[Tuple[int, int]]
        """
        list_of_coords = []

        if shape == SkillShapes.TARGET:
            list_of_coords.append((0, 0))  # single target, centred on selection

        elif shape == SkillShapes.SQUARE:
            width = size
            height = size

            for x in range(-width, width + 1):
                for y in range(-height, height + 1):
                    list_of_coords.append((x, y))

        elif shape == SkillShapes.CIRCLE:
            radius = (size + size + 1) / 2

            for x in range(-size, size + 1):
                for y in range(-size, size + 1):
                    if x * x + y * y < radius * radius:
                        list_of_coords.append((x, y))

        elif shape == SkillShapes.CROSS:
            x_coords = [-1, 1]

            for x in x_coords:
                for y in range(-size, size + 1):

                    # ignore 0's to ensure no duplication when running through the range
                    # the multiplication of x by y means they are always both 0 if y is
                    if y != 0:
                        list_of_coords.append((x * y, y))

            list_of_coords.append((0, 0))  # add selection back in

        return list_of_coords

    def use(self, using_entity: int, skill_name: str, start_position: Tuple[int, int], target_direction: Tuple[int,
    int]):

        """
        Use the skill
        """
        # initial values
        skill_data = library.get_skill_data(skill_name)
        skill_range = skill_data.range
        terrain_collision = skill_data.terrain_collision
        travel_type = skill_data.travel_type
        expiry_type = skill_data.expiry_type
        identity = self._manager.Entity.get_identity(using_entity)
        start_x, start_y = start_position
        current_x, current_y = start_position
        dir_x, dir_y = target_direction
        direction = (target_direction[0], target_direction[1])

        # flags
        activate = False
        fizzle = False

        logging.info(f"{identity.name} used {skill_name} at ({start_x},{start_y}) in {Directions(direction)}...")

        # continue finding the position to use the skill on until we fizzle or activate
        while not activate and not fizzle:

            # get last free position in direction
            current_x, current_y = self._get_furthest_free_position(start_position, (dir_x, dir_y), skill_range,
                                                                    travel_type)

            # determine how far we've travelled
            distance = max(abs(start_x) - abs(current_x), abs(start_y) - abs(current_y))

            # are we at max distance?
            if distance >= skill_range:
                # handle expiry type
                if expiry_type == SkillExpiryTypes.FIZZLE:
                    fizzle = True
                    logging.info(f"-> and hit nothing. Skill fizzled at ({current_x},{current_y}).")
                elif expiry_type == SkillExpiryTypes.ACTIVATE:
                    activate = True
                    logging.debug(f"-> and hit nothing. Skill will activate at ({current_x},{current_y}).")
            else:
                # we arent at max so we must have hit something one space further along
                current_x, current_y = current_x + dir_x, current_y + dir_y
                tile = self._manager.Map.get_tile((current_x, current_y))

                if tile:
                    # did we hit something that has the tags we need?
                    if self._manager.Map.tile_has_tags(tile, skill_data.required_tags, using_entity):
                        activate = True
                        logging.debug(f"-> and found suitable target at ({current_x},{current_y}).")
                    else:
                        # we didnt hit the right thing so what happens now?
                        if terrain_collision == SkillTerrainCollisions.ACTIVATE:
                            activate = True
                            logging.debug(f"-> and hit something. Skill will activate at "
                                          f"({current_x},{current_y}).")
                        elif terrain_collision == SkillTerrainCollisions.REFLECT:
                            dir_x, dir_y = self._get_reflected_direction((current_x, current_y), direction)
                            logging.info(f"-> and hit something. Skill`s direction changed to ({dir_x},{dir_y}).")
                        elif terrain_collision == SkillTerrainCollisions.FIZZLE:
                            activate = False
                            logging.info(f"-> and hit something. Skill fizzled at ({current_x},{current_y}).")
                else:
                    activate = False
                    logging.warning(f"-> and went out of bounds at ({current_x},{current_y}).")

        # deal with activation
        if activate:
            coords = self._manager.Skill.create_shape(skill_data.shape, skill_data.shape_size)
            effected_tiles = self._manager.Map.get_tiles(current_x, current_y, coords)

            # apply any effects
            for effect_name, effect_data in skill_data.effects.items():
                self.apply_effect(effect_data.effect_type, skill_name, effected_tiles, using_entity)

    def _get_furthest_free_position(self, start_position: Tuple[int, int], target_direction: Tuple[int, int],
            max_distance: int, travel_type: SkillTravelTypes) -> Tuple[int, int]:
        """
        Checks each position in a line and returns the last position that doesnt block movement. If no position in
        range blocks movement then the last position checked is returned. If all positions in range block movement
        then starting position is returned.

        Args:
            start_position ():
            target_direction ():
            max_distance ():

        Returns:

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
        if travel_type == SkillTravelTypes.PROJECTILE:
            # projectile can hit a target at any point during travel
            check_for_target = True
        elif travel_type == SkillTravelTypes.THROW:
            # throw can only hit target at end of travel
            check_for_target = False

        # determine impact location N.B. +1 to make inclusive as starting from 1
        for distance in range(1, max_distance + 1):

            # allow throw to hit target
            if travel_type == SkillTravelTypes.THROW:
                if distance == max_distance + 1:
                    check_for_target = True

            # get current position
            current_x = start_x + (dir_x * distance)
            current_y = start_y + (dir_y * distance)
            tile = self._manager.Map.get_tile((current_x, current_y))

            if tile:
                # did we hit something causing projectile to stop
                if self._manager.Map.tile_has_tag(tile, TargetTags.BLOCKED_MOVEMENT):
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

    def _get_reflected_direction(self, current_position: Tuple[int, int], target_direction: Tuple[int,
    int]) -> Tuple[int, int]:
        """
        Use surrounding walls to understand how the object should be reflected.

        Args:
            current_position ():
            target_direction ():

        Returns:

        """
        current_x, current_y = current_position
        dir_x, dir_y = target_direction

        # work out position of adjacent walls
        adj_tile = self._manager.Map.get_tile((current_x, current_y - dir_y))
        if adj_tile:
            collision_adj_y = self._manager.Map.tile_has_tag(adj_tile, TargetTags.BLOCKED_MOVEMENT)
        else:
            # found no tile
            collision_adj_y = True

        adj_tile = self._manager.Map.get_tile((current_x - dir_x, current_y))
        if adj_tile:
            collision_adj_x = self._manager.Map.tile_has_tag(adj_tile, TargetTags.BLOCKED_MOVEMENT)
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

    ############ EFFECTS ################

    def apply_effect(self, effect_type: EffectTypes, skill_name: str, effected_tiles: List[Tile], using_entity: int):
        """
        Apply an effect to all tiles in a list.

        Args:
            effect_type ():
            skill_name ():
            effected_tiles ():
            using_entity ():
        """
        log_string = f"Applying {effect_type.name} effect; caused by `{skill_name}` from `{using_entity}`."
        logging.debug(log_string)

        if effect_type == EffectTypes.DAMAGE:
            self._apply_damage_effect(skill_name, effected_tiles, using_entity)
        elif effect_type == EffectTypes.APPLY_AFFLICTION:
            self._apply_affliction_effect(skill_name, effected_tiles, using_entity)
        elif effect_type == EffectTypes.ADD_ASPECT:
            self._apply_aspect_effect(skill_name, effected_tiles)

    def _apply_aspect_effect(self, skill_name: str, effected_tiles: List[Tile]):
        data = library.get_skill_effect_data(skill_name, EffectTypes.ADD_ASPECT)

        for tile in effected_tiles:
            self._create_aspect(data.aspect_name, tile)

    def _create_aspect(self, aspect_name: str, tile: Tile):
        data = library.get_aspect_data(aspect_name)
        entity, position, aspects = self._manager.Entity.get_entities_and_components_in_area([tile], Aspect)

        # if there is an active version of the same aspect already
        if aspects:
            # increase duration to initial value
            aspects.aspects[aspect_name] = data.duration
        else:
            self._manager.Entity.create([Position(position.x, position.y), Aspect({aspect_name: data.duration})])

    def _apply_affliction_effect(self, skill_name: str, effected_tiles: List[Tile], attacker: int):
        world = self._manager
        effect_data = library.get_skill_effect_data(skill_name, EffectTypes.APPLY_AFFLICTION)
        affliction_data = library.get_affliction_data(effect_data.affliction_name)
        attackers_stats = world.Entity.get_combat_stats(attacker)

        # get relevant entities
        entities = world.Entity.get_entities_and_components_in_area(effected_tiles, Resources, HasCombatStats, Identity)

        # loop all relevant entities
        for defender, (position, resources, has_stats, identity) in entities.items():

            # create var to hold the modified duration, if it does change, or the base duration
            base_duration = effect_data.duration
            modified_duration = base_duration
            defender_stats = world.Entity.get_combat_stats(defender)

            # check we have all tags
            tile = world.Map.get_tile((position.x, position.y))
            if tile:
                if world.Map.tile_has_tags(tile, effect_data.required_tags, attacker):
                    # Roll for BANE application
                    if affliction_data.category == AfflictionCategory.BANE:
                        to_hit_score = self._calculate_to_hit_score(defender_stats, effect_data.accuracy,
                                                                    effect_data.stat_to_target, attackers_stats)
                        hit_type = self._get_hit_type(to_hit_score)

                        # check if afflictions applied
                        if hit_type == HitTypes.GRAZE:
                            msg = f"{identity.name} resisted {effect_data.affliction_name}."
                            publisher.publish(MessageEvent(MessageTypes.LOG, msg))
                        else:
                            hit_msg = ""

                            # check if there was a crit and if so modify the duration of the afflictions
                            if hit_type == HitTypes.CRIT:
                                modified_duration = int(base_duration * HitModifiers.CRIT.value)
                                hit_msg = f"a critical "

                            msg = f"{identity.name} succumbed to {hit_msg}{effect_data.affliction_name}."
                            publisher.publish(MessageEvent(MessageTypes.LOG, msg))

                            self._create_affliction(defender, effect_data.affliction_name, modified_duration)

                    # Just apply the BOON
                    elif affliction_data.affliction_category == AfflictionCategory.BOON:
                        self._create_affliction(defender, effect_data.affliction_name, modified_duration)

    def _create_affliction(self, entity: int, affliction_name: str, duration: int):
        data = library.get_affliction_data(affliction_name)
        identity = self._manager.Entity.get_identity(entity)
        afflictions = self._manager.Entity.get_entitys_component(entity, Affliction)
        active_affliction_duration = False
        boon = {}
        bane = {}

        # check if entity already has the afflictions component
        if afflictions:
            if data.category == AfflictionCategory.BANE:
                if afflictions.banes[affliction_name]:
                    active_affliction_duration = afflictions.banes[affliction_name]
                else:
                    active_affliction_duration = False
            elif data.category == AfflictionCategory.BOON:
                if afflictions.boons[affliction_name]:
                    active_affliction_duration = afflictions.boons[affliction_name]
                else:
                    active_affliction_duration = False

        # if affliction exists
        if active_affliction_duration:
            logging.debug(f"{identity.name} already has {affliction_name}:{active_affliction_duration}...")

            # alter the duration of the current afflictions if the new one will last longer
            if active_affliction_duration < duration:
                if data.category == AfflictionCategory.BANE:
                    afflictions.banes[affliction_name] = duration
                elif data.category == AfflictionCategory.BOON:
                    afflictions.boons[affliction_name] = duration

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
            logging.info(f"Applying {affliction_name} afflictions to '{identity.name}' with duration of {duration}.")

        if data.category == AfflictionCategory.BANE:
            bane = {affliction_name: duration}
        elif data.category == AfflictionCategory.BOON:
            boon = {affliction_name: duration}

        self._manager.World.add_component(entity, Affliction(boon, bane))

    def _apply_damage_effect(self, skill_name: str, effected_tiles: List[Tile], attacker: int):
        world = self._manager
        data = library.get_skill_effect_data(skill_name, EffectTypes.DAMAGE)
        attackers_stats = world.Entity.get_combat_stats(attacker)

        # get relevant entities
        entities = world.Entity.get_entities_and_components_in_area(effected_tiles, Resources, HasCombatStats)

        # loop all relevant entities
        for defender, (position, resources, has_stats) in entities.items():
            tile = world.Map.get_tile((position.x, position.y))
            if tile:
                if world.Map.tile_has_tags(tile, data.required_tags, attacker):
                    # get the info to apply the damage
                    entitys_stats = world.Entity.get_combat_stats(defender)
                    to_hit_score = self._calculate_to_hit_score(entitys_stats, data.accuracy, data.stat_to_target,
                                                                attackers_stats)
                    hit_type = self._get_hit_type(to_hit_score)
                    damage = self._calculate_damage(entitys_stats, hit_type, data, attackers_stats)

                    # who did the damage? (for informing the player)
                    if attacker:
                        identity = world.Entity.get_identity(attacker)
                        attacker_name = identity.name
                    else:
                        attacker_name = "???"
                    identity = world.Entity.get_identity(defender)
                    defender_name = identity.name

                    # resolve the damage
                    if damage > 0:
                        resources.health -= damage

                        # log the outcome
                        if hit_type == HitTypes.GRAZE:
                            hit_type_desc = "grazes"
                        elif hit_type == HitTypes.HIT:
                            hit_type_desc = "hits"
                        elif hit_type == HitTypes.CRIT:
                            hit_type_desc = "crits"
                        else:
                            hit_type_desc = "does something unknown"  # catch all

                        msg = f"{attacker_name} {hit_type_desc} {defender_name} for {damage}."
                        publisher.publish(MessageEvent(MessageTypes.LOG, msg))

                        # TODO - add the damage type to the text and replace the type with an icon
                        # TODO - add the explanation of the damage roll to a tooltip

                        if resources.health <= 0:
                            publisher.publish(DieEvent(defender))

                    else:
                        # log no damage
                        msg = f" {defender_name} resists damage from {attacker_name}."
                        publisher.publish(MessageEvent(MessageTypes.LOG, msg))

    ############ UTILITY ################

    @staticmethod
    def _calculate_damage(defenders_stats: CombatStats, hit_type: HitTypes, effect_data: EffectData,
            attackers_stats: CombatStats = None):
        """
        Work out the damage to be dealt. if attacking entity is None then value used is 0.
        Args:
            defenders_stats(CombatStats):
            hit_type(HitTypes):
            effect_data (EffectData):
            attackers_stats(CombatStats): Optional. Defaults to None.

        Returns:
            int: damage to be dealt
        """
        logging.debug(f"Calculate damage...")
        data = effect_data

        initial_damage = data.damage
        damage_from_stats = 0

        # get damage from stats of attacker
        if attackers_stats:
            stat_amount = 0
            # get the stat
            for stat in PrimaryStatTypes:
                if stat == data.mod_stat:
                    stat_amount = getattr(attackers_stats, stat.name.lower())
                    break

            damage_from_stats = stat_amount * data.mod_amount

        # get resistance value
        resist_value = getattr(defenders_stats, "resist_" + data.damage_type.name.lower())

        # mitigate damage with defence
        mitigated_damage = (initial_damage + damage_from_stats) - resist_value

        # apply to hit modifier to damage
        if hit_type == HitTypes.CRIT:
            modified_damage = mitigated_damage * HitModifiers.CRIT.value
        elif hit_type == HitTypes.HIT:
            modified_damage = mitigated_damage * HitModifiers.HIT.value
        else:
            modified_damage = mitigated_damage * HitModifiers.GRAZE.value

        # round down the dmg
        int_modified_damage = int(modified_damage)

        # log the info
        log_string = f"-> Initial:{initial_damage}, Mitigated: {format(mitigated_damage, '.2f')},  Modified" \
                     f":{format(modified_damage, '.2f')}, Final: {int_modified_damage}"
        logging.debug(log_string)

        return int_modified_damage

    @staticmethod
    def _get_hit_type(to_hit_score):
        """
        Get the hit type from the to hit score
        Args:
            to_hit_score:

        Returns:
            HitTypes:
        """
        if to_hit_score >= HitValues.CRIT.value:
            return HitTypes.CRIT
        elif to_hit_score >= HitValues.HIT.value:
            return HitTypes.HIT
        else:
            return HitTypes.GRAZE

    @staticmethod
    def _calculate_to_hit_score(defenders_stats: CombatStats, skill_accuracy: int, stat_to_target: PrimaryStatTypes,
            attackers_stats: CombatStats = None):
        """
        Get the to hit score from the stats of both entities. If Attacker is None then 0 is used for attacker values.

        Args:

            defenders_stats (CombatStats):
            skill_accuracy (int):
            stat_to_target (PrimaryStatTypes):
            attackers_stats (CombatStats):
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
        defender_value = getattr(defenders_stats, stat_to_target.name.lower())

        mitigated_to_hit_score = modified_to_hit_score - defender_value

        # log the info
        log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
        logging.debug(log_string)

        return mitigated_to_hit_score
