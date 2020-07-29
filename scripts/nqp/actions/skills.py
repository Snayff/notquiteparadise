from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterator
import collections
from snecs.typedefs import EntityID

from scripts.engine import library, world
from scripts.engine.component import Aesthetic, Position
from scripts.engine.core.constants import (DamageType, Direction,
                                           DirectionType, PrimaryStat,
                                           ProjectileExpiry,
                                           ProjectileExpiryType,
                                           ProjectileSpeed,
                                           ProjectileSpeedType, Resource,
                                           ResourceType, Shape, ShapeType,
                                           TargetingMethod,
                                           TargetingMethodType, TargetTag,
                                           TargetTagType, TerrainCollision,
                                           TerrainCollisionType, TravelMethod,
                                           TravelMethodType)
from scripts.engine.effect import (
    ApplyAfflictionEffect, DamageEffect, Effect, MoveActorEffect,
    ReduceSkillCooldownEffect)
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Tuple, List, Optional


def data_defined_skill(cls):
    """
    Class decorator used for initializing skills so as to avoid repeating code.
    """
    cls.set_properties()
    return cls


class Skill(ABC):
    """
    A subclass of Skill represents a skill and holds all the data that is
    not dependent on the individual cast - stuff like shape, base accuracy, etc.

    An instance of Skill represents an individual use of that skill,
    and holds only the data that is tied to the individual use - stuff like
    the user and target.
    """

    # to be overwritten in subclass
    name: str = ""
    description: str = ""
    icon_path: str = ""
    resource_type: ResourceType = Resource.STAMINA
    resource_cost: int = 0
    time_cost: int = 0
    base_cooldown: int = 0
    targeting_method: TargetingMethodType = TargetingMethod.TARGET
    target_directions: List[DirectionType] = []
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1
    required_tags: List[TargetTagType] = [TargetTag.OTHER_ENTITY]
    uses_projectile: bool = False
    projectile_speed: ProjectileSpeedType = ProjectileSpeed.SLOW
    projectile_sprite: str = ""
    travel_method: TravelMethodType = TravelMethod.STANDARD
    range: int = 1
    terrain_collision: TerrainCollisionType = TerrainCollision.FIZZLE
    expiry_type: ProjectileExpiryType = ProjectileExpiry.FIZZLE
    ignore_entities: List[int] = []

    def __init__(self, user: EntityID, target_tile: Tile, direction: DirectionType):
        self.user = user
        self.target_tile = target_tile
        self.direction = direction
        self.projectile = None

    def use(self):
        """
        If uses_projectile then create a projectile to carry the skill effects. Otherwise call self.apply
        """
        logging.debug(f"'{world.get_name(self.user)}' used '{self.name}'.")

        # animate the skill user
        self._play_animation()

        # set the skill on cooldown
        world.set_skill_on_cooldown(self)

        # create the projectile
        if self.uses_projectile:
            from scripts.engine.core.definitions import ProjectileData
            projectile_data = ProjectileData(
                creator=self.user,
                skill_name=self.name,
                skill_instance=self,
                required_tags=self.required_tags,
                direction=self.direction,
                speed=self.projectile_speed,
                travel_method=self.travel_method,
                range=self.range,
                terrain_collision=self.terrain_collision,
                expiry_type=self.expiry_type,
                sprite=self.projectile_sprite
            )
            projectile = world.create_projectile(self.user, (self.target_tile.x, self.target_tile.y), projectile_data)
            self.projectile = projectile
        else:
            world.apply_skill(self)

    def _play_animation(self):
        """
        Play the provided animation on the entity's aesthetic component
        """
        aesthetic = world.get_entitys_component(self.user, Aesthetic)
        animation = self.get_animation(aesthetic)
        if aesthetic and animation:
            aesthetic.current_sprite = animation
            aesthetic.current_sprite_duration = 0

    @abstractmethod
    def get_animation(self, aesthetic: Aesthetic):
        """
        Return the animation to play when executing the skill
        """
        pass

    def apply(self) -> Iterator[Tuple[EntityID, List[Effect]]]:
        """
        An iterator over pairs of (affected entity, [effects])
        """
        applied_entities = collections.defaultdict(lambda: 1)
        entitiy_names = []

        for entity in world.get_affected_entities((self.target_tile.x, self.target_tile.y), self.shape,
                                                  self.shape_size, self.direction):

            yield entity, self.build_effects(entity, applied_entities[entity])
            entitiy_names.append(world.get_name(entity))
            applied_entities[entity] -= library.GAME_CONFIG.reduced_effectiveness_multi_tile_modifier

        logging.debug(f"'{world.get_name(self.user)}' applied '{self.name}' to {entitiy_names}.")

    @abstractmethod
    def build_effects(self, entity, effect_strength: float):
        """
        Build the effects of this skill applying to a single entity. Must be overridden by subclass.
        """
        pass

    @classmethod
    def set_properties(cls):
        """
        Sets the class properties of the skill from a skill name
        """
        cls.data = library.SKILLS[cls.name]
        cls.required_tags = cls.data.required_tags
        cls.description = cls.data.description
        cls.icon_path = cls.data.icon
        cls.resource_type = cls.data.resource_type
        cls.resource_cost = cls.data.resource_cost
        cls.time_cost = cls.data.time_cost
        cls.base_cooldown = cls.data.cooldown
        cls.targeting_method = cls.data.targeting_method
        cls.target_directions = cls.data.target_directions
        cls.shape = cls.data.shape
        cls.shape_size = cls.data.shape_size
        cls.uses_projectile = cls.data.uses_projectile
        if cls.uses_projectile:
            cls.projectile_speed = getattr(ProjectileSpeed, cls.data.projectile_speed.upper())
        cls.projectile_sprite = cls.data.projectile_sprite
        cls.travel_method = cls.data.travel_method
        cls.range = cls.data.range
        cls.terrain_collision = cls.data.terrain_collision
        cls.expiry_type = cls.data.expiry_type


