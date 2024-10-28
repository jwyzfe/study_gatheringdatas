# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

import requests
from pymongo import MongoClient

def main_1():
# MongoDB 서버에 연결 : Both connect in case local and remote
    client = MongoClient('mongodb://192.168.0.46:27017/')
    # 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
    db = client['ozdatabase']
    # 'users' 컬렉션 선택 (없으면 자동 생성)
    collection = db['oz']
    # 입력할 데이터
    user_data = run()
    # {
    #     'name': 'John Doe',
    #     'age': 30,
    #     'email': 'johndoe@example.com'
    # }
    # 데이터 입력
    result = collection.insert_many(user_data)
    # 입력된 문서의 ID 출력
    print('Inserted user id:', result.inserted_ids)


webdriver_manager_directory = ChromeDriverManager().install()


browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

capabilities = browser.capabilities


browser.get("https://underkg.co.kr/news")


pass

html = browser.page_source
print(html)

#제목, 날짜, 읽은 수, 기사본문
from selenium.webdriver.common.by import By
news_list = browser.find_elements(by=By.CSS_SELECTOR, value='#board_list')


for index, element_bundle in enumerate(news_list):
    title_tag = f'h1 > a'
    title = element_bundle.find_element(By.CSS_SELECTOR, title_tag)
    news_date_tag = f' span.time > span'
    news_date = element_bundle.find_element(By.CSS_SELECTOR, news_date_tag)
    read_count_tag = f'span.readNum > span'
    read_count = element_bundle.find_element(By.CSS_SELECTOR, read_count_tag)
    
    
    result = f'title : {title.text}, date : {news_date.text}, count : {read_count.text}'
    print(result)
    pass
pass