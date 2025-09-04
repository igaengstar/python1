from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)   # 코드 끝나도 브라우저 자동 닫힘 방지
# options.add_argument('headless')                # (주석처리) 창을 띄우지 않고 실행하는 옵션
browser = webdriver.Chrome(options=options)       # 크롬 드라이버 실행
browser.maximize_window()                         # 창 최대화 (화면 요소 안 잘리게)

# 기상청 메인 페이지 접속
url='https://www.weather.go.kr/w/index.do'
browser.get(url)

# [전국] 탭 클릭
el = browser.find_element(By.XPATH, '//a[text()="전국"]')
el.click()
time.sleep(1)   # 탭 전환 후 페이지 로딩 대기

# [예보] 탭 클릭
xpath='//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[3]/a/span'
el = browser.find_element(By.XPATH, xpath)
el.click()
time.sleep(1)   # 탭 전환 후 페이지 로딩 대기

# 지역별 날씨 정보 크롤링 (1~7까지 반복)
for i in range(1, 8):
    # 지역 제목(예: 서울, 부산 등) 링크 XPath
    xpath = f'//*[@id="local-weather"]/div/div[{i}]/h3/a'
    el = browser.find_element(By.XPATH, xpath)

    # 지역 이름 텍스트 추출 (줄바꿈 제거)
    title = el.text.replace('\n','')
    print(f'---------------- {title} ----------------')

    # 지역 클릭 → 해당 지역 날씨 상세 페이지 이동
    el.click()
    time.sleep(1)   # 상세 페이지 로딩 대기

    # 현재 페이지 HTML을 BeautifulSoup으로 파싱
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # 상세 날씨 영역(id=weather) 선택
    local = soup.find('div', {'id':'weather'})

    # 'po_'로 시작하는 class를 가진 dl 태그들 찾기 (지역 날씨 카드들)
    els = local.find_all('dl', {'class':re.compile('^po_')})

    # 각 지역별 날씨 정보 추출
    for el in els:
        name = el.dt.getText()     # 동네/지역 이름
        temp = el.span.getText()  # 기온
        weather = el.i.getText()  # 날씨 설명 (맑음, 흐림 등)
        print(name, temp, weather)