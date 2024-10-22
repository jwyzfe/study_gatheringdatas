# underkg.co.kr에 있는news정보 수집
#refer : https://underkg.co.kr/news
# *리스트에서 링크와 제목 가져오기*
# #board_list > div > div:nth-child(2) > div > h1 > a[]
# #board_list > div > div:nth-child(2) > div > h1 > a[href]
# #board_list > div > div:nth-child(2) > div > h1 > [href]
# ✨✨#board_list  h1 > a
# ✨기사내용 확인 url
# [href[
# .✨기사 내용 가져요기


import requests
from bs4 import BeautifulSoup 

def main():
    respone = requests.get(f'https://underkg.co.kr/news')
    soup = BeautifulSoup(respone.text, 'html.parser')
    titles_link =  soup.select('#board_list h1 > a')
    for title_link in titles_link:
        print(f'title : {title_link.text}')
        news_content_url = title_link.attrs['href']
        print(f'news_content_url : {news_content_url}')
        
        
        #기사 내용 가져오기
        respone_content = requests.get(f'{news_content_url}')
        soup_content = BeautifulSoup(respone_content.text, 'html.parser')
        content = soup_content.select_one(f'div.docInner > div.read_body')
        print(f'content : {content.text}')
        print(f'--'*10)
        pass
    return

if __name__=='__main__':
    main()
    pass