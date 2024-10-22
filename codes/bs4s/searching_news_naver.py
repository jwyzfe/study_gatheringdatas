import requests
from bs4 import BeautifulSoup 

def main():
    respone = requests.get(f'https://news.naver.com/breakingnews/section/105/228')
    soup = BeautifulSoup(respone.text, 'html.parser')
    titles_link =  soup.select('#newsct > div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META div.sa_text > a')
    for title_link in titles_link:
        print(f'title : {title_link.text.strip()}')
        news_content_url = title_link.attrs['href']
        print(f'news_content_url : {news_content_url}')
        
        
        #기사 내용 가져오기
        respone_content = requests.get(f'{news_content_url}')
        soup_content = BeautifulSoup(respone_content.text, 'html.parser')
        content = soup_content.select_one(f'#dic_area')
        print(f'content : {content.text.strip()}')
        print(f'--'*10)
        pass
    return

if __name__=='__main__':
    main()
    pass