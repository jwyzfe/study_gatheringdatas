import requests #url 주소 입력과 해당 html 가져오기

#브라우저 주소창
response = requests.get('https://finance.naver.com/marketindex/')

#print(response.text)   #html 컨텐츠

#-환율 변동 가격
#refer : https://finance.naver.com/marketindex/
#<span class="value">1,374.80</span>
#span.value
from bs4 import BeautifulSoup
response = requests.get('https://www.google.com/')

#Dom 구조화
soup = BeautifulSoup(response.text, 'html.parser')

currency_prices = soup.select('span.value')
type(currency_prices)

for  currency in currency_prices:
    print(currency)
    

pass