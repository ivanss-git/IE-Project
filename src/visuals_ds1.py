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
    fig.savefig("visuals/temp_TS.png", dpi = 300, bbox_inches = "tight")

# relative frequency histogram
def relative_frequency_histogram(temperature):
    fig, ax = plt.subplots()

    ax.hist(
        temperature,
        bins = 8,
        weights = np.ones(len(temperature)) / len(temperature),
        edgecolor = "white", 
    )

    ax.set(
        title = "Body Temperature - Relative Frequency Histogram",
        xlabel = "Temperature (Fahrenheit)",
        ylabel = "Relative Frequency",
    )

    fig.savefig("visuals/temp_RFH.png", dpi = 300, bbox_inches = "tight")

# cumulative relative frequency graph
def cumulative_relative_frequency_graph(temperature):
    fig, ax = plt.subplots()

    counts, edges = np.histogram(temperature, bins = 8)
    cumulative = np.cumsum(counts) / len(temperature)

    ax.plot(edges, np.insert(cumulative, 0, 0), marker = "o")

    ax.set(
        title = "Body Temp - Cumulative Relative Frequency",
        xlabel = "Temperature (Fahrenheit)",
        ylabel = "Cumulative Relative Frequency",
        ylim = (0,1),
    )

    fig.savefig("visuals/temp_CRFG.png", dpi = 300, bbox_inches = "tight")
 