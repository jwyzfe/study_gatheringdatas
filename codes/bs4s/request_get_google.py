from bs4 import BeautifulSoup #html 해석

import requests #url 주소 입력과 해당 html 가져오기

#브라우저 주소창
response = requests.get('https://www.google.com/')

print(response.text)

pass