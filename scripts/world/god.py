
from typing import Dict


class God:
    """
    A god who passes judgement on the actions taken

    Attributes:
        name (str):
        interventions (dict[key, Intervention]):
        opinions (dict):

    """
    def __init__(self, god_name):
        self.name = god_name
        self.opinions = {}

        from scripts.world.intervention import Intervention
        from scripts.global_singletons.data_library import library
        interventions_data = library.get_god_interventions_data(god_name)
        interventions = {}
        # create interventions for god
        for name, intervention in interventions_data.items():
            interventions[intervention.name] = Intervention(self, intervention.name)

        self.interventions = interventions  # type: Dict[Intervention]


