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

> **Optional (recommended):** Use `webdriver-manager` to auto-manage ChromeDriver:
```bash
pip install webdriver-manager
```

---

## 2) Project Setup (Step-by-Step)

1. **Create a project folder** and save your script (e.g., `scrape_jeduka.py`) with the code you shared.
2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -U pip
   pip install selenium pandas
   # optional
   pip install webdriver-manager
   ```
4. **Install ChromeDriver (if not using webdriver-manager)**  
   - **Windows:** Download a matching version from the official site and put `chromedriver.exe` on PATH.  
   - **macOS (Homebrew):**
     ```bash
     brew install --cask chromedriver
     ```
     If you see **“Apple could not verify 'chromedriver'”**, either:
     - Right‑click the app → **Open** (bypass Gatekeeper once), or
     - Remove the quarantine flag (adjust path as needed):
       ```bash
       sudo xattr -d com.apple.quarantine /usr/local/bin/chromedriver
       ```
   - **Linux (Debian/Ubuntu):**
     ```bash
     sudo apt-get update
     sudo apt-get install chromium-driver
     ```

---

## 3) Run the scraper

From the folder containing your script:
```bash
python scrape_jeduka.py
```

When it finishes, it will create:
```
universities_courses_multi_country.csv
```
in the current directory.

---

## 4) Configuration & Customization

### A. Country list
Your script already includes a list of countries. **Make sure every item is separated by a comma.**  
Below is a **corrected** example (note the comma after `"armenia"`), which you can paste into your script if needed:

```python
countries = [
    # North America
    "usa", "canada",

    # Oceania
    "australia", "new-zealand",

    # Europe
    "uk", "germany", "france", "italy", "spain", "portugal", "netherlands",
    "belgium", "switzerland", "austria", "sweden", "norway", "denmark",
    "finland", "ireland", "czech-republic", "hungary", "greece", "iceland",
    "slovakia", "slovenia", "croatia", "estonia", "latvia", "lithuania",
    "luxembourg", "malta", "monaco", "liechtenstein", "albania", "armenia",

    # Asia
    "china", "japan", "south-korea", "singapore", "thailand", "malaysia", "hong-kong",

    # Middle East
    "saudi-arabia",

    # Africa
    "south-africa",

    # South America
    "argentina",
]
```

### B. Headless mode (run without opening a browser window)
Add these lines before creating the driver:
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")     # headless Chrome
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)
```

### C. Use webdriver-manager (skip manual ChromeDriver installs)
Replace your `driver = webdriver.Chrome()` with:
```python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

### D. Tuning waits & pacing
- The script uses both `WebDriverWait` and `time.sleep`.  
  If you get timeouts, increase waits or add small random sleeps to be polite to the server:
  ```python
  import random, time
  time.sleep(random.uniform(1.0, 2.5))
  ```

### E. Selectors (in case the site changes)
The script relies on:
- University cards: elements with class **`list`**
- Pagination: `.pagination-numbers` → `li.page-numbers-next a`
- Course boxes: elements with class **`box`**
- Various **XPath** selectors for university details

If the site layout changes, update these selectors accordingly.

---

## 5) Output Details

- **CSV file:** `universities_courses_multi_country.csv`
- **Exam columns:** The script adds `IELTS`, `TOEFL`, `PTE`, `GRE`, `GMAT`, `SAT` as **Yes/No** flags based on whether each keyword appears in `exams_accepted`.

Example logic used:
```python
exam_list = ["IELTS", "TOEFL", "PTE", "GRE", "GMAT", "SAT"]
for exam in exam_list:
    df[exam] = df["exams_accepted"].apply(lambda x: "Yes" if exam in str(x) else "No")
```

---

## 6) Troubleshooting

- **SyntaxError near the country list**  
  Ensure each string is comma-separated (especially after `"armenia"`).

- **Chrome/ChromeDriver version mismatch**  
  Update Chrome, then update ChromeDriver to the matching major version (or switch to `webdriver-manager`).

- **“Apple could not verify 'chromedriver'” on macOS**  
  Use the **Open** workaround or remove the quarantine flag (see above).

- **Timeouts / “NoSuchElementException”**  
  Increase `WebDriverWait` timeouts; add small sleeps; verify selectors (the site may have changed).

- **Empty CSV or missing courses**  
  Some universities may not list courses or block automated access. Confirm the **“View All Courses”** link logic and `class="box"` elements.

- **Blocking / 403 / Captcha**  
  Slow down requests, add jittered sleeps, avoid long continuous runs, and consider rotating user agents or IPs if necessary (while following the site’s terms).

---

## 7) Good‑citizen scraping

- Review and respect the website’s **Terms of Service** and **robots.txt**.
- Add polite delays; avoid sending too many requests too quickly.
- Use the data responsibly and credit the source when appropriate.

---

## 8) Optional enhancements

- Save incremental checkpoints (write partial CSV after each country).
- Add logging (`logging` module) for progress and errors.
- Resume logic if the script stops mid-run.
- Convert `time.sleep` calls to more robust, condition-based waits.

---

## 9) License & attribution

Use and adapt this script for educational or research purposes. If you redistribute, please keep attribution to the original author(s).


---
# How to Clone and Run This Repository

## 1️⃣ Clone the repository
Open your terminal (or Git Bash on Windows) and run:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
```

Replace `<your-username>` and `<repo-name>` with your GitHub username and repository name.  

Then, navigate into the cloned folder:

```bash
cd <repo-name>
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

## 4️⃣ Run the scraper

```bash
python scrape_jeduka.py
```

The script will scrape universities and courses for all countries in the list.  
After it finishes, the output CSV will be:

```
universities_courses_multi_country.csv
```

## 5️⃣ Optional: Run headless (no browser window)

Modify the scraper to include:

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
```

## 6️⃣ Notes & Tips
- Make sure ChromeDriver matches your Chrome version or use `webdriver-manager`.
- Slow down scraping by adjusting `time.sleep()` to avoid being blocked.
- Check that all country URLs in the `countries` list are correct and comma-separated.
