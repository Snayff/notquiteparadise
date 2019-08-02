
from scripts.core.constants import SecondaryStatTypes


class SecondaryStats:
    """
    Stats derived from the primary stats.
    """
    # TODO - load the modifiers and base values from a json

    def __init__(self, owner):
        self.owner = owner

    @property
    def max_hp(self):
        base_amount = 20
        vigour = self.owner.primary_stats.vigour
        modifier = 4

        stat_total = (vigour * modifier) + base_amount
        return int(stat_total)

    @property
    def dodge_speed(self):
        base_amount = 5
        exactitude = self.owner.primary_stats.exactitude
        exactitude_modifier = 1
        bustle = self.owner.primary_stats.bustle
        bustle_modifier = 2

        stat_total = (exactitude * exactitude_modifier) + (bustle * bustle_modifier) + base_amount
        return int(stat_total)

    @property
    def dodge_toughness(self):
        base_amount = 5
        clout = self.owner.primary_stats.clout
        clout_modifier = 1
        vigour = self.owner.primary_stats.vigour
        vigour_modifier = 2

        stat_total = (clout * clout_modifier) + (vigour * vigour_modifier) + base_amount
        return int(stat_total)

    @property
    def dodge_intelligence(self):
        base_amount = 5
        skullduggery = self.owner.primary_stats.skullduggery
        subtlety_modifier = 3
        exactitude = self.owner.primary_stats.exactitude
        exactitude_modifier = 1

        stat_total = (skullduggery * subtlety_modifier) + (exactitude * exactitude_modifier) + base_amount
        return int(stat_total)

    @property
    def resist_blunt(self):
        vigour = self.owner.primary_stats.vigour
        vigour_modifier = 1

        stat_total = (vigour * vigour_modifier)
        return int(stat_total)

    @property
    def resist_pierce(self):
        bustle = self.owner.primary_stats.bustle
        bustle_modifier = 1

        stat_total = (bustle * bustle_modifier)
        return int(stat_total)

    @property
    def resist_elemental(self):
        skullduggery = self.owner.primary_stats.skullduggery
        subtlety_modifier = 2

        stat_total = (skullduggery * subtlety_modifier)
        return int(stat_total)

    @property
    def chance_to_hit(self):
        base_amount = 20
        clout = self.owner.primary_stats.clout
        clout_modifier = 1
        exactitude = self.owner.primary_stats.exactitude
        exactitude_modifier = 1

        stat_total = (clout * clout_modifier) + (exactitude * exactitude_modifier) + base_amount
        return int(stat_total)

    @property
    def base_damage(self):
        base_amount = 5
        clout = self.owner.primary_stats.clout
        clout_modifier = 1

        stat_total = (clout * clout_modifier) + base_amount
        return int(stat_total)

    @property
    def action_cost_change(self):
        bustle = self.owner.primary_stats.bustle
        bustle_modifier = 2

        entity = self.owner.owner
        from scripts.global_singletons.managers import world_manager
        affliction_modifier = world_manager.Affliction.get_stat_modifier_from_afflictions_on_entity(entity,
            SecondaryStatTypes.ACTION_COST_CHANGE)
        # convert to fraction to enable multiplication
        affliction_modifier = 1 + (affliction_modifier / 100)

        stat_total = (bustle * bustle_modifier) * affliction_modifier
        return int(stat_total)

    @property
    def status_length(self):
        skullduggery = self.owner.primary_stats.skullduggery
        skullduggery_modifier = 3

        stat_total = (skullduggery * skullduggery_modifier)
        return stat_total
