import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pymongo import MongoClient

# MongoDB 연결 함수
def connect_mongo():
    client = MongoClient('mongodb://192.168.0.63:27017/')
    return client['ozdatabase']['oz3']  # 데이터베이스와 컬렉션 반환

# 감정 분석 API 호출 함수
def analyze_sentiment(text):
    sentiment_api_url = 'https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze'
    headers = {
        'X-NCP-APIGW-API-KEY-ID': 'nivpuqkp2t',
        'X-NCP-APIGW-API-KEY': 'EIs9KbvW1QiAMSfkmAJ3UfYRy5q8Meh02OotsFhN',
        'Content-Type': 'application/json'
    }
    response = requests.post(
        url=sentiment_api_url,
        headers=headers,
        data=json.dumps({"content": text})
    )
    if response.status_code == 200:
        return response.json().get('document', {}).get('sentiment', 'unknown')
    else:
        print("감정 분석 API 요청 오류:", response.status_code)
        return 'unknown'

# 댓글 수집 함수
def collect_comments(url, browser):
    browser.get(url)
    time.sleep(3)  # 페이지 로드 대기

    # 댓글 섹션 로드 대기
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body'))
    )

    # 스크롤하며 댓글을 로드
    element_body = browser.find_element(By.TAG_NAME, 'body')
    comment_data_list = []

    # 페이지를 5번 스크롤하며 댓글 로드
    for _ in range(5):
        element_body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # 스크롤 후 댓글 로드 대기

        # 현재 페이지에 로드된 댓글 찾기
        comments = browser.find_elements(By.CSS_SELECTOR, 'ytd-comment-thread-renderer')

        for comment in comments:
            try:
                # 댓글 텍스트 추출
                text = comment.find_element(By.CSS_SELECTOR, '#content-text').text

                # 감정 분석 API 호출
                sentiment = analyze_sentiment(text)

                # 데이터 저장
                comment_item = {
                    'comment': text,
                    'sentiment': sentiment  # 긍정/부정/중립
                }

                # MongoDB에 데이터 추가
                comment_data_list.append(comment_item)

            except Exception as e:
                print("댓글 추출 오류:", e)
                continue

    return comment_data_list

# 메인 실행 함수
def main():
    url = "https://www.youtube.com/watch?v=aRrteDRC3kQ&t=31s"
    
    # 브라우저 설정 및 드라이버 실행
    webdriver_manager_directory = ChromeDriverManager().install()
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

    # 댓글 수집
    comment_data_list = collect_comments(url, browser)

    # MongoDB 연결
    collection = connect_mongo()

    # MongoDB에 데이터 삽입
    if comment_data_list:
        collection.insert_many(comment_data_list)

    # 크롤링 결과 출력
    for idx, item in enumerate(comment_data_list, 1):
        print(f"{idx}: {item}")

    # 브라우저 닫기
    browser.quit()

if __name__ == '__main__':
    main()
