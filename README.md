# Data Analysis of Global University 

This repository contains a Selenium-based Python script that scrapes **university and course information** from [jeduka.com](https://www.jeduka.com) for multiple countries and exports the results to a CSV.

> **What you get (columns):**
- `university_name`
- `subject`
- `duration`
- `tuition_fees`
- `application_fees`
- `exams_accepted`
- `university_type`
- `location`
- `country`
- `year_of_establish`
- `university_website`
- Auto-generated flags: `IELTS`, `TOEFL`, `PTE`, `GRE`, `GMAT`, `SAT` (Yes/No based on `exams_accepted`)

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