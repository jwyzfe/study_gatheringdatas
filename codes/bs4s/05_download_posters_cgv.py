# 이미지 다운로드
# refer : http://www.cgv.co.kr/movies/?lt=1&ft=0
# target image link tag : div.box-image > a > span > img

import requests

# html 파일 요청
response = requests.get('http://www.cgv.co.kr/movies/?lt=1&ft=0')
from bs4 import BeautifulSoup

# html 구조화
soup = BeautifulSoup(response.text, 'html.parser')
image_link_list = soup.select('div.box-image > a > span > img')

# 저장 위치 정하기
import os
folder_name = f'./downloads'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
import urllib.request as req
for index, image_link in enumerate(image_link_list):   #enumerate : 변수와 인덱스를 같이 뽑을때
    image_uri = image_link.attrs['src']     #모아놓은 딕셔너리 뽑아오기
    
    # ./downloads/1.jpg, ./downloads/2.jpg
    req.urlretrieve(image_uri, f'{folder_name}/{index}.jpg')
    pass