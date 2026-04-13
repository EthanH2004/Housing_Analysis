# Texas Housing Price Analysis

This project analyzes how economic factors influence housing prices in Texas using linear regression.

The goal is to understand how variables such as interest rates and unemployment rates impact housing prices, and to quantify their effect.

## Project Overview

The pipeline follows a simple workflow:

1. Load raw housing data
2. Clean and preprocess the dataset
3. Fit a linear regression model
4. Evaluate model performance (R² and coefficients)
5. Save results for analysis

## Structure

* `data/raw/` — raw input data (e.g. `texas_housing.csv`)
* `data/processed/` — cleaned datasets
* `notebooks/eda.ipynb` — exploratory analysis and visualization
* `src/data_cleaning.py` — handles missing values and prepares data
* `src/model.py` — runs regression and outputs results
* `outputs/` — saved model results

## Expected Input

Place a CSV file at:

```
data/raw/texas_housing.csv
```

With the following columns:

* `price` — housing price
* `interest_rate` — mortgage or market interest rate
* `unemployment_rate` — unemployment percentage

## Setup

Install dependencies:

```
pip install -r requirements.txt
```

## Run

```
python src/data_cleaning.py
python src/model.py
```

## Output

* Cleaned dataset:

```
data/processed/cleaned_housing.csv
```

* Model results:

```
outputs/model_results.json
```

These results include:

* regression coefficients (impact of each variable)
* R² score (model fit quality)