from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Log in
driver = webdriver.Edge()
url = 'https://www.xiaohongshu.com/search_result?keyword=xx'
driver.get(url)
time.sleep(30)

# New list for URLs
url_list = []

def scroll_and_collect_urls():
    # scroll and get new notes
    previous_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Get URL on this page
        url_texts = driver.find_elements(By.CSS_SELECTOR, 'a.cover.ld.mask')
        for url_text in url_texts:
            href = url_text.get_attribute('href')
            if href:
                url_list.append(href)

        # Scroll
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        
        # Check if there is new note
        current_height = driver.execute_script("return document.body.scrollHeight")
        if current_height == previous_height:
            break
        previous_height = current_height

# Collect URLs
scroll_and_collect_urls()
url_list = list(set(url_list))
url_list.sort()

print(f"URL number: {len(url_list)}")

for url in url_list:
    print(url)

# Write in a new Excel file
df = pd.DataFrame(url_list, columns = ['URLs'])
df.to_excel("url1.xlsx", index = False)

driver.quit()
