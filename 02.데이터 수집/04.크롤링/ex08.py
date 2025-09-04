from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)   # 디버깅 시 브라우저 자동 닫힘 방지
options.add_argument('headless')                   # 창을 띄우지 않고 실행 (백그라운드 모드)
browser = webdriver.Chrome(options=options)        # 크롬 드라이버 실행
browser.maximize_window()                          # 창 최대화 (레이아웃 깨짐 방지)

# 기상청 메인 페이지 접속
url='https://www.weather.go.kr/w/index.do'
browser.get(url)

# [전국] 탭 클릭
el = browser.find_element(By.XPATH, '//a[text()="전국"]')
el.click()
time.sleep(2)   # 페이지 전환 대기

# [어제] 탭 클릭
xpath='//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[1]/a/span'
el = browser.find_element(By.XPATH, xpath)
el.click()
time.sleep(2)   # 데이터 로딩 대기

# 현재 페이지 HTML을 BeautifulSoup으로 파싱
soup = BeautifulSoup(browser.page_source, 'lxml')

# id=minmax 영역(최고/최저 기온 정보)을 찾음
local = soup.find('div', {'id':'minmax'})

# class가 po2_로 시작하는 dl 태그들 선택 (지역별 날씨 정보 블록)
els = local.find_all('dl', {'class':re.compile('^po2_')})

# 각 지역별 최고/최저 기온 출력
for idx, el in enumerate(els):
    name = el.dt.getText()                                # 지역명
    red = el.find('span', {'class':'red'}).getText()      # 최고기온
    blue = el.find('span', {'class':'blue'}).getText()    # 최저기온
    print(idx+1, name, red, blue)