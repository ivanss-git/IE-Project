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

