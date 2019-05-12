
from scripts.ui_elements.colours import Colour

class Palette:
    """
    A collection of Colours defined for specific purposes.

    Attributes:
        menu_background (Colour): Colour of the Menu background.
        debug_font_colour (Colour): Colour of the Debug Font.

    """
    def __init__(self):
        colour = Colour()

        # menu
        self.menu_background = colour.secondary.darker

        # debug
        self.debug_font_colour = colour.primary.lightest
        self.message_log = self.MessageLogPalette()
        self.game_map = self.GameMapPalette()
        self.entity_info = self.EntityInfoPalette()
        self.targeting_overlay = self.TargetingOverlayPalette()
        self.skill_bar = self.SkillBarPalette()

    class MessageLogPalette:
        """
        The palette for the messagelog

        Attributes:
            background (Colour): Colour of the Message Log background.
            expressions_player (Colour): Colour of the  player's expression.
            default_text (Colour): Colour of the default text.
            hyperlink (Colour): Colour of hyperlinks .
            tooltip_background(Colour): Colour of the tooltip window background.
            tooltip_text(Colour): Colour of the tooltip text.
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.tertiary.darker
            self.border = colour.complement.darker
            self.keyword_player = colour.complement.lightest
            self.default_text = colour.white
            self.hyperlink = colour.black
            self.tooltip_text = colour.white
            self.tooltip_background = colour.black

    class GameMapPalette:
        """
        The palette for the map

        Attributes:
            border (Colour): Colour of the game map border
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.black
            self.border = colour.complement.darker

    class EntityInfoPalette:
        """
        The palette for the entity info panel
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.black
            self.border = colour.complement.darker
            self.default_text = colour.white  # TODO - use

    class TargetingOverlayPalette:
        """
        The palette for the targeting overlay
        """
        def __init__(self):
            colour = Colour()
            self.selected_tile_border = colour.tertiary.neutral
            self.highlighted_range_border = colour.complement.lighter

    class SkillBarPalette:
        """
        The palette for the skill bar
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.black
            self.border = colour.complement.darker
            self.skill_border = colour.complement.lighter
            self.default_text = colour.white