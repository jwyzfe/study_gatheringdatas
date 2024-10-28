import requests
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# MongoDB 연결 및 데이터 저장
client = MongoClient('mongodb://192.168.0.63:27017/')
db = client['ozdatabase']
collection = db['oz2']

# 웹 크롤링 및 데이터 수집
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
browser.get("https://underkg.co.kr/news")

currency_list = browser.find_elements(By.CSS_SELECTOR, '#board_list > div > div')
result = []

for element_bundle in currency_list:
    title_tag = 'h1 > a'
    news_date_tag = 'span.time > span'
    read_count_tag = 'span.readNum > span'
    
    try:
        title = element_bundle.find_element(By.CSS_SELECTOR, title_tag)
        news_date = element_bundle.find_element(By.CSS_SELECTOR, news_date_tag)
        read_count = element_bundle.find_element(By.CSS_SELECTOR, read_count_tag)

        news_item = {
            'title': title.text,
            'date': news_date.text,
            'read_count': read_count.text,
        }
        
        result.append(news_item)
        print(f'title: {title.text}, date: {news_date.text}, count: {read_count.text}')
    except Exception as e:
        print(f"Error while parsing news item: {e}")

browser.quit()

# MongoDB에 데이터 입력
result_insert = collection.insert_many(result)
print('Inserted user id:', result_insert.inserted_ids)
