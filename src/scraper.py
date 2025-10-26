import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 🌍 Countries to scrape
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
    "argentina"
]

# Initialize Chrome driver
driver = webdriver.Chrome()
all_data = []

for country in countries:
    print(f"\n🌍 Scraping universities for: {country.upper()}")

    university_links = []
    page = 1

    # STEP 1️⃣: Collect all university links page by page
    while True:
        url = f"https://www.jeduka.com/{country}/universities/1-{page}"
        print(f"\n🔎 Visiting page {page}: {url}")
        driver.get(url)
        time.sleep(2)

        # Check if page not found or empty
        if "Page Not Found" in driver.page_source or "404" in driver.title:
            print(f"🛑 Page {page} not found. Stopping pagination.")
            break

        try:
            universities = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "list"))
            )
            if not universities:
                print(f"✔️ No universities found on page {page}. Stopping pagination.")
                break

            count_before = len(university_links)
            for uni in universities:
                try:
                    link = uni.find_element(By.TAG_NAME, "a").get_attribute("href")
                    if link and link not in university_links:
                        university_links.append(link)
                except:
                    continue

            count_after = len(university_links)
            new_links = count_after - count_before

            if new_links == 0:
                print(f"⚠️ No new universities on page {page}. Assuming last page.")
                break

            print(f"📄 Page {page}: {new_links} new universities collected.")
            page += 1
            time.sleep(2)

        except Exception as e:
            print(f"❌ Error on page {page}: {e}")
            break

    print(f"\n🔗 Total universities found in {country.upper()}: {len(university_links)}")

    # STEP 2️⃣: Visit each university and scrape details
    for i, uni_url in enumerate(university_links, start=1):
        print(f"\n🏫 [{i}/{len(university_links)}] Scraping: {uni_url}")
        driver.get(uni_url)
        time.sleep(2)

        try:
            uni_name = driver.find_element(By.TAG_NAME, "h1").text.strip()
        except:
            uni_name = "N/A"

        # --- Basic Details ---
        try:
            Address = driver.find_element(
                By.XPATH,
                '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/h5[1]'
            ).text
            location_clean = Address.replace("Location :", "").replace("Location  :", "").strip()
        except:
            location_clean = "N/A"

        try:
            country_name = driver.find_element(
                By.XPATH,
                '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/h5[2]/span[1]'
            ).text
            country_name = country_name.replace("Country :", "").strip()
        except:
            country_name = country

        try:
            university_type = driver.find_element(
                By.XPATH,
                '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/h5[2]/span[2]'
            ).text
            university_type = university_type.replace("Type :", "").strip()
        except:
            university_type = "N/A"

        try:
            established = driver.find_element(
                By.XPATH,
                '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/h5[2]/span[3]'
            ).text
            established = established.replace("Established :", "").strip()
        except:
            established = "N/A"

        try:
            university_website = driver.find_element(
                By.XPATH,
                '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/ul'
            ).text
        except:
            university_website = "N/A"

        # --- Course Details ---
        try:
            view_all_link = driver.find_element(By.CSS_SELECTOR, "#view_course_link a").get_attribute("href")
            driver.get(view_all_link)
            time.sleep(2)
        except:
            pass

        course_boxes = driver.find_elements(By.CLASS_NAME, "box")

        if len(course_boxes) == 0:
            print(f"⚠️ No courses found for {uni_name}")
            continue

        for course in course_boxes:
            try:
                subject = course.find_element(By.TAG_NAME, "h4").text.strip()
            except:
                subject = "N/A"

            try:
                duration = course.find_element(By.XPATH, ".//table/tbody/tr[2]/td[1]").text.replace("Duration:", "").strip()
            except:
                duration = "N/A"

            try:
                tuition = course.find_element(By.XPATH, ".//table/tbody/tr[2]/td[2]").text.replace("Tuition Fee:", "").strip()
            except:
                tuition = "N/A"

            try:
                application_fees = course.find_element(By.XPATH, ".//table/tbody/tr[2]/td[3]").text.replace("Application fees:", "").strip()
            except:
                application_fees = "N/A"

            try:
                exams = course.find_element(By.XPATH, ".//table/tbody/tr[2]/td[4]").text.replace("Exams Accepted:", "").strip()
            except:
                exams = "N/A"

            all_data.append({
                "university_name": uni_name,
                "subject": subject,
                "duration": duration,
                "tuition_fees": tuition,
                "application_fees": application_fees,
                "exams_accepted": exams,
                "university_type": university_type,
                "location": location_clean,
                "country": country_name,
                "year_of_establish": established,
                "university_website": university_website
            })

# Close browser
driver.quit()

# STEP 3️⃣: Save data to CSV
df = pd.DataFrame(all_data)
exam_list = ["IELTS", "TOEFL", "PTE", "GRE", "GMAT", "SAT"]
for exam in exam_list:
    df[exam] = df["exams_accepted"].apply(lambda x: "Yes" if exam in str(x) else "No")

df.to_csv("scraped_datas.csv", index=False)
print("\n✅ Data saved successfully to scraped_data.csv")
