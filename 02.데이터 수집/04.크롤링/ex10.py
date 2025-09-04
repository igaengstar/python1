from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time
import requests
import os

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)   # 코드 끝나도 브라우저 자동 닫힘 방지
# options.add_argument('headless')                # (주석처리) 창을 띄우지 않고 실행하는 옵션
browser = webdriver.Chrome(options=options)       # 크롬 드라이버 실행
browser.maximize_window()                         # 창 최대화 (화면 요소 안 잘리게)

# 커피빈 매장찾기 메인 페이지 접속
url='https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

browser.execute_script("storePop2('31')")
time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'lxml')

#매장이름
name = soup.select('div.store_txt > h2')[0].string
info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
#address = list(info[2])[0].string
address = info[2].getText()
phone = info[3].string
print('매장이름', name)
print('매장주소', address)
print('매장전화', phone)

#사진
import requests
import os
path ='data/store'
if not os.path.exists(path):
    os.mkdir(path)

imgs = soup.select('div.slick-slide > img')
for img in imgs:
    src = 'https://www.coffeebeankorea.com/' + img.attrs['src']
    print(src)
    index = src.rindex('/')
    file_name = src[index:]
    print(file_name)

    #이미지저장
    with open(path + file_name, 'wb') as file:
        res= requests.get(src)
        file.write(res.content)