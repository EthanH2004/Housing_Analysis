import glob
import os
import pandas as pd

os.makedirs("data/processed", exist_ok=True)

# add CSVs to data/raw/ to include them automatically
files = sorted(glob.glob("data/raw/*.csv"))

df = pd.read_csv(files[0])

# outer join so no months are lost
for file in files[1:]:
    df = df.merge(pd.read_csv(file), on="Date", how="outer")

df = df.iloc[pd.to_datetime(df["Date"]).argsort()].reset_index(drop=True)

# fill gaps with last known value
df.ffill(inplace=True)
df.to_csv("data/processed/merged_data.csv", index=False)
