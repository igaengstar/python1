from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time, csv

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # 크롬 창 자동 종료 방지
#options.add_argument('headless')  # 브라우저 창 숨기기 옵션

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = 'https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')
ul = soup.find('ul', {'id': 'storeListUL'})  # 매장 목록이 담긴 ul 태그
stores = ul.find_all('li')  # 매장별 li 태그 모으기

stores_list = []  # 매장 정보를 담을 리스트

for store in stores:
    # 매장명, 주소, 전화번호 추출
    name = store.find('p', {'class': 'name'}).find('span').contents[0].strip()
    address = store.find('p', {'class': 'address'}).get_text().strip()
    tel = store.find('p', {'class': 'tel'}).get_text().strip()
    print(name, address, tel)  # 콘솔 출력
    stores_list.append([name, address, tel])  # 리스트에 추가

# CSV 파일 저장 (for문 밖에서 실행)
with open('커피빈/커피빈.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Tel'])
    writer.writerows(stores_list)