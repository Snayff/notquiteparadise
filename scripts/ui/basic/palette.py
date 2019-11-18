
from scripts.ui.basic.colours import Colour

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
        self.entity_info = self.EntityInfoPalette()
        self.targeting_overlay = self.TargetingOverlayPalette()
        self.skill_bar = self.SkillBarPalette()
        self.entity_queue = self.EntityQueuePalette()
        self.camera = self.CameraPalette()

    class MessageLogPalette:
        """
        The palette for the messagelog

        Attributes:
            background (Colour): Colour of the Message Log background.
            expressions_player (Colour): Colour of the  player`s expression.
            text_default (Colour): Colour of the default text.
            hyperlink (Colour): Colour of hyperlinks .
            tooltip_background(Colour): Colour of the tooltip window background.
            tooltip_text(Colour): Colour of the tooltip text.
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.tertiary.darker
            self.border = colour.complement.darker

            self.keyword_player = colour.complement.lightest
            self.keyword_grazes = colour.red
            self.keyword_crits = colour.green

            self.text_default = colour.white
            self.text_negative = colour.red
            self.text_info = colour.blue
            self.text_positive = colour.green

            self.hyperlink = colour.black
            self.tooltip_text = colour.white
            self.tooltip_background = colour.black

    class EntityInfoPalette:
        """
        The palette for the entity info panel
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.black
            self.border = colour.complement.darker
            self.text_default = colour.white  # TODO - combine text palettes into one

    class TargetingOverlayPalette:
        """
        The palette for the targeting overlay
        """
        def __init__(self):
            colour = Colour()
            self.selected_tile_border = colour.tertiary.neutral
            self.highlighted_range_border = colour.secondary.neutral
            self.highlighted_effect_border = colour.complement.lighter

    class SkillBarPalette:
        """
        The palette for the skill bar
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.black
            self.border = colour.complement.darker
            self.skill_border = colour.complement.lighter
            self.text_default = colour.white

    class EntityQueuePalette:
        """
        The palette for the entity queue
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.black
            self.border = colour.complement.darker
            self.text_default = colour.white

    class CameraPalette:
        """
        The palette for the camera
        """
        def __init__(self):
            colour = Colour()
            self.background = colour.black
            self.border = colour.complement.darker
            self.skill_border = colour.complement.lighter
            self.text_default = colour.white
            self.selected_tile_border = colour.tertiary.neutral
            self.overlay_border = colour.secondary.neutral
            self.overlay = colour.secondary.lighter