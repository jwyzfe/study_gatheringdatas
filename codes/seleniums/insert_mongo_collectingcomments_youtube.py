from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pymongo import MongoClient

# MongoDB 연결 및 데이터 저장
client = MongoClient('mongodb://192.168.0.63:27017/')
db = client['ozdatabase']
collection = db['oz3']

# 브라우저 설정 및 드라이버 실행
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# YouTube 페이지 열기
browser.get("https://www.youtube.com/watch?v=aRrteDRC3kQ&t=31s")
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
    comments = browser.find_elements(By.CSS_SELECTOR, 'ytd-comment-thread-renderer') #태그 사용

    for comment in comments:
        try:
            # 댓글 텍스트 추출
            writer = comment.find_element(By.CSS_SELECTOR, '#author-text').text
            date = comment.find_element(By.CSS_SELECTOR, '#published-time-text').text
            text = comment.find_element(By.CSS_SELECTOR, '#content-text').text
            like_count = comment.find_element(By.CSS_SELECTOR, '#vote-count-middle').text
            bad_count = 0

            # 데이터 저장
            comment_item = {
                'comment writer': writer,
                'comment date': date,
                'comment': text,
                'number of like': like_count,
                'number of bad': bad_count,
            }

            # comment_data_list에 항목 추가
            comment_data_list.append(comment_item)

        except Exception as e:
            print("댓글 추출 오류:", e)
            continue

# MongoDB에 데이터 입력
result = []  # 빈 리스트 초기화
for item in comment_data_list:
    result.append(item)  # 각 항목을 result 리스트에 추가

# 크롤링 결과 출력
for idx, item in enumerate(comment_data_list, 1):
    print(f"{idx}: {item}")

# MongoDB에 데이터 삽입

result_insert = collection.insert_many(result)
    


# 브라우저 닫기
browser.quit()



