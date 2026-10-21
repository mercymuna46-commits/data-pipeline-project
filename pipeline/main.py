"""Entry point — orchestrates the ETL pipeline."""
from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data

RAW_PATH = "data/raw_sales.csv"


def run_pipeline() -> None:
    """Run the full extract-transform-load pipeline."""
    print("=" * 50)
    print("Starting data pipeline...")
    print("=" * 50)

    raw_df = extract_data(RAW_PATH)
    clean_df, summary_df = transform_data(raw_df)
    load_data(clean_df, summary_df)

    print("=" * 50)
    print("Pipeline completed successfully.")
    print("=" * 50)


if __name__ == "__main__":
    run_pipeline()
