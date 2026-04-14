import pandas as pd

files = ["data/raw/texas_housing_price.csv", "data/raw/cpi.csv", "data/raw/interest_rate.csv", "data/raw/unemployment_rate.csv"]

df = pd.read_csv(files[0])

for file in files[1:]:
    df = df.merge(pd.read_csv(file), on="Date")

df.to_csv("data/processed/merged_data.csv", index=False)
