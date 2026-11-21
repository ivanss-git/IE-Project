import pandas as pd
import numpy as np


# checking to make sure the data is correct
df = pd.read_csv('data/births14.csv')
print(f"\nTotal rows: {len(df)}")

counts = df["premie"].value_counts(dropna=False)
counts = counts.rename(index={"premie": "premature"})
print()
print(counts.rename_axis("Birth Classification"))

eligible = df["premie"] == "full term"
raw_weights = df.loc[eligible, "weight"]
numeric_weights = pd.to_numeric(raw_weights, errors="coerce")
finite_weights = numeric_weights[np.isfinite(numeric_weights)]
birth_weight = pd.to_numeric(df.loc[eligible, "weight"], errors="coerce").dropna()

birth_weight.to_csv("data/full_term_birth_weights.csv",index=False, header=["Birth Weight (lb)"])

print(f"Full-term rows: {len(raw_weights)}")
print(f"Missing weights: {raw_weights.isna().sum()}")
print(f"Nonnumeric weights: {(raw_weights.notna() & numeric_weights.isna()).sum()}")
print(f"Infinite weights: {np.isinf(numeric_weights).sum()}")
print(f"Nonpositive weights: {(finite_weights <= 0).sum()}")
print(f"Usable weights: {len(birth_weight)}")
print(f"Minimum and maximum (lb): {birth_weight.min():.2f}, {birth_weight.max():.2f}")
print(f"\nFirst 10 usable weights:\n{birth_weight.head(10)}")
print(f"\nRandom Sample of 10 usable weights:\n{birth_weight.sample(n=min(10, len(birth_weight)), random_state=42)}\n")


# (3) “Descriptive Statistical Analysis” for calculations and results
# sample mean
def sample_mean():
    sample_mean = birth_weight.mean()

    print(f"Sample Mean: {sample_mean}")

sample_mean()

# sample median
def sample_median():
    sample_median = birth_weight.median()

    print(f"Sample Median: {sample_median}")

sample_median()

# sample standard deviation
def sample_standard_deviation():
    sample_stdev = birth_weight.std()

    print(f"Sample Standard Deviation: {sample_stdev}")

sample_standard_deviation()

# sample range
def sample_range():
    sample_max = birth_weight.max()
    sample_min = birth_weight.min()
    sample_range = birth_weight.max() - birth_weight.min()

    print(f"Sample Max: {sample_max}")
    print(f"Sample Min: {sample_min}")
    print(f"Sample Range: {sample_range}")

sample_range()

# quartiles (Q1, Q2, Q3)
def quartiles():
    birth_weight_q1= birth_weight.quantile(0.25)
    birth_weight_q2 = birth_weight.quantile(0.50)
    birth_weight_q3 = birth_weight.quantile(0.75)

    print(f"birth_weight Q1: {birth_weight_q1}")
    print(f"birth_weight Q2: {birth_weight_q2}")
    print(f"birth_weight Q3: {birth_weight_q3}")

quartiles()
