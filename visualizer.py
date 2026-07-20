import matplotlib.pyplot as plt


def plot_benchmark_comparison(benchmark):

    metrics = []

    player_values = []

    benchmark_values = []


    for metric, data in benchmark.items():

        metrics.append(
            metric
        )

        player_values.append(
            data["player"]
        )

        benchmark_values.append(
            data["benchmark"]
        )


    x = range(
        len(metrics)
    )


    width = 0.35


    plt.figure(
        figsize=(8,5)
    )


    plt.bar(
        [i - width/2 for i in x],
        player_values,
        width,
        label="Player"
    )


    plt.bar(
        [i + width/2 for i in x],
        benchmark_values,
        width,
        label="Benchmark"
    )


    plt.xticks(
        x,
        metrics
    )


    plt.ylabel(
        "Performance Value"
    )


    plt.title(
        "Player vs Benchmark Comparison"
    )


    plt.legend()


    plt.tight_layout()


    plt.show()

def plot_progress_history(records):

    match_numbers = []

    gpm_values = []

    lh_values = []

    kda_values = []


    for record in records:

        match_numbers.append(
            record[0]
        )

        gpm_values.append(
            record[1]
        )

        lh_values.append(
            record[2]
        )

        kda_values.append(
            record[3]
        )


    plt.figure(
        figsize=(10,6)
    )


    plt.plot(
        match_numbers,
        gpm_values,
        marker="o",
        label="GPM"
    )


    plt.plot(
        match_numbers,
        lh_values,
        marker="s",
        label="LH/min"
    )


    plt.plot(
        match_numbers,
        kda_values,
        marker="^",
        label="KDA"
    )


    plt.title(
        "Player Improvement Progress"
    )


    plt.xlabel(
        "Match Record"
    )


    plt.ylabel(
        "Performance"
    )


    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.show()