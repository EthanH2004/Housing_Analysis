import sys
sys.path.insert(0, "src")
import runpy
import nbformat
import matplotlib
from fetch_fred import run as fetch_fred

# settings — add new FRED IDs here to include them automatically
START = "1984-01-01"
END   = "2025-12-01"
IDS = {
    "MSPUS":         "HomePrice",             # quarterly, starts 1963
    "CPIAUCSL":      "CPI",                   # monthly, starts 1947
    "UNRATE":        "UnemploymentRate",      # monthly, starts 1948
    "MORTGAGE30US":  "MortgageRate",          # weekly, starts 1971
    "MEHOINUSA646N": "MedianHouseholdIncome", # annual, starts 1984
    "POPTHM":        "Population",            # monthly, starts 1959
    "HOUST":         "HousingStarts",         # monthly, starts 1959
}

fetch_fred(IDS, START, END)                   # download from FRED
runpy.run_path("src/resampler.py")            # standardize to monthly
runpy.run_path("src/merge_data.py")           # merge into one dataset
runpy.run_path("src/calculate_real_price.py") # inflation-adjust home price
runpy.run_path("src/model.py")                # run regression

matplotlib.use("Agg")                         # run matplotlib script 
with open("src/InspectBook.ipynb") as f:
    nb = nbformat.read(f, as_version=4)
ns = {}
for cell in nb.cells:
    if cell.cell_type == "code":
        exec(cell.source, ns)
        matplotlib.pyplot.close("all")
print("Saved charts to outputs/charts/")
