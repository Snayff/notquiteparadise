from __future__ import annotations

import logging
import sys
from dataclasses import asdict
from typing import TYPE_CHECKING, Union

import numpy as np
from snecs import RegisteredComponent
from snecs.typedefs import EntityID

from scripts.engine.internal import library
from scripts.engine.internal.constant import (
    HeightType,
    PrimaryStat,
    PrimaryStatType,
    ReactionTriggerType,
    RenderLayer,
    SecondaryStat,
    SecondaryStatType,
    SpriteCategory,
    SpriteCategoryType,
)
from scripts.engine.internal.definition import ReactionData

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
    "Sight",
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
        )  # type: ignore
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
        sprites: TraitSpritesData,
        sprite_paths: List[TraitSpritePathsData],
        render_layer: RenderLayer,
        draw_pos: Tuple[float, float],
    ):
        self._sprite_paths: List[TraitSpritePathsData] = sprite_paths
        self.sprites: TraitSpritesData = sprites
        self.current_sprite: pygame.Surface = self.sprites.idle
        self.current_sprite_category: SpriteCategoryType = getattr(self.sprites, SpriteCategory.IDLE)
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

        return Aesthetic(sprites, sprite_paths, render_layer, (x, y))

    def set_current_sprite(self, sprite_category: SpriteCategoryType):
        """
        Set the current sprite. Set current sprite duration to 0.
        """
        sprite = getattr(self.sprites, sprite_category)
        self.current_sprite = sprite
        self.current_sprite_category = sprite_category
        self.current_sprite_duration = 0

    def set_draw_to_target(self):
        """
        Set draw_x and draw_y to their target values
        """
        self.draw_x = self.target_draw_x
        self.draw_y = self.target_draw_y


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

        self.skill_order: List[str] = skill_order
        self.cooldowns: Dict[str, int] = cooldowns
        self.skill_names: List[str] = []
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

    def __init__(self, active: Optional[List[Affliction]] = None):
        active = active or []

        self.active: List[Affliction] = active  # TODO - should this be a dict for easier querying?

    def serialize(self):
        active = {}
        for affliction in self.active:
            active[affliction.__class__.__name__] = (
                affliction.origin,
                affliction.affected_entity,
                affliction.duration,
            )

        _dict = {"active": active}

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

        return Afflictions(active_instances)

    def add(self, affliction: Affliction):
        self.active.append(affliction)

    def remove(self, affliction: Affliction):
        if affliction in self.active:
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
    """
    An entities stats used for combat.
    """

    def __init__(self, vigour: int, clout: int, skullduggery: int, bustle: int, exactitude: int):
        """
        Set primary stats. Secondary stats pulled from library.
        """
        self._vigour: int = vigour
        self._clout: int = clout
        self._skullduggery: int = skullduggery
        self._bustle: int = bustle
        self._exactitude: int = exactitude

        self._vigour_mod: Dict[str, int] = {}  # cause, amount
        self._clout_mod: Dict[str, int] = {}
        self._skullduggery_mod: Dict[str, int] = {}
        self._bustle_mod: Dict[str, int] = {}
        self._exactitude_mod: Dict[str, int] = {}

        self._max_health: int = 0
        self._max_stamina: int = 0
        self._accuracy: int = 0
        self._resist_burn: int = 0
        self._resist_cold: int = 0
        self._resist_chemical: int = 0
        self._resist_astral: int = 0
        self._resist_mundane: int = 0
        self._rush: int = 0

        self._max_health_mod: Dict[str, int] = {}  # cause, amount
        self._max_stamina_mod: Dict[str, int] = {}
        self._accuracy_mod: Dict[str, int] = {}
        self._resist_burn_mod: Dict[str, int] = {}
        self._resist_cold_mod: Dict[str, int] = {}
        self._resist_chemical_mod: Dict[str, int] = {}
        self._resist_astral_mod: Dict[str, int] = {}
        self._resist_mundane_mod: Dict[str, int] = {}
        self._rush_mod: Dict[str, int] = {}

    def serialize(self):

        _dict = {
            "vigour": self._vigour,
            "clout": self._clout,
            "skullduggery": self._skullduggery,
            "bustle": self._bustle,
            "exactitude": self._exactitude,
            "vigour_mod": self._vigour_mod,
            "clout_mod": self._clout_mod,
            "skullduggery_mod": self._skullduggery_mod,
            "bustle_mod": self._bustle_mod,
            "exactitude_mod": self._exactitude_mod,
            "max_health": self._max_health,
            "max_stamina": self._max_stamina,
            "accuracy": self._accuracy,
            "resist_burn": self._resist_burn,
            "resist_cold": self._resist_cold,
            "resist_chemical": self._resist_chemical,
            "resist_astral": self._resist_astral,
            "resist_mundane": self._resist_mundane,
            "rush": self._rush,
            "max_health_mod": self._max_health_mod,
            "max_stamina_mod": self._max_stamina_mod,
            "accuracy_mod": self._accuracy_mod,
            "resist_burn_mod": self._resist_burn_mod,
            "resist_cold_mod": self._resist_cold_mod,
            "resist_chemical_mod": self._resist_chemical_mod,
            "resist_astral_mod": self._resist_astral_mod,
            "resist_mundane_mod": self._resist_mundane_mod,
            "rush_mod": self._rush_mod,
        }
        return _dict

    @classmethod
    def deserialize(cls, serialised):
        stats = CombatStats(
            serialised["vigour"],
            serialised["clout"],
            serialised["skullduggery"],
            serialised["bustle"],
            serialised["exactitude"],
        )

        stats._vigour_mod = serialised["vigour_mod"]
        stats._clout_mod = serialised["clout_mod"]
        stats._skullduggery_mod = serialised["skullduggery_mod"]
        stats._bustle_mod = serialised["bustle_mod"]
        stats._exactitude_mod = serialised["exactitude_mod"]

        stats._max_health = serialised["max_health"]
        stats._max_stamina = serialised["max_stamina"]
        stats._accuracy = serialised["accuracy"]
        stats._resist_burn = serialised["resist_burn"]
        stats._resist_cold = serialised["resist_cold"]
        stats._resist_chemical = serialised["resist_chemical"]
        stats._resist_astral = serialised["resist_astral"]
        stats._resist_mundane = serialised["resist_mundane"]
        stats._rush = serialised["rush"]

        stats._max_health_mod = serialised["max_health_mod"]
        stats._max_stamina_mod = serialised["max_stamina_mod"]
        stats._accuracy_mod = serialised["accuracy_mod"]
        stats._resist_burn_mod = serialised["resist_burn_mod"]
        stats._resist_cold_mod = serialised["resist_cold_mod"]
        stats._resist_chemical_mod = serialised["resist_chemical_mod"]
        stats._resist_astral_mod = serialised["resist_astral_mod"]
        stats._resist_mundane_mod = serialised["resist_mundane_mod"]
        stats._rush_mod = serialised["rush_mod"]

        return stats

    def amend_base_value(self, stat: Union[PrimaryStatType, SecondaryStatType], amount: int):
        """
        Amend the base value of a stat
        """
        current_value = getattr(self, "_" + stat)
        setattr(self, "_" + stat, current_value + amount)

    def add_mod(self, stat: Union[PrimaryStatType, SecondaryStatType], cause: str, amount: int) -> bool:
        """
        Amend the modifier of a stat. Returns True if successfully amended, else False.
        """
        mod_to_amend = getattr(self, "_" + stat + "_mod")

        if cause in mod_to_amend:
            logging.info(f"Stat not modified as {cause} has already been applied.")
            return False
        else:
            mod_to_amend[cause] = amount
            return True

    def remove_mod(self, cause: str) -> bool:
        """
        Remove a modifier from a stat. Returns True if successfully removed, else False.
        """
        from scripts.engine.core import utility

        for stat in utility.get_class_members(self.__class__):
            if cause in stat:
                assert isinstance(stat, dict)
                del stat[cause]
                return True

        logging.info(f"Modifier not removed as {cause} does not exist in modifier list.")
        return False

    def _get_secondary_stat(self, stat: SecondaryStatType) -> int:
        """
        Get the value of the secondary stat
        """
        stat_data = library.SECONDARY_STAT_MODS[stat]

        value = getattr(self, "_" + stat.lower())
        value += self.vigour * stat_data.vigour_mod
        value += self.clout * stat_data.clout_mod
        value += self.skullduggery * stat_data.skullduggery_mod
        value += self.bustle * stat_data.bustle_mod
        value += self.exactitude * stat_data.exactitude_mod
        value += self._get_mod_value(stat)

        return value

    def _get_mod_value(self, stat: Union[PrimaryStatType, SecondaryStatType]) -> int:
        mod = getattr(self, "_" + stat + "_mod")

        value = 0
        for modifier in mod.values():
            value += modifier

        return value

    @property
    def vigour(self) -> int:
        """
        Influences healthiness. Never below 1.
        """
        return max(1, self._vigour + self._get_mod_value(PrimaryStat.VIGOUR))

    @property
    def clout(self) -> int:
        """
        Influences forceful things. Never below 1.
        """
        return max(1, self._clout + self._get_mod_value(PrimaryStat.CLOUT))

    @property
    def skullduggery(self) -> int:
        """
        Influences sneaky things. Never below 1.
        """
        return max(1, self._skullduggery + self._get_mod_value(PrimaryStat.SKULLDUGGERY))

    @property
    def bustle(self) -> int:
        """
        Influences speedy things. Never below 1.
        """
        return max(1, self._bustle + self._get_mod_value(PrimaryStat.BUSTLE))

    @property
    def exactitude(self) -> int:
        """
        Influences preciseness. Never below 1.
        """
        return max(1, self._exactitude + self._get_mod_value(PrimaryStat.EXACTITUDE))

    @property
    def max_health(self) -> int:
        """
        Total damage an entity can take before death.
        """
        return max(1, self._get_secondary_stat(SecondaryStat.MAX_HEALTH))

    @property
    def max_stamina(self) -> int:
        """
        An entities energy to take actions.

        """
        return max(1, self._get_secondary_stat(SecondaryStat.MAX_STAMINA))

    @property
    def accuracy(self) -> int:
        """
        An entities likelihood to hit.
        """
        return max(1, self._get_secondary_stat(SecondaryStat.ACCURACY))

    @property
    def resist_burn(self) -> int:
        """
        An entities resistance to burn damage.

        """
        return max(1, self._get_secondary_stat(SecondaryStat.RESIST_BURN))

    @property
    def resist_cold(self) -> int:
        """
        An entities resistance to cold damage.

        """
        return max(1, self._get_secondary_stat(SecondaryStat.RESIST_COLD))

    @property
    def resist_chemical(self) -> int:
        """
        An entities resistance to chemical damage.
        """
        return max(1, self._get_secondary_stat(SecondaryStat.RESIST_CHEMICAL))

    @property
    def resist_astral(self) -> int:
        """
        An entities resistance to astral damage.
        """
        return max(1, self._get_secondary_stat(SecondaryStat.RESIST_ASTRAL))

    @property
    def resist_mundane(self) -> int:
        """
        An entities resistance to mundane damage.
        """
        return max(1, self._get_secondary_stat(SecondaryStat.RESIST_MUNDANE))

    @property
    def rush(self) -> int:
        """
        How quickly an entity does things. Reduce time cost of actions.
        """
        return max(1, self._get_secondary_stat(SecondaryStat.RUSH))


class Sight(NQPComponent):
    """
    An entity's ability to see.
    """

    def __init__(self, sight_range: int):
        self.sight_range: int = sight_range

    def serialize(self):
        _dict = {"sight_range": self.sight_range}
        return _dict

    @classmethod
    def deserialize(cls, serialised):
        return Sight(**serialised)
