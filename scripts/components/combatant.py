
class Combatant:
    """
    [Component] Can fight.

    """
    def __init__(self, hp=0):
        """

        Args:
            hp (int): Starting health value.
        """
        self.hp = hp
        self.primary_stats = self.PrimaryStats()
        self.primary_stats.owner = self
        self.secondary_stats = self.SecondaryStats()
        self.secondary_stats.owner = self

    class PrimaryStats:

        @property
        def vigour(self):
            base_amount = 5
            entity = self.owner.owner
            stat_total = 0

            if entity.race:
                stat_total += entity.race.vigour

            if entity.trade:
                stat_total += entity.trade.vigour

            if entity.homeland:
                stat_total += entity.homeland.vigour

            return stat_total + base_amount

        @property
        def clout(self):
            base_amount = 5
            entity = self.owner.owner
            stat_total = 0

            if entity.race:
                stat_total += entity.race.clout

            if entity.trade:
                stat_total += entity.trade.clout

            if entity.homeland:
                stat_total += entity.homeland.clout

            return stat_total + base_amount

        @property
        def skullduggery(self):
            base_amount = 5
            entity = self.owner.owner
            stat_total = 0

            if entity.race:
                stat_total += entity.race.skullduggery

            if entity.trade:
                stat_total += entity.trade.skullduggery

            if entity.homeland:
                stat_total += entity.homeland.skullduggery

            return stat_total + base_amount

        @property
        def bustle(self):
            base_amount = 5
            entity = self.owner.owner
            stat_total = 0

            if entity.race:
                stat_total += entity.race.bustle

            if entity.trade:
                stat_total += entity.trade.bustle

            if entity.homeland:
                stat_total += entity.homeland.bustle

            return stat_total + base_amount

        @property
        def exactitude(self):
            base_amount = 5
            entity = self.owner.owner
            stat_total = 0

            if entity.race:
                stat_total += entity.race.exactitude

            if entity.trade:
                stat_total += entity.trade.exactitude

            if entity.homeland:
                stat_total += entity.homeland.exactitude

            return stat_total + base_amount

    class SecondaryStats:
        # TODO - load the modifiers and base values from a json

        @property
        def max_hp(self):
            base_amount = 20
            vigour = self.owner.primary_stats.vigour
            modifier = 4

            stat_total = (vigour * modifier) + base_amount
            return stat_total

        @property
        def dodge_speed(self):
            base_amount = 5
            exactitude = self.owner.primary_stats.exactitude
            exactitude_modifier = 1
            bustle = self.owner.primary_stats.bustle
            bustle_modifier = 2

            stat_total = (exactitude * exactitude_modifier) + (bustle * bustle_modifier) + base_amount
            return stat_total

        @property
        def dodge_toughness(self):
            base_amount = 5
            clout = self.owner.primary_stats.clout
            clout_modifier = 1
            vigour = self.owner.primary_stats.vigour
            vigour_modifier = 2

            stat_total = (clout * clout_modifier) + (vigour * vigour_modifier) + base_amount
            return stat_total

        @property
        def dodge_intelligence(self):
            base_amount = 5
            skullduggery = self.owner.primary_stats.skullduggery
            subtlety_modifier = 3
            exactitude = self.owner.primary_stats.exactitude
            exactitude_modifier = 1

            stat_total = (skullduggery * subtlety_modifier) + (exactitude * exactitude_modifier) + base_amount
            return stat_total

        @property
        def resist_blunt(self):
            vigour = self.owner.primary_stats.vigour
            vigour_modifier = 1

            stat_total = (vigour * vigour_modifier)
            return stat_total

        @property
        def resist_pierce(self):
            bustle = self.owner.primary_stats.bustle
            bustle_modifier = 1

            stat_total = (bustle * bustle_modifier)
            return stat_total

        @property
        def resist_elemental(self):
            skullduggery = self.owner.primary_stats.skullduggery
            subtlety_modifier = 2

            stat_total = (skullduggery * subtlety_modifier)
            return stat_total

        @property
        def chance_to_hit(self):
            base_amount = 20
            clout = self.owner.primary_stats.clout
            clout_modifier = 1
            exactitude = self.owner.primary_stats.exactitude
            exactitude_modifier = 1

            stat_total = (clout * clout_modifier) + (exactitude * exactitude_modifier) + base_amount
            return stat_total

        @property
        def base_damage(self):
            base_amount = 5
            clout = self.owner.primary_stats.clout
            clout_modifier = 1

            stat_total = (clout * clout_modifier) + base_amount
            return stat_total

        @property
        def action_cost_change(self):
            bustle = self.owner.primary_stats.bustle
            bustle_modifier = 2

            stat_total = (bustle * bustle_modifier)
            return stat_total

        @property
        def status_length(self):
            skullduggery = self.owner.primary_stats.skullduggery
            subtlety_modifier = 3

            stat_total = (skullduggery * subtlety_modifier)
            return stat_total