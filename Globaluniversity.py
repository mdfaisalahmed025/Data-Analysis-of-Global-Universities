import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 🌍 List of countries to scrape
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
    "luxembourg", "malta", "monaco", "liechtenstein", "albania", "armenia"
    
    # Asia
    "china", "japan", "south-korea", "singapore", "thailand", "malaysia","hong-kong",
    
    # Middle East
    "saudi-arabia",
    
    # Africa
    "south-africa",
    
    # South America
    "argentina"
]

driver = webdriver.Chrome()
all_data = []

for country in countries:
    print(f"\n🌍 Scraping universities for: {country.upper()}")
    driver.get(f"https://www.jeduka.com/{country}/universities")
    time.sleep(2)

    university_links = []

    # STEP 1: Collect all university links (with pagination)
    while True:
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "list"))
            )
        except:
            print(f"⚠️ No universities found for {country.upper()}... Skipping")
            break

        universities = driver.find_elements(By.CLASS_NAME, "list")
        for uni in universities:
            try:
                link = uni.find_element(By.TAG_NAME, "a").get_attribute("href")
                university_links.append(link)
            except:
                continue

        # Handle pagination
        try:
            pagination = driver.find_element(By.CLASS_NAME, "pagination-numbers")
            next_btn = pagination.find_element(By.XPATH, ".//li[@class='page-numbers-next']/a")
            driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(5)
        except:
            print(f"✔️ Finished collecting all university links for {country.upper()}.")
            break

    print(f"🔗 Total universities found in {country.upper()}: {len(university_links)}")

    # STEP 2: Visit each university page and scrape structured details
    for uni_url in university_links:
        driver.get(uni_url)
        time.sleep(2)

        try:
            uni_name = driver.find_element(By.TAG_NAME, "h1").text.strip()
        except:
            uni_name = "N/A"

        # --- University primary details ---
        try:
            Address = driver.find_element(By.XPATH, '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/h5[1]').text
            location_clean = Address.replace("Location  :", "").replace("Location :", "").strip()
            location_clean = " ".join(location_clean.replace(" ,", ",").split())
        except:
            location_clean = "N/A"

        try:
            country_name = driver.find_element(By.XPATH, '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/h5[2]/span[1]').text
            country_name = country_name.replace("Country :", "").strip()
        except:
            country_name = country

        try:
            university_type = driver.find_element(By.XPATH, '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/h5[2]/span[2]').text
            university_type = university_type.replace("Type :", "").strip()
        except:
            university_type = "N/A"

        try:
            established = driver.find_element(By.XPATH, '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/h5[2]/span[3]').text
            established = established.replace("Established :", "").strip()
        except:
            established = "N/A"

        try:
            university_website = driver.find_element(By.XPATH, '//*[@id="removeinlinestyle"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/ul').text
        except:
            university_website = "N/A"

        # --- Course details ---
        # Step 1: Check if "View All Courses" link exists
        try:
            view_all_link = driver.find_element(By.CSS_SELECTOR, "#view_course_link a").get_attribute("href")
            driver.get(view_all_link)
            time.sleep(2)
        except:
            # "View All Courses" link not found, stay on main page
            pass

        # Step 2: Scrape course boxes
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

            row = {
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
            }
            all_data.append(row)

# Quit driver
driver.quit()

# STEP 3: Save to DataFrame
df = pd.DataFrame(all_data)

# Add exam columns (Yes/No)
exam_list = ["IELTS", "TOEFL", "PTE", "GRE", "GMAT", "SAT"]
for exam in exam_list:
    df[exam] = df["exams_accepted"].apply(lambda x: "Yes" if exam in str(x) else "No")

df.to_csv("universities_courses_multi_country.csv", index=False)
print("✅ Data saved to universities_courses_multi_country.csv")
