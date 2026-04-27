import glob
import pandas as pd

for path in glob.glob("data/raw/*.csv"):
    df = pd.read_csv(path, parse_dates=["Date"]).set_index("Date")
    avg_gap = df.index.to_series().diff().dt.days.mean()

    if avg_gap < 10:    # weekly → average to monthly
        df = df.resample("MS").mean().round(3)
    elif avg_gap > 40:  # annual → forward-fill to monthly
        df = df.resample("MS").ffill()
    else:
        continue        # already monthly

    df.reset_index(inplace=True)
    df["Date"] = df["Date"].dt.strftime("%-m/%-d/%Y")
    df.to_csv(path, index=False)
    print(f"Resampled: {path.split('/')[-1]}")
