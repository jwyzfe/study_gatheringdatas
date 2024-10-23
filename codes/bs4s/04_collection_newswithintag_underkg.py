# - underkg.co.kr 있는 news 정보 수집
# refer : https://underkg.co.kr/news
# - 리스트에서 링크와 제목,날짜, 읽은 횟수 가져오기
# #div.col-inner
# 제목, 링크 : h1.title > a
#날짜 : div.new_info > span.time > span
# - 기사내용 확인 uri
# [href]
# - 기사 내용 가져오기
# div.docInner > div.read_body
import requests
from bs4 import BeautifulSoup

url = (f'https://underkg.co.kr/news')

def main():
    respone = requests.get(url)
    soup = BeautifulSoup(respone.text, 'html.parser')
    news_list = soup.select('div.col-inner')
    
    
    for news in news_list:
        title_link = news.select_one('h1.title > a')
        print(title_link.text)
        print(f'link : {title_link.attrs["href"]}')
        date = news.select_one('span.time > span')
        print(f'date : {date.text}')
        r_count = news.select_one('span.readNum')
        print(f'read count : {r_count.text}')
        pass
    
    return
        
        # 기사 내용 가져오기
       
if __name__ == '__main__':
    main()
    pass