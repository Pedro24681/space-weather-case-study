```markdown
# Data Folder — Space Weather Case Study

Place your raw datasets here. Recommended filenames and descriptions:

- solar_wind.csv
  - Description: Time series of solar wind parameters (speed, density, B-field components, Bz) — e.g., OMNI or ACE.
  - Source: NASA OMNIWeb or CDAWeb.

- kp_index.csv
  - Description: Planetary K-index (3-hourly) or converted 1-hour proxies.
  - Source: GFZ Potsdam, NOAA.

- goes_xray.csv
  - Description: GOES X-ray flux (1-min or 5-min), flares catalog.
  - Source: NOAA (GOES).

- geomagnetic_storms.csv
  - Description: Catalog of storm intervals (start/end times, intensity Dst/Kp).
  - Source: various geomagnetic indices datasets.

- satellite_anomalies.csv (optional)
  - Description: Time-stamped satellite anomaly reports (if available) — vendor reports, space situational awareness feeds, or curated logs.

- technology_impacts.csv (optional)
  - Description: Aggregated reports of HF outages, GNSS error spikes, airline rerouting, power grid disturbances with timestamps.

Notes
- If a dataset is large, include a sample CSV (first N rows) for the repo and keep the full raw data offline or in cloud storage.
- Typical datetime fields: use ISO 8601 (UTC). Convert all timestamps to UTC for consistent merging.
- If using API downloads, store raw responses in data/raw/ and processed datasets in data/processed/.
