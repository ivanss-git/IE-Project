import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# tabular summary
def tabular_summary(seconds):
    rows = [
        ["Observartions: ", len(seconds)],
        ["Mean: ", f"{seconds.mean():.3f}"],
        ["Median: ", f"{seconds.median():.3f}"],
        ["Sample Standard Deviation: ", f"{seconds.std():.3f}"],
        ["Range: ", f"{seconds.max() - seconds.min():.3f}"],
        ["Q1: ", f"{seconds.quantile(0.25):.3f}"],
        ["Q2: ", f"{seconds.quantile(0.50):.3f}"],
        ["Q3: ", f"{seconds.quantile(0.75):.3f}"],
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

    ax.set_title("Library - Split Time Tabular Summary (seconds)", pad = 10)
    fig.savefig("visuals/library_TS.png", dpi = 300, bbox_inches = "tight")


# relative frequency histogram
def relative_frequency_histogram(seconds):
    fig, ax = plt.subplots()

    ax.hist(
        seconds,
        bins = 8,
        weights = np.ones(len(seconds)) / len(seconds),
        edgecolor = "white", 
    )

    ax.set(
        title = "Library Split Times",
        xlabel = "Time between arrivals (seconds)",
        ylabel = "Relative Frequency",
    )

    fig.savefig("visuals/library_RFH.png", dpi = 300, bbox_inches = "tight")


# cumulative relative frequency graph
def cumulative_relative_frequency_graph(seconds):
    fig, ax = plt.subplots()

    counts, edges = np.histogram(seconds, bins = 8)
    cumulative = np.cumsum(counts) / len(seconds)

    ax.plot(edges, np.insert(cumulative, 0, 0), marker = "o")

    ax.set(
        title = "Library - Cumulative Relative Frequency",
        xlabel = "Time between arrivals (seconds)",
        ylabel = "Cumulative Relative Frequency",
        ylim = (0,1),
    )

    fig.savefig("visuals/library_CRFG.png", dpi = 300, bbox_inches = "tight")
 