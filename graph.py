import matplotlib.pyplot as plt


def create_benchmark_chart(performance):

    metrics = []
    player_values = []
    benchmark_values = []


    for metric, data in performance.items():

        metrics.append(metric)

        player_values.append(
            data["player"]
        )

        benchmark_values.append(
            data["benchmark"]
        )


    x = range(len(metrics))


    plt.figure(figsize=(8,5))


    plt.bar(
        x,
        player_values,
        width=0.4,
        label="Player"
    )


    plt.bar(
        [i + 0.4 for i in x],
        benchmark_values,
        width=0.4,
        label="Benchmark"
    )


    plt.xticks(
        [i + 0.2 for i in x],
        metrics
    )


    plt.ylabel("Performance Value")

    plt.title(
        "Carry Performance vs Benchmark"
    )


    plt.legend()


    plt.show()