import matplotlib.pyplot as plt
from src.processing import df
from src.visuals import tabular_summary, relative_frequency_histogram

tabular_summary(df["Split Time"])
relative_frequency_histogram(df["Split Time"])

plt.show()