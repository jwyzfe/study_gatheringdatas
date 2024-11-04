import requests
import pydeck as pdk
import json
import pandas as pd
from pymongo import MongoClient

class SeoulBikeMap:
    def __init__(self):
        self.uri = 'http://openapi.seoul.go.kr:8088/526265697761697937315370727a44/json/bikeList/1/5/'  # 인증키는 빼는게 좋음
        self.data_bikes = {
            "stationName": [],
            "parkingBikeTotCnt": [],
            "stationLatitude": [],
            "stationLongitude": [],
            "rackTotCnt":[],
            "stationId":[],
            
        }
    
    def fetch_data(self):
        response = requests.get(url=self.uri)#
        if response.status_code == 200:#
            print(f'{response.text}')#
            data_dict = json.loads(response.text)#
            return data_dict
        
    
    def parse_data(self, data_dict):
        
        for row in data_dict['rentBikeStatus']['row']:
            print(f'stationName : {row["stationName"]}, parkingBikeTotCnt : {row["parkingBikeTotCnt"]}, '
                  f'stationLatitude : {row["stationLatitude"]}, stationLongitude : {row["stationLongitude"]}, '
                  f'rackTotCnt : {row["rackTotCnt"]}, stationId : {row["stationId"]}')
            self.data_bikes['stationName'].append(row["stationName"])
            self.data_bikes['parkingBikeTotCnt'].append(int(row["parkingBikeTotCnt"]))
            self.data_bikes['stationLatitude'].append(float(row["stationLatitude"]))
            self.data_bikes['stationLongitude'].append(float(row["stationLongitude"]))
            self.data_bikes['rackTotCnt'].append(int(row["rackTotCnt"]))
            self.data_bikes['stationId'].append(row["stationId"])

    def create_map(self):
        
        df = pd.DataFrame(self.data_bikes)
        
        #Scatter plot 그리기
        layer = pdk.Layer(
            "ScatterplotLayer",
            df,
            get_position=["stationLongitude", "stationLatitude"],
            get_fill_color=["255-shared", "255-shared", "255"],  
            get_radius="60 * parkingBikeTotCnt / 100",  # 주차 대수에 따라 반경 설정
            pickable=True,
        )
        
        # 서울의 중심점 좌표 구해 지도 만들기
        lat_center = df["stationLatitude"].mean()
        lon_center = df["stationLongitude"].mean()
        initial_view = pdk.ViewState(latitude=lat_center, longitude=lon_center, zoom=10)
        
        # 지도 생성 및 저장
        map = pdk.Deck(layers=[layer], initial_view_state=initial_view, 
                       tooltip={
                           "text": "대여소: {stationName}\n현재 주차 대수: {parkingBikeTotCnt}\n대여소ID: {stationId}\n자전거주차총건수: {rackTotCnt}"})
        map.to_html("./seoul_bikes.html")
        print("지도가 seoul_bikes.html로 저장되었습니다.")

# MongoDB 작업
        self.save_to_mongo(df)

    def save_to_mongo(self, df):
        client = MongoClient('mongodb://192.168.0.63:27017/')
        db = client['ozdatabase']
        collection = db['oz4']
        # 데이터 삽입
        results = collection.insert_many(df.to_dict(orient='records'))
        print(f"{len(results.inserted_ids)}개의 문서가 MongoDB에 저장되었습니다.")


    def run(self):
        
        data_dict = self.fetch_data()
        if data_dict:
            self.parse_data(data_dict)
            self.create_map()

if __name__ == '__main__':
    bike_map = SeoulBikeMap()
    bike_map.run()
    
    
from pymongo import MongoClient

