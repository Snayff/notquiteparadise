from __future__ import annotations

import sys
from dataclasses import asdict
from typing import TYPE_CHECKING, Union

import numpy as np
from snecs import RegisteredComponent
from snecs.typedefs import EntityID

from scripts.engine.internal import library
from scripts.engine.internal.constant import (
    EffectType,
    HeightType,
    PrimaryStatType,
    ReactionTrigger,
    ReactionTriggerType,
    RenderLayer, SecondaryStat, SecondaryStatType,
)
from scripts.engine.internal.definition import EffectData, ReactionData

if TYPE_CHECKING:
    from typing import Dict, List, Optional, Tuple, Type

    import pygame

    from scripts.engine.internal.action import Affliction, Behaviour, Skill
    from scripts.engine.internal.definition import TraitSpritePathsData, TraitSpritesData


__all__ = [
    "Exists",
    "IsPlayer",
    "IsActive",
    "CombatStats",
    "WinCondition",
    "MapCondition",
    "Position",
    "Aesthetic",
    "Tracked",
    "Resources",
    "Physicality",
    "Identity",
    "Traits",
    "Thought",
    "Knowledge",
    "Afflictions",
    "Opinion",
    "FOV",
    "LightSource",
    "Reaction",
    "Lifespan",
    "Immunities",
]


##########################################################
# Components are to hold data that is subject to change.
#########################################################


class NQPComponent(RegisteredComponent):
    """
    Subclass snecs' RegisteredComponent to extend with an on_delete method
    """

    def on_delete(self):
        pass


########################### FLAGS ##############################


class Exists(NQPComponent):
    """
    Empty flag for all entities. Used to allow filters to search for a single component i.e. use a single condition.
    """

    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return Exists()


class IsPlayer(NQPComponent):
    """
    Whether the entity is the player.
    """

    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return IsPlayer()


class IsActive(NQPComponent):
    """
    Whether the entity is active or not. Used to limit entity processing.
    """

    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return IsActive()


class WinCondition(NQPComponent):
    """
    A flag to show that an entity is a win objective
    """

    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return WinCondition()


class MapCondition(NQPComponent):
    """
    A flag to show that an entity will take the player to the next map
    """

    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return MapCondition()


#################### OTHERS #########################

class Position(NQPComponent):
    """
    An entity's position on the map. At initiation provide all positions the entity holds. After initiation only need
     to set the top left, or reference position as the other coordinates are held as offsets.
    """

    def __init__(self, *positions: Tuple[int, int]):
        # Sort the positions from top-left to down-right
        if not positions:
            raise ValueError("Must provide at least 1 coordinate for the entity.")

        sorted_positions = sorted(positions, key=lambda x: (x[0] ** 2 + x[1] ** 2))
        top_left = sorted_positions[0]
        self.offsets = [(x - top_left[0], y - top_left[1]) for x, y in sorted_positions]
        self.reference_position = top_left

    def serialize(self):
        return self.coordinates

    @classmethod
    def deserialize(cls, serialised):
        return Position(*serialised)

    def set(self, x: int, y: int):
        self.reference_position = (x, y)

    def get_outermost(self, direction: Tuple[int, int]) -> Tuple[int, int]:
        """
        Calculate the outermost tile in the direction provided
        :param direction: Direction to use
        :return: The position of the outermost tile
        """
        coordinates = self.coordinates
        # Calculate center
        center = (sum(c[0] for c in coordinates), sum(c[1] for c in coordinates))
        transformed = [np.dot((c[0], c[1]), direction) for c in coordinates]
        # Find the coordinate that is nearest the direction
        arg_max = np.argwhere(transformed == np.amax(transformed))
        # From all the nearest coordinates find the one nearest to the center of the entity
        arg_min = np.argmin(
            np.sqrt((center[0] - transformed[i[0]][0]) ** 2 + (center[1] - transformed[i[0]][1]) ** 2) for i in arg_max
        )
        return coordinates[arg_max[arg_min][0]][0], coordinates[arg_max[arg_min][0]][1]

    @property
    def x(self) -> int:
        """
        :return: The x component of the top-left position
        """
        return self.reference_position[0]

    @property
    def y(self) -> int:
        """
        :return: The y component of the top-left position
        """
        return self.reference_position[1]

    @property
    def coordinates(self) -> List[Tuple[int, int]]:
        """
        :return: The list of coordinates that this Position represents
        """
        return [(self.x + x, self.y + y) for x, y in self.offsets]

    def __contains__(self, key: Tuple[int, int]):
        """
        :param key: Coordinate to test against
        :return: A bool that represents if the Position contains the provided coordinates
        """
        for coordinate in self.coordinates:
            if coordinate == key:
                return True
        return False


