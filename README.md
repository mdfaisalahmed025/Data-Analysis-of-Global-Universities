# Global University Insights

This repository contains a **Selenium-based Python script** that scrapes university and course information from [Jeduka.com](https://www.jeduka.com) for multiple countries and exports the results to a CSV. The dataset is then analyzed using Python for insights into global higher education trends.

---

<h2 style="color:red;">🚀 <b>Quick Links</b></h2>

📊 <a href="https://public.tableau.com/app/profile/md.faisal.ahmed/viz/GlobalUniversityInsights/COUNTRYANDTUTIONFEES?publish=yes" style="color:red;"><b>Live Tableau Dashboard</b></a> – Interactive visualization

💻 <a href="https://github.com/mdfaisalahmed025/Data-Analysis-of-Global-Universities" style="color:red;"><b>GitHub Repository</b></a> – Source code and data

📝 <a href="https://www.jeduka.com" style="color:red;"><b>Data Source</b></a> – Jeduka Website

---

## 🌟 Motivation

In today’s globalized world, pursuing higher education abroad has become an essential step for students seeking academic excellence, international exposure, and career advancement. However, finding the right university and program can be **overwhelming and confusing**, as information is scattered across multiple websites, presented inconsistently, and often lacks clear comparisons.

Students struggle to answer questions like:

- Which countries offer the most cost-effective programs?
- How long do programs last across different universities and subjects?
- What are the common exam requirements for international admissions?

The motivation behind this project is to **simplify and centralize global university information**, enabling students to make **data-driven decisions** about their higher education journey. By combining automation, data analysis, and visualization, the project empowers students and educators with **actionable insights**.

---

## 📚 Project Background

**Global University Insights** is a data-driven initiative that leverages **Selenium-based Python scripts** to automatically collect detailed information about universities and programs from [Jeduka.com](https://www.jeduka.com). The collected dataset is then **cleaned, validated, and structured** for analysis.

Key aspects of the project include:

- Gathering information on **university name, type, location, courses, tuition fees, application fees, program duration, accepted exams, and year of establishment**.  
- Converting and standardizing **tuition fees to USD** and **course durations to months** for uniform analysis.  
- Creating **calculated flags for exams accepted** (`IELTS`, `TOEFL`, `PTE`, `GRE`, `GMAT`, `SAT`) to enable easier comparison.  
- Using **Python** (`Pandas`, `Matplotlib`, `Seaborn`, `Plotly`) and **Tableau Public** to generate **interactive visualizations** that highlight global education trends.  

The project provides a **comprehensive overview of higher education worldwide**, offering insights for students, researchers, and policymakers. It helps in understanding **global tuition trends, program durations, university types, and exam requirements**, making it a valuable tool for **data-driven decision-making in international education**.

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


## Dataset Validation & Processing

This repository contains the cleaned and processed dataset of universities and courses, along with the steps taken to ensure data quality and consistency.

### 📑 Dataset Validation & Processing Results

- **Initial Dataset:** 6,387 records  
- **Final Clean Dataset:** 4,223 records  
- **Missing Values:** Rows with missing values were removed to ensure data integrity  
- **Duplicates:** Removed based on `university_name` and `course` combination  
- **Parse and Convert Tuition Fees to USD:** All tuition fees standardized to USD for consistency across countries  
- **Convert Duration to Months:** Duration values normalized to months for uniformity  
- **Handling Missing Values:** Imputed or removed missing entries to maintain dataset quality  
- **Numeric Column Exploration:** Analyzed numeric columns like tuition fees, application fees, and exam scores for outliers, ranges, and distributions  
- **Categorical Column Exploration:** Analyzed categorical columns like university type, location, and exams accepted for unique values, consistency, and potential normalization  

### 📊 Data Quality Checks

- **Completeness:** Checked for missing values across all columns  
- **Uniqueness:** Removed duplicates to ensure unique university-course combinations  
- **Validity:** Verified numeric and categorical columns for valid ranges and formats  
- **Consistency:** Standardized categorical fields for uniformity (e.g., public/private, location names)  
- **Integrity:** Ensured relationships between related fields are valid (e.g., location matches country)


### 🗂️ Data Schema

| Column Name           |    Description                                  | Data Type    |
|-----------------------|----------------------------------------------|-------------|
| university_name       | Name of the university                        | String      |
| subject               | Name of the course or program                 | String      |
| duration              | Duration of the course                        | String / Months (converted to numeric) |
| tuition_fees          | Tuition fees for the course (in USD)         | Float       |
| application_fees      | Application fees (in USD)                     | Float       |
| exams_accepted        | Exams accepted for admission (IELTS, TOEFL, etc.) | String / List |
| university_type       | Type of university (Public / Private / Others)| String      |
| location              | City or state where the university is located | String      |
| country               | Country where the university is located      | String      |
| year_of_establish     | Year the university was established          | Integer     |
| university_website    | Official website URL of the university       | String      |
| IELTS                 | IELTS minimum score required                  | Float       |
| TOEFL                 | TOEFL minimum score required                  | Float       |
| PTE                   | PTE minimum score required                    | Float       |
| GRE                   | GRE minimum score required                    | Float       |
| GMAT                  | GMAT minimum score required                   | Float       |
| SAT                   | SAT minimum score required                    | Float       |




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

## 📊 Tableau Dashboard Analysis

The dataset is visualized using **Tableau Public**. The interactive dashboard allows exploration of global university trends and provides insights for prospective students.

### Key Analysis

**1. Top Overseas Study Destinations vs Tuition Fees**

- Compare countries based on the number of international programs available.
- Visualize average tuition fees per country to identify cost-effective destinations for overseas study.

📌 **Analysis Output:**  
From the visualization, the **USA holds the first position** as the top overseas study destination, followed by the **UK** in second place, and **Australia** in third place.

**2. European Countries vs Tuition Fees**

- Compare tuition fees among European countries.
- Identify countries with the **highest** and **lowest** study costs.

📌 **Analysis Output:**

- **France** holds the **top position** with the highest tuition fees among European countries.
- **Switzerland** comes next, followed by **Ireland**.
- At the **bottom position**, **Croatia** has the lowest tuition fees.

**3. Asian Countries vs Tuition Fees**

- Compare tuition fees among Asian study destinations.
- Identify cost-effective options and premium tuition destinations.

📌 **Analysis Output:**

- **Singapore** ranks at the **top position** with the highest tuition fees in Asia.
- At the **lowest position**, **Korea (Republic)** has the most affordable tuition fees.

[![Top Overseas Country](/images/Overseas_country.png)](https://public.tableau.com/app/profile/md.faisal.ahmed/viz/dataanalysisofglobaluniversities/COUNTRYANDTUTIONFEES?publish=yes)
---

**4. Cost of Master’s Degrees in the USA by Subject**

- Compare tuition fees across different master’s degree subjects in the USA.
- Identify the most expensive and most affordable subjects.

📌 **Analysis Output:**

- The **Master’s in Leadership of Global Operation** is the **most expensive** program.
- The **Master of Arts and Communication** holds the **lowest tuition cost** among USA master’s programs.

**5. Cost of Bachelor’s Degrees in the USA by Subject**

- Compare tuition fees across different bachelor’s degree subjects in the USA.
- Identify the most expensive and most affordable subjects.

📌 **Analysis Output:**

- The **Bachelor of Science in Electrical Engineering** ranks at the **top position** with the highest tuition fees.
- The **Bachelor of Science in Biology** holds the **lowest tuition cost** among USA bachelor’s programs.

[![Cost of University](/images/cost_of_university.png)](https://public.tableau.com/app/profile/md.faisal.ahmed/viz/dataanalysisofglobaluniversities/COUNTRYANDTUTIONFEES?publish=yes)
---

**6. Course Duration in the USA by Subject**

- Compare program durations across different universities and subjects.
- Helps students plan based on time commitment for degree completion.

📌 **Analysis Output (Sample):**  
| Subject | University Name | Duration |
|---------------------------------------|------------------------------------------|-----------------|
| Master’s in Computer Science | Stanford University | 24 months |
| Master’s in Business Administration | Harvard University | 24 months |
| Master’s in Electrical Engineering | Stanford University | 36 months |
| Bachelor of Science in Biology | University of pennsylvania | 48 months |
| Master's of Businesss Analytics | Massachusetts Institute of technology | 12 months |
| Bachelor of Arts in Biological Science| University of Chicago | 48 months |

---

---

**7. Public vs Private Universities**

- Compare the number of **public** and **private** universities across the dataset.
- Highlight the **first established institutions** in both categories.

📌 **Analysis Output:**

- The **first public university** was established in **Austria** in **1367**, named **University of Vienna**.
- The **first private university** was established in the **Netherlands** in **1575**, named **Vilnius University**.

| Type of University | First University (Historical) | Country     | Year |
| ------------------ | ----------------------------- | ----------- | ---- |
| Public             | University of Vienna          | Austria     | 1367 |
| Private            | Vilnius University            | Netherlands | 1575 |

📊 **Trend Analysis:**

- Before **1800**, **public universities** were more common, reflecting state-driven education.
- After **1800**, the trend shifted — **private universities began to grow more rapidly than public ones**, particularly due to industrialization, globalization, and demand for specialized education.
- This trend continues today, where **private institutions dominate in number** compared to public ones.

---

---

**8. GRE & IELTS Requirements for USA Universities (by Subject)**

- Many U.S. universities require **GRE** and/or **IELTS** depending on the subject area.
- STEM (Science, Technology, Engineering, Mathematics) programs are **more likely** to require **GRE scores**, while non-STEM programs may waive GRE in favor of academic records or professional experience.
- **IELTS (or TOEFL)** is required for almost all international applicants unless they come from an English-speaking country.

📌 **Analysis Output:**

| Subject Area                        | GRE Requirement | IELTS Requirement | Notes                                       |
| ----------------------------------- | --------------- | ----------------- | ------------------------------------------- |
| Computer Science / Data Science     | Mandatory       | Mandatory.        | Strong GRE Quant score needed.              |
| Electrical & Mechanical Engineering | Mandatory       | Mandatory         | High GRE Quantitative section expected.     |
| Business / MBA                      | Sometimes       | Mandatory         | GRE/GMAT may be waived for work experience. |
| Social Sciences                     | Optional        | Mandatory.        | GRE less common.                            |
| Arts & Humanities                   | Rarely          | Mandatory         | Focus more on IELTS/TOEFL.                  |
| Public Health / Education           | Optional        | Mandatory         | GRE waived in many universities.            |

[![Exams Accepted](/images/exam_accepted.png)](https://public.tableau.com/app/profile/md.faisal.ahmed/viz/dataanalysisofglobaluniversities/COUNTRYANDTUTIONFEES?publish=yes)

---

📊 **Key Insights:**

- **GRE** is heavily required in **STEM fields**.
- **IELTS** is nearly universal across subjects.
- Business schools are flexible with GRE/GMAT waivers.
- Humanities and social sciences usually emphasize **language proficiency (IELTS)** rather than GRE.

---

---

# Run and Installation of the Project

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
```


# 📞 Contact / Author

**Project Maintainer:** Md faisal Ahmed  
**Portfolio:** [mdfaisalahmed.online](https://mdfaisalahmed.online/)  
**GitHub:** [@mdfaisalahmed025](https://github.com/mdfaisalahmed025)  
