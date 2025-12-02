# Space Weather Case Study

Hello to all that may be reading this! This repository contains a complete, reproducible analysis pipeline to investigate geomagnetic activity (Kp index) and related solar wind drivers. The project demonstrates data integration, event detection, and an impact assessment with production-quality visualizations and a final summary report.

## Repository Structure

- `notebooks/` — Jupyter notebooks for each analysis phase (Phase 1 → Phase 4)
- `src/` — Reusable Python modules for loading, processing, and plotting
- `data/` — Raw and reference datasets used in the analysis
- `outputs/` — Generated figures, processed datasets, and results
- `ANALYSIS_SUMMARY.md` — Concise technical summary of findings

## Key Phases & Artifacts

1. Phase 1 — Data Load & Exploratory Data Analysis (`notebooks/01-data-load-and-eda.ipynb`)  
2. Phase 2 — Data Integration & Correlation (`notebooks/02-data-integration.ipynb`, `outputs/processed/space_weather_master.csv`)  
3. Phase 3 — Event Detection & Storm Catalog (`notebooks/03-correlation-and-events.ipynb`, `outputs/processed/storm_catalog.csv`)  
4. Phase 4 — Impact Assessment & Visualizations (`notebooks/04-impact-assessment.ipynb`, `outputs/figures/`)

## Quickstart

1. Clone the repo:
   git clone https://github.com/Pedro24681/space-weather-case-study.git
2. Install dependencies:
   pip install -r requirements.txt
3. Open notebooks and run in order:
   jupyter notebook notebooks/
   Run: 01 → 02 → 03 → 04

Note: Some outputs are large and may be stored locally; check `.gitignore` for file handling rules.

## License & Contact

Author: Pedro24681  
Contact: (add your preferred email or LinkedIn link)  

For full technical findings, please see my `ANALYSIS_SUMMARY.md`.
