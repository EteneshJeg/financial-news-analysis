from src.financial_analysis import load_stock_data, calculate_technical_indicators, calculate_financial_metrics
from src.sentiment_analysis import load_data, perform_sentiment_analysis
import matplotlib.pyplot as plt

# Load Data
stock_data = load_stock_data("data/stock_data.csv")

# Calculate Indicators
stock_data = calculate_technical_indicators(stock_data)
stock_data = calculate_financial_metrics(stock_data)

# Visualize Indicators
plt.figure(figsize=(10, 5))
plt.plot(stock_data.index, stock_data["Close"], label="Close Price")
plt.plot(stock_data.index, stock_data["SMA_20"], label="SMA 20-day")
plt.legend()
plt.show()
