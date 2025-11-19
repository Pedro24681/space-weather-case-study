# Source Code Folder (src/)

This folder contains reusable Python modules and scripts for your space weather analysis.



## What Goes Here?

This folder is for **reusable code** that you'll use across multiple notebooks. Instead of copying the same code into every notebook, you create functions here and import them.

### Examples of what to put in `src/`:
- **data_loader.py** - Functions to load and preprocess datasets
- **plotting.py** - Custom visualization functions
- **analysis.py** - Statistical analysis functions
- **utils.py** - Helper functions (date conversions, calculations)



## Why Use a src/ Folder?

### Benefits:
1. **Don't Repeat Yourself (DRY)** - Write code once, use it everywhere
2. **Easier to maintain** - Fix a bug in one place, not in 10 notebooks
3. **Cleaner notebooks** - Focus on analysis, not implementation details
4. **Professional structure** - This is how real projects are organized



## Example: data_loader.py

```python
"""
Data loading utilities for space weather analysis
"""
import pandas as pd

def load_kp_data(filepath='../data/Space_Weather_Indices_Subset.csv'):
    """
    Load and preprocess Kp index data
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Processed dataframe with datetime index
    """
    df = pd.read_csv(filepath)
    df['Time (UTC)'] = pd.to_datetime(df['Time (UTC)'], format='%d-%m-%Y %H:%M')
    df = df.set_index('Time (UTC)')
    return df

def filter_storm_events(df, kp_threshold=5):
    """
    Filter dataframe for storm events above threshold
    
    Args:
        df (pd.DataFrame): Kp index dataframe
        kp_threshold (float): Minimum Kp value
        
    Returns:
        pd.DataFrame: Filtered dataframe
    """
    return df[df['median'] >= kp_threshold]
```



## Example: plotting.py

```python
"""
Visualization utilities for space weather data
"""  
import matplotlib.pyplot as plt
import seaborn as sns

def plot_kp_timeseries(df, title='Kp Index Over Time'):
    """
    Create a time series plot of Kp index
    
    Args:
        df (pd.DataFrame): Kp index dataframe
        title (str): Plot title
        
    Returns:
        matplotlib.figure.Figure: The created figure
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df.index, df['median'], marker='o', linewidth=2)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('Time (UTC)', fontsize=12)
    ax.set_ylabel('Kp Index', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig
```



## How to Use These Modules

In your Jupyter notebooks, import your custom functions:

```python
# Add src/ to Python path (run once at top of notebook)
import sys
sys.path.append('../src')

# Now import your modules
from data_loader import load_kp_data, filter_storm_events
from plotting import plot_kp_timeseries

# Use your functions
df = load_kp_data()
storms = filter_storm_events(df, kp_threshold=6)
fig = plot_kp_timeseries(storms, title='Strong Geomagnetic Storms')
```



## Best Practices

### 1. Use Docstrings
Always document your functions:
```python
def my_function(param1, param2):
    """
    Brief description of what the function does
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
        
    Returns:
        type: Description of return value
    """
    # Your code here
    return result
```

### 2. Follow Naming Conventions
- **Files:** lowercase with underscores (`data_loader.py`)
- **Functions:** lowercase with underscores (`load_kp_data()`)  
- **Classes:** CapitalizedWords (`DataProcessor`)
- **Constants:** UPPERCASE (`MAX_KP_VALUE = 9`)

### 3. Keep Functions Focused
Each function should do ONE thing well.

### 4. Write Tests (Advanced)
Later, you can add a `tests/` folder to test your functions.



## Getting Started

For now, this folder is empty - that's OK! As you write notebooks, you'll notice patterns:
- "I'm copying this code a lot..."
- "This function would be useful in multiple places..."

That's when you create a new module in `src/`!



## When You're Ready

Start with these modules:
1. **data_loader.py** - Load all your datasets
2. **plotting.py** - Common visualization functions
3. **analysis.py** - Statistical calculations

---

**Status:** Empty (to be populated as project grows)  
**Last Updated:** 2025-11-13
