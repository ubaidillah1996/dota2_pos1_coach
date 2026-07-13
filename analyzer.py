# untuk cari hero
from benchmark import BENCHMARK


def find_player_by_hero(players, hero_map, target_hero):

    for player in players :

        hero_name = hero_map[player["hero_id"]] # cari hero melalui siapa player apa hero id

        if hero_name.lower() == target_hero.lower():
            return player
        
    return None

# sekarang untuk keluarkan data asas pos 1 dulu :

def display_performance(player):

    print("\n====== PLAYER PERFORMANCE ======") # new line atau title

    # print ("player:", player ["personaname"])

    print(
        "KDA:",
        player["kills"],
        "/",
        player["deaths"],
        "/",
        player["assists"]
    )

    # print("Last Hits:", player["last_hits"])
    print("Denies:", player["denies"])

    print("GPM:", player["gold_per_min"])
    print("XPM:", player["xp_per_min"])

    print("Net Worth:", player["net_worth"])

    print("Hero Damage:", player["hero_damage"])
    print("Tower Damage:", player["tower_damage"])

def farming_analysis(player): # function baru : farming analisis
        
        duration_minutes = player["duration"] /60

        lh_per_min = player["last_hits"] / duration_minutes

        print("\n ======= FARMING ANALYSIS========")

        print("Last Hits:", player["last_hits"])
        print("Match Duration:", round(duration_minutes,1), "minutes")
        print("LH/Min:", round(lh_per_min,2 ))


        if lh_per_min >= 8:
             rating = "Excellent"
             insight = "Strong farming efficiency, Good gold accumulation"

        elif lh_per_min >=6:
             rating = "Good"
             insight = "Decent farming, but can improve lane efficiency"

        else:
             rating = "Need Improvement"
             insight = "Farming efficency is low. Focus on lane control and creep priority"
        
        print("Rating:", rating)
        print("Insight:", insight)

def kda_analysis(player):

    kills = player["kills"]
    deaths = player["deaths"]
    assists = player["assists"]

    kda_ratio = (kills + assists) / deaths if deaths != 0 else kills + assists

    print("\n====== KDA ANALYSIS ======")

    print("Kills:", kills)
    print("Deaths:", deaths)
    print("Assists:", assists)

    print("KDA Ratio:", round(kda_ratio, 2))

    if deaths <= 5:
        rating = "Excellent"
        insight = "Good survival and positioning."

    elif deaths <= 8:
        rating = "Average"
        insight = "Acceptable, but positioning needs improvement."

    else:
        rating = "Needs Improvement"
        insight = "High death count. Focus on positioning and fight selection."

    print("Rating:", rating)
    print("Insight:", insight)

    # problem muncul : space atau jarak. solusi : CTR + A , lepas tu SHIFT + ALTERNATE + F untuk auto format indentation.

def display_items(player, item_map):

    print("\n====== CURRENT ITEMS ======")

    item_slots = [
        "item_0",
        "item_1",
        "item_2",
        "item_3",
        "item_4",
        "item_5"
    ]

    for slot in item_slots:

        item_id = player[slot]

        if item_id != 0:
            item_name = item_map.get(item_id, "Unknown Item") # guna item_map.get sbb kalau ada format item pelik, py tak crash.

            print("-", item_name)

def get_enemy_players(players, target_player):

    enemy_players = []

    for player in players:

        if player["team_number"] != target_player["team_number"]:
            enemy_players.append(player)
        
    return enemy_players

def threat_analysis(enemy_players, hero_map):

    print("\n====== THREAT ANALYSIS ======")

    for enemy in enemy_players:

        hero_name = hero_map[enemy["hero_id"]]

        if hero_name in THREATS:

            print("\nHero:", hero_name)

            print(
                "Threat:",
                THREATS[hero_name]
            )

THREATS = {

    "Kunkka":
    "Strong teamfight control and burst damage.",

    "Skywrath Mage":
    "High magical burst damage.",

    "Axe":
    "Can lock down carries and punish positioning.",

    "Sniper":
    "Long range damage dealer.",

    "Legion Commander":
    "Dangerous single target lockdown.",

    "Omniknight":
    "Can protect allies and extend fights."
}

def item_recommendation(enemy_players, hero_map):

    print("\n====== ITEM RECOMMENDATION ======")

    recommended = []

    for enemy in enemy_players:

        hero_name = hero_map[enemy["hero_id"]]

        if hero_name in ITEM_RECOMMENDATION:

            item = ITEM_RECOMMENDATION[hero_name]

            recommended.append(item)

            print("\nAgainst:", hero_name)
            print("Suggest:", item["item"])
            print("Reason:", item["reason"])


ITEM_RECOMMENDATION = {

    "Skywrath Mage":
    {
        "item": "Black King Bar",
        "reason": "Need magic immunity against high burst damage."
    },

    "Sniper":
    {
        "item": "Butterfly",
        "reason": "Increase survivability against physical damage."
    },

    "Axe":
    {
        "item": "Linken's Sphere",
        "reason": "Avoid single target initiation."
    },

    "Legion Commander":
    {
        "item": "Linken's Sphere",
        "reason": "Avoid Duel lockdown."
    }
}

from benchmark import BENCHMARK


def benchmark_analysis(player):

    duration_minutes = player["duration"] / 60

    lh_per_min = player["last_hits"] / duration_minutes

    kda_ratio = (
        player["kills"] + player["assists"]
    ) / player["deaths"] if player["deaths"] != 0 else (
        player["kills"] + player["assists"]
    )

    damage_per_min = (
        player["hero_damage"] / duration_minutes
    )


    print("\n====== BENCHMARK ANALYSIS ======")


    # Farming

    print("\nFarming:")

    print(
        "Your LH/min:",
        round(lh_per_min,2)
    )

    print(
        "Benchmark:",
        BENCHMARK["lh_per_min"]
    )


    if lh_per_min >= BENCHMARK["lh_per_min"]:
        print("Status: Above Average")
    else:
        print("Status: Needs Improvement")


    # GPM

    print("\nGold:")

    print(
        "Your GPM:",
        player["gold_per_min"]
    )

    print(
        "Benchmark:",
        BENCHMARK["gpm"]
    )


    if player["gold_per_min"] >= BENCHMARK["gpm"]:
        print("Status: Above Average")
    else:
        print("Status: Needs Improvement")


    # KDA

    print("\nKDA:")

    print(
        "Your KDA:",
        round(kda_ratio,2)
    )

    print(
        "Benchmark:",
        BENCHMARK["kda_ratio"]
    )


    if kda_ratio >= BENCHMARK["kda_ratio"]:
        print("Status: Good")
    else:
        print("Status: Improve Fighting Decision")