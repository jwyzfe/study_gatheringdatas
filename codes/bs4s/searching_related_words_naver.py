import requests
from bs4 import BeautifulSoup

# URL 설정
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%97%B0%EA%B8%88%EC%A0%80%EC%B6%95'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


def topic():
    materials = soup.select('span.fds-comps-keyword-chip-text')
    topics = [material.text for material in materials]  
    return topics


def search():
    titles = soup.select('span.lnk_tit')
    title_list = [title.text for title in titles]  
    return title_list


print(f'인기주제: {topic()}')
print(f'인기주제 타이틀: {search()}')

    
    