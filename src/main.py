import sys
sys.path.insert(0, "src")
import runpy
from fetch_fred import run as fetch_fred

# SETTINGS
# Add new FRED IDs to list and they'll be included automatically!!!
START = "2015-01-01"
END   = "2025-12-01"
IDS = {
    "CPIAUCSL":            "CPI",
    "TXUR":                "UnemploymentRate",
    "MORTGAGE30US":        "MortgageRate",
    "TXUCSFRCONDOSMSAMID": "HomePrice",
    "MEHOINUSTXA646N":     "MedianHouseholdIncome",
    "TXPOP":               "Population",
    "HOUST":               "HousingStarts",
}

fetch_fred(IDS, START, END)                    # download all series from FRED
runpy.run_path("src/resample_mortgage.py")     # average weekly mortgage to monthly
runpy.run_path("src/merge_data.py")            # join all raw files into one dataset
runpy.run_path("src/calculate_real_price.py")  # adjust housing price for inflation
runpy.run_path("src/model.py")                 # run linear regression and save results
