# Global University Insights

Analyzes global university data to uncover tuition, exam requirements, establishment year, and education trends.

---

## Motivation

In today’s globalized world, pursuing higher education abroad has become an essential step for students seeking academic excellence, international exposure, and career advancement. However, finding the right university and program can be **overwhelming and confusing**, as information is scattered across multiple websites, presented inconsistently, and often lacks clear comparisons.

Students struggle to answer questions like:

- Which countries offer the most cost-effective programs?
- How long do programs last across different universities and subjects?
- What are the common exam requirements for international admissions?

The motivation behind this project is to **simplify and centralize global university information**, enabling students to make **data-driven decisions** about their higher education journey. By combining automation, data analysis, and visualization, the project empowers students and educators with **actionable insights**.

---

## Project Background

**Global University Insights** is a data-driven initiative that leverages **Selenium-based Python scripts** to automatically collect detailed information about universities and programs from [Jeduka.com](https://www.jeduka.com). The collected dataset is then **cleaned, validated, and structured** for analysis.

Key aspects of the project include:

- Gathering information on **university name, type, location, courses, tuition fees, application fees, program duration, accepted exams, and year of establishment**.  
- Converting and standardizing **tuition fees to USD** and **course durations to months** for uniform analysis.  
- Creating **calculated flags for exams accepted** (`IELTS`, `TOEFL`, `PTE`, `GRE`, `GMAT`, `SAT`) to enable easier comparison.  
- Using **Python** (`Pandas`, `Matplotlib`, `Seaborn`, `Plotly`) and **Tableau Public** to generate **interactive visualizations** that highlight global education trends.  

The project provides a **comprehensive overview of higher education worldwide**, offering insights for students, researchers, and policymakers. It helps in understanding **global tuition trends, program durations, university types, and exam requirements**, making it a valuable tool for **data-driven decision-making in international education**.

---

## Project Overview

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

<h2 style="color:red;">🚀 <b>Quick Links</b></h2>

📊 <a href="https://public.tableau.com/app/profile/md.faisal.ahmed/viz/GlobalUniversityInsights/COUNTRYANDTUTIONFEES?publish=yes" style="color:red;"><b>Live Tableau Dashboard</b></a> – Interactive visualization

💻 <a href="https://github.com/mdfaisalahmed025/Data-Analysis-of-Global-Universities" style="color:red;"><b>GitHub Repository</b></a> – Source code and data

📝 <a href="https://www.jeduka.com" style="color:red;"><b>Data Source</b></a> – Jeduka Website

---


## Dataset Validation & Processing

This repository contains the cleaned and processed dataset of universities and courses, along with the steps taken to ensure data quality and consistency.

### Dataset Validation & Processing Results

- **Initial Dataset:** 6,387 records  
- **Final Clean Dataset:** 4,223 records  
- **Missing Values:** Rows with missing values were removed to ensure data integrity  
- **Duplicates:** Removed based on `university_name` and `course` combination  
- **Parse and Convert Tuition Fees to USD:** All tuition fees standardized to USD for consistency across countries  
- **Convert Duration to Months:** Duration values normalized to months for uniformity  
- **Handling Missing Values:** Imputed or removed missing entries to maintain dataset quality  
- **Numeric Column Exploration:** Analyzed numeric columns like tuition fees, application fees, and exam scores for outliers, ranges, and distributions  
- **Categorical Column Exploration:** Analyzed categorical columns like university type, location, and exams accepted for unique values, consistency, and potential normalization  

### Data Quality Checks

- **Completeness:** Checked for missing values across all columns  
- **Uniqueness:** Removed duplicates to ensure unique university-course combinations  
- **Validity:** Verified numeric and categorical columns for valid ranges and formats  
- **Consistency:** Standardized categorical fields for uniformity (e.g., public/private, location names)  
- **Integrity:** Ensured relationships between related fields are valid (e.g., location matches country)


### Data Schema

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


---

## Key Findings

### Exploring Tuition Fees Across Nations

![Exploring Tuition Fees Across Nations](/dashboard_screenshots/Exploring%20Tuition%20Fees%20and%20Across%20Nations.png)

**Findings:**
- The analysis reveals a significant variation in tuition fees across countries.  
- North American and European universities tend to have higher tuition costs, while Asian and African universities generally offer more affordable options.  
- The data highlights clear regional differences — with the USA, UK, and Australia showing the highest average tuition fees.  
- Countries such as South Korea, Malaysia, and Thailan provide cost-effective study opportunities for international students.  

**Insights:**
- Tuition fees directly correlate with the country's economic index and institutional ranking.  
- Students prioritizing affordability can consider Asian and Eastern European institutions without compromising educational quality.

### Global Study Insights — U.S. Course Duration & Asian Tuition Fees

![Global Study Insights — U.S. Course Duration & Asian Tuition Fees](/dashboard_screenshots/global%20study%20insights%20and%20usa%20course%20duration.png)

**Findings:**
- U.S. courses generally range between **24 to 48 months**, aligning with global master’s and bachelor’s program durations.  
- Asian countries display **diverse tuition patterns**, with wide variation depending on subject area and institutional type.  
- **Engineering and medical programs** in Asia show moderate costs with high duration variability.  

**Insights:**
- The comparison highlights how **course length and tuition are interrelated** — longer programs often lead to higher tuition costs.  
- Students seeking **shorter, cost-effective programs** can explore Asian universities offering condensed curricula with competitive academic standards.

### Location vs Year of Establishment

![Location vs Year of Establishment](/dashboard_screenshots/Location%20vs%20Year%20of%20Establishment%20.png)

**Findings:**
- The visualization shows that **older universities** are primarily concentrated in the **USA and Europe**, reflecting a rich history of higher education in these regions.  
- Many **Asian and Middle Eastern universities** were established after **1950**, showing the expansion of global education infrastructure in recent decades.  

**Insights:**
- The establishment trend suggests a **global shift in educational growth**, with developing nations investing heavily in new universities post-2000.  
- **Emerging regions** are catching up in academic infrastructure, signaling **increasing global competition** in higher education.

### Exam Accepted in Different Subjects and Requirements

![Exam Accepted in Different Subjects and Requirements](/dashboard_screenshots/Exam%20Accepted%20in%20Different%20Subject%20and%20Establishment%20.png)

**Findings:**
- Many U.S. universities require **GRE** and/or **IELTS** depending on the subject area.  
- **STEM programs** (Science, Technology, Engineering, Mathematics) are the most likely to demand **GRE scores**, while **non-STEM programs** often waive GRE in favor of academic or professional achievements.  
- **IELTS (or TOEFL)** is a near-universal requirement for international applicants, especially for non-English-speaking countries.  
- Business programs show flexibility, frequently allowing **GRE/GMAT waivers** for applicants with significant work experience.  

**Insights:**
- **GRE** remains a critical requirement for **STEM disciplines**, emphasizing strong quantitative skills.  
- **IELTS** is essential across all programs, demonstrating the importance of language proficiency in academic admissions.  
- Business, social science, and humanities programs are increasingly shifting toward a **holistic evaluation** process, reducing reliance on standardized tests.  
- The data suggests a growing trend among universities to **diversify admission pathways**, making global education more accessible to a broader range of students.


## Tableau Dashboard Analysis

The dataset is visualized using **Tableau Public**. The interactive dashboard allows exploration of global university trends and provides insights for prospective students.

### Key Analysis

**1. Exploring Tuition Fees Across Nations**
- Compare countries based on the number of international programs available.
- Visualize average tuition fees per country to identify cost-effective destinations for overseas study.
- Compare tuition fees among European countries.
- Identify countries with the **highest** and **lowest** study costs.
- Compare tuition fees among Asian study destinations.
- Identify cost-effective options and premium tuition destinations.

**2. Global Study Insights — U.S. Course Duration & Asian Tuition Fees**

- Compare program durations across different universities and subjects.
- Helps students plan based on time commitment for degree completion.

---

**3. Location vs Year of Establishment and University Type**

- Compare the number of **public** and **private** universities across the dataset.
- Highlight the **first established institutions** in both categories.

📌 **Analysis Output:**.

| Type of University | First University (Historical) | Country     | Year |
| ------------------ | ----------------------------- | ----------- | ---- |
| Public             | University of Vienna          | Austria     | 1367 |
| Private            | Vilnius University            | Netherlands | 1575 |

📊 **Trend Analysis:**

- Before **1800**, **public universities** were more common, reflecting state-driven education.
- After **1800**, the trend shifted — **private universities began to grow more rapidly than public ones**, particularly due to industrialization, globalization, and demand for specialized education.
- This trend continues today, where **private institutions dominate in number** compared to public ones.

---

**4. Exam Accepted in Different Subjects and Requirements**

- Many U.S. universities require **GRE** and/or **IELTS** depending on the subject area.
- STEM (Science, Technology, Engineering, Mathematics) programs are **more likely** to require **GRE scores**, while non-STEM programs may waive GRE in favor of academic records or professional experience.
- **IELTS (or TOEFL)** is required for almost all international applicants unless they come from an English-speaking country.

📌 **Analysis Insights:**

| Subject Area                        | GRE Requirement | IELTS Requirement | Notes                                       |
| ----------------------------------- | --------------- | ----------------- | ------------------------------------------- |
| Computer Science / Data Science     | Mandatory       | Mandatory.        | Strong GRE Quant score needed.              |
| Electrical & Mechanical Engineering | Mandatory       | Mandatory         | High GRE Quantitative section expected.     |
| Business / MBA                      | Sometimes       | Mandatory         | GRE/GMAT may be waived for work experience. |
| Social Sciences                     | Optional        | Mandatory.        | GRE less common.                            |
| Arts & Humanities                   | Rarely          | Mandatory         | Focus more on IELTS/TOEFL.                  |
| Public Health / Education           | Optional        | Mandatory         | GRE waived in many universities.            |


---

# Run and Installation of the Project


## 1) Clone Repository

```bash
https://github.com/mdfaisalahmed025/Global-University-Insights.git
cd global-university-Insights
```

## 2) Prerequisites

- **OS:** Windows / macOS / Linux
- **Python:** 3.9+ recommended
- **Google Chrome:** Installed
- **ChromeDriver:** Must be compatible with your installed Chrome version (or use `webdriver-manager`, see below)

## 3) Create a virtual environment (recommended)

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

## 4) Install dependencies

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

# 📞 Contact / Author

**Project Maintainer:** Md Faisal Ahmed  
**Portfolio:** [mdfaisalahmed.online](https://mdfaisalahmed.online/)  
**GitHub:** [@mdfaisalahmed025](https://github.com/mdfaisalahmed025)  
