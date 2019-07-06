import json



def get_value_from_actor_json(actor_name, value="all"):
    """

    Args:
        actor_name:
        value:

    Returns:

    """
    with open('Data/game/entity/actor_template.json') as file:
        data = json.load(file)

    if value == "all":
        return data[actor_name]
    else:
        return data[actor_name].get(value)

