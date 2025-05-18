# Week 0 - Solar Data Discovery Challenge

This project is part of the 10 Academy Artificial Intelligence Mastery program. The goal is to analyze solar farm data from Benin, Sierra Leone, and Togo to extract insights and identify high-potential regions for solar energy investment.

## Objectives

- Profile and clean solar environmental data
- Perform exploratory data analysis (EDA)
- Compare solar potential across countries
- Deliver insights through visualizations
- Optionally build an interactive Streamlit dashboard

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/haileamlak/kifiya-ai-mastery-training.git
   cd kifiya-ai-mastery-training/week0_solar_challenge
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate          # On Windows
   # or
   source venv/bin/activate       # On macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Launch Jupyter notebooks:

   ```bash
   jupyter notebook
   ```

## Tasks Overview

### Task 1: Git & Environment Setup

* GitHub repo initialized with CI via GitHub Actions
* Environment set up with `venv` and `requirements.txt`
* Folder structure organized and documented

### Task 2: EDA & Cleaning

* Loaded and profiled data for each country
* Cleaned missing values and outliers using Z-score method
* Visualized solar patterns, temperature, humidity, and wind effects
* Saved cleaned datasets for cross-country comparison

## Key Visualizations

* Time series plots (GHI, DNI, DHI, Tamb)
* Correlation heatmaps
* Cleaning impact on irradiance (ModA/ModB)
* Scatter plots and bubble charts for feature relationships

## Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* SciPy (Z-score)
* Jupyter Notebook
* Git & GitHub
* GitHub Actions (CI)

## Next Steps

* Task 3: Compare countries and statistically test GHI differences
* Task 4 (Optional): Build an interactive Streamlit dashboard

## Notes

* All `.csv` files are excluded via `.gitignore`
* Cleaned files are saved in `data/` but not tracked in version control
* All insights are reproducible via notebooks
