import matplotlib.pyplot as plt
import numpy as np

# tabular summary
def tabular_summary(birth_weight):
    rows = [
        ["Observations: ", len(birth_weight)],
        ["Mean: ", f"{birth_weight.mean():.3f}"],
        ["Median: ", f"{birth_weight.median():.3f}"],
        ["Sample Standard Deviation: ", f"{birth_weight.std():.3f}"],
        ["Range: ", f"{birth_weight.max() - birth_weight.min():.3f}"],
        ["Q1: ", f"{birth_weight.quantile(0.25):.3f}"],
        ["Q2: ", f"{birth_weight.quantile(0.50):.3f}"],
        ["Q3: ", f"{birth_weight.quantile(0.75):.3f}"],
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

    ax.set_title("Full-Term Birth Weight Summary (lb)", pad = 10)
    fig.savefig("visuals/birth_weight_TS.png", dpi = 300, bbox_inches = "tight")

# relative frequency histogram
def relative_frequency_histogram(birth_weight):
    fig, ax = plt.subplots()

    ax.hist(
        birth_weight,
        bins = 8,
        weights = np.ones(len(birth_weight)) / len(birth_weight),
        edgecolor = "white", 
    )

    ax.set(
        title = "Full-Term Birth Weight - Relative Frequency Histogram",
        xlabel = "Birth Weight (lb)",
        ylabel = "Relative Frequency",
    )

    fig.savefig("visuals/birth_weight_RFH.png", dpi = 300, bbox_inches = "tight")

# cumulative relative frequency graph
def cumulative_relative_frequency_graph(birth_weight):
    fig, ax = plt.subplots()

    counts, edges = np.histogram(birth_weight, bins = 8)
    cumulative = np.cumsum(counts) / len(birth_weight)

    ax.plot(edges, np.insert(cumulative, 0, 0), marker = "o")

    ax.set(
        title = "Full-Term Birth Weight - Cumulative Relative Frequency",
        xlabel = "Birth Weight (lb)",
        ylabel = "Cumulative Relative Frequency",
        ylim = (0,1),
    )

    fig.savefig("visuals/birth_weight_CRFG.png", dpi = 300, bbox_inches = "tight")
 