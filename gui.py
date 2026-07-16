# DOTA POS 1 COACH
# GUI Layer (Tkinter)

import tkinter as tk

from services import (
    prepare_match_data,
    get_target_player,
    analyse_player
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

    print(analysis)


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()

root.title(
    "DOTA POS 1 COACH"
)

root.geometry(
    "800x600"
)



# =========================
# TITLE
# =========================

title = tk.Label(
    root,
    text="DOTA POS 1 COACH",
    font=("Arial", 20)
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

result_box = tk.Text(
    root,
    height=15,
    width=70
)

result_box.pack(
    pady=20
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