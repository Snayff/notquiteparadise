from __future__ import annotations

import dataclasses
import json
from typing import TYPE_CHECKING, Dict, Type

if TYPE_CHECKING:
    pass

####################### UTILITY ############################

def deserialise_dataclasses(dct):
    if "__dataclass__" in dct:
        dataclass_ = ExtendedJsonEncoder.__dataclassses__[dct["__dataclass__"]]
        del dct["__dataclass__"]
        return dataclass_(
            **{
                k: v if not isinstance(v, dict) else deserialise_dataclasses(v)
                for k, v in dct.items()
            }
        )
    return dct


def register_dataclass_with_json(cls):
    ExtendedJsonEncoder.__dataclassses__[cls.__name__] = cls
    return cls

####################### JSON ENCODING ############################


JSON_TYPES = [str, int, dict, float, bool, tuple, list, type(None)]


class ExtendedJsonEncoder(json.JSONEncoder):
    """
    Extend the json Encoder to handle dataclass types
    """
    __dataclassses__: Dict[str, Type] = {}

    def default(self, obj):
        """
        Override the base default method to handle enum and dataclasses
        """
        if dataclasses.is_dataclass(obj):
            return {
                **dict(__dataclass__=obj.__class__.__name__),
                **{
                    field.name: self.default(getattr(obj, field.name))
                    for field in dataclasses.fields(obj)
                },
            }
        elif type(obj) in JSON_TYPES:
            return obj
        super(ExtendedJsonEncoder, self).default(obj)


