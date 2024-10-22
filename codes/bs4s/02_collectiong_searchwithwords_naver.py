import requests #url 주소 입력과 해당 html 가져오기


#print(response.text)   #html 컨텐츠

#-naver지식인 검색어 따른 title 수집
#https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B8%88%EC%9C%B5
#span.lnk_tit

#검색어 받기
keyword = input('input search word : ')

#브라우저 주소창
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}'
response = requests.get(url)

from bs4 import BeautifulSoup

#Dom 구조화
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('span.lnk_tit')

for title in titles :
    print(title.text)
    
pass