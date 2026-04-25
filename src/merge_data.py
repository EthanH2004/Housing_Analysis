import glob
import pandas as pd

# Grab every CSV in data/raw/ — add new series there and they'll be included automatically
files = sorted(glob.glob("data/raw/*.csv"))

df = pd.read_csv(files[0])

# Outer join keeps all months; gaps from short series (e.g. annual Census data) get filled below
for file in files[1:]:
    df = df.merge(pd.read_csv(file), on="DATE", how="outer")

df = df.iloc[pd.to_datetime(df["DATE"]).argsort()].reset_index(drop=True)

# Fill any missing values with the previous month's value (e.g. annual series, government shutdowns)
df.ffill(inplace=True)
df.to_csv("data/processed/merged_data.csv", index=False)
