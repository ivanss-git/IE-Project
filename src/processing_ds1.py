import os 
import pandas as pd


# checking to make sure the data is correct
df = pd.read_csv('data/thermometry.csv')
temperature = df["body.temp"]
print(temperature[:11])

print(df[1:])
print(f" Total Observations: {len(df)}")
print(f"Column Types: {df.dtypes}")
print(f"\nSample of first 10 entries: {df[:10]}")
print(f"\nRandom Sample of 10 entries: {df.sample(n=10)}")

# (3) “Descriptive Statistical Analysis” for calculations and results
# sample mean
def sample_mean():
    sample_mean = temperature.mean()

    print(f"Sample Mean: {sample_mean}")

sample_mean()

# sample median
def sample_median():
    sample_median = temperature.median()

    print(f"Sample Median: {sample_median}")

sample_median()

# sample standard deviation
def sample_standard_deviation():
    sample_stdev = temperature.std()

    print(f"Sample Standard Deviation: {sample_stdev}")

sample_standard_deviation()

# sample range
def sample_range():
    sample_max = temperature.max()
    sample_min = temperature.min()
    sample_range = temperature.max() - temperature.min()

    print(f"Sample Max: {sample_max}")
    print(f"Sample Min: {sample_min}")
    print(f"Sample Range: {sample_range}")

sample_range()

# quartiles (Q1, Q2, Q3)
def quartiles():
    temp_q1 = temperature.quantile(0.25)
    temp_q2 = temperature.quantile(0.50)
    temp_q3 = temperature.quantile(0.75)

    print(f"Temperature Q1: {temp_q1}")
    print(f"Temperature Q2: {temp_q2}")
    print(f"Temperature Q3: {temp_q3}")

quartiles()
