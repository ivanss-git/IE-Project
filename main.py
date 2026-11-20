import matplotlib.pyplot as plt
from pathlib import Path
from src.processing_ds1 import birth_weight 
from src.processing_ds2 import df as library_df
from  src import visuals_ds1, visuals_ds2

Path("visuals/birth_weight").mkdir(exist_ok = True)

visuals_ds1.tabular_summary(birth_weight)
visuals_ds1.relative_frequency_histogram(birth_weight)
visuals_ds1.cumulative_relative_frequency_graph(birth_weight)

visuals_ds2.tabular_summary(library_df["Split Time"])
visuals_ds2.relative_frequency_histogram(library_df["Split Time"])
visuals_ds2.cumulative_relative_frequency_graph(library_df["Split Time"])

plt.show()