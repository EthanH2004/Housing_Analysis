"""
Download a FRED series to data/raw/<name>.csv.

Usage:
    python src/fetch_fred.py
"""

import os
import re
import sys
from urllib.parse import urlparse, parse_qs
from datetime import datetime

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
DEFAULT_START = "2015-01-01"
DEFAULT_END = "2025-12-01"


def extract_series_id(raw: str) -> str:
    """Pull the series ID from a FRED URL or return it as-is if it looks like a plain ID."""
    raw = raw.strip()
    if raw.startswith("http"):
        parsed = urlparse(raw)
        qs = parse_qs(parsed.query)
        if "id" in qs:
            return qs["id"][0].upper()
        # handle paths like /series/CPIAUCSL
        match = re.search(r"/series/([A-Z0-9]+)", parsed.path, re.IGNORECASE)
        if match:
            return match.group(1).upper()
        raise ValueError(f"Could not extract a series ID from: {raw}")
    return raw.upper()


def prompt_dates() -> tuple[str, str]:
    print("\nDate range options:")
    print("  1 — Default (1/1/2015 – 12/1/2025)")
    print("  2 — Enter custom dates")
    choice = input("Choose [1/2]: ").strip()
    if choice == "2":
        start = input("  Start date (YYYY-MM-DD): ").strip()
        end = input("  End date   (YYYY-MM-DD): ").strip()
        # basic validation
        for d in (start, end):
            datetime.strptime(d, "%Y-%m-%d")
        return start, end
    return DEFAULT_START, DEFAULT_END


def download_series(series_id: str, start: str, end: str, out_name: str) -> str:
    url = (
        f"https://fred.stlouisfed.org/graph/fredgraph.csv"
        f"?id={series_id}&vintage_date=&cosd={start}&coed={end}"
    )
    print(f"\nDownloading {series_id} …")
    df = pd.read_csv(url)

    # FRED returns two columns: observation_date and the series ID
    df.columns = ["Date", out_name]
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%-m/%-d/%Y")

    os.makedirs(DATA_DIR, exist_ok=True)
    out_path = os.path.join(DATA_DIR, f"{out_name.lower()}.csv")
    df.to_csv(out_path, index=False)
    return out_path


def main():
    raw_input = input("Paste a FRED URL or series ID: ").strip()
    if not raw_input:
        print("Nothing entered — exiting.")
        sys.exit(0)

    try:
        series_id = extract_series_id(raw_input)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Let the user name the output column / file (defaults to series ID)
    suggested = series_id.lower()
    name_input = input(f"Variable name for CSV column and filename [{suggested}]: ").strip()
    out_name = name_input if name_input else suggested

    try:
        start, end = prompt_dates()
    except ValueError:
        print("Invalid date format — use YYYY-MM-DD.")
        sys.exit(1)

    try:
        out_path = download_series(series_id, start, end, out_name)
        print(f"Saved → {os.path.relpath(out_path)}")
    except Exception as e:
        print(f"Download failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
