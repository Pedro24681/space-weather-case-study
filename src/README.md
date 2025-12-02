# Source Code (src/)

This folder contains reusable Python modules used across the notebooks. The goal is to keep analysis notebooks concise and import commonly used utilities from here.

Modules
- `data_loader.py` — functions to load, clean, and transform datasets (Kp index, solar wind).
- `plotting.py` — plotting helpers for consistent figure styling and saving.
- `analysis.py` — statistical utilities and event/storm classification helpers.

Usage
- Add the `src/` folder to the Python path in notebooks:
```python
import sys
sys.path.append('../src')
from data_loader import load_kp_index_data
```

What I was going for here is functionality. Keeping functionality here helps with reproducibility and makes the notebooks easier to present.
