
from scripts.global_singletons.data_library import library


class Entity:
    """
    Game object that is extended by the inclusion of components. Every component has the entity as an `owner`.

    Attributes:
            current_sprite (list(pygame.image)): List of frames for the current sprite.
            current_sprite_frame (int): Frame of sprite to display
            animation_timer (float): Duration of current animation
            delay_until_idle_animation (int): Seconds until the next idle animation is played
    """

    def __init__(self, spritesheet=None, name="", blocks_movement=True, blocks_sight=True, combatant=None,
            race=None, savvy=None, homeland=None, ai=None, actor=None, player=None, icon=None):
        """
        Args:
            spritesheet (dict(list(pygame.image))) : dictionary of sprites
            name (str) : Name of the entity.
            blocks_movement (bool) : Does entity block movement?
            blocks_sight (bool) : Does entity block sight?
            combatant (Combatant): Component.
            race (Race): Component.
            savvy (savvys): Component.
            homeland (Homeland): Component.
            ai (AI): Component.
            actor(Actor) : Component.
            player (bool): if the entity is controlled by the player
        """
        self.owner = None

        self.spritesheet = spritesheet  # N.B. currently only taking a single image
        self.icon = icon
        self.name = name
        self.blocks_movement = blocks_movement
        self.blocks_sight = blocks_sight

        # animation config
        self.current_sprite = ""  # self.spritesheet.get("still")  # start using still
        self.current_sprite_frame = 0
        self.current_sprite_name = "still"
        self.animation_timer = 0
        self.delay_until_idle_animation = 2  # seconds

        # components
        self.race = race
        self.combatant = combatant
        self.savvy = savvy
        self.homeland = homeland
        self.ai = ai
        self.actor = actor
        self.player = player

        # Create owners so all components can refer to the owning entity
        if self.combatant:
            self.combatant.owner = self

        if self.race:
            self.race.owner = self

        if self.savvy:
            self.savvy.owner = self

        if self.homeland:
            self.homeland.owner = self

        if self.ai:
            self.ai.owner = self

        if self.actor:
            self.actor.owner = self

    @property
    def x(self):
        """
        The tile_x of the Entity.

        Returns:

        """
        return self.owner.x

    @property
    def y(self):
        """
        The tile_y of the Entity.

        Returns:

        """
        return self.owner.y

    @property
    def sight_range(self):
        """
        How far an entity can see.

        Returns:
            int: Number of tiles an entity can see.
        """
        race_data = library.get_race_data(self.race.name)
        return race_data.sight_range