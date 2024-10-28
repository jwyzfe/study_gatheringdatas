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

#daum exchange 환율 가져오기
#boxForexes table > tbody > tr : element bundle
#boxForexes table > tbody > tr >td.pL > a   : country_currency
#boxForexes > tbody > tr.first > td:nth-child(3) > span : country_price
from selenium.webdriver.common.by import By
currency_list = browser.find_elements(by=By.CSS_SELECTOR, value='boxForexes table > tbody > tr')

for index, element_bundle in enumerate(currency_list):
    country_currency_tag = f'td.pL > a'
    country_currency = element_bundle.find_element(By.CSS_SELECTOR, country_currency_tag)
    country_price_tag = f' td:nth-child(3) > span'
    country_price = element_bundle.find_element(By.CSS_SELECTOR, country_price_tab)
    
    result = f'currency : {country_currency.text}, price : {country_price.text}'
    print(result)
    pass
    
pass