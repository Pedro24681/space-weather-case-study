# Outputs Folder

This folder stores generated visualizations, processed datasets, and analysis results.



## What Goes Here?

### Visualizations:
- **figures/** - All plots and charts (PNG, JPG, PDF)
- **interactive/** - Interactive HTML plots (Plotly, Bokeh)

### Processed Data:
- **processed/** - Cleaned and merged datasets
- **results/** - Analysis results (CSV, Excel)

### Reports:
- **reports/** - Generated PDF/HTML reports
- **presentations/** - Slides and presentation materials



## Folder Structure (Recommended)

```
outputs/
├── figures/
│   ├── kp_timeseries.png
│   ├── correlation_heatmap.png
│   ├── storm_events_timeline.png
│   └── ...
├── processed/
│   ├── space_weather_master.csv
│   ├── storm_events_catalog.csv
│   └── ...
├── results/
│   ├── correlation_matrix.csv
│   ├── summary_statistics.csv
│   └── ...
└── reports/
    ├── final_report.pdf
    ├── phase1_summary.md
    └── ...
```



## Saving Outputs from Notebooks

### Save a Plot:
```python
import matplotlib.pyplot as plt

# Create your plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['Time (UTC)'], df['median'])
ax.set_title('Kp Index Over Time')

# Save it
fig.savefig('../outputs/figures/kp_timeseries.png', 
            dpi=300, 
            bbox_inches='tight')
print("✓ Figure saved to outputs/figures/kp_timeseries.png")
```

### Save Processed Data:
```python
# Save your cleaned dataframe
df_clean.to_csv('../outputs/processed/space_weather_master.csv', index=True)
print("✓ Processed data saved!")
```

### Save Analysis Results:
```python
# Save correlation matrix
correlation_results.to_csv('../outputs/results/correlations.csv')
print("✓ Results saved!")
```

---

## Best Practices

### 1. Use Descriptive Names
**Good:**
- `kp_median_timeseries_2025-11.png`
- `storm_events_kp_gt_6.csv`
- `correlation_heatmap_all_variables.png`

**Bad:**
- `plot1.png`
- `data.csv`
- `output.png`

### 2. Include Dates
For time-sensitive outputs:
- `analysis_results_2025-11-13.csv`
- `daily_report_2025-11-13.pdf`

### 3. Use High Resolution for Plots
```python
# Good for presentations and reports
fig.savefig('plot.png', dpi=300)  # High quality

# Good for quick previews
fig.savefig('plot.png', dpi=100)  # Lower file size
```

### 4. Organize by Analysis Phase
Create subfolders:
- `outputs/phase1_eda/`
- `outputs/phase2_integration/`
- `outputs/final/`



## Example: Complete Workflow

```python
# In your Jupyter notebook

# 1. Do your analysis
df = pd.read_csv('../data/Space_Weather_Indices_Subset.csv')
df['Time (UTC)'] = pd.to_datetime(df['Time (UTC)'], format='%d-%m-%Y %H:%M')

# 2. Create visualization
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Time (UTC)'], df['median'], marker='o', linewidth=2)
ax.set_title('Kp Index Median Over Time', fontsize=16, fontweight='bold')
ax.set_xlabel('Time (UTC)', fontsize=12)
ax.set_ylabel('Kp Index', fontsize=12)
ax.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# 3. Save it
fig.savefig('../outputs/figures/kp_median_timeseries.png', 
            dpi=300, 
            bbox_inches='tight',
            facecolor='white')

# 4. Calculate statistics
summary_stats = df['median'].describe()

# 5. Save statistics
summary_df = pd.DataFrame(summary_stats)
summary_df.to_csv('../outputs/results/kp_summary_statistics.csv')

print("✓ All outputs saved successfully!")
```



## What to Save

### Always Save:
-  Final visualizations for your report
-  Processed/cleaned datasets
-  Summary statistics
-  Model results and predictions

### Consider Saving:
-  Intermediate analysis results
-  Exploratory plots (if interesting)
-  Data subsets for specific analysis

### Don't Save:
-  Raw data (keep in `data/` folder)
-  Temporary test outputs
-  Duplicate files



## File Format Guide

### Images:
- **PNG** - Best for web, presentations (300 dpi recommended)
- **PDF** - Best for publications, scalable
- **SVG** - Vector format, perfect for editing later
- **JPG** - Smaller file size, good for photos

### Data:
- **CSV** - Simple, universal, human-readable
- **Excel (.xlsx)** - Multiple sheets, formatting
- **Parquet** - Fast, compressed (advanced)
- **JSON** - Hierarchical data



## Quick Start

Create the subfolders:
```bash
# In your terminal (from project root)
mkdir -p outputs/figures
mkdir -p outputs/processed
mkdir -p outputs/results
mkdir -p outputs/reports
```

Or create them as you save files - Python will create folders automatically:
```python
import os

# This creates the folder if it doesn't exist
os.makedirs('../outputs/figures', exist_ok=True)
```



##  Keeping Track

Create a log of your outputs:

**outputs/OUTPUT_LOG.md:**
```markdown
# Output Log

## 2025-11-13
- Created: kp_timeseries.png - Time series plot of Kp median
- Created: summary_statistics.csv - Basic stats for Phase 1 EDA
- Note: Initial exploratory analysis complete

## 2025-11-14
- Created: correlation_heatmap.png - All variables correlation
- Created: storm_events.csv - Filtered Kp >= 6 events
```



## Tips

1. **Clean up regularly** - Delete test outputs, keep only finals
2. **Version important files** - `analysis_v1.csv`, `analysis_v2.csv`
3. **Use .gitignore** - Don't upload huge files to GitHub (already configured!)
4. **Backup important results** - Copy to cloud storage periodically



## .gitignore Note

Your `.gitignore` file prevents large outputs from being uploaded to GitHub:
```
outputs/*.png
outputs/*.jpg
```

This is good! GitHub has size limits. For large outputs:
- Store locally
- Use cloud storage (Google Drive, Dropbox)
- Use Git LFS (Large File Storage) for important files



**Status:** Empty (will be populated as you create outputs)  
**Last Updated:** 2025-11-13 19:31:25

---

**Remember:** Good outputs tell the story of your analysis! 
