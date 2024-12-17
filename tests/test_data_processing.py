import os
import pandas as pd
from src.data_processing import generate_news_data, generate_stock_data, save_csv

def test_generate_news_data():
    df = generate_news_data()
    assert not df.empty, "News DataFrame should not be empty"
    assert "Date" in df.columns and "Headline" in df.columns, "Columns should be Date and Headline"

def test_generate_stock_data():
    df = generate_stock_data()
    assert not df.empty, "Stock DataFrame should not be empty"
    assert "Date" in df.columns and "Close" in df.columns, "Columns should be Date and Close"

def test_save_csv():
    df = pd.DataFrame({"Col1": [1, 2], "Col2": [3, 4]})
    test_file_path = "test_file.csv"
    save_csv(df, test_file_path)
    assert os.path.exists(test_file_path), "CSV file should exist after saving"
    os.remove(test_file_path)
