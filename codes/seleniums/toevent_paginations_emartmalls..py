# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/)
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

from selenium.webdriver.common.by import By
page_list = browser.find_elements(by=By.CSS_SELECTOR, value='#area_itemlist > div.paginate > div > a')

for page_number in range(1, len(page_list)-1):
    pass
pass