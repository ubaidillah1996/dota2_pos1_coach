# DOTA POS 1 COACH
# Service Layer

from api import (
    get_match,
    get_heroes,
    get_items
)

def prepare_match_data(match_id):

    print("DEBUG 1")

    data = get_match(match_id)

    print("DEBUG 2")

    heroes = get_heroes()

    print("DEBUG 3")

    items = get_items()

    print("DEBUG 4")

def prepare_match_data(match_id):

    data = get_match(match_id)

    if not data:

        return None


    heroes = get_heroes()

    items = get_items()


    hero_map = {}

    for hero in heroes:

        hero_map[
            hero["id"]
        ] = hero["localized_name"]


    item_map = {}

    for item_name, item_data in items.items():

        if "id" in item_data and "dname" in item_data:

            item_map[
                item_data["id"]
            ] = item_data["dname"]


    return (
        data,
        hero_map,
        item_map
    )