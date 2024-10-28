# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

webdriver_manager_directory = ChromeDriverManager().install()


browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

capabilities = browser.capabilities


browser.get("https://finance.daum.net/domestic/exchange")


pass

html = browser.page_source
print(html)

from selenium.webdriver.common.by import By
currency_prices = browser.find_elements(by=By.CSS_SELECTOR, value='td.pR > span.num' )

for number, currency_price in enumerate (currency_prices):  #몇번째라인 확인
    print(f'number : {number}, exchange percent : {currency_price.text}')
    pass
pass