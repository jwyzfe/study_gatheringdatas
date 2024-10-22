import requests
from bs4 import BeautifulSoup

url = 'https://finance.daum.net/domestic/exchange'


response = requests.get(url)

# 요청 성공 여부 확인
if response.status_code == 200:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 원자재 종가가 포함된 HTML 요소 찾기
    # 이 부분은 사이트의 HTML 구조에 따라 다를 수 있습니다.
    prices = soup.find_all('span', class_='num')  # 클래스 이름을 실제로 확인하세요

    # 종가 출력
    for price in prices:
        print(price.get_text(strip=True))
else:
    print(f'Failed to retrieve data: {response.status_code}')