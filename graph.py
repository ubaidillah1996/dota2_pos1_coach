import matplotlib.pyplot as plt


def create_benchmark_chart(performance):

    metrics = []

    player_scores = []

    benchmark_scores = []


    for metric, data in performance.items():

        metrics.append(metric)


        player_score = (
            data["player"]
            /
            data["benchmark"]
        ) * 100


        benchmark_score = 100


        player_scores.append(
            round(player_score, 1)
        )


        benchmark_scores.append(
            benchmark_score
        )


    x = range(len(metrics))


    plt.figure(figsize=(8,5))


    plt.bar(
        x,
        player_scores,
        width=0.4,
        label="Player"
    )


    plt.bar(
        [i + 0.4 for i in x],
        benchmark_scores,
        width=0.4,
        label="Benchmark"
    )


    plt.xticks(
        [i + 0.2 for i in x],
        metrics
    )


    plt.ylabel(
        "Performance Score (%)"
    )


    plt.title(
        "Carry Performance vs Benchmark"
    )


    plt.legend()


    plt.ylim(
        0,
        max(player_scores) + 30
    )


    for i, value in enumerate(player_scores):

        plt.text(
            i,
            value + 3,
            f"{value}%",
            ha="center"
        )


    plt.savefig(
        "performance_chart.png",
        bbox_inches="tight"
    )


    plt.show()