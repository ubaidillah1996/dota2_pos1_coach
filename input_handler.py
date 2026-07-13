def get_user_input():

    print("\n====== DOTA POS 1 COACH ======")

    while True:

        try:

            match_id = int(
                input("Enter Match ID: ")
            )

            break

        except ValueError:

            print(
                "Invalid Match ID. Please enter numbers only."
            )


    target_hero = input(
        "Enter Carry Hero: "
    )


    return match_id, target_hero