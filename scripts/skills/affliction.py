from scripts.core.constants import AfflictionTypes, Afflictions


class Affliction():
    # TODO -
    #  Attempt to apply and check if successful
    #  Log the affliction on the entity
    #  Log the affliction on a central list
    #  create central method of managing afflictions
    #       Trigger the affliction's effects (skill effects) at required intervals
    #          decrement time remaining
    #          remove affliction if expired

    def __init__(self, affliction_type, affliction, duration):
        self.affliction_type = affliction_type  # type: AfflictionTypes
        self.affliction = affliction
        self.duration = duration
        self.name = self.get_affliction_name(affliction)

    @staticmethod
    def get_affliction_name(affliction):
        """
        Get affliction name from Afflictions Enum
        Args:
            affliction (Afflictions):

        Returns:
            string: Name of affliction
        """
        # TODO - add remaining types
        if affliction == Afflictions.MYOPIC:
            name = "Myopic"
        elif affliction == Afflictions.SLUGGISH:
            name = "Sluggish"
        elif affliction == Afflictions:
            name = ""
        elif affliction == Afflictions:
            name = ""
        elif affliction == Afflictions:
            name = ""
        elif affliction == Afflictions:
            name = ""
        elif affliction == Afflictions:
            name = ""
        elif affliction == Afflictions:
            name = ""
        elif affliction == Afflictions:
            name = ""
        elif affliction == Afflictions:
            name = ""
        elif affliction == Afflictions:
            name = ""

        return name
