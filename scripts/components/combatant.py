
from scripts.entity.primary_stats import PrimaryStats
from scripts.entity.secondary_stats import SecondaryStats


class Combatant:
    """
    [Component] Can fight.

    """
    def __init__(self, hp=0):
        """

        Args:
            hp (int): Starting health value.
        """
        from scripts.world.entity import Entity
        self.owner = None  # type: Entity
        self.hp = hp
        self.primary_stats = PrimaryStats(self)
        self.secondary_stats = SecondaryStats(self)