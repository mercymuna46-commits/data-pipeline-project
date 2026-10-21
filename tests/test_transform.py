"""Unit tests for the transform stage."""
import unittest

import pandas as pd

from pipeline.transform import transform_data


class TestTransform(unittest.TestCase):

    def setUp(self):
        self.raw = pd.DataFrame({
            "order_id": [1, 1, 2, 3],
            "date": ["2024-01-01", "2024-01-01", None, "2024-02-01"],
            "product": ["A", "A", "B", "C"],
            "region": ["north", "north", "South", None],
            "quantity": [2, 2, 3, 1],
            "unit_price": [10.0, 10.0, 5.0, 20.0],
            "customer_email": ["x@x.com"] * 4,
        })

    def test_duplicates_removed(self):
        clean, _ = transform_data(self.raw)
        self.assertEqual(len(clean), 2)  # row 1 deduped, rows 2 & 3 dropped (missing fields)

    def test_revenue_calculated(self):
        clean, _ = transform_data(self.raw)
        self.assertIn("revenue", clean.columns)
        self.assertTrue((clean["revenue"] == clean["quantity"] * clean["unit_price"]).all())

    def test_region_normalized(self):
        clean, _ = transform_data(self.raw)
        self.assertTrue(clean["region"].str.istitle().all())

    def test_summary_dimensions(self):
        _, summary = transform_data(self.raw)
        self.assertEqual(set(summary["dimension"]), {"product", "region", "month"})


if __name__ == "__main__":
    unittest.main()
