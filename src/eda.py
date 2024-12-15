import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def load_data(filepath):
    return pd.read_csv(filepath)

def calculate_headline_length(df):
    df['headline_length'] = df['headline'].apply(len)
    return df

def perform_sentiment_analysis(df):
    sia = SentimentIntensityAnalyzer()
    df['sentiment'] = df['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
    return df
