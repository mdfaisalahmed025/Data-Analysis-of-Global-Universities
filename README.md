# Global University Data Analysis

This repository contains a **Selenium-based Python script** that scrapes university and course information from [Jeduka.com](https://www.jeduka.com) for multiple countries and exports the results to a CSV. The dataset is then analyzed using Python for insights into global higher education trends.

---

## 🚀 Project Overview

The script automatically collects detailed information about universities and programs, including:

- University name and type
- Subjects / programs offered
- Program duration
- Tuition fees and application fees
- Accepted exams (IELTS, TOEFL, PTE, GRE, GMAT, SAT)
- Location, country, and year of establishment
- University website
- Auto-generated flags (`IELTS`, `TOEFL`, `PTE`, `GRE`, `GMAT`, `SAT`) based on exams accepted

The goal of this project is to create a structured dataset for data analysis and visualization, enabling prospective students to compare universities and programs across the globe.

---

## 📊 Python Data Analysis

The exported CSV dataset can be analyzed using Python libraries like `pandas`, `matplotlib`, `seaborn`, and `plotly`. Key analysis includes:

- **Distribution of program durations**
- **Tuition fees comparison** by country or university type
- **Currency conversion of tuition fees** (to USD or other currencies)
- **Duration conversion** (e.g., months → years)
- **Heatmap of exam requirements** across different universities
- **Top countries for overseas study**
- **University type analysis** (Public vs Private)
- **Interactive visualizations** using Plotly for better exploration

Example code snippets:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
df = pd.read_csv("global_university_data.csv")

# Convert duration to months if needed
df['duration_months'] = df['duration'].apply(lambda x: int(x.split()[0]) if isinstance(x, str) else x)

# Convert tuition fees to USD (assuming a conversion function)
# Example: df['tuition_fees_usd'] = df['tuition_fees_local'].apply(lambda x: convert_to_usd(x, currency))

# Histogram of program durations
df['duration_months'].hist(bins=10, color='pink')
plt.title("Distribution of Program Duration (Months)")
plt.xlabel("Months")
plt.ylabel("Number of Programs")
plt.show()

# Heatmap of test requirements by university type
test_cols = ['IELTS', 'TOEFL', 'PTE', 'GRE', 'GMAT', 'SAT']
heatmap_data = df.groupby("university_type")[test_cols].apply(lambda x: (x=="Yes").sum())
sns.heatmap(heatmap_data, annot=True, cmap="Blues", fmt="d")
plt.title("Test Requirements by University Type")
plt.show()

# Interactive tuition fees vs duration scatter plot using Plotly
fig = px.scatter(df, x='duration_months', y='tuition_fees_usd',
                 color='country', hover_data=['university_name', 'subject'])
fig.update_layout(title="Tuition Fees vs Program Duration by Country")
fig.show()


---

## 1) Prerequisites

- **OS:** Windows / macOS / Linux
- **Python:** 3.9+ recommended
- **Google Chrome:** Installed
- **ChromeDriver:** Must be compatible with your installed Chrome version (or use `webdriver-manager`, see below)

### Python packages
- `selenium`
- `pandas`

You can install them with:
```bash
pip install selenium pandas
```

## 2️⃣ Create a virtual environment (recommended)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

## 3️⃣ Install dependencies

```bash
pip install -U pip
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, create one with:
```text
selenium
pandas
webdriver-manager
```

---

### 1️⃣ Clone Repository
```bash
git clone https://github.com/mdfaisalahmed025/global-university-data.git
cd global-university-data
Tablaeu Public :https://public.tableau.com/views/Globaluniversitydataanalysis/Dashboard1?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link