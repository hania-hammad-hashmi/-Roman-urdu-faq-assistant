"""
load_data.py
Loads the FAQ dataset from a CSV file and returns it as a pandas DataFrame.
"""

import pandas as pd


def load_faq_data(filepath):
    """
    Reads the FAQ CSV file and returns it as a pandas DataFrame.
    filepath: path to the CSV file (must have columns: question, category, answer)
    returns: pandas DataFrame with the loaded data
    """
    df = pd.read_csv(filepath)
    return df


if __name__ == "__main__":
    data = load_faq_data("data/sample_data.csv")
    print("Number of rows loaded:", len(data))
    print(data.head())
