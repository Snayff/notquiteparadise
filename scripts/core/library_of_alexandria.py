
import json


class LibraryOfAlexandria:
    """
    The centre of all knowledge in the world.
    """
    def __init__(self):
        # TODO -
        #  override __getitem__ to allow . notation
        #  point all data references here
        #  where we are converting string to enum revert to string use. Enums are internal only. 

        self.skills = self.get_values_from_skill_json()
        self.homeland = self.get_values_from_homeland_json()
        self.race = self.get_values_from_race_json()
        self.savvy = self.get_values_from_savvy_json()
        self.general = self.get_values_from_general_json()
        self.afflictions = self.get_values_from_affliction_json()
        self.aspect = self.get_values_from_aspect_json()
        self.terrain = self.get_values_from_terrain_json()

        self.test = 1


    def get_skill(self, skill_tree, skill_name):

        x = self.skills
        y = "cleromancer"
        z = "throw_dice"

        from collections import namedtuple
        named_tuple = namedtuple(z, list(x[y][z]))
        skill_data = named_tuple(**x[y][z])

        return skill_data

    def get_aspect(self, aspect_string):
        """

        Args:
            aspect_string ():

        Returns:
            self.aspect:
        """


        return self.aspect[aspect_string]

    @staticmethod
    def get_values_from_skill_json():
        """

        Returns:

        """
        # TODO - move general into skills and create rules to confirm every tree has a basic attack
        with open('Data/game/skills/skill_trees.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_general_json():
        """

        Returns:

        """
        with open('Data/game/skills/general.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_affliction_json():
        """

        Returns:

        """
        with open('Data/game/skills/afflictions.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_aspect_json():
        """

        Returns:

        """
        with open('Data/game/world/aspect.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_terrain_json():
        """

        Returns:

        """
        with open('Data/game/world/terrain.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_homeland_json():
        """

        Returns:

        """
        with open('Data/game/entity/homeland.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_savvy_json():
        """

        Returns:

        """
        with open('Data/game/entity/savvy.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_race_json():
        """

        Returns:

        """
        with open('Data/game/entity/race.json') as file:
            data = json.load(file)

        return data