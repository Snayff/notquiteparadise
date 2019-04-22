class Effect:
    """
    Base class for effects that make up skills.
    """

    def __init__(self, name, description, target_type, tags):
        self.owner = None
        self.name = name
        self.description = description
        self.target_type = target_type
        self.target_tags = tags

    def trigger(self):
        """
        Trigger the effect
        """
        pass


