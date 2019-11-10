
import logging
import random

from typing import List
from scripts.core.constants import MessageEventTypes, PrimaryStatTypes, SecondaryStatTypes, HitValues, HitTypes, \
    EffectTypes, SkillShapes
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.effects.add_aspect import AddAspectEffect
from scripts.skills.effects.affect_stat import AffectStatEffect
from scripts.skills.skill import Skill
from scripts.skills.effects.apply_affliction import ApplyAfflictionEffect
from scripts.skills.effects.change_terrain import ChangeTerrainEffect
from scripts.skills.effects.damage import DamageEffect
from scripts.skills.effects.move import MoveEffect
from scripts.world.entity import Entity
from scripts.world.tile import Tile


class SkillMethods:
    """
    Methods for querying skills and skill related info and taking skill actions.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """
    def __init__(self, manager):
        from scripts.managers.world_manager import WorldManager
        self.manager = manager  # type: WorldManager

    def can_use_skill(self, entity, target_pos, skill):
        """
        Confirm entity can use skill on targeted position

        Args:
            entity (Entity):
            target_pos (tuple(int, int)):
            skill (Skill):

        Returns:
            bool: True if can use the skill. Else False.
        """
        from scripts.global_singletons.managers import world

        start_tile = world.Map.get_tile(entity.x, entity.y)
        target_x, target_y = target_pos
        target_tile = world.Map.get_tile(target_x, target_y)
        skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)

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
                    logging.debug( f"Target out of skill range, "
                    f"range {skill_range} < distance {distance}")

            else:
                msg = f"You can't afford the cost."
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

        return False

    def has_required_tags(self, target_tile, required_tags, active_entity=None):
        """
        Check a tile has all required tags

        Args:
            target_tile(Tile):
            required_tags(List):
            active_entity(Entity):

        Returns:
            bool: True if tile has all tags
        """
        # log what is being targeted
        target = ""
        if target_tile.entity:
            if target_tile.entity.name == "player":
                pass
            target += target_tile.entity.name + ", "
        else:
            target += "no entity, "
        if target_tile.aspects:
            for key, aspect in target_tile.aspects.items():
                target += aspect.name + ", "
        else:
            target += "no aspects, "
        target += target_tile.terrain.name  # all tiles have terrain

        # log_string = f"Checking ({target}) for tags {required_tags}..."
        # logging.debug(log_string)

        tags_checked = {}

        # assess all tags
        for tag in required_tags:
            tags_checked[tag.name] = self.manager.Map.tile_has_tag(target_tile, tag, active_entity)

        # if all tags came back true return true
        if all(value for value in tags_checked.values()):
            # log_string = f"-> All tags OK! Tags checked are {tags_checked}"
            # logging.debug(log_string)
            return True
        else:
            # log_string = f"-> Some tags WRONG! Tags checked are {tags_checked}"
            # logging.debug(log_string)
            return False

    @staticmethod
    def can_afford_cost(entity, resource, cost):
        """
        Check if entity can afford the resource cost

        Args:
            entity (Entity):
            resource (SecondaryStatTypes): HP or Stamina
            cost (int):

        Returns:
            bool: True for success, False otherwise.
        """

        # Check if cost can be paid
        value = getattr(entity.combatant, resource.name.lower())
        if value - cost >= 0:
            logging.debug(f"'{entity.name}' can afford cost.")
            return True
        else:
            logging.debug(f"'{entity.name}' cannot afford cost.")
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

    @staticmethod
    def create_skill(actor, skill_tree_name, skill_name):
        """
        Create a SKill object
        Args:
            actor ():
            skill_tree_name ():
            skill_name ():

        Returns:
            Skill: The created skill
        """
        skill = Skill(actor, skill_tree_name, skill_name)

        return skill

    @staticmethod
    def pay_resource_cost(entity, resource, cost):
        """
        Remove the resource cost from the using entity

        Args:
            entity (Entity):
            resource (SecondaryStatTypes): HP or STAMINA
            cost (int):
        """
        resource_value = getattr(entity.combatant, resource.name.lower())
        resource_left = resource_value - cost

        setattr(entity.combatant, resource.name.lower(), resource_left)

        log_string = f"'{entity.name}' paid {cost} {resource.name} and has {resource_left} left."
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
