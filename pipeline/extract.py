"""Extract stage: read raw data from source."""
import pandas as pd


def extract_data(filepath: str) -> pd.DataFrame:
    """Read raw sales CSV into a DataFrame.

    Args:
        filepath: Path to the raw CSV file.

    Returns:
        Raw DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty.
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {filepath}")

    if df.empty:
        raise ValueError("Source file is empty.")

    print(f"[EXTRACT] Loaded {len(df)} raw records from {filepath}")
    return df
