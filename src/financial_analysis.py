import pandas as pd
import talib

def load_stock_data(filepath):
    df = pd.read_csv(filepath, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return df

def calculate_technical_indicators(df):
    df["SMA_20"] = talib.SMA(df["Close"], timeperiod=20)
    df["RSI"] = talib.RSI(df["Close"], timeperiod=14)
    macd, signal, hist = talib.MACD(df["Close"])
    df["MACD"] = macd
    df["Signal"] = signal
    df["Histogram"] = hist
    return df

def calculate_financial_metrics(df):
    # Calculate daily returns using pandas
    df["Daily Returns"] = df["Close"].pct_change()
    return df[["Daily Returns"]]
