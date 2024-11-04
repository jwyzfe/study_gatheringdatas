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
product_name_selector = 'div.s-goods-title'  # 상품명 선택자
product_price_selector = 'div.s-goods-price > strong > span.s-goods-price__number'  # 가격 선택자
product_description_selector = '#m2zoom'  # 상품 상세 설명 선택자

# 페이지 리스트 가져오기
while True:
    time.sleep(3)  # 페이지 로딩 대기

    # 현재 페이지 HTML 가져오기
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 상품 목록에서 각 상품의 정보 수집
    detail_list = soup.select(product_selector)
    for detail in detail_list:
        try:
            detail_uri = detail.attrs['href']
            if not detail_uri.startswith('http'):
                detail_uri = f'https://www.lotteon.com{detail_uri}'  # 절대 경로로 변환
            
            
            
            # 상품 상세 페이지로 요청
            response = requests.get(detail_uri)
            response.raise_for_status()  # 요청 실패 시 예외 발생
            detail_soup = BeautifulSoup(response.text, 'html.parser')

            # 상품명, 가격 및 상세 설명 가져오기
            product_name_element = detail_soup.select_one(product_name_selector)
            product_price_element = detail_soup.select_one(product_price_selector)
            product_description_element = detail_soup.select_one(product_description_selector)

            product_name = product_name_element.get_text(strip=True) if product_name_element else "상품명 정보 없음"
            product_price = product_price_element.get_text(strip=True) if product_price_element else "가격 정보 없음"
            product_description = product_description_element.get_text(strip=True) if product_description_element else "상세 설명 정보 없음"

            # 출력
            print(f"상품명: {product_name}")
            print(f"가격: {product_price}")
            print(f"상세 설명: {product_description}")
            print("-" * 40)  # 구분선 출력

        except Exception as e:
            print(f"정보 수집 중 오류 발생: {e}")  # 오류 메시지 출력

    # 다음 페이지로 이동
    pagination_list = browser.find_elements(by=By.CSS_SELECTOR, value=pagination_selector)
    next_button = None
    for page in pagination_list:
        if 'btn_next' in page.get_attribute('class'):
            next_button = page
            break

    if next_button is not None and "disabled" not in next_button.get_attribute('class'):
        next_button.click()  # 다음 페이지 클릭
    else:
        print("모든 페이지를 완료했습니다.")
        break  # 더 이상 페이지가 없으면 종료


