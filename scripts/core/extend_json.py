from __future__ import annotations

import logging
from enum import Enum
from typing import TYPE_CHECKING
from typing import List, Any, cast
import dataclasses

import json

if TYPE_CHECKING:
    pass


def _get_object_by_qualname(qualname: str) -> Any:
    try:
        import_path, objname = qualname.rsplit(".", maxsplit=1)
    except ValueError:
        return globals()[qualname]
    else:
        if import_path:
            return __import__(import_path, fromlist=objname)


def deserialize_dataclasses(dct):
    if "__dataclass__" in dct:
        dataclass_ = _get_object_by_qualname(dct["__dataclass__"])
        del dct["__dataclass__"]
        return dataclass_(
            **{
                k: v if not isinstance(v, dict) else deserialize_dataclasses(v)
                for k, v in dct.items()
            }
        )
    return dct


####################### JSON ENCODERS ############################


JSON_TYPES = [str, int, dict, float, bool, tuple, list, type(None)]


class ExtendedJsonEncoder(json.JSONEncoder):
    """
    Extend the json Encoder to handle Enum and dataclass types
    """
    def default(self, obj):
        if dataclasses.is_dataclass(obj):
            return {
                **dict(__dataclass__=obj.__class__.__qualname__),
                **{
                    field.name: self.default(getattr(obj, field.name))
                    for field in dataclasses.fields(obj)
                },
            }
        elif isinstance(obj, Enum):
            return obj.name
        elif type(obj) in JSON_TYPES:
            return obj
        super(ExtendedJsonEncoder, self).default(obj)
