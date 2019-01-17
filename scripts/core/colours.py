class Palette:
    def __init__(self):
        colour = Colour()

        # menu
        self.menu_background = colour.secondary.darker

        # debug
        self.debug_font_colour = colour.primary.lightest


class Colour:
    def __init__(self):
        self.primary = self.PrimaryColour()
        self.secondary = self.SecondaryColour()
        self.tertiary = self.TertiaryColour()
        self.complement = self.ComplementColour()

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    class PrimaryColour:
        def __init__(self):
            self.darkest = (66, 48, 28)
            self.darker = (73, 60, 46)
            self.neutral = (121, 105, 88)
            self.lighter = (164, 146, 126)
            self.lightest = (211, 193, 175)

    class SecondaryColour:
        def __init__(self):
            self.darkest = (66, 61, 28)
            self.darker = (73, 69, 46)
            self.neutral = (121, 116, 88)
            self.lighter = (164, 159, 129)
            self.lightest = (211, 206, 175)

    class TertiaryColour:
        def __init__(self):
            self.darkest = (29, 22, 45)
            self.darker = (39, 33, 50)
            self.neutral = (69, 62, 83)
            self.lighter = (96, 89, 112)
            self.lightest = (129, 122, 144)

    class ComplementColour:
        def __init__(self):
            self.darkest = (18, 36, 42)
            self.darker = (30, 41, 45)
            self.neutral = (56, 71, 75)
            self.lighter = (80, 97, 103)
            self.lightest = (110, 126, 132)