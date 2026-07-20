from visualizer import plot_benchmark_comparison


benchmark = {

    "Farming":
    {
        "player":10.07,
        "benchmark":7
    },


    "Gold":
    {
        "player":538,
        "benchmark":550
    },


    "KDA":
    {
        "player":0.67,
        "benchmark":3
    }

}


plot_benchmark_comparison(
    benchmark
)