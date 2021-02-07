Content Guide
======================

Almost all data is held in the external json files, certainly as much as is possible without limiting gameplay diversity. This is a guide on how to add new content to the game, broken down by content type.

Playable Traits
--------------------
Create a new entry in the traits.json and ensure the `group` is not set to "npc". That's it!

One thing to note is that the `known_skills` must match the class name of a `Skill` registered with the engine. See the Action section for more details.

Example:
.. code-block:: json
    "dandy": {
            "__dataclass__": "TraitData",
            "group":"savvy",
            "bustle": 2,
            "clout": 2,
            "description": "Lounging around the taverns of the world they can always be found one word away from an indignant splutter and a grasp for their sword.",
            "exactitude": -1,
            "name": "irascible dandy",
            "sight_range": 5,
            "known_skills": [
                "Lunge",
                "TarAndFeather"
            ],
            "permanent_afflictions": [
                "none"
            ],
            "skullduggery": 1,
            "sprite_paths": {
                "__dataclass__": "TraitSpritePathsData",
                "idle": "actor/savvy/dandy_idle.png",
                "attack": "actor/savvy/dandy_attack.png",
                "hit": "actor/savvy/dandy_hit.png",
                "dead": "actor/savvy/dandy_dead.png",
                "icon": "actor/savvy/dandy_icon.png",
                "move": "actor/savvy/dandy_move.png"
            },
            "vigour": -1
        },

Actors (NPCs)
-------------------
Create a new entry in traits.json and specify `group` as "npc". Next, create an entry in actors.json and set the `trait_names` to include the key of the trait you just created. The `behaviour_name` must exactly match a `Behaviour` class registered with the engine. See the Action section for more information.

Trait example:
.. code-block:: json
    "dandy": {
            "__dataclass__": "TraitData",
            "group":"savvy",
            "bustle": 2,
            "clout": 2,
            "description": "Lounging around the taverns of the world they can always be found one word away from an indignant splutter and a grasp for their sword.",
            "exactitude": -1,
            "name": "irascible dandy",
            "sight_range": 5,
            "known_skills": [
                "Lunge",
                "TarAndFeather"
            ],
            "permanent_afflictions": [
                "none"
            ],
            "skullduggery": 1,
            "sprite_paths": {
                "__dataclass__": "TraitSpritePathsData",
                "idle": "actor/savvy/dandy_idle.png",
                "attack": "actor/savvy/dandy_attack.png",
                "hit": "actor/savvy/dandy_hit.png",
                "dead": "actor/savvy/dandy_dead.png",
                "icon": "actor/savvy/dandy_icon.png",
                "move": "actor/savvy/dandy_move.png"
            },
            "vigour": -1
        },

Actor example:
.. code-block:: json
    "training_dummy": {
            "__dataclass__": "ActorData",
            "key": "training_dummy",
            "possible_names": [
                "sally dummy",
                "steve dummy"
            ],
            "description": "It just looks so darn punchable.",
            "position_offsets": [
                [0, 0]
            ],
            "trait_names": [
                "dummy"
            ],
            "behaviour_name": "SkipTurn",
            "height": "diminutive"
        },

Terrain
-----------------
Create a new entry in terrain.json.
Example:
.. code-block:: json
    "bog": {
        "__dataclass__": "TerrainData",
        "blocks_movement": false,
        "height": "min",
        "description": "This is a bog. It slows entities down.",
        "name": "bog",
        "sprite_paths": {
            "__dataclass__": "TraitSpritePathsData",
            "idle": "terrain/bog.png"
        },
        "position_offsets": [
            [0, 0]
        ],
        "light": null,
        "reactions": {
            "proximity": {
                "__dataclass__": "ReactionData",
                "required_opinion": null,
                "reaction": {
                    "__dataclass__": "ApplyAfflictionEffectData",
                    "affliction_name": "BoggedDown",
                    "duration": 3
                }
            }
        }
    }


Map (a game level)
-----------------------
Create the rooms you want to include in the map within rooms.json. Next, create an entry for the map in maps.json.
Room example:
.. code-block:: json
    "combat": {
        "name": "Combat Room",
        "key": "combat",
        "__dataclass__": "RoomConceptData",
        "design": "square",
        "min_actors": 1,
        "max_actors": 3,
        "min_width": 8,
        "min_height": 8,
        "max_width": 10,
        "max_height": 10,
        "chance_of_spawning_wall": 0.45,
        "max_neighbouring_walls_in_room": 4,
        "sprite_paths": {
            "floor": "world/floor.png",
            "wall": "world/wall.png"
        },
        "actors": {
            "training_dummy": 0.2,
            "crocturion": 0.8
        }
    }

