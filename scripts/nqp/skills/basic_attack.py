from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List

def use():
    print("used skill")

def activate():
    print("activated")

#                 "damage": {
#                     "__dataclass__": "DamageEffectData",
#                     "accuracy": 0,
#                     "stat_to_target": "vigour",
#                     "shape": "target",
#                     "shape_size": 1,
#                     "required_tags": [
#                         "other_entity"
#                     ],
#                     "damage": 2,
#                     "damage_type": "mundane",
#                     "mod_amount": 0.1,
#                     "mod_stat": "clout"
#                 },


# from importlib import reload,import_module
#     module_name = "skills." + data.file_name
#     module = import_module(module_name)
#     module = reload(module)
#     method_to_call = getattr(module, "use")
#     result = method_to_call()

##################################################
# something triggers a UseSkillEvent
# this checks affordability, pays skill costs and  creates a projectile
# -> we could move projectile creation to a "use" method here to allow for additional creation actions
# projectile given turn, as any other entity
# projectile travels in direction until it activates or expires
# -> this should call the relevant skill activation

# ! make sure to use standardised funcs held in skills.py where possible
# ! think about how to make it easy to amend lots of values - use base values and an offset?
# ! there probs needs to be an activation effect in the json