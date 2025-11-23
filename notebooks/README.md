# Space Weather Analysis Notebooks

This directory contains Jupyter notebooks for the space weather case study analysis pipeline.

## Notebooks

### Phase 1: Data Loading and EDA
**File:** `01-data-load-and-eda.ipynb`

Initial exploratory data analysis of the Kp index dataset. Includes:
- Data loading and inspection
- Basic time-series visualizations
- Distribution analysis
- Data quality checks

### Phase 2: Data Integration
**File:** `02-data-integration.ipynb`

Integration of multiple data sources. Includes:
- Loading solar wind data
- Time alignment between datasets
- Data merging strategies
- Unified dataset creation

### Phase 3: Correlation and Events
**File:** `03-correlation-and-events.ipynb`

Correlation analysis and event detection. Includes:
- Statistical correlation analysis
- Event detection and classification
- Storm catalog generation
- Relationship exploration

### Phase 4: Impact Assessment ⭐ **NEW**
**File:** `04-impact-assessment.ipynb`

Comprehensive impact assessment synthesizing insights from Phases 1-3. Includes:

#### Analysis Components:
1. **Storm Impact Analysis**
   - Storm severity classification (Quiet to Extreme Storm G5)
   - Frequency analysis (% of storm events)
   - Duration patterns (consecutive storm periods)
   - Event statistics (mean, std dev, percentiles)

2. **Temporal Analysis**
   - Hourly activity patterns
   - Daily patterns and trends
   - Day of week analysis
   - Peak activity time identification

3. **Statistical Analysis**
   - Descriptive statistics for Kp index
   - Probability distribution analysis
   - Ensemble member correlation analysis
   - Distribution characteristics (skewness, kurtosis, normality tests)

4. **Solar Wind Characteristics**
   - Mean values and variability for all parameters (Bx, By, Bz, Bt, Density, Speed, Temperature)
   - Extreme event detection (high speed, strong Bz, high density)
   - Key parameter relationships and correlations

5. **Comprehensive Visualizations**
   - Figure 9: Storm severity analysis (4 plots)
   - Figure 10: Temporal patterns (4 plots)
   - Figure 11: Impact metrics (4 plots)
   - Figure 12: Solar wind characteristics (6 plots)

6. **Final Summary Report**
   - Key findings from all analyses
   - Patterns discovered
   - Data limitations
   - Recommendations for future analysis

#### Outputs Generated:
- `outputs/figures/09_storm_severity_analysis.png`
- `outputs/figures/10_temporal_patterns.png`
- `outputs/figures/11_impact_metrics.png`
- `outputs/figures/12_solar_wind_characteristics.png`

## Running the Notebooks

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### Execution Order
The notebooks should be run in sequence (1 → 2 → 3 → 4) as each phase builds on previous results.

```bash
jupyter notebook notebooks/
```

Then open and run:
1. `01-data-load-and-eda.ipynb`
2. `02-data-integration.ipynb`
3. `03-correlation-and-events.ipynb`
4. `04-impact-assessment.ipynb`

### Phase 4 Quick Start
If Phases 1-3 have been completed, Phase 4 can be run independently as it loads data directly from the `data/` directory.

```bash
jupyter notebook notebooks/04-impact-assessment.ipynb
```

## Data Requirements

Phase 4 requires:
- `data/Space_Weather_Indices_Subset.csv` - Kp index forecast data
- `data/solar_wind.txt` - Solar wind parameter measurements

## Expected Results

After running Phase 4, you will have:
- Comprehensive statistical analysis of storm patterns
- Temporal activity patterns (hourly, daily, weekly)
- Solar wind characteristic analysis
- 4 multi-panel visualization figures (15 plots total)
- Detailed summary report with findings and recommendations

## Notebook Structure

Each notebook follows best practices:
- Clear markdown documentation
- Well-commented code cells
- Reproducible analysis
- Generated visualizations saved to `outputs/figures/`
- Summary statistics printed inline

## Troubleshooting

### Common Issues

**Issue:** "No module named 'pandas'"
```bash
pip install -r requirements.txt
```

**Issue:** "File not found: Space_Weather_Indices_Subset.csv"
- Ensure you're running from the repository root
- Check that data files exist in `data/` directory

**Issue:** Visualization errors
- Ensure `outputs/figures/` directory exists
- Check matplotlib backend configuration

## Contributing

When adding new notebooks:
1. Follow the Phase N naming convention
2. Include comprehensive markdown documentation
3. Add summary to this README
4. Ensure reproducibility

## License

See repository LICENSE file.

---

Last Updated: 2025-11-23
