import pandas as pd

def run(ids, start, end):
    # Downloads each FRED series as a CSV to data/raw/ using the proper name as the filename
    for series_id, name in ids.items():
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}&cosd={start}&coed={end}"
        df = pd.read_csv(url)
        df.columns = ["DATE", name]
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%-m/%-d/%Y")
        df.to_csv(f"data/raw/{name}.csv", index=False)
        print(f"Saved {name}.csv")
