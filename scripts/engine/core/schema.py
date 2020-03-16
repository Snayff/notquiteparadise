from __future__ import annotations

from typing import TYPE_CHECKING
from marshmallow import Schema, fields, ValidationError
from scripts.engine.core.constants import Effect

if TYPE_CHECKING:
    from typing import Type, Union, Optional, Any, Tuple, Dict, List


######################### VALIDATORS ####################################

def _validate_effect_type(s):
    if s is not None and not hasattr(Effect, s):
        raise ValidationError(f"{s} is not a valid effect type")


######################### SCHEMA  ####################################

class EffectDataSchema(Schema):
    effect_type = fields.Str(validate=_validate_effect_type)


