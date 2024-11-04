from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 웹사이트 열기
browser.get("https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EB%94%A5%EB%94%94%ED%81%AC&mallId=1")

# 페이지 이동 및 정보 수집
pagination_selector = '#s-search-app > div.srchResultProductArea > div.s-goods-layout.s-goods-layout__grid > div.srchPagination > a'
product_selector = '#s-search-app .s-goods__thumbnail a'  # 썸네일을 포함한 링크

# 페이지 리스트 가져오기
page_list = browser.find_elements(by=By.CSS_SELECTOR, value=pagination_selector)

for index in range(1, len(page_list)):
    time.sleep(3)  # 페이지 로딩 대기

    pagination_list = browser.find_elements(by=By.CSS_SELECTOR, value=pagination_selector)
    pagination_tag = pagination_list[index]

    btn_next = pagination_tag.get_attribute('class')
    if btn_next == 'btn_next':
        break
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.keys import Keys
    # 상세 정보 수집
    ActionChains(browser).key_down(Keys.END).perform()
    pagination_tag.click()  # 클릭 메서드 호출
    time.sleep(2)  # 페이지 로딩 대기

    # HTML 가져오기
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # 상세 정보 수집
    detail_list = soup.select(product_selector)
    for detail in detail_list:
        try:
            detail_uri = detail.attrs['href']  # href 속성 가져오기
            response = requests.get(detail_uri)
            print(response.text)  # 응답 내용 출력
        except KeyError as e:
            print(f"속성을 찾을 수 없음: {e}")
        except Exception as e:
            print(f"요청 실패: {e}")

# 대기 후 브라우저 종료
input("Press Enter to close the browser...")
browser.quit()
