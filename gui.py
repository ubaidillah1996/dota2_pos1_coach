# DOTA POS 1 COACH
# GUI Layer (Tkinter)

import tkinter as tk

from services import (
    prepare_match_data,
    get_target_player,
    analyse_player
)

def display_analysis_result(analysis):

    result_box.delete(
        "1.0",
        tk.END
    )


    player = analysis["player"]

    farming = analysis["farming"]

    kda = analysis["kda"]

    benchmark = analysis["benchmark"]


    output = f"""
================================
        DOTA POS 1 COACH
================================


PLAYER
{player.get("personaname")}


FARMING ANALYSIS
----------------

Last Hits:
{farming["last_hits"]}

LH/min:
{farming["lh_per_min"]}

Rating:
{farming["rating"]}

Insight:
{farming["insight"]}



KDA ANALYSIS
------------

Kills:
{kda["kills"]}

Deaths:
{kda["deaths"]}

Assists:
{kda["assists"]}

KDA Ratio:
{kda["ratio"]}

Rating:
{kda["rating"]}

Insight:
{kda["insight"]}



BENCHMARK RESULT
----------------
"""


    for metric, data in benchmark.items():

        output += f"""

{metric}

Performance:
{data["player"]}

Benchmark:
{data["benchmark"]}

Difference:
{data["difference"]}

Status:
{data["status"]}

"""


    result_box.insert(
        tk.END,
        output
    )

# =========================
# BUTTON FUNCTION
# =========================

def analyse_match():

    match_id = int(
        match_entry.get()
    )

    hero = hero_entry.get().strip().lower()


    result = prepare_match_data(
        match_id
    )


    if result is None:

        print("Match not found")
        return


    data, hero_map, item_map = result


    player = get_target_player(
        data,
        hero_map,
        hero
    )

    print("SEARCH HERO:", hero)

    print("AVAILABLE HERO:")

    for player in data["players"]:

        print(
        hero_map[player["hero_id"]]
    )

    if player is None:

        print("Player not found")
        return
    
    analysis = analyse_player(
    player
    )


    result_box.delete(
    "1.0",
    tk.END
)


    output = f"""
    PLAYER PERFORMANCE

    Player:
    {player.get('personaname')}

    Hero:
    {hero.title()}

    KDA:
    {player['kills']} / {player['deaths']} / {player['assists']}

    Last Hits:
    {player['last_hits']}

    GPM:
    {player['gold_per_min']}

    XPM:
    {player['xp_per_min']}

    Net Worth:
    {player['net_worth']}
    """


    result_box.insert(
    tk.END,
    output
    )

    display_analysis_result(
    analysis
    )

# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()

root.title(
    "DOTA POS 1 COACH"
)

root.geometry("900x700")



# =========================
# TITLE
# =========================

title = tk.Label(
    root,
    text="DOTA POS 1 COACH",
    font=("Consolas",20,"bold")
)

title.pack(
    pady=20
)



# =========================
# MATCH ID INPUT
# =========================

match_label = tk.Label(
    root,
    text="Match ID"
)

match_label.pack()


match_entry = tk.Entry(
    root,
    width=40
)

match_entry.pack(
    pady=10
)


# =========================
# RESULT DISPLAY
# =========================

result_frame = tk.Frame(root)

result_frame.pack(
    pady=20
)


scrollbar = tk.Scrollbar(
    result_frame
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


result_box = tk.Text(
    result_frame,
    height=25,
    width=90,
    font=("Consolas", 11)
)

result_box.pack(
    side=tk.LEFT
)


scrollbar.config(
    command=result_box.yview
)


# =========================
# HERO INPUT
# =========================

hero_label = tk.Label(
    root,
    text="Carry Hero"
)

hero_label.pack()


hero_entry = tk.Entry(
    root,
    width=40
)

hero_entry.pack(
    pady=10
)



# =========================
# ANALYSE BUTTON
# =========================

analyse_button = tk.Button(
    root,
    text="Analyse Match",
    command=analyse_match
)

analyse_button.pack(
    pady=20
)



# =========================
# START APP
# =========================

root.mainloop()

def clear_result():

    result_box.delete(
        "1.0",
        tk.END
    )

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_result
)

clear_button.pack()