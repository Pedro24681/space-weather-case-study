import pandas as pd
from datetime import datetime


def load_kp_index_data(file_path):
    """Load Kp index data from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing Kp index data.

    Returns:
        pd.DataFrame: A DataFrame containing the Kp index data.
    """    
    return pd.read_csv(file_path)


def filter_storm_events(df, threshold=5):
    """Filter storm events based on the Kp index threshold.

    Args:
        df (pd.DataFrame): DataFrame containing the Kp index data.
        threshold (int): The threshold for storm events. Default is 5.

    Returns:
        pd.DataFrame: A DataFrame containing only storm events where the Kp index is above the threshold.
    """    
    return df[df['Kp'] > threshold]


def convert_timestamps_to_datetime(df, timestamp_col='Timestamp'):
    """Convert timestamp strings to datetime objects in the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing the Kp index data.
        timestamp_col (str): The name of the column containing timestamp data. Default is 'Timestamp'.

    Returns:
        pd.DataFrame: A DataFrame with the timestamp column converted to datetime objects.
    """    
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])
    return df