from scripts.core.constants import AfflictionTypes


class Affliction():
    # TODO -
    #  Attempt to apply and check if successful
    #  Log the affliction on the entity
    #  Log the affliction on a central list
    #  create central method of managing afflictions
    #       Trigger the affliction's effects (skill effects) at required intervals
    #          decrement time remaining
    #          remove affliction if expired

    def __init__(self, affliction_type):
        self.affliction_type = affliction_type  # type: AfflictionTypes