class Move(Skill):
    """
    Basic move for an entity.
    """
    # Move's definitions are not defined in the json. They are set here and only here.
    name = "move"
    required_tags = [TargetTag.SELF]
    description = "this is the normal movement."
    icon_path = ""
    resource_type = Resource.STAMINA
    resource_cost = 0
    time_cost = library.GAME_CONFIG.base_values.move_cost
    base_cooldown = 0
    targeting_method = TargetingMethod.TARGET
    target_directions = [
        Direction.UP_LEFT,
        Direction.UP,
        Direction.UP_RIGHT,
        Direction.LEFT,
        Direction.CENTRE,
        Direction.RIGHT,
        Direction.DOWN_LEFT,
        Direction.DOWN,
        Direction.DOWN_RIGHT
    ]
    shape = Shape.TARGET
    shape_size = 1
    uses_projectile = False

    def __init__(self, user: EntityID, target_tile: Tile, direction):
        """
        Only Move needs an init as it overrides the target tile
        """
        # override target
        position = world.get_entitys_component(user, Position)
        if position:
            tile = world.get_tile((position.x, position.y))
        else:
            tile = world.get_tile((0, 0))

        super().__init__(user, tile, direction)

    def build_effects(self, entity: EntityID, effect_strength: float) -> List[MoveActorEffect]:
        """
        Build the effects of this skill applying to a single entity.
        """

        move_effect = MoveActorEffect(
            origin=self.user,
            target=entity,
            success_effects=[],
            failure_effects=[],
            direction=self.direction,
            move_amount=1
        )

        return [move_effect]

    def get_animation(self, aesthetic: Aesthetic):
        # this special case is handled in the MoveActorEffect
        return None


@data_defined_skill
class BasicAttack(Skill):
    """
    Basic attack for an entity
    """
    name = "basic_attack"

    def build_effects(self, entity: EntityID, effect_strength: float) -> List[DamageEffect]:
        """
        Build the effects of this skill applying to a single entity.
        """
        # TODO - externalise effect data to allow specifying in json
        damage_effect = DamageEffect(
            origin=self.user,
            success_effects=[],
            failure_effects=[],
            target=entity,
            stat_to_target=PrimaryStat.VIGOUR,
            accuracy=library.GAME_CONFIG.base_values.accuracy,
            damage=int(library.GAME_CONFIG.base_values.damage * effect_strength),
            damage_type=DamageType.MUNDANE,
            mod_stat=PrimaryStat.CLOUT,
            mod_amount=0.1
        )

        return [damage_effect]

    def get_animation(self, aesthetic: Aesthetic):
        # we can show animations depending on the direction with self.direction
        return aesthetic.sprites.attack


