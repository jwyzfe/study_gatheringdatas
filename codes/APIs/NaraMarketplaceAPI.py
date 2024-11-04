# import requests

# #?&&&&
# url = 'https://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'
# params ={'serviceKey' : 'zOzxdWBmYUJTAzO1yRAowID2oCBwM9kKpkjQGjbWS6XhI2dee1p1jbeAfIPwg8MpAgBUvF2DBgGUAErPiQGHNQ%3D%3D' ,
#          'pageNo' : '1',
#          'numOfRows' : '10',
#          'type' : 'json',
#          'bidNtceBgnDt' : '201712010000',
#          'bidNtceEndDt' : '201712312359'}

# response = requests.get(url, params=params)
# print(response.content)


# 데이터명 : 조달청_나라장터 공공데이터개방표준서비스
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests
# url 주소 변수 지정
url = 'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo?serviceKey=ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw==&pageNo=1&numOfRows=10&type=json&bidNtceBgnDt=201712010000&bidNtceEndDt=201712312359'
pass
# respose라는 변수로 받음
response = requests.get(url)
pass
# response의 내용을 출력
print(response.content)