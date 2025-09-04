#[쿠팡]-[검색어]-[노트북] 1페이지 결과 상품이름, 상품가격
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) # 코드 끝나도 창 유지
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36') 
 # ㄴ크롤링 막힘 방지를 위해 User-Agent 위장
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#검색 페이지 접속
keyword='노트북'
url=f'https://www.gmarket.co.kr/n/search?keyword={keyword}'
browser.get(url)

#스크롤 내려서 전체 로딩
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)

#HTML 파싱 준비
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'lxml')
import re, json

#상품 정보 찾기
items = soup.find_all('div', attrs={'class':'box__item-container'})
cnt = 0
results = [] 

#각 상품별 정보 추출
for idx, item in enumerate(items):
    title=item.find('span', {'class':'text__item'}).getText() # 상품명
    price=item.find('strong', {'class':'text text__value'}).getText()  # 가격
    image='https:' + item.find('img', {'class':'image__item'})['src'] # 이미지 링크
    link = item.a['href'] #링크
    #구매건수(판매량) 추출
    pay_count = item.find('li', {'class':re.compile('list-item__pay-count$')})
    if pay_count:
        pay_count=re.sub('구매|건|,','',pay_count.getText()).strip()
        pay_count=int(pay_count)
    else:
        pay_count=0

    #조건 필터링 (100건 이상 판매 상품만 출력)
    if pay_count >=100:
        cnt += 1
        print(cnt, title, price, image, f'구매건수:{pay_count}')
        
        data = {'no':cnt, 'title':title, 'price':price, 'count':pay_count, 'image':image, 'link':link}
        results.append(data)

with open('02.데이터 수집/data/gmarket.json','w', encoding='utf-8') as file:
    json.dump(results, file, indent='\t', ensure_ascii=False) #리스트, 파일로 덤프, 들여쓰기, 한글깨지는거 방지

#마무리
browser.quit()
print('프로그램종료!')