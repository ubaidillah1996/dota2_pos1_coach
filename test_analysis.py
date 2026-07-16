from services import analyse_player


player = {

    "personaname": "Test Player",

    "kills": 10,
    "deaths": 3,
    "assists": 8,

    "last_hits": 300,
    "duration": 1800,

    "gold_per_min": 600,
    "xp_per_min": 700,

    "net_worth": 20000
}


result = analyse_player(player)


print(result)