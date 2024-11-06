# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

webdriver_manager_directory = ChromeDriverManager().install()

def main():
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    
    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities

    browser.get("https://www.courtauction.go.kr/")
    
    # iframe 전환
    browser.switch_to.frame("indexFrame")
    time.sleep(3)
    
    # 검색 버튼 클릭
    search_button = browser.find_element(by=By.CSS_SELECTOR, value="#main_btn > a > img")  # 검색 버튼의 CSS 선택자
    search_button.click()
    time.sleep(3) 
    
    # 리스트 추출
    number_list = browser.find_elements(by=By.CSS_SELECTOR, value="tr > td:nth-child(2)")
    contents_list = browser.find_elements(by=By.CSS_SELECTOR, value="tr > td:nth-child(4) > div")
    price_list = browser.find_elements(by=By.CSS_SELECTOR, value = "tr > td.txtright")
    
    # 두 리스트를 동시에 순회
    for number, content, price in zip(number_list, contents_list , price_list): 
        print(f'No. : {number.text}, contents : {content.text}, price :{price.text}')
    
    # 브라우저 종료
    browser.quit()

if __name__ == '__main__':
    main()
