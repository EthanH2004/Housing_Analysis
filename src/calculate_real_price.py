import pandas as pd

df = pd.read_csv("data/processed/merged_data.csv")

df["RealPrice"] = (df["NominalPrice"] / df["CPI"] * 100).round(2)

cols = df.columns.tolist()
cols.insert(1, cols.pop(cols.index("RealPrice")))
df = df[cols]

df.drop(columns=["NominalPrice", "CPI"], inplace=True)

df.to_csv("data/processed/final_dataset.csv", index=False)
