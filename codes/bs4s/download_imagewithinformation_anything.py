#저장 위치 
#./news/

#mongodb ip
#mongodb://192.168.0.63:27017/

import requests
from bs4 import BeautifulSoup

url = (f'https://news.naver.com/breakingnews/section/105/227')

from pymongo import MongoClient

def main():
# MongoDB 서버에 연결 : Both connect in case local and remote
    client = MongoClient('mongodb://192.168.0.7:27017/')
    # 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
    db = client['ozdatabase']
    # 'users' 컬렉션 선택 (없으면 자동 생성)
    collection = db['oz']
    # 입력할 데이터
    user_data = run()
    
    result = collection.insert_many(user_data)
    # 입력된 문서의 ID 출력
    print('Inserted user id:', result.inserted_id)



def run():
    respone = requests.get(url)
    soup = BeautifulSoup(respone.text, 'html.parser')
    news_list = soup.select('#newsct div.section_latest_article._CONTENT_LIST._PERSIST_META')
    
    list_result =[]
    for news in news_list:
        title_link = news.select_one('#newsct  div.section_latest_article._CONTENT_LIST._PERSIST_META strong')
        print(title_link.text)
        
        
        
        result ={
            'title':title_link.text,
            
        
        }
        list_result.append(result)
        pass
    
    return list_result
        
        
       
if __name__ == '__main__':
    main()
    pass