class Aesthetic(NQPComponent):
    """
    An entity's sprite.

    N.B. translation to screen coordinates is handled by the camera
    """

    def __init__(
        self,
        current_sprite: pygame.Surface,
        sprites: TraitSpritesData,
        sprite_paths: List[TraitSpritePathsData],
        render_layer: RenderLayer,
        draw_pos: Tuple[float, float],
    ):
        self._sprite_paths: List[TraitSpritePathsData] = sprite_paths
        self.current_sprite: pygame.Surface = current_sprite
        self.sprites: TraitSpritesData = sprites
        self.render_layer = render_layer

        draw_x, draw_y = draw_pos
        self.draw_x: float = draw_x
        self.draw_y: float = draw_y

        self.target_draw_x: float = draw_x
        self.target_draw_y: float = draw_y
        self.current_sprite_duration: float = 0

    def serialize(self):

        # loop all sprite paths and convert to dict
        sprite_paths = []
        for sprite_path in self._sprite_paths:
            sprite_paths.append(asdict(sprite_path))

        _dict = {
            "draw_pos": (self.target_draw_x, self.target_draw_y),  # use target to align with actual position
            "render_layer": self.render_layer,
            "sprite_paths": sprite_paths,
        }
        return _dict

    @classmethod
    def deserialize(cls, serialised):

        x, y = serialised["draw_pos"]
        render_layer = serialised["render_layer"]
        _sprite_paths = serialised["sprite_paths"]

        # unpack sprite paths
        sprite_paths = []
        from scripts.engine.internal.definition import TraitSpritePathsData

        for sprite_path in _sprite_paths:
            sprite_paths.append(TraitSpritePathsData(**sprite_path))

        # convert sprite paths to sprites
        from scripts.engine.core import utility

        sprites = utility.build_sprites_from_paths(sprite_paths)

        return Aesthetic(sprites.idle, sprites, sprite_paths, render_layer, (x, y))


class Tracked(NQPComponent):
    """
    A component to hold info on activities of an entity
    """

    def __init__(self, time_spent: int = 0):
        self.time_spent: int = time_spent

    def serialize(self):
        return self.time_spent

    @classmethod
    def deserialize(cls, serialised):
        return Tracked(serialised)


class Resources(NQPComponent):
    """
    An entity's resources. Members align to Resource constants.
    """

    def __init__(self, health: int = 1, stamina: int = 1):
        self.health: int = health
        self.stamina: int = stamina

    def serialize(self):
        return self.health, self.stamina

    @classmethod
    def deserialize(cls, serialised):
        return Resources(*serialised)


class Physicality(NQPComponent):
    """
    An entity's physical existence within the world.
    """

    def __init__(self, blocks_movement: bool, height: HeightType):
        self.blocks_movement: bool = blocks_movement
        self.height: HeightType = height

    def serialize(self):
        return self.blocks_movement, self.height

    @classmethod
    def deserialize(cls, serialised):
        return Physicality(*serialised)


class Identity(NQPComponent):
    """
    An entity's identity, such as name and description.
    """

    def __init__(self, name: str, description: str = ""):
        self.name: str = name
        self.description: str = description

    def serialize(self):
        return self.name, self.description

    @classmethod
    def deserialize(cls, serialised):
        return cls(*serialised)


class Traits(NQPComponent):
    """
    An entity's traits. Class, archetype, skill set or otherwise defining group.
    """

    def __init__(self, trait_names: List[str]):
        self.names: List[str] = trait_names

    def serialize(self):
        return self.names

    @classmethod
    def deserialize(cls, serialised):
        return Traits(serialised)


class Thought(NQPComponent):
    """
    An ai behaviour to control an entity.
    """

    def __init__(self, behaviour: Behaviour):
        self.behaviour = behaviour

    def serialize(self):
        _dict = {"behaviour_name": self.behaviour.__class__.__name__, "entity": self.behaviour.entity}

        return _dict

    @classmethod
    def deserialize(cls, serialised):
        from scripts.engine.internal.data import store

        behaviour = store.behaviour_registry[serialised["behaviour_name"]]

        return Thought(behaviour(serialised["entity"]))


