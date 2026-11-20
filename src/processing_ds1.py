import pandas as pd


# checking to make sure the data is correct
df = pd.read_csv('data/births14.csv')
eligible = df["premie"] == "full term"
birth_weight = pd.to_numeric(df.loc[eligible, "weight"], errors="coerce").dropna()

print(f"Total usable birth weights: {len(birth_weight)}")
print(f"Column Types: {birth_weight.dtype}")
print(f"\nSample of first 10 entries: {birth_weight.head(10)}")
print(f"\nRandom Sample of 10 entries: {birth_weight.sample(n=10)}")

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
