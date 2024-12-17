import os
from src.data_processing import generate_news_data,generate_stock_data,save_csv

# Define file paths
news_file_path = "../data/news.csv"  # Save in the root or data folder
stock_file_path = "../data/stock_prices.csv"

def main():
    """Main script to generate and save sample datasets."""
    print("Generating sample news and stock price data...")

    # Generate datasets
    news_df = generate_news_data()
    stock_df = generate_stock_data()

    # Save to CSV
    save_csv(news_df, news_file_path)
    save_csv(stock_df, stock_file_path)

    print(f"Sample news data saved to {news_file_path}")
    print(f"Sample stock price data saved to {stock_file_path}")

if __name__ == "__main__":
    main()
