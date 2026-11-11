import os
import pandas as pd

TOTAL_TIME = 'Total Time'
SPLIT_TIME = 'Split Time'

# converting the data to seconds so its easier to use
def time_to_seconds(val):
    if pd.isna(val) or str(val).strip() == "":
        return None

    parts = str(val).split(":")

    if len(parts) == 1:
        return float(parts[0])

    minutes = float(parts[0])
    seconds = float(parts[1])
    return (minutes * 60) + seconds


# creating a pandas dataframe that contains the actual data we will use
df = pd.read_csv(
    'data/library.csv', 
    index_col='Lap', 
    converters={'Total Time': time_to_seconds, 'Split Time': time_to_seconds})

df = df.iloc[1:].copy()

# veryfying that the csv file data type matches
print(f"Column Types: {df.dtypes}")
print(f"Total Observations: {len(df)}")
print(f"\nSample of first 10 entries: {df[:10]}")
print(f"\nRandom Sample of 10 entries: {df.sample(n=10)}")


# (3) “Descriptive Statistical Analysis” for calculations and results
# sample mean
def sample_mean(df):
    mean_value1 = df[TOTAL_TIME].mean()
    mean_value2 = df[SPLIT_TIME].mean()

    print(f"Sample Mean 1: {mean_value1}")
    print(f"Sample Mean 2: {mean_value2}")

sample_mean(df)

# sample median
def sample_median(df):
    median_value1 = df[TOTAL_TIME].median()
    median_value2 = df[SPLIT_TIME].median()

    print(f"Sample Median 1: {median_value1}")
    print(f"Sample Median 2: {median_value2}")

sample_median(df)

# sample standard deviation
def sample_standard_deviation(df):
    sample_stdev1 = df[TOTAL_TIME].std()
    sample_stdev2 = df[SPLIT_TIME].std()

    print(f"Sample Standard Deviation 1: {sample_stdev1}")
    print(f"Sample Standard Deviation 2: {sample_stdev2}")

sample_standard_deviation(df)

# sample range
def sample_range(df):
    sample_range1 = df[TOTAL_TIME].max() - df[TOTAL_TIME].min()
    sample_range2 = df[SPLIT_TIME].max() - df[SPLIT_TIME].min() 

    print(f"Sample Range 1: {sample_range1}")
    print(f"Sample Range 2: {sample_range2}")

sample_range(df)

# quartiles (Q1, Q2, and Q3) 
def quartiles(df):
    total_time_q1 = df[TOTAL_TIME].quantile(0.25)
    total_time_q2 = df[TOTAL_TIME].quantile(0.50)
    total_time_q3 = df[TOTAL_TIME].quantile(0.75)

    split_time_q1 = df[SPLIT_TIME].quantile(0.25)
    split_time_q2 = df[SPLIT_TIME].quantile(0.50) 
    split_time_q3 = df[SPLIT_TIME].quantile(0.75)

    print(f"{'Total Time Q1':<10}: {total_time_q1}")
    print(f"{'Total Time Q2':<10}: {total_time_q2}")
    print(f"{'Total Time Q3':<10}: {total_time_q3}")

    print(f"{'Split Time Q1':<10}: {split_time_q1}")
    print(f"{'Split Time Q2':<10}: {split_time_q2}")
    print(f"{'Split Time Q3':<10}: {split_time_q3}")

quartiles(df)
