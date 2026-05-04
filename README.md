# U.S. Housing Market Analysis
**ISQS 3358 – Spring 2026 | Texas Tech University**

Samuel Melghem · Omar Hernandez · Ryan Rhodes · Ethan Hennenhoefer · Logan Crider

A regression study on what economic factors drive real U.S. home prices from 1984 to 2025. Data is pulled automatically from FRED, cleaned, merged, and used to train a linear regression model.

---

## Findings

The model achieved an **R² of 0.8775**, meaning it explains about 88% of the variation in inflation-adjusted home prices across 40 years of data.

**Key results:**
- **Mortgage rate** had the strongest negative effect — every 1% increase in the 30-year rate corresponds to roughly an $847 drop in real home price. The four-decade decline from 14% to 3% quietly subsidized price growth the entire time.
- **Unemployment rate** also had a strong negative effect — job losses reduce buying power and force distressed selling. The 2008 crash shows this clearly.
- **Median household income** had the strongest positive effect — as earnings grow, buyers qualify for larger mortgages and bid prices higher.
- **Population** and **housing starts** both had small positive effects.

**Affordability:** The price-to-income ratio more than doubled from 1984 to 2025 — from roughly 3.5× to over 7× median annual income. Nominal prices rose ~5×, but inflation-adjusted real prices rose about 2×. Inflation accounts for most of the apparent price explosion.

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

**Target variable:** `RealPrice` = `HomePrice / CPI × 100` (inflation-adjusted home price)

Weekly data is averaged to monthly. Annual data is forward-filled month-to-month. Missing values are forward-filled after merging.

---

## How It Works

Running `main.py` executes the full pipeline in one command:

1. Downloads every FRED series listed in `IDS` to `data/raw/`
2. Resamples weekly/annual data to monthly
3. Merges all series into one dataset
4. Calculates the inflation-adjusted real price
5. Runs linear regression and saves results to `outputs/regression/`
6. Generates all charts and saves them to `outputs/charts/`

**To add a new variable**, add one line to the `IDS` dict in `main.py`:
```python
IDS = {
    "MSPUS": "HomePrice",
    "FEDFUNDS": "FedFundsRate",  # ← new variable, that's it
    ...
}
```
Everything else — downloading, merging, modeling, charting — picks it up automatically.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

---

## Outputs

| File | Description |
|---|---|
| `outputs/regression/results.txt` | Coefficients, R², MSE |
| `outputs/regression/predictions.csv` | Actual vs. predicted for every month |
| `outputs/charts/*.png` | All generated charts |
| `outputs/housing_analysis.pptx` | Final presentation slides |
| `outputs/presentation_script.docx` | Speaker script (outline + word-for-word) |

---

## Project Structure

```
src/
├── main.py                 # run this — executes the full pipeline
├── fetch_fred.py           # downloads data from FRED
├── resampler.py            # standardizes all series to monthly
├── merge_data.py           # merges raw files into one dataset
├── calculate_real_price.py # inflation-adjusts home prices
├── model.py                # linear regression + saves results
└── InspectBook.ipynb       # charts and exploratory analysis
outputs/
├── charts/                 # all generated plots (.png)
├── regression/             # predictions.csv and results.txt
├── housing_analysis.pptx   # presentation slides
└── presentation_script.docx # speaker script
```
