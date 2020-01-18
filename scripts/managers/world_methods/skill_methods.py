from __future__ import annotations

import logging
import random
from typing import TYPE_CHECKING
from scripts.core.constants import MessageTypes, PrimaryStatTypes, SecondaryStatTypes, HitValues, HitTypes, \
    EffectTypes, SkillShapes, Directions, TargetTags, SkillTerrainCollisions, SkillTravelTypes, SkillExpiryTypes
from scripts.events.game_events import EndTurnEvent
from scripts.events.ui_events import MessageEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.skills.effects.add_aspect import AddAspectEffect
from scripts.skills.effects.affect_stat import AffectStatEffect

from scripts.skills.effects.apply_affliction import ApplyAfflictionEffect
from scripts.skills.effects.change_terrain import ChangeTerrainEffect
from scripts.skills.effects.damage import DamageEffect
from scripts.skills.effects.move import MoveEffect
from scripts.world.components import Resources, Identity, Position
from scripts.world.entity import Entity
from scripts.world.tile import Tile

if TYPE_CHECKING:
    from scripts.managers.world_manager import WorldManager
    from typing import List, Tuple


class SkillMethods:
    """
    Methods for querying skills and skill related info and taking skill actions.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """
    def __init__(self, manager):
        self.manager = manager  # type: WorldManager

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
        world = self.manager
        position = world.Entity.get_component(entity, Position)
        start_tile = world.Map.get_tile((position.x, position.y))
        target_x, target_y = target_pos
        target_tile = world.Map.get_tile((target_x, target_y))
        skill_data = library.get_skill_data(skill_name)

        # check we have everything we need and if so use the skill
        if self.has_required_tags(target_tile, skill_data.required_tags, entity):
            resource_type = skill_data.resource_type
            resource_cost = skill_data.resource_cost
            if self.can_afford_cost(entity, resource_type, resource_cost):
                distance = world.Entity.get_chebyshev_distance_between_tiles(start_tile, target_tile)
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

    def has_required_tags(self, target_tile: Tile, required_tags: List[TargetTags], active_entity: int = None):
        """
        Check a tile has all required tags

        Args:
            target_tile(Tile):
            required_tags(List):
            active_entity(int):

        Returns:
            bool: True if tile has all tags
        """
        tags_checked = {}

        # assess all tags
        for tag in required_tags:
            tags_checked[tag.name] = self.manager.Map.tile_has_tag(target_tile, tag, active_entity)

        # if all tags came back true return true
        if all(value for value in tags_checked.values()):
            return True
        else:
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
        resources = self.manager.Entity.get_component(entity, Resources)
        identity = self.manager.Entity.get_identity(entity)

        # Check if cost can be paid
        value = getattr(resources, resource.name.lower())
        if value - cost >= 0:
            logging.debug(f"'{identity.name}' can afford cost.")
            return True
        else:
            logging.debug(f"'{identity.name}' cannot afford cost.")
            return False

    @staticmethod
    def get_hit_type(to_hit_score):
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
    def create_effect(owner, effect_type):
        """
        Create an effect and assign the owner.

        Args:
            owner (object): Skill or Affliction
            effect_type(EffectTypes):
        """
        created_effect = None

        if effect_type == EffectTypes.DAMAGE:
            created_effect = DamageEffect(owner)
        elif effect_type == EffectTypes.APPLY_AFFLICTION:
            created_effect = ApplyAfflictionEffect(owner)
        elif effect_type == EffectTypes.MOVE:
            created_effect = MoveEffect(owner)
        elif effect_type == EffectTypes.CHANGE_TERRAIN:
            created_effect = ChangeTerrainEffect(owner)
        elif effect_type == EffectTypes.AFFECT_STAT:
            created_effect = AffectStatEffect(owner)
        elif effect_type == EffectTypes.ADD_ASPECT:
            created_effect = AddAspectEffect(owner)

        return created_effect

    @staticmethod
    def calculate_to_hit_score(defender, skill_accuracy, stat_to_target, attacker=None):
        """
        Get the to hit score from the stats of both entities. If Attacker is None then 0 is used for attacker values.
        Args:

            defender (Entity):
            skill_accuracy (int):
            stat_to_target (PrimaryStatTypes):
            attacker (Entity):
        """
        logging.debug(f"Get to hit scores...")

        roll = random.randint(-3, 3)

        # if attacker get their accuracy
        if attacker:
            attacker_value = attacker.combatant.secondary_stats.accuracy
        else:
            attacker_value = 0

        modified_to_hit_score = attacker_value + skill_accuracy + roll

        # mitigate the to hit
        defender_value = getattr(defender.combatant.primary_stats, stat_to_target.name.lower())

        mitigated_to_hit_score = modified_to_hit_score - defender_value

        # log the info
        log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
        logging.debug(log_string)

        return mitigated_to_hit_score

    def pay_resource_cost(self, entity, resource, cost):
        """
        Remove the resource cost from the using entity

        Args:
            entity (Entity):
            resource (SecondaryStatTypes): HP or STAMINA
            cost (int):
        """
        resources = self.manager.Entity.get_component(entity, Resources)
        identity = self.manager.Entity.get_identity(entity)

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

    def use(self, entity: int, skill_name: str, target_direction: Tuple):

        """
        Use the skill

        Args:
            skill_name ():
            entity ():
            target_direction (tuple): x y of the target direction
        """

        data = library.get_skill_data("fungechist", skill_name)  # TODO - remove skill stree
        skill_range = data.range

        # initial values
        position = self.manager.Entity.get_component(entity, Position)
        identity = self.manager.Entity.get_identity(entity)
        start_x = position.x
        start_y = position.y
        dir_x = target_direction[0]
        dir_y = target_direction[1]
        direction = (target_direction[0], target_direction[1])

        # flags
        activate = False
        found_target = False
        check_for_target = False

        logging.info(f"{identity.name} used {skill_name} at ({start_x},{start_y}) in {Directions(direction)}...")

        # determine impact location N.B. +1 to make inclusive
        for distance in range(1, skill_range + 1):
            current_x = start_x + (dir_x * distance)
            current_y = start_y + (dir_y * distance)
            tile = self.manager.Map.get_tile((current_x, current_y))

            # did we hit terrain?
            if self.manager.Map.tile_has_tag(tile, TargetTags.BLOCKED_SPACE, entity):
                # do we need to activate, reflect or fizzle?
                if data.terrain_collision == SkillTerrainCollisions.ACTIVATE:
                    activate = True
                    logging.debug(f"-> and hit a wall. Skill will activate at ({current_x},{current_y}).")
                    break
                elif data.terrain_collision == SkillTerrainCollisions.REFLECT:
                    # work out position of adjacent walls
                    adj_tile = self.manager.Map.get_tile((current_x, current_y - dir_y))
                    collision_adj_y = self.manager.Map.tile_has_tag(adj_tile, TargetTags.BLOCKED_SPACE)
                    adj_tile = self.manager.Map.get_tile((current_x - dir_x, current_y))
                    collision_adj_x = self.manager.Map.tile_has_tag(adj_tile, TargetTags.BLOCKED_SPACE)

                    # where did we collide?
                    if collision_adj_x:
                        if collision_adj_y:
                            # hit a corner, bounce back towards entity
                            dir_x *= -1
                            dir_y *= -1
                        else:
                            # hit horizontal wall, revere y direction
                            dir_y *= -1
                    else:
                        if collision_adj_y:
                            # hit a vertical wall, reverse x direction
                            dir_x *= -1
                        else:  # not collision_adj_x and not collision_adj_y:
                            # hit a single piece, on the corner, bounce back towards entity
                            dir_x *= -1
                            dir_y *= -1

                    logging.info(f"-> and hit a wall. Skill`s direction changed to ({dir_x},{dir_y}).")
                elif data.terrain_collision == SkillTerrainCollisions.FIZZLE:
                    activate = False
                    logging.info(f"-> and hit a wall. Skill fizzled at ({current_x},{current_y}).")
                    break

            # determine travel method
            if data.travel_type == SkillTravelTypes.PROJECTILE:
                # projectile can hit a target at any point during travel
                check_for_target = True
            elif data.travel_type == SkillTravelTypes.THROW:
                # throw can only hit target at end of travel
                if distance == data.range:
                    check_for_target = True
                else:
                    check_for_target = False

            # did we hit something that has the tags we need?
            if check_for_target:
                for tag in data.required_tags:
                    if not self.manager.Map.tile_has_tag(tile, tag, entity):
                        found_target = False
                        break
                    else:
                        found_target = True
                        logging.debug(f"-> and found suitable target at ({current_x},{current_y}).")

            # have we found a suitable target?
            if found_target:
                activate = True
                break

        # if at end of range and activate not triggered
        if distance >= data.range and not activate:
            if data.expiry_type == SkillExpiryTypes.FIZZLE:
                activate = False
                logging.info(f"-> and hit nothing. Skill fizzled at ({current_x},{current_y}).")
            elif data.expiry_type == SkillExpiryTypes.ACTIVATE:
                activate = True
                logging.debug(f"-> and hit nothing. Skill will activate at ({current_x},{current_y}).")

        # deal with activation
        if activate:
            coords = self.manager.Skill.create_shape(data.shape, data.shape_size)
            effected_tiles = self.manager.Map.get_tiles(current_x, current_y, coords)

            # apply any effects
            for effect_name, effect_data in data.effects.items():
                effect = self.manager.Skill.create_effect(self, effect_data.effect_type)
                effect.trigger(effected_tiles)

            # end the turn
            publisher.publish(EndTurnEvent(entity, data.time_cost))

