import unittest
from src.eda import calculate_headline_length, perform_sentiment_analysis
import pandas as pd

class TestEDA(unittest.TestCase):
    def test_calculate_headline_length(self):
        data = {'headline': ['short', 'a bit longer']}
        df = pd.DataFrame(data)
        df = calculate_headline_length(df)
        self.assertEqual(df['headline_length'].iloc[0], 5)

    def test_perform_sentiment_analysis(self):
        data = {'headline': ['great profit', 'bad loss']}
        df = pd.DataFrame(data)
        df = perform_sentiment_analysis(df)
        self.assertGreater(df['sentiment'].iloc[0], 0)

if __name__ == '__main__':
    unittest.main()
