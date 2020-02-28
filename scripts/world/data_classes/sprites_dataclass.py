from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING
from scripts.core.extend_json import register_dataclass_with_json

if TYPE_CHECKING:
    import pygame


@register_dataclass_with_json
@dataclass
class CharacteristicSpritesData:
    """
    Possible sprites for a characteristic
    """    
    icon: pygame.Surface = None
    idle: pygame.Surface = None
    attack: pygame.Surface = None
    hit: pygame.Surface = None
    dead: pygame.Surface = None
    move: pygame.Surface = None
    
    
@register_dataclass_with_json
@dataclass
class CharacteristicSpritePathsData:
    """
    Possible sprites paths for a characteristic
    """
    icon: str = "none"
    idle: str = "none"
    attack: str = "none"
    hit: str = "none"
    dead: str = "none"
    move: str = "none"
