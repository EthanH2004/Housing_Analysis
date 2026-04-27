import os
import pandas as pd

def run(ids, start, end):
    os.makedirs("data/raw", exist_ok=True)
    for series_id, name in ids.items():
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}&cosd={start}&coed={end}"
        df = pd.read_csv(url)
        df.columns = ["Date", name]
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%-m/%-d/%Y")
        df.to_csv(f"data/raw/{name}.csv", index=False)
        print(f"Saved {name}.csv")
