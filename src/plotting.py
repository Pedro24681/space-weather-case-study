import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_kp_timeseries(dataframe: pd.DataFrame) -> plt.Figure:
    """
    Plots a time series of Kp index values.
    
    Parameters:
    dataframe (pd.DataFrame): DataFrame containing 'timestamp' and 'kp' columns.
    
    Returns:
    plt.Figure: Matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dataframe['timestamp'], dataframe['kp'], marker='o', linestyle='-', color='b')
    ax.set_title('Kp Index Time Series')
    ax.set_xlabel('Time')
    ax.set_ylabel('Kp Index')
    ax.grid(True)
    plt.xticks(rotation=45)
    return fig


def plot_kp_distribution(dataframe: pd.DataFrame) -> plt.Figure:
    """
    Plots the distribution of Kp index values using a histogram.
    
    Parameters:
    dataframe (pd.DataFrame): DataFrame containing 'kp' column.
    
    Returns:
    plt.Figure: Matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(dataframe['kp'], bins=10, kde=True, color='c', ax=ax)
    ax.set_title('Kp Index Distribution')
    ax.set_xlabel('Kp Index')
    ax.set_ylabel('Frequency')
    return fig


def plot_probability_analysis(dataframe: pd.DataFrame, threshold: float) -> plt.Figure:
    """
    Plots probability analysis of Kp index values.
    
    Parameters:
    dataframe (pd.DataFrame): DataFrame containing 'kp' column.
    threshold (float): Kp threshold for which to calculate probability.
    
    Returns:
    plt.Figure: Matplotlib figure object.
    """
    fraction_above_threshold = (dataframe['kp'] > threshold).mean()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(['Above Threshold', 'Below Threshold'], [fraction_above_threshold, 1 - fraction_above_threshold], color=['g', 'r'])
    ax.set_title(f'Probability Analysis for Kp > {threshold}')
    ax.set_ylabel('Proportion')
    return fig

