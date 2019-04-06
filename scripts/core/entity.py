class Entity:
    """
    Game object that is extended by the inclusion of components. Every component has the entity as an `owner`.

    Attributes:
            current_sprite (list(pygame.image)): List of frames for the current sprite.
            current_sprite_frame (int): Frame of sprite to display
            animation_timer (float): Duration of current animation
            delay_until_idle_animation (int): Seconds until the next idle animation is played
    """

    def __init__(self, x, y, spritesheet, name, blocks_movement=True, blocks_sight=True, combatant=None, race=None,
            youth=None, adulthood=None, ai=None, actor=None, sight_range=0, player=None):
        """
        Args:
            x (int) : X position, in tiles.
            y (int) : Y position, in tiles.
            spritesheet (dict(list(pygame.image))) : dictionary of sprites
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
            player (Player): if the entity is controlled by the player
        """

        self.x = x
        self.y = y
        self.spritesheet = spritesheet  # N.B. currently only taking a single image
        self.name = name
        self.blocks_movement = blocks_movement
        self.blocks_sight = blocks_sight
        self.sight_range = sight_range

        # animation config
        self.current_sprite = ""  # self.spritesheet.get("still")  # start using still
        self.current_sprite_frame = 0
        self.current_sprite_name = "still"
        self.animation_timer = 0
        self.delay_until_idle_animation = 2  # seconds

        # components
        self.race = race
        self.combatant = combatant
        self.youth = youth
        self.adulthood = adulthood
        self.ai = ai
        self.actor = actor
        self.player = player

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

        if self.player:
            self.player.owner = self

        if self.actor and self.combatant:
            self.actor.learn_skill("basic_attack")