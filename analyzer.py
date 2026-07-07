# untuk cari hero

def find_player_by_hero(players, hero_map, target_hero):

    for player in players :

        hero_name = hero_map[player["hero_id"]] # cari hero melalui siapa player apa hero id

        if hero_name.lower() == target_hero.lower():
            return player
        
    return None

# sekarang untuk keluarkan data asas pos 1 dulu :

def display_performance(player):

    print("\n====== PLAYER PERFORMANCE ======") # new line atau title

    print ("player:", player ["personaname"])

    print(
        "KDA:",
        player["kills"],
        "/",
        player["deaths"],
        "/",
        player["assists"]
    )

    print("Last Hits:", player["last_hits"])
    print("Denies:", player["denies"])

    print("GPM:", player["gold_per_min"])
    print("XPM:", player["xp_per_min"])

    print("Net Worth:", player["net_worth"])

    print("Hero Damage:", player["hero_damage"])
    print("Tower Damage:", player["tower_damage"])