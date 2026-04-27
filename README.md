# U.S. Housing Market Analysis
**ISQS 3358 – Spring 2026 | Texas Tech University**

A regression study on what economic factors drive real U.S. home prices from 1984 to 2025. Data is pulled automatically from FRED, cleaned, and used to train a linear regression model.

---

## Findings

The model achieved an **R² of 0.8775**, meaning it explains about 88% of the variation in inflation-adjusted home prices. Median household income had the strongest positive effect on home prices, which makes sense — as people earn more, they can afford more. Mortgage rate and unemployment rate both had negative effects, with higher rates and unemployment pushing prices down. Housing starts (supply) also played a role, with more construction putting downward pressure on prices.

---

## Data

All pulled from [FRED](https://fred.stlouisfed.org/). The dataset runs **January 1984 – December 2025**.

| Variable | FRED ID | Description | Frequency |
|---|---|---|---|
| `HomePrice` | MSPUS | Median U.S. home sale price | Quarterly |
| `CPI` | CPIAUCSL | Consumer Price Index (for inflation adjustment) | Monthly |
| `MortgageRate` | MORTGAGE30US | 30-year fixed mortgage rate | Weekly |
| `UnemploymentRate` | UNRATE | U.S. unemployment rate | Monthly |
| `MedianHouseholdIncome` | MEHOINUSA646N | U.S. median household income | Annual |
| `Population` | POPTHM | U.S. total population | Monthly |
| `HousingStarts` | HOUST | New housing construction starts | Monthly |

**Target:** `RealPrice` = `HomePrice / CPI × 100` (inflation-adjusted)

Weekly and annual series are automatically resampled to monthly. Missing values are forward-filled.

---

## How It Works

Running `main.py` executes the full pipeline:

1. Downloads every FRED series listed in `IDS` to `data/raw/`
2. Resamples weekly/annual data to monthly
3. Merges all series into one dataset
4. Calculates the inflation-adjusted real price
5. Runs linear regression and saves results to `outputs/regression/`
6. Generates all charts and saves them to `outputs/charts/`

**To add a new variable**, just add a line to the `IDS` dict in `main.py`:
```python
IDS = {
    "MSPUS": "HomePrice",
    "FEDFUNDS": "FedFundsRate",  # ← new variable, that's it
    ...
}
```
Everything else — downloading, merging, modeling — picks it up automatically.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

---

## Project Structure

```
src/
├── main.py                 # run this
├── fetch_fred.py           # downloads data from FRED
├── resampler.py            # standardizes all series to monthly
├── merge_data.py           # merges raw files into one dataset
├── calculate_real_price.py # inflation-adjusts home prices
├── model.py                # linear regression + saves results
└── InspectBook.ipynb       # charts and exploration
outputs/
├── charts/                 # all generated plots (.png)
└── regression/             # predictions.csv and results.txt
```