class Knowledge(NQPComponent):
    """
    An entity's knowledge, including skills.
    """

    def __init__(
        self,
        skills: List[Type[Skill]],
        skill_order: Optional[List[str]] = None,
        cooldowns: Optional[Dict[str, int]] = None,
    ):
        skills = skills or []
        skill_order = skill_order or []
        cooldowns = cooldowns or {}

        # determine if we need to add cooldowns or not - must be before setting self
        if cooldowns:
            _set_cooldown = False
        else:
            _set_cooldown = True

        # dont override skill order if it has been provided
        if skill_order:
            _add_to_order = False
        else:
            _add_to_order = True

        # TODO - make vars private if we should use methods
        self.skill_order: List[str] = skill_order
        self.cooldowns: Dict[str, int] = cooldowns  # TODO - can this be folded into skills?
        self.skill_names: List[str] = []  # TODO - do we even need this anymore?
        self.skills: Dict[str, Type[Skill]] = {}  # dont set skills here, use learn skill

        for skill_class in skills:
            self.add(skill_class, _add_to_order, _set_cooldown)

    def set_skill_cooldown(self, name: str, value: int):
        """
        Sets the cooldown of a skill
        """
        self.cooldowns[name] = max(0, value)

    def add(self, skill: Type[Skill], add_to_order: bool = True, set_cooldown: bool = True):
        """
        Learn a new skill.
        """
        self.skill_names.append(skill.__name__)
        self.skills[skill.__name__] = skill
        if add_to_order:
            self.skill_order.append(skill.__name__)
        if set_cooldown:
            self.cooldowns[skill.__name__] = 0

    def serialize(self):
        _dict = {"skill_names": self.skill_names, "cooldowns": self.cooldowns, "skill_order": self.skill_order}
        return _dict

    @classmethod
    def deserialize(cls, serialised):
        skill_names = serialised["skill_names"]
        cooldowns = serialised["cooldowns"]
        skill_order = serialised["skill_order"]

        skills = []

        from scripts.engine.internal.data import store

        for name in skill_names:
            skills.append(store.skill_registry[name])

        return Knowledge(skills, skill_order, cooldowns)


class Afflictions(NQPComponent):
    """
    An entity's Boons and Banes. held in .active as a list of Affliction.
    """

    def __init__(
        self,
        active: Optional[List[Affliction]] = None,
        stat_modifiers: Optional[Dict[str, Tuple[PrimaryStatType, int]]] = None,
    ):
        active = active or []
        stat_modifiers = stat_modifiers or {}

        self.active: List[Affliction] = active  # TODO - should this be a dict for easier querying?
        self.stat_modifiers: Dict[str, Tuple[PrimaryStatType, int]] = stat_modifiers

    def serialize(self):
        active = {}
        for affliction in self.active:
            active[affliction.__class__.__name__] = (
                affliction.origin,
                affliction.affected_entity,
                affliction.duration,
            )

        _dict = {"active": active, "stat_modifiers": self.stat_modifiers}

        return _dict

    @classmethod
    def deserialize(cls, serialised):
        active_dict = serialised["active"]

        active_instances = []

        from scripts.engine.internal.data import store

        for name, value_tuple in active_dict.items():
            _affliction = store.affliction_registry[name]
            affliction = _affliction(value_tuple[0], value_tuple[1], value_tuple[2])
            active_instances.append(affliction)

        return Afflictions(active_instances, serialised["stat_modifiers"])

    def add(self, affliction: Affliction):
        self.active.append(affliction)

    def remove(self, affliction: Affliction):
        if affliction in self.active:
            # if it is affect_stat remove the affect
            if EffectType.AFFECT_STAT in affliction.identity_tags:
                self.stat_modifiers.pop(affliction.__class__.__name__)

            # remove from active list
            self.active.remove(affliction)


class Opinion(NQPComponent):
    """
    An entity's views on other entities. {entity, opinion}
    """

    def __init__(self, attitudes: Dict[ReactionTriggerType, int], opinions: Optional[Dict[EntityID, int]] = None):
        opinions = opinions or {}
        self.opinions: Dict[EntityID, int] = opinions
        self.attitudes: Dict[ReactionTriggerType, int] = attitudes

    def serialize(self):
        _dict = {"attitudes": self.attitudes, "opinions": self.opinions}
        return _dict

    @classmethod
    def deserialize(cls, serialised):
        attitudes = serialised["attitudes"]
        opinions = {}

        for entity, opinion in serialised["opinions"].items():
            opinions[int(entity)] = opinion

        return Opinion(attitudes, opinions)


class FOV(NQPComponent):
    """
    An entity's field of view. Always starts blank.
    """

    def __init__(self):
        from scripts.engine.core import world

        game_map = world.get_game_map()
        self.map: np.array = game_map.block_sight_map.astype(bool)  # return of compute_fov is bool

    def serialize(self):
        fov_map = self.map.tolist()
        return fov_map

    @classmethod
    def deserialize(cls, serialised):
        fov = FOV()
        fov.map = np.array(serialised)
        return fov


