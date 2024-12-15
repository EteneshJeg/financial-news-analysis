import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

def load_data(filepath):
    return pd.read_csv(filepath)

def calculate_headline_length(df):
    df['headline_length'] = df['headline'].apply(len)
    return df

def perform_sentiment_analysis(df):
    """
    Perform sentiment analysis on the 'headline' column of the DataFrame.
    """
    if "headline" not in df.columns:
        raise ValueError("Input DataFrame must contain a 'headline' column.")

    df["sentiment"] = df["headline"].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df

