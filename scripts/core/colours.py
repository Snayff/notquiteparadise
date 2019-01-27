class Palette:
    """
    A collection of Colours defined for specific purposes.

    Attributes:
        menu_background (Colour): Colour of the Menu background.
        debug_font_colour (Colour): Colour of the Debug Font.
        message_log_background (Colour): Colour of the Message Log background.
    """
    def __init__(self):
        colour = Colour()

        # menu
        self.menu_background = colour.secondary.darker

        # debug
        self.debug_font_colour = colour.primary.lightest

        # message log
        self.message_log_background = colour.tertiary.darker


class Colour:
    """
    A Colour value; a tuple containing RGB values.

    Attributes:
        primary (PrimaryColour): Selection of main Colours.
        secondary (SecondaryColour): Selection of secondary Colours.
        tertiary (TertiaryColour): Selection of tertiary Colours.
        complement (ComplementColour): Selection of complement Colours.
    """
    def __init__(self):
        self.primary = self.PrimaryColour()
        self.secondary = self.SecondaryColour()
        self.tertiary = self.TertiaryColour()
        self.complement = self.ComplementColour()

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    class PrimaryColour:
        """
        A set of gradients for the main Colour.

        Attributes:
            darkest (Tuple[int,int,int]) : Darkest colour in gradient.
            darker (Tuple[int,int,int]) : Darker colour in gradient.
            neutral (Tuple[int,int,int]) : Neutral colour in gradient.
            lighter (Tuple[int,int,int]) : Lighter colour in gradient.
            lightest (Tuple[int,int,int]) : Lightest colour in gradient.
        """
        def __init__(self):
            self.darkest = (66, 48, 28)
            self.darker = (73, 60, 46)
            self.neutral = (121, 105, 88)
            self.lighter = (164, 146, 126)
            self.lightest = (211, 193, 175)

    class SecondaryColour:
        """
        A set of gradients for the secondary Colour.

        Attributes:
            darkest (Tuple[int,int,int]) : Darkest colour in gradient.
            darker (Tuple[int,int,int]) : Darker colour in gradient.
            neutral (Tuple[int,int,int]) : Neutral colour in gradient.
            lighter (Tuple[int,int,int]) : Lighter colour in gradient.
            lightest (Tuple[int,int,int]) : Lightest colour in gradient.
        """
        def __init__(self):
            self.darkest = (66, 61, 28)
            self.darker = (73, 69, 46)
            self.neutral = (121, 116, 88)
            self.lighter = (164, 159, 129)
            self.lightest = (211, 206, 175)

    class TertiaryColour:
        """
        A set of gradients for the tertiary Colour.

        Attributes:
            darkest (Tuple[int,int,int]) : Darkest colour in gradient.
            darker (Tuple[int,int,int]) : Darker colour in gradient.
            neutral (Tuple[int,int,int]) : Neutral colour in gradient.
            lighter (Tuple[int,int,int]) : Lighter colour in gradient.
            lightest (Tuple[int,int,int]) : Lightest colour in gradient.
        """
        def __init__(self):
            self.darkest = (29, 22, 45)
            self.darker = (39, 33, 50)
            self.neutral = (69, 62, 83)
            self.lighter = (96, 89, 112)
            self.lightest = (129, 122, 144)

    class ComplementColour:
        """
        A set of gradients for the complement Colour.

        Attributes:
            darkest (Tuple[int,int,int]) : Darkest colour in gradient.
            darker (Tuple[int,int,int]) : Darker colour in gradient.
            neutral (Tuple[int,int,int]) : Neutral colour in gradient.
            lighter (Tuple[int,int,int]) : Lighter colour in gradient.
            lightest (Tuple[int,int,int]) : Lightest colour in gradient.
        """
        def __init__(self):
            self.darkest = (18, 36, 42)
            self.darker = (30, 41, 45)
            self.neutral = (56, 71, 75)
            self.lighter = (80, 97, 103)
            self.lightest = (110, 126, 132)