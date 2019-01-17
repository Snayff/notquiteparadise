
class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x, y, sprite, name, blocks_movement=True, blocks_sight=True,
            combatant=None, race=None, youth=None, adulthood=None, ai=None, actor=None, sight_range=0 ):

        # item=None, inventory=None, stairs=None, level=None, equipment=None, equippable=None, sight_range=None

        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name
        self.blocks_movement = blocks_movement
        self.blocks_sight = blocks_sight
        self.sight_range = sight_range

        # components
        self.race = race
        self.combatant = combatant
        self.youth = youth
        self.adulthood = adulthood
        self.ai = ai
        self.actor = actor
        # self.item = item
        # self.inventory = inventory
        # self.stairs = stairs
        # self.level = level
        # self.equipment = equipment
        # self.equippable = equippable

        # Create owners so all components can refer to the owning entity
        if self.combatant:
            self.combatant.owner = self

        if self.race:
            self.race.owner = self

        if self.youth:
            self.youth.owner = self

        if self.adulthood:
            self.adulthood.owner = self

        if self.ai:
            self.ai.owner = self

        if self.actor:
            self.actor.owner = self

    # if self.item:
    # 	self.item.owner = self
    #
    # if self.inventory:
    # 	self.inventory.owner = self
    #
    # if self.stairs:
    # 	self.stairs.owner = self
    #
    # if self.level:
    # 	self.level.owner = self
    #
    # if self.equipment:
    # 	self.equipment.owner = self
    #
    # if self.equippable:
    # 	self.equippable.owner = self
    #
    # 	if not self.item:
    # 		item = Item()
    # 		self.item = item
    # 		self.item.owner = self



