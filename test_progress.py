from database import get_progress_history

from visualizer import plot_progress_history


records = get_progress_history()

plot_progress_history(
    records
)