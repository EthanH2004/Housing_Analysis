import json
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


BASE_DIR = Path(__file__).resolve().parents[1]
CLEANED_DATA_PATH = BASE_DIR / "data" / "processed" / "cleaned_housing.csv"
RESULTS_PATH = BASE_DIR / "outputs" / "model_results.json"
FEATURE_COLUMNS = ["interest_rate", "unemployment_rate"]
TARGET_COLUMN = "price"


def load_cleaned_data(csv_path: Path = CLEANED_DATA_PATH) -> pd.DataFrame:
    """Load cleaned housing data for modeling."""
    return pd.read_csv(csv_path)


def train_model(df: pd.DataFrame) -> dict:
    """Fit a linear regression model and capture metrics."""
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)

    results = {
        "intercept": float(model.intercept_),
        "coefficients": {
            feature: float(coefficient)
            for feature, coefficient in zip(FEATURE_COLUMNS, model.coef_)
        },
        "r2": float(r2_score(y, predictions)),
    }
    return results


def save_results(results: dict, output_path: Path = RESULTS_PATH) -> Path:
    """Save model results to the outputs directory."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)
    return output_path


def main() -> None:
    df = load_cleaned_data()
    results = train_model(df)
    output_path = save_results(results)

    print("Linear regression results:")
    print(f"Intercept: {results['intercept']:.4f}")
    for feature, coefficient in results["coefficients"].items():
        print(f"{feature}: {coefficient:.4f}")
    print(f"R^2: {results['r2']:.4f}")
    print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
