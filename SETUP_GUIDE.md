# 🚀 Setup Guide for Space Weather Case Study

Welcome! This guide will help you get started with your space weather analysis project on your personal computer.

## 📋 Prerequisites

Before you begin, make sure you have:
- Python 3.8 or higher installed ([Download here](https://www.python.org/downloads/))
- Git installed ([Download here](https://git-scm.com/downloads))
- A text editor (VS Code, Notepad++, or any editor you prefer)

---

## 🏁 Step-by-Step Setup Instructions

### Step 1: Clone the Repository to Your Computer

Open your terminal/command prompt and run:

```bash
# Navigate to where you want to save the project (e.g., Documents)
cd Documents

# Clone the repository
git clone https://github.com/Pedro24681/space-weather-case-study.git

# Navigate into the project folder
cd space-weather-case-study
```

**Alternative:** Use [GitHub Desktop](https://desktop.github.com/) for a graphical interface.

---

### Step 2: Install Required Python Packages

Once you're in the project folder, install all dependencies:

```bash
pip install -r requirements.txt
```

This will install:
- **pandas** - for data manipulation
- **numpy** - for numerical operations
- **matplotlib** - for creating plots
- **seaborn** - for statistical visualizations
- **jupyter** - for interactive notebooks

**Note:** Installation may take 2-3 minutes.

---

### Step 3: Verify Installation

Test that everything is installed correctly:

```bash
python -c "import pandas; import numpy; import matplotlib; import seaborn; import jupyter; print('✅ All packages installed successfully!')"
```

If you see the success message, you're ready to go! 🎉

---

### Step 4: Launch Jupyter Notebook

Start Jupyter Notebook to begin your analysis:

```bash
jupyter notebook
```

This will:
- Start a local server
- Open Jupyter in your default web browser
- Show a file browser of your project

---

### Step 5: Open Your First Notebook

In the Jupyter interface:
1. Navigate to the `notebooks/` folder
2. Click on `01-data-load-and-eda.ipynb`
3. Run each cell by pressing **Shift + Enter**

Watch as your data comes to life with visualizations! 📊

---

## 🎯 Your Current Project Structure

```
space-weather-case-study/
├── README.md                           # Main project README
├── requirements.txt                    # Python dependencies (✅ created!)
├── SETUP_GUIDE.md                     # This file
├── data/
│   ├── README.md                       # Data folder documentation
│   └── Space_Weather_Indices_Subset.csv  # Your Kp index data
├── notebooks/
│   └── 01-data-load-and-eda.ipynb     # Exploratory analysis notebook (✅ created!)
├── src/                                # Python modules (empty - future use)
└── outputs/                            # Figures and results (empty - will be populated)
```

---

## 📚 What You'll Learn from the First Notebook

The `01-data-load-and-eda.ipynb` notebook will teach you:
- ✅ How to load CSV data with pandas
- ✅ How to explore dataset structure and statistics
- ✅ How to handle datetime columns
- ✅ How to create time-series visualizations
- ✅ How to interpret Kp index values (geomagnetic activity)

---

## 🎓 Next Steps After Running the First Notebook

1. **Add More Data Sources**
   - Download solar wind data from [NASA OMNIWeb](https://omniweb.gsfc.nasa.gov/)
   - Get GOES X-ray flux from [NOAA](https://www.ngdc.noaa.gov/stp/satellite/goes/)
   - Place new CSV files in the `data/` folder

2. **Create Additional Notebooks**
   - `02-solar-wind-analysis.ipynb` - Analyze solar wind parameters
   - `03-correlation-analysis.ipynb` - Find relationships between variables
   - `04-event-detection.ipynb` - Identify space weather events

3. **Build Python Modules**
   - Create helper functions in the `src/` folder
   - Example: `src/data_loader.py`, `src/plotting.py`

4. **Generate Reports**
   - Save figures to the `outputs/` folder
   - Create a final report notebook with all insights

---

## 🚨 Troubleshooting

### Issue: "pip is not recognized"
**Solution:** Try `python -m pip install -r requirements.txt`

### Issue: Permission denied (Mac/Linux)
**Solution:** Add `--user` flag: `pip install --user -r requirements.txt`

### Issue: Multiple Python versions
**Solution:** Use `pip3` instead: `pip3 install -r requirements.txt`

### Issue: Jupyter not opening in browser
**Solution:** Copy the URL from terminal (looks like `http://localhost:8888/?token=...`) and paste it into your browser

---

## 💡 Pro Tips

- **Save your work often:** Jupyter auto-saves, but manually save with `Ctrl+S` (Windows/Linux) or `Cmd+S` (Mac)
- **Use Markdown cells:** Add explanations between code cells to document your thinking
- **Restart kernel if needed:** If something goes wrong, go to **Kernel → Restart & Clear Output**
- **Virtual environments:** Consider using `venv` to keep project dependencies isolated

---

## 🌟 Understanding Your Data: Kp Index Quick Reference

The Kp index measures geomagnetic activity (disturbance in Earth's magnetic field):

| Kp Value | Classification | Effects |
|----------|----------------|---------|
| 0-2      | Quiet          | Normal conditions |
| 3        | Unsettled      | Minor effects |
| 4        | Active         | Weak power grid fluctuations |
| 5        | Minor Storm    | Voltage irregularities possible |
| 6        | Moderate Storm | High-latitude power issues |
| 7        | Strong Storm   | Satellite navigation degraded |
| 8        | Severe Storm   | Power blackouts possible |
| 9        | Extreme Storm  | Widespread technology disruption |

Your dataset shows a **Kp=7 event** on November 12, 2025 - a strong geomagnetic storm! 🌪️

---

## 📞 Need Help?

- Check the [pandas documentation](https://pandas.pydata.org/docs/)
- Explore [matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- Review [seaborn examples](https://seaborn.pydata.org/examples/index.html)
- Ask questions on [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

---

## ✅ Checklist for First Session

- [ ] Clone repository to your computer
- [ ] Install Python packages from requirements.txt
- [ ] Launch Jupyter Notebook
- [ ] Open and run `01-data-load-and-eda.ipynb`
- [ ] View all the visualizations
- [ ] Read the key findings summary
- [ ] Plan your next analysis steps

---

**Good luck with your space weather analysis! You've got this! 🚀📊**

Last updated: 2025-11-13