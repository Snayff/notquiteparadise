
class Entity:
    """ A generic object to represent players, enemies, items, etc. """

    def __init__(self, x, y, sprite, name, blocks_movement=False, blocks_sight=False,
            living=False, race=None, youth=None, adulthood=None, ai=None, ):

        # item=None, inventory=None, stairs=None, level=None, equipment=None, equippable=None, sight_range=None
        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name
        self.blocks_movement = blocks_movement
        self.blocks_sight = blocks_sight
        # self.sight_range = sight_range

        # components
        self.race = race
        self.living = living
        self.youth = youth
        self.adulthood = adulthood
        self.ai = ai
        # self.item = item
        # self.inventory = inventory
        # self.stairs = stairs
        # self.level = level
        # self.equipment = equipment
        # self.equippable = equippable

        # Create owners so all components can refer to the owning entity
        if self.living:
            self.living.owner = self

        if self.race:
            self.race.owner = self

        if self.youth:
            self.youth.owner = self

        if self.adulthood:
            self.adulthood.owner = self

        if self.ai:
            self.ai.owner = self

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

    def move(self, dx, dy):
        # Move the entity to a specified tile
        self.x = dx
        self.y = dy

