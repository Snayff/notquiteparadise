import json


def get_text_from_lang_json(string_id):
    language_file_name = "eng"  # TODO inherit from lang selection

    with open('Data/language/' + language_file_name + '.json') as file:  # TODO move filepaths to global/config
        data = json.load(file)

    return data[string_id]


def get_value_from_race_json(race_name, value="all"):
    with open('Data/game/entity/race.json') as file:
        data = json.load(file)

    if value == "all":
        return data[race_name]
    else:
        return data[race_name].get(value)


def get_value_from_youth_json(youth_name, value="all"):
    with open('Data/game/entity/youth.json') as file:
        data = json.load(file)

    if value == "all":
        return data[youth_name]
    else:
        return data[youth_name].get(value)


def get_value_from_adulthood_json(adulthood_name, value="all"):
    with open('Data/game/entity/adulthood.json') as file:
        data = json.load(file)

    if value == "all":
        return data[adulthood_name]
    else:
        return data[adulthood_name].get(value)


def get_value_from_actor_json(actor_name, value="all"):
    with open('Data/game/entity/actor_template.json') as file:
        data = json.load(file)

    if value == "all":
        return data[actor_name]
    else:
        return data[actor_name].get(value)


def get_value_from_skill_json(skill_name):
    with open('Data/game/skills/general.json') as file:
        data = json.load(file)

        return data[skill_name]

