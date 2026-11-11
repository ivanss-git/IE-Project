import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# tabular summary
def tabular_summary(temperature):
    rows = [
        ["Observations: ", len(temperature)],
        ["Mean: ", f"{temperature.mean():.3f}"],
        ["Median: ", f"{temperature.median():.3f}"],
        ["Sample Standard Deviation: ", f"{temperature.std():.3f}"],
        ["Range: ", f"{temperature.max() - temperature.min():.3f}"],
        ["Q1: ", f"{temperature.quantile(0.25):.3f}"],
        ["Q2: ", f"{temperature.quantile(0.50):.3f}"],
        ["Q3: ", f"{temperature.quantile(0.75):.3f}"],
    ]

    fig, ax = plt.subplots(figsize=(8,4))
    ax.axis("off")

    table = ax.table(
        cellText = rows,
        colLabels = ["Statistic", "Value"],
        cellLoc = "center",
        loc = "center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1,2)

    ax.set_title("Thermometry - Body Temperature Tabular Summary (Fahrenheit)", pad = 10)
    fig.savefig("visuals/temperature_TS.png", dpi = 300, bbox_inches = "tight")

# relative frequency histogram
# cumulative relative frequency graph