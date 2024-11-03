import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=800, 800")
#options.add_argument("--incognito")
options.add_argument("--disable-cache")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    ref = 'https://bmstu.ru/bachelor/previous_points'
    driver.get(ref)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    data = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells:
            data.append([cell.text for cell in cells])

    df = pd.DataFrame(data)

    print(df.head())

except Exception as e:
    print(f"An error occurred: {e}")

