from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterator, TYPE_CHECKING, Type
from snecs.typedefs import EntityID
from scripts.engine import world
from scripts.engine.component import Position
from scripts.engine.core.constants import AfflictionCategory, AfflictionCategoryType, BASE_ACCURACY, BASE_DAMAGE, \
    DamageType, EffectType, EffectTypeType, PrimaryStat, Shape, ShapeType, TargetTag, TargetTagType
from scripts.engine.effect import AffectStatEffect, DamageEffect, Effect
from scripts.engine.library import library

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class Affliction(ABC):
    """
    A subclass of Affliction represents an affliction (a semi-permanent modifier) and holds all the data that is
    not dependent on the individual instances -  stuff like applicable targets etc.

    An instance of Affliction represents an individual application of that affliction,
    and holds only the data that is tied to the individual use - stuff like
    the user and target.
    """

    # to be overwritten in subclass
    name: str = ""
    description: str = ""
    icon_path: str = ""
    required_tags: List[TargetTagType] = [TargetTag.OTHER_ENTITY]
    identity_tags: List[EffectTypeType] = [EffectType.DAMAGE]
    category: AfflictionCategoryType = AfflictionCategory.BANE
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1

    def __init__(self, creator: EntityID, affected_entity: EntityID, duration: int):
        self.creator = creator
        self.affected_entity = affected_entity
        self.duration = duration

    def apply(self) -> Iterator[Tuple[EntityID, List[Effect]]]:
        """
        An iterator over pairs of (affected entity, [effects])
        """
        position = world.get_entitys_component(self.affected_entity, Position)
        for entity in world.get_affected_entities((position.x, position.y), self.shape, self.shape_size):
            yield entity, self.build_effects(entity)

    @abstractmethod
    def build_effects(self, entity: EntityID):
        """
        Build the effects of this affliction applying to a single entity. Must be overridden by subclass.
        """
        pass


class BoggedDown(Affliction):
    data = library.get_affliction_data("bogged_down")
    name = data.name
    required_tags = data.required_tags
    identity_tags = data.identity_tags
    description = data.description
    icon_path = data.icon
    category = data.category


    def build_effects(self, entity: EntityID) -> List[AffectStatEffect]:
        # TODO - externalise effect data to allow specifying in json

        affect_stat_effect = AffectStatEffect(
            origin=self.creator,
            cause_name=self.name,
            success_effects=[],
            failure_effects=[],
            target=self.affected_entity,
            stat_to_target=PrimaryStat.BUSTLE,
            affect_amount=2
        )

        return [affect_stat_effect]


class Flaming(Affliction):
    data = library.get_affliction_data("flaming")
    name = data.name
    required_tags = data.required_tags
    identity_tags = data.identity_tags
    description = data.description
    icon_path = data.icon
    category = data.category


    def build_effects(self, entity: EntityID) -> List[DamageEffect]:
        """
        Build the effects of this skill applying to a single entity.
        """
        # TODO - externalise effect data to allow specifying in json
        damage_effect = DamageEffect(
            origin=self.creator,
            success_effects=[],
            failure_effects=[],
            target=entity,
            stat_to_target=PrimaryStat.BUSTLE,
            accuracy=BASE_ACCURACY,
            damage=int(BASE_DAMAGE / 2),
            damage_type=DamageType.BURN,
            mod_stat=PrimaryStat.SKULLDUGGERY,
            mod_amount=0.1
        )

        return [damage_effect]

