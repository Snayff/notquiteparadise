
from scripts.core.constants import AfflictionCategory, AfflictionTypes


class Affliction():
    """
    Affliction, either Bane or Boon. Applies a periodic effect to an entity.
    """
    # TODO -
    #  Log the affliction on a central list
    #  create central method of managing afflictions
    #       Trigger the affliction's effects (skill effects) at required intervals
    #          decrement time remaining
    #          remove affliction if expired

    def __init__(self, affliction_category, affliction_type, duration):
        self.affliction_category = affliction_category  # type: AfflictionCategory
        self.affliction_type = affliction_type
        self.duration = duration
        self.name = self.get_affliction_name(affliction_type)
        self.trigger_event = trigger_event

    @staticmethod
    def get_affliction_name(affliction):
        """
        Get affliction name from AfflictionTypes
        Args:
            affliction (AfflictionTypes):

        Returns:
            string: Name of affliction
        """
        # TODO - add remaining types
        if affliction == AfflictionTypes.MYOPIC:
            name = "Myopic"
        elif affliction == AfflictionTypes.SLUGGISH:
            name = "Sluggish"
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""
        elif affliction == AfflictionTypes:
            name = ""

        return name
