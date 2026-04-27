import os
import pandas as pd

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/processed/merged_data.csv")

# inflation-adjust home price using CPI
df["RealPrice"] = (df["HomePrice"] / df["CPI"] * 100).round(2)

# move to second column
cols = df.columns.tolist()
cols.insert(1, cols.pop(cols.index("RealPrice")))
df = df[cols]

# drop now that we have real price
df.drop(columns=["HomePrice", "CPI"], inplace=True)

df.to_csv("data/processed/final_dataset.csv", index=False)
