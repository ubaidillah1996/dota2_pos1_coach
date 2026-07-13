#  BAHAGIAN BUSINESS LOGIC IS BASED APA YANG AKU FAHAM UNTUK MASALAH APA YANG AKU NAK OVERCOME .
# AI HANYA BAGI CODE, LOGIC IS FROM ME.

# from api import get_match
from api import get_match, get_heroes, get_items
from analyzer import (find_player_by_hero, display_performance, farming_analysis, kda_analysis, display_items, threat_analysis, benchmark_analysis, generate_coach_report)
from analyzer import get_enemy_players
from analyzer import item_recommendation
from graph import create_benchmark_chart
from input_handler import get_user_input


# match_id = 845004963

match_id, target_hero = get_user_input()

# match_id = int(
#     input("Enter Match ID: ")
# )

data = get_match(match_id)

if not data:

    print(
        "Match data not found."
    )

    exit()

heroes = get_heroes()
items = get_items()


hero_map ={}

for hero in heroes:
    hero_map[hero["id"]] = hero ["localized_name"]

# for player in data["players"]:
#     hero_name = hero_map[player["hero_id"]]
#     print(
#         player["personaname"],
#         "|",
#         hero_name,
#         "|",
#         player["kills"],
#         player["deaths"],
#         player["assists"]
#     )

item_map = {}

for item_name, item_data in items.items():

#   print(items["blink"])

#   item_map[item_data["id"]] = item_data["localized_name"]

## selepas diuji berkali2, ketika mencari items, format localized tidak boleh dipakai .

# SOLUSI :

    if "id" in item_data and "dname" in item_data:
        item_map[item_data["id"]] = item_data["dname"] # kat sini python akan cek guna dua konsep, id dan dname, if ada print out,if takde skip.

#  print(item_map[1]) # testing output :

# print(heroes[0])



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

# target_hero = "spectre"

# target_hero = input(
#     "Enter Carry Hero: "
# )

player = find_player_by_hero(
    data["players"],
    hero_map,
    target_hero # data = get_match(match_id)

)

if player is None:

    print(
        "\nPlayer not found."
    )

    print(
        "Please check hero name or match ID."
    )

    exit()

print("TARGET HERO:", target_hero)

print("\n=== HERO DALAM MATCH ===")

for p in data["players"]:
    print(hero_map[p["hero_id"]])

print("PLAYER CHECK:")
print(player)

display_performance(player)

farming_analysis(player)

kda_analysis(player)

benchmark_result = benchmark_analysis(player)


generate_coach_report(
    benchmark_result,
    player
)


create_benchmark_chart(
    benchmark_result
)

## report or summary pertama is done : match id + hero = display performance.

# display_items(player, item_map)
# dah keluar output pasal item

# print(player["purchase_log"]) # testing purchase log item player
# output : keyerror.

# print(player.keys()) # testing untuk tengok key yang ada 
# output : mmg takde bagi item history dengn cara ini.

display_items(player, item_map)

enemy_players = get_enemy_players(
    data["players"],
    player
)

threat_analysis(enemy_players, hero_map)

item_recommendation(enemy_players, hero_map)

print("\n====== ENEMY TEAM ======")

for enemy in enemy_players:

    player_name = enemy.get("personaname", "Unknown Player")
    hero_name = hero_map[enemy["hero_id"]]

    print(f"{player_name} | {hero_name}")

## problems : OpenDota API returns hero information as hero_id instead of hero name.
## solutions : Created hero mapping dictionary to convert hero_id into readable hero name.