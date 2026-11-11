import matplotlib.pyplot as plt
from src.processing import df
from src.visuals import tabular_summary, relative_frequency_histogram, cumulative_relative_frequency_graph

tabular_summary(df["Split Time"])
relative_frequency_histogram(df["Split Time"])
cumulative_relative_frequency_graph(df["Split Time"])

plt.show()