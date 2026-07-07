# from api import get_match
from api import get_match, get_heroes
from analyzer import find_player_by_hero, display_performance

match_id = 8881925243

data = get_match(match_id)
heroes = get_heroes()

hero_map ={}

for hero in heroes:
    hero_map[hero["id"]] = hero ["localized_name"]

for player in data["players"]:
    hero_name = hero_map[player["hero_id"]]

    print(
        player["personaname"],
        "|",
        hero_name,
        "|",
        player["kills"],
        player["deaths"],
        player["assists"]
    )



# print(heroes[0])


# data = get_match(match_id)

# if data: 
#     print("Api Connected")
#     print(data["players"][0]) # cek type data yang dibentangkan, guna data.keys

# else:
#     print("Failed")

# for player in data["players"]:
#     print(
#         player["personaname"],
#         player["hero_id"],
#         player["kills"],
#         player["deaths"],
#         player["assists"]
#     )

target_hero = "Spectre"

player = find_player_by_hero(
    data["players"],
    hero_map,
    target_hero
)

if player:

    print("PLAYER FOUND")
    display_performance(player)

    print(
        "KDA:",
        player["kills"],
        "/",
        player["deaths"],
        "/",
        player["assists"]
    )

else:

    print("PLAYER NOT FOUND")

## report or summary pertama is done : match id + hero = display performance.