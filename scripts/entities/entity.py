class Entity:
    """
    Game object that is extended by the inclusion of components. Every component has the entity as an `owner`.
    """

    def __init__(self, x, y, sprite, name, blocks_movement=True, blocks_sight=True, combatant=None, race=None,
            youth=None, adulthood=None, ai=None, actor=None, sight_range=0):
        """
        Args:
            x (int) : X position, in tiles.
            y (int) : Y position, in tiles.
            sprite (pygame.image) :
            name (str) : Name of the entity.
            blocks_movement (bool) : Does entity block movement?
            blocks_sight (bool) : Does entity block sight?
            combatant (Combatant): Component.
            race (Race): Component.
            youth (Youth): Component.
            adulthood (Adulthood): Component.
            ai (AI): Component.
            actor(Actor) : Component.
            sight_range (int): How far the entity can see.
        """

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
