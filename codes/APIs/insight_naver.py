import requests
import json
from pymongo import MongoClient

def main():
    uri = f'https://openapi.naver.com/v1/search/shop'
    params = {'query':'가방'}
    headers = {
        'X-Naver-Client-Id':'Sr8cPEsouiciAFZy8N59'
        ,'X-Naver-Client-Secret':'BZyit1FMeH'
        
    }
    response = requests.get(url=uri,  params=params, headers=headers) #like postman
    if response.status_code == 200:     # 200 == 200
        contents = json.loads(response.text)        #python에서 다루기 편하게 format 수정
        pass
    return

if __name__ == '__main__':
    main()
    pass