```markdown
# Space Weather & Technology Impact — Case Study

This repository explores space weather (solar flares, coronal mass ejections, solar wind, geomagnetic indices) and its observed or potential impacts on modern technology (satellites, HF radio, GNSS, power grids, aviation).

Goals
- Collect and clean space weather time-series and event data.
- Analyze correlations between space weather events and disruptions (satellite anomalies, HF outages, GNSS errors, power-grid disturbances).
- Produce visualizations and a reproducible analysis notebook showing insights and recommendations.

Project Structure
- data/: datasets used for analysis (CSV files, small samples included)
- notebooks/: Jupyter notebooks for exploration and final report
- src/: Python modules (data loading, cleaning, analysis, plotting)
- outputs/: figures, processed datasets, and exported results
- README.md: this file

Data sources (good starting points)
- NOAA Space Weather Prediction Center (SWPC): https://www.swpc.noaa.gov/
- NASA OMNIWeb (solar wind & geomagnetic indices): https://omniweb.gsfc.nasa.gov/
- CDAWeb: https://cdaweb.gsfc.nasa.gov/
- NOAA GOES (satellite X-ray flux, energetic particles): https://www.ngdc.noaa.gov/stp/satellite/goes/
- Public incident/technology disruption logs (search for satellite anomaly datasets, GNSS degradation logs, power grid event reports, or use proxies like NOTAMs or outage reports)

Requirements
- Python 3.8+
- pandas, numpy
- matplotlib, seaborn
- jupyterlab or notebook
- (optional) scikit-learn, statsmodels

How to start
1. Add raw CSVs into data/ (see data/README.md for recommended filenames).
2. Use notebooks/01-data-load-and-eda.ipynb to explore datasets.
3. Run src scripts to preprocess then analyze and plot.

License & attribution
- Cite data sources when publishing or sharing results.
```
