import requests
from bs4 import BeautifulSoup

# URL 설정
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%97%B0%EA%B8%88%EC%A0%80%EC%B6%95'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


def topic():
    materials = soup.select('span.BqZGMHlcQKUqdI_4Wl43')
    topics = [material.text for material in materials]  
    return topics

# 인기 주제에 대한 타이틀 추출
def search():
    titles = soup.select('span.lnk_tit')
    title_list = [title.text for title in titles]  
    return title_list

# 결과 출력
print(f'인기주제: {topic()}')
print(f'인기주제 타이틀: {search()}')

    
    