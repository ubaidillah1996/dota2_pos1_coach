from services import (
    prepare_match_data,
    get_target_player,
    analyse_player
)


match_id = 8872864614


result = prepare_match_data(
    match_id
)


data, hero_map, item_map = result


player = get_target_player(
    data,
    hero_map,
    "sven"
)


result = analyse_player(
    player,
    item_map
)


print(result)