
import json


class LibraryOfAlexandria:
    """
    The centre of all knowledge in the world.
    """
    def __init__(self):
        # TODO -
        #  override __getitem__ to allow . notation
        #  reformat skills.json to be contained by skill tree
        #  load all json data here
        #  point all data references here
        #  where we are converting string to enum revert to string use. Enums are internal only. 


        self.skills = self.get_values_from_skill_json()
        self.test = 1

    @staticmethod
    def get_values_from_skill_json():
        """

        Returns:

        """
        with open('Data/game/skills/cleromancer.json') as file:
            data = json.load(file)

        return data