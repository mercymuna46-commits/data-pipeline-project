"""Transform stage: clean, validate, and aggregate data."""
import pandas as pd


def transform_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Clean raw sales data and produce aggregate summaries.

    Steps:
        1. Remove exact duplicate rows.
        2. Drop rows missing critical fields (date, region, unit_price).
        3. Cast columns to correct types.
        4. Compute a `revenue` column.
        5. Build aggregate summaries.

    Returns:
        (clean_df, summary_df)
    """
    original_count = len(df)

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Drop rows with missing critical values
    critical_cols = ["date", "region", "unit_price"]
    df = df.dropna(subset=critical_cols)

    # 3. Type casting
    df["date"] = pd.to_datetime(df["date"])
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].astype(float)
    df["region"] = df["region"].astype(str).str.strip().str.title()
    df["product"] = df["product"].astype(str).str.strip()

    # 4. Revenue column
    df["revenue"] = (df["quantity"] * df["unit_price"]).round(2)

    # 5. Aggregates
    by_product = (
        df.groupby("product")["revenue"]
        .sum()
        .reset_index()
        .rename(columns={"revenue": "total_revenue"})
        .assign(dimension="product")
    )
    by_region = (
        df.groupby("region")["revenue"]
        .sum()
        .reset_index()
        .rename(columns={"revenue": "total_revenue"})
        .assign(dimension="region")
    )
    by_month = (
        df.assign(month=df["date"].dt.to_period("M").astype(str))
        .groupby("month")["revenue"]
        .sum()
        .reset_index()
        .rename(columns={"revenue": "total_revenue"})
        .assign(dimension="month")
    )
    # Normalize column names for a single summary table
    by_product = by_product.rename(columns={"product": "category"})
    by_region = by_region.rename(columns={"region": "category"})
    by_month = by_month.rename(columns={"month": "category"})

    summary = pd.concat([by_product, by_region, by_month], ignore_index=True)

    print(f"[TRANSFORM] Cleaned {original_count} -> {len(df)} records")
    return df.reset_index(drop=True), summary
