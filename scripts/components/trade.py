from scripts.data_loaders.getters import get_value_from_trade_json


class Trade:
    """
    [Component] Adds some stats from the Trade.

    """
    def __init__(self, youth_name):
        """
        Args:
            youth_name (str): Name of the Trade type.
        """
        values = get_value_from_trade_json(youth_name)

        self.name = values["name"]
        self.description = values["description"]
        self.vigour = values["vigour"]
        self.clout = values["clout"]
        self.subtlety = values["subtlety"]
        self.bustle = values["bustle"]
        self.exactitude = values["exactitude"]
