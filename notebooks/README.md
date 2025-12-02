# Project Notebooks

This directory contains the main Jupyter notebooks for the space weather case study. Run notebooks in sequence for full reproducibility.

Notebooks
- `01-data-load-and-eda.ipynb` — Phase 1: load data, data quality checks, EDA and initial visualizations.
- `02-data-integration.ipynb` — Phase 2: parse solar wind files, time alignment, and merged master dataset.
- `03-correlation-and-events.ipynb` — Phase 3: correlation analysis, event detection, and storm catalog generation.
- `04-impact-assessment.ipynb` — Phase 4: impact assessment, temporal analysis, and final visualizations.

Running
1. Ensure `data/` and `outputs/` directories exist.
2. Start Jupyter from repo root and open the notebooks folder:
   jupyter notebook notebooks/
3. Run each notebook from top to bottom.

Each notebook contains explanatory markdown and saving steps for figures and processed outputs.
