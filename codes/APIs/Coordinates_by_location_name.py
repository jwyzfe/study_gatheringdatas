import requests

#?&
url = 'http://api.openweathermap.org/geo/1.0/direct'  #물음표 앞까지
params ={'q':'seoul'
        ,'appid':'0a1871fcab444525cdab4c50c6ea9761'} #모양 딕셔너리로 맞추기

response = requests.get(url, params=params)
#print(response.content)

import json
content = json.loads(response.content)

# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["study_finance"]
# collection 작업
collection = database['coordinatesbylocationonname']
result = collection.insert_many(content)