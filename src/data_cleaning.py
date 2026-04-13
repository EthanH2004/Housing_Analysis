from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "texas_housing.csv"
CLEANED_DATA_PATH = BASE_DIR / "data" / "processed" / "cleaned_housing.csv"
REQUIRED_COLUMNS = ["price", "interest_rate", "unemployment_rate"]


def load_data(csv_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw housing dataset and validate required columns."""
    df = pd.read_csv(csv_path)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    return df[REQUIRED_COLUMNS].copy()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Convert to numeric values and impute missing values with column medians."""
    cleaned_df = df.copy()
    for column in REQUIRED_COLUMNS:
        cleaned_df[column] = pd.to_numeric(cleaned_df[column], errors="coerce")
        cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].median())
    return cleaned_df


def save_cleaned_data(df: pd.DataFrame, output_path: Path = CLEANED_DATA_PATH) -> Path:
    """Persist the cleaned dataset to disk."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path


def main() -> None:
    df = load_data()
    cleaned_df = clean_data(df)
    output_path = save_cleaned_data(cleaned_df)
    print(f"Cleaned data saved to {output_path}")


if __name__ == "__main__":
    main()
