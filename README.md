Data Pipeline Project

A lightweight ETL (Extract–Transform–Load) pipeline written in Python that ingests raw e-commerce sales data, cleans and validates it, computes business aggregates, and loads the results into both a SQLite database and a summary CSV.

 📌 Overview

This project simulates a real-world data pipeline used by analytics teams to turn messy transactional data into clean, queryable datasets.

Pipeline stages:
1. Extract — reads raw sales records from `data/raw_sales.csv`
2. Transform — cleans data, handles missing values, removes duplicates, validates types, and computes aggregates (revenue per product, per region, monthly totals)
3. Load — writes cleaned records to a SQLite database (`output/sales.db`) and exports aggregate summaries to `output/summary.csv`

 🛠️ Tools & Technologies

- Language: Python 3.10+
- Libraries: Pandas, SQLite3 (standard library), unittest (standard library)
- Concepts: ETL design, data validation, unit testing, modular architecture

 🚀 How to Run

```bash
 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/data-pipeline-project.git
cd data-pipeline-project

 2. Install dependencies
pip install -r requirements.txt

 3. Run the pipeline
python -m pipeline.main
