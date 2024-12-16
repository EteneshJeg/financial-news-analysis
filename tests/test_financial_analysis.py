import unittest
import pandas as pd
from src.financial_analysis import calculate_technical_indicators, calculate_financial_metrics

class TestFinancialAnalysis(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "Date": pd.date_range(start="2023-01-01", periods=100),
            "Open": [100 + i for i in range(100)],
            "High": [105 + i for i in range(100)],
            "Low": [95 + i for i in range(100)],
            "Close": [100 + i for i in range(100)],
            "Volume": [1000 + i for i in range(100)],
        })
        self.data.set_index("Date", inplace=True)

    def test_calculate_technical_indicators(self):
        result = calculate_technical_indicators(self.data)
        self.assertIn("SMA_20", result.columns)
        self.assertIn("RSI", result.columns)
        self.assertIn("MACD", result.columns)

    def test_calculate_financial_metrics(self):
        result = calculate_financial_metrics(self.data)
        self.assertIn("Daily Returns", result.columns)
