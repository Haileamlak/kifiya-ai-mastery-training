
# 🌞 Final Report – Solar Data Discovery (Week 0 Challenge)

## 🧠 Introduction – Full Understanding of the Project

The Week 0 challenge of the 10 Academy Artificial Intelligence Mastery program focused on the analysis of environmental solar data from three countries: **Benin**, **Sierra Leone**, and **Togo**. The project was set in the context of a simulated role as an Analytics Engineer for MoonLight Energy Solutions, with the objective of leveraging solar energy data to identify optimal regions for investment in solar farms.

The overarching goal was to conduct a thorough exploratory data analysis (EDA), clean the datasets, compare regional solar potential, and present insights in a reproducible and interactive way. The challenge emphasized practical skills such as Git, CI/CD, Python scripting, statistical analysis, and dashboard development.

---

## ⚙️ Methodology – What Was Done and the Results

### Tools & Technologies Used

- **Python**: Core data analysis and cleaning
- **Pandas, NumPy, SciPy**: Data manipulation and statistical testing
- **Matplotlib, Seaborn**: Data visualization
- **Git & GitHub**: Version control and collaboration
- **GitHub Actions**: CI/CD automation
- **Streamlit**: Interactive dashboard
- **Jupyter Notebook**: Exploratory analysis

---

### Step-by-Step Implementation

#### ✅ Task 1: Git & Environment Setup

- Initialized a GitHub repository with structured folders for weekly tasks.
- Created a virtual environment and `requirements.txt` to manage dependencies.
- Configured a CI pipeline with GitHub Actions to ensure reproducibility.
- Maintained clean commit history and used pull requests for each task.

#### 📊 Task 2: Data Profiling, Cleaning, and EDA

Each dataset (Benin, Togo, Sierra Leone) was analyzed using a separate Jupyter notebook.

- **Profiling**: Summary statistics, missing values, data types
- **Cleaning**:
  - Imputed missing values using the median
  - Removed outliers using the Z-score method (threshold: |z| > 3)
- **Exploration**:
  - Line plots for GHI, DNI, DHI, Tamb
  - Correlation heatmaps
  - Cleaning impact on irradiance modules
  - Bubble charts (RH vs Tamb vs GHI)

#### 🌍 Task 3: Cross-Country Comparison

- Merged cleaned datasets and added country labels.
- Generated boxplots for GHI, DNI, and DHI by country.
- Calculated summary statistics (mean, median, std).
- Conducted **ANOVA** and **Kruskal-Wallis tests** to assess significance.
- Found that Benin had the highest average GHI.

#### 📊 Task 4: Streamlit Dashboard

Developed an interactive dashboard with the following features:

- Country and feature selector
- Boxplot visualizations for selected features
- Summary statistics by country
- Bubble chart showing RH vs Tamb vs GHI
- Average GHI comparison bar chart

📸 *See screenshots in the dashboard_screenshots/ folder for a preview of the dashboard.*

---

## 🚧 Challenges & Solutions

| Challenge | Solution |
|----------|----------|
| Pip not recognized in the virtual environment | Used `ensurepip` and `--user` installs |
| Permission error with pip upgrade | Avoided system installs and used virtual environments |
| Z-score method dropped too many rows in some datasets | Reviewed thresholds and handled edge cases conservatively |
| GitHub Actions not triggering initially | Fixed YAML indentation and branch targeting |
| Handling large or missing environmental data | Used median imputation and `.apply(pd.to_numeric)` safely |

These solutions ensured a clean and reproducible pipeline for data cleaning and analysis.

---

## 💡 Recommendations – Future Improvements

- 🧠 **Feature Engineering**: Create new features like solar power efficiency or irradiance-to-temperature ratio.
- 📈 **Modeling**: Apply machine learning models to predict future solar potential.
- 📊 **Visualization**: Use Plotly or Altair for more interactive visuals.
- ☁️ **Deployment**: Host the dashboard on Streamlit Community Cloud for public access.
- 🌍 **Scalability**: Integrate more countries or live solar datasets for real-time analysis.

---

## ✅ Conclusion – Final Thoughts and Evaluation

This project successfully met its initial goals by:
- Cleaning and exploring real-world time series data
- Identifying key differences in solar potential across countries
- Applying statistical methods to back up findings
- Delivering insights through a professional dashboard

Benin was found to have the highest solar potential on average. The use of Streamlit for delivery and GitHub for collaboration made the workflow efficient and reproducible.

This project laid a solid foundation in practical data engineering and analytics for the AI Mastery track. It not only developed technical confidence but also simulated a real-world business impact use case.

---

## 🖼️ Visuals

**[Include screenshots here in your final document]**
- Summary statistics table
- Boxplots for GHI
- Streamlit dashboard interface

---
