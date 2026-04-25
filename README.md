# Texas Housing Market Analysis
**ISQS 3358 – Spring 2026 | Final Project**

We analyze what economic factors drive real housing prices in Texas from 2015 to 2025. All data is pulled automatically from FRED (Federal Reserve Economic Data) and merged into a single clean dataset used to train a linear regression model.

---

## Datasets

| Variable | FRED Series | Description | Frequency |
|---|---|---|---|
| `HomePrice` | TXUCSFRCONDOSMSAMID | Texas median home sale price (dollars) | Monthly |
| `CPI` | CPIAUCSL | Consumer Price Index – used to inflation-adjust prices | Monthly |
| `MortgageRate` | MORTGAGE30US | 30-year fixed mortgage rate (%) | Weekly → Monthly avg |
| `UnemploymentRate` | TXUR | Texas unemployment rate (%) | Monthly |
| `MedianHouseholdIncome` | MEHOINUSTXA646N | Texas median household income (dollars) | Annual → Monthly fill |
| `Population` | TXPOP | Texas population (thousands) | Annual → Monthly fill |
| `HousingStarts` | HOUST | National new housing construction starts (thousands) | Monthly |

**Target variable:** `REALPRICE` — inflation-adjusted home price calculated as `HomePrice / CPI × 100`

---

## Project Structure

```
Housing_Analysis/
├── src/
│   ├── main.py                 # Run this — executes the full pipeline
│   ├── fetch_fred.py           # Downloads all series from FRED
│   ├── resample_mortgage.py    # Standardizes all series to monthly frequency
│   ├── merge_data.py           # Joins all raw files into one dataset
│   ├── calculate_real_price.py # Adjusts home prices for inflation
│   └── model.py                # Linear regression + saves results
├── data/
│   ├── raw/                    # Downloaded CSVs (one per FRED series)
│   └── processed/
│       ├── merged_data.csv     # All series joined on DATE
│       └── final_dataset.csv   # Cleaned dataset used for modeling
├── outputs/
│   ├── predictions.csv         # Actual vs predicted REALPRICE
│   └── results.txt             # R², MSE, and model coefficients
├── notebooks/
│   └── InspectBook.ipynb       # Scratch notebook for exploration
├── final_proj_undergrad.pdf    # Project requirements
└── requirements.txt
```

---

## Setup

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt
```

## Running the Pipeline

```bash
python src/main.py
```

This will:
1. Download all FRED series to `data/raw/`
2. Standardize everything to monthly frequency
3. Merge into `data/processed/merged_data.csv`
4. Calculate inflation-adjusted price → `data/processed/final_dataset.csv`
5. Train and evaluate a linear regression model
6. Save outputs to `outputs/`

To add a new FRED variable, add its series ID and a name to the `IDS` dict in `src/main.py` — everything else updates automatically.

---

## Data Notes

- **Missing values** (e.g. October 2025 government shutdown) are forward-filled with the previous month's value.
- **Weekly → Monthly:** Mortgage rate is averaged across all weeks in each month.
- **Annual → Monthly:** Household income and population are forward-filled from their yearly values since FRED only publishes them once per year. The latest income figure is 2024 (Census Bureau hasn't released 2025 yet).
