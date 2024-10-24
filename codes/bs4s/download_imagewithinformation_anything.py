#저장 위치 
#./news/

#mongodb ip
#mongodb://192.168.0.63:27017/


import requests
from bs4 import BeautifulSoup
import os
import urllib.request as req

url = 'https://news.naver.com/breakingnews/section/105/227'

def main():
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    news_list = soup.select('#newsct div.section_latest_article._CONTENT_LIST._PERSIST_META')

    for news in news_list:
        title = news.select_one('#newsct  div.section_latest_article._CONTENT_LIST._PERSIST_META strong')
        print(f'Title: {title.text}')
        
    download_images(soup)
    
    return

def download_images(soup):
    
    image_link_list = soup.select('#newsct  img')

    
    folder_name = './news'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    
    for index, image_link in enumerate(image_link_list):
        image_uri = image_link.attrs['data-src']  # img 태그의 src 속성 가져오기
        req.urlretrieve(image_uri, f'{folder_name}/{index}.jpg')

if __name__ == '__main__':
    main()
