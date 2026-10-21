"""Load stage: persist cleaned data and summaries."""
import os
import sqlite3

import pandas as pd


def load_data(clean_df: pd.DataFrame, summary_df: pd.DataFrame,
              db_path: str = "output/sales.db",
              summary_path: str = "output/summary.csv") -> None:
    """Write cleaned records to SQLite and summary to CSV."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # --- Load to SQLite ---
    conn = sqlite3.connect(db_path)
    try:
        clean_df.to_sql("clean_sales", conn, if_exists="replace", index=False)
        print(f"[LOAD] Wrote {len(clean_df)} rows to table 'clean_sales' in {db_path}")
    finally:
        conn.close()

    # --- Export summary CSV ---
    summary_df.to_csv(summary_path, index=False)
    print(f"[LOAD] Wrote summary ({len(summary_df)} rows) to {summary_path}")
