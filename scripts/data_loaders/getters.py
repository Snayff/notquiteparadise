import json


def get_text_from_lang_json(string_id):
    """

    Args:
        string_id:

    Returns:

    """
    language_file_name = "eng"  # TODO inherit from lang selection

    with open('Data/language/' + language_file_name + '.json') as file:  # TODO move filepaths to global/config
        data = json.load(file)

    return data[string_id]


def get_value_from_race_json(race_name, value="all"):
    """

    Args:
        race_name:
        value:

    Returns:

    """
    with open('Data/game/entity/race.json') as file:
        data = json.load(file)

    if value == "all":
        return data[race_name]
    else:
        return data[race_name].get(value)


def get_value_from_trade_json(trade_name, value="all"):
    """

    Args:
        trade_name:
        value:

    Returns:

    """
    with open('Data/game/entity/trade.json') as file:
        data = json.load(file)

    if value == "all":
        return data[trade_name]
    else:
        return data[trade_name].get(value)


def get_value_from_homeland_json(homeland, value="all"):
    """

    Args:
        homeland:
        value:

    Returns:

    """
    with open('Data/game/entity/homeland.json') as file:
        data = json.load(file)

    if value == "all":
        return data[homeland]
    else:
        return data[homeland].get(value)


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


def get_value_from_skill_json(skill_tree_name, skill_name):
    """

    Args:
        skill_tree_name:
        skill_name:

    Returns:

    """
    with open('Data/game/skills/' + skill_tree_name + '.json') as file:
        data = json.load(file)

        return data[skill_name]


def get_value_from_afflictions_json(affliction_name):
    """
    Get all values for an affliction
    Args:
        affliction_name ():

    Returns:

    """
    with open('Data/game/skills/afflictions.json') as file:
        data = json.load(file)

        return data[affliction_name]


def get_value_from_aspects_json(aspect_name):
    """
    Get all values for an aspect
    Args:
        aspect_name ():

    Returns:

    """
    with open('Data/game/world/aspect.json') as file:
        data = json.load(file)

        return data[aspect_name]
