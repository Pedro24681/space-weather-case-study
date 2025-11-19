#  Data Dictionary - Space Weather Indices

This document explains all the columns in your space weather datasets.



##  Space_Weather_Indices_Subset.csv

This file contains Kp index forecasts and ensemble predictions for geomagnetic activity.

### Column Descriptions:

| Column Name | Data Type | Description | Example Value | Unit |
|------------|-----------|-------------|---------------|------|
| **Time (UTC)** | DateTime | Forecast timestamp in UTC | 12-11-2025 18:00 | UTC |
| **minimum** | Float | Minimum predicted Kp value from ensemble | 7.0 | Kp index (0-9) |
| **0.25-quantile** | Float | 25th percentile of Kp predictions | 7.0 | Kp index (0-9) |
| **median** | Float | Median (50th percentile) Kp prediction | 7.0 | Kp index (0-9) |
| **0.75-quantile** | Float | 75th percentile of Kp predictions | 7.0 | Kp index (0-9) |
| **maximum** | Float | Maximum predicted Kp value from ensemble | 7.0 | Kp index (0-9) |
| **prob 4-5** | Float | Probability of Kp being between 4 and 5 | 0.0 | Probability (0-1) |
| **prob 5-6** | Float | Probability of Kp being between 5 and 6 | 0.0 | Probability (0-1) |
| **prob 6-7** | Float | Probability of Kp being between 6 and 7 | 1.0 | Probability (0-1) |
| **prob 7-8** | Float | Probability of Kp being between 7 and 8 | 1.0 | Probability (0-1) |
| **prob >= 8** | Float | Probability of Kp being 8 or higher | 0.0 | Probability (0-1) |
| **kp_0** to **kp_9** | Float | Individual ensemble member predictions | Various | Kp index (0-9) |



##  Understanding the Kp Index

### What is Kp?
The **Kp index** (Planetary K-index) is a global measure of geomagnetic activity. It indicates how disturbed Earth's magnetic field is due to solar activity.

### Kp Scale:

| Kp Range | Classification | NOAA Scale | What It Means |
|----------|----------------|------------|---------------|
| **0 - 2** | Quiet | G0 | Normal conditions, minimal aurora |
| **3** | Unsettled | G0 | Slightly disturbed, weak aurora at high latitudes |
| **4** | Active | G0 | Active conditions, aurora visible at 60-65° latitude |
| **5** | Minor Storm | G1 | Minor power grid fluctuations, aurora at 60° |
| **6** | Moderate Storm | G2 | Voltage alarms, satellite orientation issues |
| **7** | Strong Storm | G3 | Power grid issues, satellite navigation degraded |
| **8** | Severe Storm | G4 | Widespread voltage problems, GPS errors |
| **9** | Extreme Storm | G5 | Complete power blackouts possible, widespread tech failures |

### Fun Fact:
During a Kp=7 storm (like in your dataset on Nov 12, 2025), auroras can be visible as far south as mid-latitude cities! 🌌



##  Ensemble Forecast Explained

Your dataset uses **ensemble forecasting**, which means:
- Multiple models run with slightly different parameters
- Each model produces a Kp prediction (`kp_0` through `kp_9`)
- Statistics summarize the ensemble (min, median, max, quantiles)
- Probabilities show the range of uncertainty

**Example:**
If `median = 5.0` but `maximum = 7.0`, there's uncertainty. Some models predict moderate activity while others predict strong storms.



##  Probability Columns

The `prob X-Y` columns tell you the **likelihood** of Kp falling in a certain range:

**Example from your data (12-11-2025 18:00):**
- `prob 6-7 = 1.0` → 100% chance Kp will be between 6 and 7
- `prob 7-8 = 1.0` → 100% chance Kp will be between 7 and 8
- All models agree this will be a **strong storm**!

**Another Example (13-11-2025 21:00):**
- `prob 4-5 = 0.3` → 30% chance of minor storm
- `prob 5-6 = 0.5` → 50% chance of moderate storm
- More uncertainty in this forecast



##  Time Format

- **Format:** DD-MM-YYYY HH:MM
- **Timezone:** UTC (Coordinated Universal Time)
- **Frequency:** 3-hour intervals (common for Kp forecasts)

**Important:** Always convert to UTC when merging with other datasets!



##  Future Datasets (Planned)

### solar_wind.csv (To be added)
| Column | Description | Unit |
|--------|-------------|------|
| Time | Timestamp | UTC |
| Speed | Solar wind speed | km/s |
| Density | Proton density | particles/cm³ |
| Temperature | Solar wind temperature | Kelvin |
| Bx, By, Bz | Magnetic field components | nT (nanoTesla) |

**Why it matters:** Bz (southward component) is crucial for predicting geomagnetic storms!

### goes_xray.csv (To be added)
| Column | Description | Unit |
|--------|-------------|------|
| Time | Timestamp | UTC |
| XRS-A | Long wavelength X-ray flux | W/m² |
| XRS-B | Short wavelength X-ray flux | W/m² |
| Flare_Class | Solar flare classification | A/B/C/M/X |

**Why it matters:** X-class flares can cause radio blackouts and satellite damage!

### satellite_anomalies.csv (To be added - optional)
| Column | Description | Example |
|--------|-------------|---------|
| Time | Anomaly timestamp | 2025-11-12 19:30 |
| Satellite_ID | Satellite identifier | GOES-16 |
| Anomaly_Type | Type of issue | Orientation error |
| Severity | Impact level | Moderate |



##  Key Concepts for Beginners

### What causes geomagnetic storms?
1. **Solar flares** emit X-rays and UV radiation
2. **Coronal Mass Ejections (CMEs)** send plasma toward Earth
3. **Solar wind** carries magnetic field that interacts with Earth's magnetosphere
4. When solar wind's magnetic field points **south (Bz < 0)**, it can trigger storms

### Technology Impacts by Kp Level:

**Kp 5 (Minor Storm):**
- Weak power grid fluctuations
- Minor satellite operations issues
- Aurora visible at high latitudes

**Kp 6 (Moderate Storm):**
- High-latitude power systems affected
- Satellite drag increases (orbit changes)
- GPS errors possible
- Aurora visible at mid-latitudes

**Kp 7 (Strong Storm):**
- Power grid voltage problems
- Satellite surface charging
- Increased GPS navigation errors
- HF radio communication disrupted

**Kp 8-9 (Severe/Extreme Storm):**
- Widespread power blackouts
- Satellite failures
- Complete GPS/GNSS outages
- Radio blackouts
- Transformer damage possible



##  Additional Resources

- [NOAA Space Weather Scales](https://www.swpc.noaa.gov/noaa-scales-explanation)
- [Kp Index Explanation](https://www.swpc.noaa.gov/products/planetary-k-index)
- [GFZ Potsdam Kp Index](https://www.gfz-potsdam.de/en/kp-index/)



##  Tips for Using This Data

1. **Always check the median first** - It's the most reliable single prediction
2. **Look at the spread** - Large difference between min and max = high uncertainty
3. **Use probability columns** - They tell you the forecast confidence
4. **Watch for Kp ≥ 5** - This is when impacts start
5. **Check trends** - Rising Kp is more concerning than stable high Kp

---

**Last Updated:** 2025-11-13  
**Data Source:** [GFZ Potsdam Kp Forecast](https://spaceweather.gfz.de/products-data/forecasts/forecast-kp-index)