@data_defined_skill
class Lunge(Skill):
    """
    Lunge skill for an entity
    """
    name = "lunge"
    # FIXME - only applying damage when moving 2 spaces, anything less fails to apply.

    def __init__(self, user: EntityID, tile: Tile, direction: DirectionType):
        """
        Set the target tile as the current tile since we need to move.
        N.B. ignores provided tile.
        """
        position = world.get_entitys_component(user, Position)
        if position:
            _tile = world.get_tile((position.x, position.y))
        else:
            _tile = world.get_tile((0, 0))  # should always have position but just in case
        super().__init__(user, _tile, direction)
        self.move_amount = 2

    def build_effects(self, entity: EntityID, effect_strength: float) -> List[Effect]:
        """
        Build the skill effects
        """

        # chain the effects conditionally

        cooldown_effect = self._build_cooldown_reduction_effect(
            entity=entity
        )
        damage_effect = self._build_damage_effect(
            success_effects=[cooldown_effect],
            effect_strength=effect_strength
        )
        move_effect = self._build_move_effect(
            entity=entity,
            success_effects=([damage_effect] if damage_effect else [])
        )

        return [move_effect]

    def _build_move_effect(self, entity: EntityID, success_effects: List[Effect]) -> MoveActorEffect:
        """
        Return the move effect for the lunge
        """
        move_effect = MoveActorEffect(
            origin=self.user,
            target=entity,
            success_effects=success_effects,
            failure_effects=[],
            direction=self.direction,
            move_amount=self.move_amount
        )
        return move_effect

    def _build_damage_effect(self, success_effects: List[Effect], effect_strength: float) -> Optional[DamageEffect]:
        """
        Return the damage effect for the lunge
        """
        target = self._find_target()
        damage_effect = None
        if target:
            damage_effect = DamageEffect(
                origin=self.user,
                success_effects=success_effects,
                failure_effects=[],
                target=target,
                stat_to_target=PrimaryStat.VIGOUR,
                accuracy=library.GAME_CONFIG.base_values.accuracy,
                damage=int(library.GAME_CONFIG.base_values.damage * effect_strength),
                damage_type=DamageType.MUNDANE,
                mod_stat=PrimaryStat.CLOUT,
                mod_amount=0.1
            )
        return damage_effect

    def _find_target(self) -> Optional[EntityID]:
        """
        Find the first entity that will be affected by the lunge
        """
        increment = (self.direction[0] * (self.move_amount + 1), self.direction[1] * (self.move_amount + 1))
        target_tile_pos = (self.target_tile.x + increment[0], self.target_tile.y + increment[1])
        entities = world.get_entities_on_tile(world.get_tile(target_tile_pos))

        if not entities:
            return None
        return entities[0]

    def _build_cooldown_reduction_effect(self, entity: EntityID) -> ReduceSkillCooldownEffect:
        """
        Returns an effect that executes the cooldown effect for the lunge
        """
        cooldown_effect = ReduceSkillCooldownEffect(
            origin=self.user,
            target=entity,
            skill_name=self.name,
            amount=2,
            success_effects=[],
            failure_effects=[]
        )
        return cooldown_effect

    def get_animation(self, aesthetic: Aesthetic):
        return aesthetic.sprites.attack


@data_defined_skill
class TarAndFeather(Skill):
    """
    TarAndFeather skill for an entity
    """
    name = "tar_and_feather"

    def __init__(self, user: EntityID, target_tile: Tile, direction: DirectionType):
        super().__init__(user, target_tile, direction)
        self.affliction_name = 'flaming'
        self.affliction_duration = 5
        self.reduced_modifier = 0.5
        self.cone_size = 1

    def build_effects(self, hit_entity: EntityID, effect_strength: float) -> List[Effect]:
        """
        Build the skill effects
        """
        # get position
        position = world.get_entitys_component(hit_entity, Position)
        if not position:
            return []

        # the cone should start where the hit occurred and in the direction of the projectile.
        entities_in_cone = world.get_affected_entities((position.x, position.y), Shape.CONE, self.cone_size,
                                                       self.direction)
        # we should also ignore the hit entity and the projectile from the extra effects
        entities_in_cone = [x for x in entities_in_cone if x is not hit_entity and x is not self.projectile]

        reduced_effects = []
        for entity_in_cone in entities_in_cone:
            reduced_effects += self._create_effects(target=entity_in_cone, modifier=self.reduced_modifier * effect_strength)
            logging.warning(f"creating effects for {entity_in_cone}")

        first_hit_effects = self._create_effects(target=hit_entity, success_effects=reduced_effects, modifier=effect_strength)

        return first_hit_effects

    def _create_effects(self, target: EntityID, success_effects: List[Effect] = None, modifier: float = 1.0):
        damage_effect = self._build_damage_effect(target, success_effects or [], modifier)
        flaming_effect = self._build_flaming_effect(target, modifier)
        return [damage_effect, flaming_effect]

    def _build_flaming_effect(self, entity: EntityID, modifier: float):
        flaming_effect = ApplyAfflictionEffect(
            origin=self.user,
            target=entity,
            affliction_name=self.affliction_name,
            duration=max(1, int(self.affliction_duration * modifier)),
            success_effects=[],
            failure_effects=[]
        )
        return flaming_effect

    def _build_damage_effect(self, entity: EntityID, success_effects: List[Effect], modifier: float):
        damage_effect = DamageEffect(
            origin=self.user,
            success_effects=success_effects,
            failure_effects=[],
            target=entity,
            stat_to_target=PrimaryStat.VIGOUR,
            accuracy=library.GAME_CONFIG.base_values.accuracy,
            damage=int(library.GAME_CONFIG.base_values.damage * modifier),
            damage_type=DamageType.MUNDANE,
            mod_stat=PrimaryStat.CLOUT,
            mod_amount=0.1
        )
        return damage_effect

    def get_animation(self, aesthetic: Aesthetic):
        return aesthetic.sprites.attack
