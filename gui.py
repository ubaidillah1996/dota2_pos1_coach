# DOTA POS 1 COACH
# GUI Layer (Tkinter)
import tkinter as tk
from tkinter import messagebox


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

    items = analysis["items"]

    coach_report = analysis["coach_report"]

    gpm = player["gold_per_min"]

    xpm = player["xp_per_min"]

    networth = player["net_worth"]

    hero_damage = player["hero_damage"]

    tower_damage = player["tower_damage"]

    duration = round(player["duration"] / 60, 1)

    level = player["level"]

    result = "WIN" if player["win"] == 1 else "LOSS"

    hero_id = player["hero_id"]

    gpm = f"{player['gold_per_min']:,}"

    xpm = f"{player['xp_per_min']:,}"

    networth = f"{player['net_worth']:,}"

    hero_damage = f"{player['hero_damage']:,}"

    tower_damage = f"{player['tower_damage']:,}"

    output = f"""
================================
        DOTA POS 1 COACH
================================

PLAYER SUMMARY
----------------

Name:
{player.get("personaname")}

Match Duration:
{duration} minutes

Level:
{level}

Result:
{result}

GPM:
{gpm}

XPM:
{xpm}

Net Worth:
{networth}

Hero Damage:
{hero_damage}

Tower Damage:
{tower_damage}

ECONOMY
-------

Last Hits:
{farming["last_hits"]}

LH/min:
{farming["lh_per_min"]}

GPM:
{gpm}

XPM:
{xpm}

Net Worth:
{networth}


COMBAT
------

Hero Damage:
{hero_damage}

Tower Damage:
{tower_damage}



ITEM ANALYSIS
-------------

"""


    for item in items["items"]:

        output += f"""
- {item}
"""


    output += f"""



FARMING ANALYSIS
----------------

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

COACH INSIGHT
-------------

"""


    for insight in coach_report:

        output += f"""
- {insight}
"""


    output += """

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

    try:

        match_id = int(match_entry.get())

    except ValueError:

        messagebox.showerror(
            "Error",
            "Match ID must be a number."
        )

        return


    hero = hero_entry.get().strip().lower()


    if not hero:

        messagebox.showerror(
            "Error",
            "Please enter Hero Name."
        )

        return


    try:

        result = prepare_match_data(
        match_id
        )

    except Exception as e:

        print("SYSTEM ERROR:", e)

        messagebox.showerror(
            "Error",
            "Unable to analyse match."
        )

        return


    if result is None:

        messagebox.showerror(
            "Error",
            "Match not found."
        )

        return


    data, hero_map, item_map = result


    player = get_target_player(
        data,
        hero_map,
        hero
    )


    if player is None:

        messagebox.showerror(
            "Error",
            "Hero not found in this match."
        )

        return


    analysis = analyse_player(
        player,
        item_map
    )

    print(analysis["items"])

    print(analysis)

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
    command=analyse_match,
    font=("Consolas",12,"bold"),
    width=20
)

analyse_button.pack(
    pady=20
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

result_box.config(
    yscrollcommand=scrollbar.set
)



# =========================
# START APP
# =========================

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

root.mainloop()

