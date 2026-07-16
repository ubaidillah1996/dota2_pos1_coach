# DOTA POS 1 COACH
# Version 0.6 Refactor


# =========================
# IMPORT
# =========================

### IMPORTING ALL DETAILS / MODULES TO THIS FILE 

from api import get_match, get_heroes, get_items

from analyzer import (
    display_performance,
    farming_analysis,
    kda_analysis,
    display_items,
    threat_analysis,
    benchmark_analysis,
    generate_coach_report,
    get_enemy_players,
    item_recommendation
)

from graph import create_benchmark_chart
from report import generate_final_summary

from input_handler import get_user_input

from database import (
    create_table,
    save_analysis,
    view_history,
    delete_analysis,
    add_notes_column,
    update_note,
    check_existing_analysis,
)
from services import (
    prepare_match_data,
    get_target_player
)


## GREETING ##

def welcome_screen():

    print("""
================================
        DOTA POS 1 COACH

   Analyze.
   Compare.
   Improve.

   Carry Performance Analytics
================================
""")

## GETTING USER DETAILS AND DISPLAY IT ##

def analyse_match():

    print("\n====== NEW MATCH ANALYSIS ======")

    ### INPUT ID

    match_id, target_hero = get_user_input()

    ## CHECKING EXISTED OR NOT, IF NOT KICK OUT ##

    existing = check_existing_analysis(
        match_id,
        target_hero
    )

    if existing:

        print(
            "\nAnalysis already exists."
        )

        return

    

    result = prepare_match_data(
        match_id
    )

    

    result = prepare_match_data(
    match_id
    )

    if not result:

        print(
        "Match data not found."
    )

        return


    data, hero_map, item_map = result
    
    ### FINDING PLAYER HERO

    player = get_target_player(
        data,
        hero_map,
        target_hero
    )

    if player is None:

        print(
            "\nPlayer not found."
        )

        print(
            "Please check hero name or match ID."
        )

        return

    print(
        "TARGET HERO:",
        target_hero
        )
    
    ### DISPLAY DATA
    
    display_performance(player)

    farming_analysis(player)

    kda_analysis(player)

    benchmark_result = benchmark_analysis(player)

    generate_coach_report(
        benchmark_result,
        player
    )

    generate_final_summary(
        benchmark_result,
        player
    )

    ## CHECKING EXISTING RECORD FUNCTION ##

    existing = check_existing_analysis(
        match_id,
        target_hero
    )


    if existing:

        print(
            "\nAnalysis already exists."
        )

        return

    ### SAVING RECORD

    save_analysis(

        match_id,

        target_hero,

        player.get(
            "personaname",
            "Unknown"
        ),

        benchmark_result["KDA"]["player"],

        benchmark_result["Farming"]["player"],

        player["gold_per_min"],

        benchmark_result["Farming"]["status"]

    )

    create_benchmark_chart(
        benchmark_result
    )

    display_items(
        player,
        item_map
    )

    enemy_players = get_enemy_players(
        data["players"],
        player
    )

    print("\n====== ENEMY TEAM ======")


    for enemy in enemy_players:

        player_name = enemy.get(
            "personaname",
            "Unknown Player"
        )

        hero_name = hero_map[
            enemy["hero_id"]
        ]

        print(
            f"{player_name} | {hero_name}"
        )

    enemy_players = get_enemy_players(
        data["players"],
        player
    )

    threat_analysis(
        enemy_players,
        hero_map
    )

    item_recommendation(
        enemy_players,
        hero_map
    )

## READ HISTORY FUNCTION ##

def show_history():

    print("\n====== ANALYSIS HISTORY ======")

    history = view_history()


    for record in history:

        print(f"\nID: {record[0]}")
        print(f"Match ID: {record[1]}")
        print(f"Hero: {record[2].title()}")
        print(f"Player: {record[3]}")
        print(f"KDA: {record[4]}")
        print(f"LH/min: {record[5]}")
        print(f"GPM: {record[6]}")
        print(f"Status: {record[7]}")
        print(f"Reflection: {record[8]}")

        print("-" * 30)

## PERSONAL NOTES USER FUNCTION ##

def update_reflection():

    print("\n====== UPDATE REFLECTION ======")


    record_id = int(
        input("Enter Analysis ID: ")
    )


    note = input(
        "Enter your reflection: "
    )


    update_note(
        record_id,
        note
    )


    print("Note updated.")

## DELETE RECORD ANALYSIS FUNCTION ##

def delete_record():

    print("\n====== DELETE ANALYSIS ======")


    record_id = int(
        input("Enter Analysis ID: ")
    )


    delete_analysis(
        record_id
    )


    print("Record deleted.")

## DISPLAY MENU BUTTON FUCNTION ##

def show_menu():

    print("""
================================
        DOTA POS 1 COACH
        AI PERFORMANCE ANALYZER
================================

[1] Analyse New Match
[2] View History
[3] Update Reflection
[4] Delete Analysis
[5] Exit

""")

## MENU CONTROLLER FUNCTION ##

if __name__ == "__main__":

    welcome_screen()

    add_notes_column()

    create_table()


    while True:

        show_menu()


        choice = input(
            "Choose option: "
        )


        if choice == "1":

            analyse_match()


        elif choice == "2":

            show_history()


        elif choice == "3":

            update_reflection()


        elif choice == "4":

            delete_record()


        elif choice == "5":

            print("Exit...")
            break


        else:

            print("Invalid choice")