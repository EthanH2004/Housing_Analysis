import pandas as pd

df = pd.read_csv("data/processed/merged_data.csv")

# Adjust the nominal housing price for inflation using CPI
df["REALPRICE"] = (df["HomePrice"] / df["CPI"] * 100).round(2)

# Move REALPRICE to the second column
cols = df.columns.tolist()
cols.insert(1, cols.pop(cols.index("REALPRICE")))
df = df[cols]

# Drop CPI and TXUCSFRCONDOSMSAMID since we only care about the real price now
df.drop(columns=["HomePrice", "CPI"], inplace=True)

df.to_csv("data/processed/final_dataset.csv", index=False)
