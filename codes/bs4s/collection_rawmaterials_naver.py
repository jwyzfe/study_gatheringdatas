import requests
from bs4 import BeautifulSoup

# URL 설정
url = 'https://finance.naver.com/marketindex/?tabSel=materials#tab_section'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
materials = soup.select('td.tit')

for material in materials:
    material.text
    
    

    # 결과 출력
    print(f'원자재: {material.text}')
    