class LightSource(NQPComponent):
    """
    An emitter of light. Takes the light_id from a Light. The Light must be added to the Lightbox of the
    Gamemap separately.
    """

    def __init__(self, light_id: str, radius: int):
        self.light_id: str = light_id
        self.radius: int = radius

    def serialize(self):
        from scripts.engine.core import world

        game_map = world.get_game_map()
        light_box = game_map.light_box
        light = light_box.get_light(self.light_id)

        _dict = {"pos": light.position, "radius": self.radius, "colour": light.colour, "alpha": light.alpha}
        return _dict

    @classmethod
    def deserialize(cls, serialised):
        pos = serialised["pos"]
        radius = serialised["radius"]
        colour = serialised["colour"]
        alpha = serialised["alpha"]

        from scripts.engine.core import world

        light_id = world.create_light(pos, radius, colour, alpha)

        return LightSource(light_id, radius)

    def on_delete(self):
        """
        Delete the associated light from the Gamemap's Lightbox
        """
        from scripts.engine.core import world

        light_box = world.get_game_map().light_box
        light_box.delete_light(self.light_id)


class Reaction(NQPComponent):
    """
    Holds info about what triggers are in place and what happens as a result
    """

    def __init__(self, reactions: Dict[ReactionTriggerType, ReactionData]):
        self.reactions: Dict[ReactionTriggerType, ReactionData] = reactions

    def serialize(self):
        _dict = {}

        for trigger, reaction_data in self.reactions.items():
            # reaction can be skill name (str) or effect data so need to handle both
            if isinstance(reaction_data.reaction, str):
                reaction = reaction_data.reaction
                effect_dataclass_name = None
            else:
                reaction = asdict(reaction_data.reaction)
                effect_dataclass_name = reaction_data.reaction.__class__.__name__

            _dict[trigger] = {
                "required_opinion": reaction_data.required_opinion,
                "reaction": reaction,
                "effect_dataclass_name": effect_dataclass_name,
                "chance": reaction_data.chance,
            }

        return _dict

    @classmethod
    def deserialize(cls, serialised):
        reactions = {}

        for trigger, reaction_data in serialised.items():
            # reaction can be skill name (str) or effect data so need to handle both
            if isinstance(reaction_data["reaction"], str):
                reaction = reaction_data["reaction"]
            else:
                effect_dataclass = getattr(
                    sys.modules["scripts.engine.internal.definition"], reaction_data["effect_dataclass_name"]
                )
                reaction = effect_dataclass(reaction_data["reaction"])

            _reaction_data = {
                "required_opinion": reaction_data["required_opinion"],
                "reaction": reaction,
                "chance": reaction_data["chance"],
            }
            reactions[trigger] = ReactionData(**_reaction_data)

        return Reaction(reactions)


class Lifespan(NQPComponent):
    """
    Holds info relating to the limited lifespan of an entity. E.g. temporary summons.

    Can be set to INFINITE, which prevents it being reduced each turn.
    """

    def __init__(self, duration: int):
        self.duration = duration

    def serialize(self):
        _dict = {"duration": self.duration}
        return _dict

    @classmethod
    def deserialize(cls, serialised):
        return Lifespan(serialised["duration"])


class Immunities(NQPComponent):
    """
    Holds the details of anything the entity is immune to.

    Can be set to INFINITE, which prevents it being reduced each turn.
    """

    def __init__(self, immunities: Dict[str, int] = None):
        # handle mutable default
        if immunities is None:
            immunities = {}

        self.active: Dict[str, int] = immunities  # name, duration

    def serialize(self):
        _dict = {"active": self.active}
        return _dict

    @classmethod
    def deserialize(cls, serialised):

        return Immunities(serialised["active"])


