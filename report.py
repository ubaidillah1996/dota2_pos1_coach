# DOTA POS 1 COACH
# Report Generator


def generate_final_summary(
    benchmark_result,
    player
):

    print("\n")
    print("=" * 40)
    print("        FINAL PERFORMANCE SUMMARY")
    print("=" * 40)


    print("\nPLAYER:")
    print(
        player.get(
            "personaname",
            "Unknown"
        )
    )


    print("\n====== BENCHMARK RESULT ======")


    for metric, data in benchmark_result.items():

        print("\n" + metric)

        print(
            "Performance:",
            data["player"]
        )

        print(
            "Benchmark:",
            data["benchmark"]
        )

        print(
            "Status:",
            data["status"]
        )


    print("\n====== COACH RECOMMENDATION ======")


    if player["deaths"] >= 8:

        print(
            "⚠ Improve positioning and fight selection."
        )

    else:

        print(
            "✓ Good survival and decision making."
        )


    if player["gold_per_min"] >= 550:

        print(
            "✓ Strong farming and gold efficiency."
        )

    else:

        print(
            "⚠ Improve farming consistency."
        )


    print("\n" + "=" * 40)