import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




import unittest
import pandas as pd
from src.sentiment_analysis import perform_sentiment_analysis

class TestEDA(unittest.TestCase):
    def setUp(self):
        """Set up a sample dataset for testing."""
        self.sample_data = pd.DataFrame({
            "headline": ["Stock prices rise", "Market crashes", "Neutral news"]
        })

    def test_perform_sentiment_analysis(self):
        """Test sentiment analysis functionality."""
        result = perform_sentiment_analysis(self.sample_data)
        # Check if the 'sentiment' column is added
        self.assertIn("sentiment", result.columns)
        # Check if the sentiment values are numeric
        self.assertTrue(pd.api.types.is_numeric_dtype(result["sentiment"]))
