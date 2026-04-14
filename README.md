# Texas Housing Price Analysis

This project studies how economic factors relate to Texas housing prices using a simple linear regression model.

The analysis combines housing price data with CPI, interest rate, and unemployment data, calculates inflation-adjusted home prices, and fits a model using `scikit-learn`.

## Project Workflow

The project runs in three simple steps:

1. Merge the raw datasets into one file
2. Calculate real housing prices using CPI
3. Train a linear regression model and save the results

## Project Structure

* `data/raw/` - raw source files
* `data/processed/merged_data.csv` - merged dataset
* `data/processed/final_dataset.csv` - final cleaned dataset used for modeling
* `src/merge_data.py` - merges the raw CSV files
* `src/calculate_real_price.py` - calculates `RealPrice`
* `src/model.py` - trains the regression model and saves outputs
* `src/main.py` - runs the full pipeline
* `outputs/predictions.csv` - actual vs predicted values
* `outputs/results.txt` - model summary
* `notebooks/InspectBook.ipynb` - notebook for exploration

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## How To Run

Run the full pipeline from the project root:

```bash
python src/main.py
```

This will:

* create `data/processed/merged_data.csv`
* create `data/processed/final_dataset.csv`
* train the linear regression model
* save prediction output to `outputs/predictions.csv`
* save model metrics to `outputs/results.txt`

## Model

The model uses:

* Features: `InterestRate`, `UnemploymentRate`
* Target: `RealPrice`

It reports:

* regression coefficients
* intercept
* `R^2`
* mean squared error (`MSE`)

## Notes

The CPI and unemployment rate values for `10/1/2025` were missing due to the government shutdown.

To keep the dataset complete, the missing values were filled using the previous month's values with a carry-forward method.

This affects the data files:

* `data/raw/cpi.csv`
* `data/raw/unemployment_rate.csv`

## Future Improvements

Possible next variables to add:

* mortgage rates
* income
* population
* additional economic indicators