class CombatStats(NQPComponent):
    def __init__(self, vigour: int, clout: int, skullduggery: int, bustle: int, exactitude: int):
        """
        Set primary stats. Secondary stats pulled from library.
        """
        self._vigour: int = vigour
        self._clout: int = clout
        self._skullduggery: int = skullduggery
        self._bustle: int = bustle
        self._exactitude: int = exactitude

        self._vigour_mod: int = 0
        self._clout_mod: int = 0
        self._skullduggery_mod: int = 0
        self._bustle_mod: int = 0
        self._exactitude_mod: int = 0

        self._max_health: int = library.BASE_STATS_SECONDARY[SecondaryStat.MAX_HEALTH].base_value
        self._max_stamina: int = library.BASE_STATS_SECONDARY[SecondaryStat.MAX_STAMINA].base_value
        self._accuracy: int = library.BASE_STATS_SECONDARY[SecondaryStat.ACCURACY].base_value
        self._resist_burn: int = library.BASE_STATS_SECONDARY[SecondaryStat.RESIST_BURN].base_value
        self._resist_cold: int = library.BASE_STATS_SECONDARY[SecondaryStat.RESIST_COLD].base_value
        self._resist_chemical: int = library.BASE_STATS_SECONDARY[SecondaryStat.RESIST_CHEMICAL].base_value
        self._resist_astral: int = library.BASE_STATS_SECONDARY[SecondaryStat.RESIST_ASTRAL].base_value
        self._resist_mundane: int = library.BASE_STATS_SECONDARY[SecondaryStat.RESIST_MUNDANE].base_value
        self._rush: int = library.BASE_STATS_SECONDARY[SecondaryStat.RUSH].base_value

        self._max_health_mod: int = 0
        self._max_stamina_mod: int = 0
        self._accuracy_mod: int = 0
        self._resist_burn_mod: int = 0
        self._resist_cold_mod: int = 0
        self._resist_chemical_mod: int = 0
        self._resist_astral_mod: int = 0
        self._resist_mundane_mod: int = 0
        self._rush_mod: int = 0


    def amend_base_value(self, stat: Union[PrimaryStatType, SecondaryStatType], amount: int):
        """
        Amend the base value of a stat
        """
        stat_to_amend = getattr(self, "_" + stat)
        stat_to_amend += amount

    def amend_mod_value(self, stat: Union[PrimaryStatType, SecondaryStatType], amount: int):
        """
        Amend the modifier of a stat
        """
        mod_to_amend = getattr(self, "_" + stat + "_mod")
        mod_to_amend += amount

    def _get_secondary_stat(self, stat: SecondaryStatType) -> int:
        """
        Get the value of the secondary stat
        """
        stat_data = library.BASE_STATS_SECONDARY[stat]

        value = getattr(self, "_" + stat.lower())
        value += self.vigour * stat_data.vigour_mod
        value += self.clout * stat_data.clout_mod
        value += self.skullduggery * stat_data.skullduggery_mod
        value += self.bustle * stat_data.bustle_mod
        value += self.exactitude * stat_data.exactitude_mod
        value += getattr(self, "_" + stat.lower() + "_mod")

        return value


    @property
    def vigour(self) -> int:
        """
        Influences healthiness. Never below 1.
        """
        return self._vigour + self._vigour_mod

    @property
    def clout(self) -> int:
        """
        Influences forceful things. Never below 1.
        """
        return self._clout + self._clout_mod

    @property
    def skullduggery(self) -> int:
        """
        Influences sneaky things. Never below 1.
        """
        return self._skullduggery + self._skullduggery_mod

    @property
    def bustle(self) -> int:
        """
        Influences speedy things. Never below 1.
        """
        return self._bustle + self._bustle_mod

    @property
    def exactitude(self) -> int:
        """
        Influences preciseness. Never below 1.
        """
        return self._exactitude + self._exactitude_mod

    @property
    def max_health(self) -> int:
        """
        Total damage an entity can take before death.
        """
        return self._get_secondary_stat(SecondaryStat.MAX_HEALTH)

    @property
    def max_stamina(self) -> int:
        """
        An entities energy to take actions.

        """
        return self._get_secondary_stat(SecondaryStat.MAX_STAMINA)

    @property
    def accuracy(self) -> int:
        """
        An entities likelihood to hit.
        """
        return self._get_secondary_stat(SecondaryStat.ACCURACY)

    @property
    def resist_burn(self) -> int:
        """
        An entities resistance to burn damage.

        """
        return self._get_secondary_stat(SecondaryStat.RESIST_BURN)

    @property
    def resist_cold(self) -> int:
        """
        An entities resistance to cold damage.

        """
        return self._get_secondary_stat(SecondaryStat.RESIST_COLD)

    @property
    def resist_chemical(self) -> int:
        """
        An entities resistance to chemical damage.
        """
        return self._get_secondary_stat(SecondaryStat.RESIST_CHEMICAL)

    @property
    def resist_astral(self) -> int:
        """
        An entities resistance to astral damage.
        """
        return self._get_secondary_stat(SecondaryStat.RESIST_ASTRAL)

    @property
    def resist_mundane(self) -> int:
        """
        An entities resistance to mundane damage.
        """
        return self._get_secondary_stat(SecondaryStat.RESIST_MUNDANE)

    @property
    def rush(self) -> int:
        """
        How quickly an entity does things. Reduce time cost of actions.
        """
        return self._get_secondary_stat(SecondaryStat.RUSH)



