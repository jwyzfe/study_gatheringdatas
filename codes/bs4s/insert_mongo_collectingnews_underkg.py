import requests
from bs4 import BeautifulSoup

url = (f'https://underkg.co.kr/news')

from pymongo import MongoClient

def main_1():
# MongoDB 서버에 연결 : Both connect in case local and remote
    client = MongoClient('mongodb://192.168.0.46:27017/')
    # 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
    db = client['ozdatabase']
    # 'users' 컬렉션 선택 (없으면 자동 생성)
    collection = db['oz']
    # 입력할 데이터
    user_data = run()
    # {
    #     'name': 'John Doe',
    #     'age': 30,
    #     'email': 'johndoe@example.com'
    # }
    # 데이터 입력
    result = collection.insert_many(user_data)
    # 입력된 문서의 ID 출력
    print('Inserted user id:', result.inserted_ids)



def run():
    respone = requests.get(url)
    soup = BeautifulSoup(respone.text, 'html.parser')
    news_list = soup.select('div.col-inner')
    
    list_result =[]
    for news in news_list:
        title_link = news.select_one('h1.title > a')
        # print(title_link.text)
        # print(f'link : {title_link.attrs["href"]}')
        date = news.select_one('span.time > span')
        #print(f'date : {date.text}')
        r_count = news.select_one('span.readNum')
        #print(f'read count : {r_count.text}')
        
        news_content_url = title_link.attrs["href"]
        respone_content = requests.get(f'{news_content_url}')
        soup_content = BeautifulSoup(respone_content.text, 'html.parser')
        content = soup_content.select_one(f'div.docInner > div.read_body')
        #print(f'content : {content.text}')
        
        result ={
            'title':title_link.text,
            'link':title_link.attrs["href"],
            'date':date.text,
            'read_count':r_count.text,
            'body': content.text
        
        }
        list_result.append(result)
        pass
    
    return list_result
        
        
       
if __name__ == '__main__':
    main_1()
    pass