# DOTA POS 1 COACH
# Service Layer

from api import (
    get_match,
    get_heroes,
    get_items
)
from analyzer import (
    find_player_by_hero,
    farming_analysis,
    kda_analysis,
    benchmark_analysis,
    generate_coach_report,
    item_analysis
)



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
                str(item_data["id"])
            ] = item_data["dname"]

    return (
        data,
        hero_map,
        item_map
    )

def get_target_player(
    data,
    hero_map,
    target_hero
):

    player = find_player_by_hero(
        data["players"],
        hero_map,
        target_hero
    )

    return player

def analyse_player(player, item_map):


    farming = farming_analysis(
        player
    )


    kda = kda_analysis(
        player
    )


    benchmark = benchmark_analysis(
        player
    )


    items = item_analysis(
        player,
        item_map
    )

    coach_report = generate_coach_report(
    farming,
    kda,
    benchmark
    )

    return {
        "player": player,
        "farming": farming,
        "kda": kda,
        "benchmark": benchmark,
        "items": items,
        "coach_report": coach_report
    }