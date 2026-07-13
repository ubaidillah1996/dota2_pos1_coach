import matplotlib.pyplot as plt


def performance_graph(player):

    metrics = {
        "GPM": player["gold_per_min"],
        "XPM": player["xp_per_min"],
        "Hero Damage": player["hero_damage"],
        "Tower Damage": player["tower_damage"]
    }

    names = list(metrics.keys())
    values = list(metrics.values())

    plt.figure(figsize=(8,5))

    plt.bar(names, values)

    plt.title("Player Performance Overview")

    plt.ylabel("Value")

    plt.xticks(rotation=45)

    plt.show()