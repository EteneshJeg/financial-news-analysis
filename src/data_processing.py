import pandas as pd
from datetime import datetime, timedelta
import random

def generate_news_data():
    """Generates a sample news dataset with headlines and dates."""
    news_dates = [datetime(2024, 6, 1) + timedelta(days=i) for i in range(10)]
    headlines = [
        "Stock prices surge after positive economic report",
        "Tech companies show growth in Q2 earnings",
        "Market dips amid inflation concerns",
        "Oil prices rise as demand increases",
        "Federal Reserve hints at interest rate hike",
        "Stock markets rally after job report",
        "Investors cautious amid global tensions",
        "Pharma stocks soar on FDA approval",
        "Energy sector outperforms expectations",
        "Automotive industry faces supply chain issues",
    ]
    news_data = {"Date": news_dates, "Headline": random.choices(headlines, k=10)}
    return pd.DataFrame(news_data)

def generate_stock_data():
    """Generates a sample stock price dataset with dates and closing prices."""
    stock_dates = [datetime(2024, 6, 1) + timedelta(days=i) for i in range(10)]
    close_prices = [100 + random.uniform(-3, 3) * i for i in range(10)]
    stock_data = {"Date": stock_dates, "Close": close_prices}
    return pd.DataFrame(stock_data)

def save_csv(dataframe, file_path):
    """Saves a DataFrame to a CSV file."""
    dataframe.to_csv(file_path, index=False)