Map example:
.. code-block:: json
    "cave": {
        "name": "cave",
        "key": "cave",
        "__dataclass__": "MapData",
        "min_rooms": 10,
        "max_rooms": 30,
        "max_tunnel_length": 20,
        "min_path_distance_for_shortcut": 5,
        "width": 40,
        "height": 40,
        "rooms": {
            "combat": 0.2,
            "empty": 0.1
        },
        "sprite_paths": {
            "wall": "world/wall.png",
            "floor": "world/floor.png"
        },
        "max_room_entrances": 2,
        "extra_entrance_chance": 10,
        "chance_of_tunnel_winding": 10
    }

God
------------
Create an entry in gods.json. The attitudes and reactions blocks can contain any number of entries.
Example:
.. code-block:: json
    "the_small_gods": {
        "__dataclass__": "GodData",
        "name": "the_small_gods",
        "description": "Hordes of small gods banded together to ensure they were finally taken seriously.",
        "attitudes": {
            "deal_damage":  -5
        },
        "reactions": {
            "deal_damage": {
                "__dataclass__": "ReactionData",
                "required_opinion": -80,
                "reaction": "BasicAttack",
                "chance": 10
            }
        }
    }

Action
------------------
As a type of Action, things are a little more involved here. In addition to the json entry there must also be a python class registered with the engine using `register_action` from scripts.engine.internal.action. The key in the json must also match the class name exactly.

Affliction
^^^^^^^^^^^^^^^^^^^^
Example json:
.. code-block:: json
    "BoggedDown": {
        "__dataclass__": "AfflictionData",
        "category": "bane",
        "description": "It weakens mundane defence and makes you a little bit slower.",
        "icon_path": "skills/root.png",
        "name": "bogged down",
        "identity_tags": [
            "affect_stat"
        ],
        "triggers": [
            "movement"
        ]
    }

Example class:
.. code-block:: python
    class BoggedDown(Affliction):
        """
        A demo of being stuck in the mud - it`ll ground you
        """

        # targeting
        target_tags: List[TileTagType] = [TileTag.OTHER_ENTITY]
        shape: ShapeType = Shape.TARGET
        shape_size: int = 1

        def _build_effects(self, entity: EntityID, potency: float = 1.0) -> List[AffectStatEffect]:  # type: ignore

            affect_stat_effect = AffectStatEffect(
                origin=self.origin,
                cause_name=self.name,
                success_effects=[],
                failure_effects=[],
                target=self.affected_entity,
                stat_to_target=PrimaryStat.BUSTLE,
                affect_amount=2,
            )

            return [affect_stat_effect]



Skill
^^^^^^^^^^^^^^^^^^^^^
Example json:
.. code-block:: json
    "Lightning": {
        "__dataclass__": "SkillData",
        "name": "Call Lightning",
        "description": "Shocking.",
        "cooldown": 1,
        "icon_path": "",
        "resource_cost": 10,
        "resource_type": "stamina",
        "time_cost": 35
    }


Example class:
.. code-block:: python
    class Lightning(Skill):
    """
    A demo of lightning - it`s shocking!
    """
    # casting
    cast_tags: List[TileTagType] = [TileTag.NO_BLOCKING_TILE]

    # targeting
    range: int = 3
    target_tags: List[TileTagType] = [TileTag.ANY]
    targeting_method: TargetingMethodType = TargetingMethod.TILE
    target_directions: List[DirectionType] = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT,
        Direction.UP_LEFT, Direction.UP_RIGHT, Direction.DOWN_LEFT, Direction.DOWN_RIGHT]
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1

    # delivery
    uses_projectile: bool = False
    projectile_data: Optional[ProjectileData] = None
    is_delayed: bool = True
    delayed_skill_data: Optional[DelayedSkillData] = DelayedSkillData(
        duration=3
    )

    def _build_effects(self, entity: EntityID, potency: float = 1.0) -> List[DamageEffect]:
        damage_effect = DamageEffect(
            origin=self.user,
            success_effects=[],
            failure_effects=[],
            target=entity,
            stat_to_target=PrimaryStat.VIGOUR,
            accuracy=library.GAME_CONFIG.base_values.accuracy + 20,
            damage=int(library.GAME_CONFIG.base_values.damage * potency),
            damage_type=DamageType.MUNDANE,
            mod_stat=PrimaryStat.CLOUT,
            mod_amount=0.1,
        )
        return [damage_effect]
