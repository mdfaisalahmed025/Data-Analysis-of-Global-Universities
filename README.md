# 🎓 University Data Analysis

This project analyzes universities based on **establishment year**, **type (Public/Private)**, and **test requirements (GRE, IELTS, TOEFL, PTE, SAT, GMAT)**.  
The goal is to understand trends in higher education and visualize them using **Tableau**.

---

## 📊 Dataset
- **Source:** Self-prepared / scraped dataset  
- **Columns:**
  - `University Name` – Name of the university  
  - `University Type` – Public or Private  
  - `Establishment Year` – Year university was founded  
  - `GRE, IELTS, TOEFL, PTE, SAT, GMAT` – Binary indicators (1 = required, 0 = not required)  

---

## 🔧 Data Preprocessing
- Converted `yes/no` values in test requirement columns → `0/1`  
- Cleaned missing values  
- Standardized column names for analysis  

---

## 📈 Analysis in Tableau
1. **University Establishment Trends**  
   - Count of universities established per year  
   - Comparison between **Public vs Private**  

2. **Test Requirements by University Type**  
   - Heatmap of test requirements across universities  
   - Identified which tests are most/least required  

3. **Cumulative Growth**  
   - Running total of universities over time  

---

## 📷 Visualizations
Screenshots of Tableau dashboards are available in the [`visualizations/`](visualizations) folder.  

Example:  

![University Establishment Trend](visualizations/university_trend.png)  

---

## 🚀 How to Use
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/university-data-analysis.git
