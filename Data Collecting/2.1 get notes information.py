import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Read Excel File
file_path = "url.xlsx"
df = pd.read_excel(file_path)
urls = df.iloc[:, 0].tolist()

data = []
number = 0

# Selenium for logging in
driver = webdriver.Edge() # use the browser you like
driver.get('https://www.xiaohongshu.com')
time.sleep(30) # Log in

for url in urls:
    try:
        # bs4 for hashtags only
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        keywords = soup.find('meta', attrs={'name': 'keywords'}).get('content')

        driver.get(url)
        time.sleep(5)

        # Get notes title
        try:
            title_element = driver.find_element(By.XPATH, "//div[@id='detail-title']")
            title = title_element.text.strip()
        # Append No Title if there is no title
        except NoSuchElementException:
            title = "No Title"

        # Get notes content including hashtags; note-content section is designed for both content and hashtags
        note_content = driver.find_element(By.XPATH, "//div[contains(@class, 'note-content')]")
        try:
            content_element = note_content.find_element(By.XPATH, ".//span")
            content = content_element.text.strip()
            # Append No Content if there is no content
        except NoSuchElementException:
            content = "No Content"

        # Get date
        date_element = note_content.find_element(By.XPATH, '//*[@class="bottom-container"]/span')
        date = date_element.text.strip()

        # Get Likes counting
        like_count = driver.find_element(By.XPATH, '//*[@class="like-wrapper like-active"]//span[@class="count"]').text.strip()

        # Get Collects counting
        collect_count = driver.find_element(By.XPATH, '//*[@id="note-page-collect-board-guide"]//span[@class="count"]').text.strip()

        # Get Comments counting
        comment_count = driver.find_element(By.XPATH, '//*[@class="chat-wrapper"]//span[@class="count"]').text.strip()

        # Get author
        author = driver.find_element(By.XPATH,'//*[@id="noteContainer"]/div[4]/div[1]/div/div[1]/a[2]/span').text.strip()
        
    except Exception as e:
        print(f"错误:{e} - URL:{url}")
        continue  # If the URL is invalid, continue to the next URL

    # data is appended to the list
    data.append({
        'URL':url,
        'Author': author,
        'Title':title,
        'Content': content,
        'Keywords': keywords,
        'Likes': like_count,
        'Collects': collect_count,
        'Comments': comment_count,
        'Date': date
    })
        
    number=number+1
    print(f"Success:{number}") # counting

driver.quit()

# Saved
result_df = pd.DataFrame(data)
result_df.to_excel("output.xlsx", index=False)

print("Successfully Saved")
