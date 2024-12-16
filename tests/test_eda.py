import unittest
import pandas as pd
from src.sentiment_analysis import perform_sentiment_analysis, calculate_headline_length

class TestEDA(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            "headline": ["Stock prices rise", "Market crashes", "Neutral news"]
        })

    def test_perform_sentiment_analysis(self):
        result = perform_sentiment_analysis(self.sample_data)
        self.assertIn("sentiment", result.columns)
        self.assertTrue(pd.api.types.is_numeric_dtype(result["sentiment"]))

    def test_calculate_headline_length(self):
        result = calculate_headline_length(self.sample_data)
        self.assertIn("headline_length", result.columns)  # Ensure the column exists
        expected_lengths = self.sample_data["headline"].apply(len)  # Calculate length of headlines
        # Ignore the name attribute while comparing
        pd.testing.assert_series_equal(result["headline_length"], expected_lengths, check_dtype=True, check_names=False)
