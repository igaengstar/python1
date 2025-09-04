from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')              # 창을 띄우지 않음
options.add_argument('--window-size=1920,1080') # 캡처 크기

browser = webdriver.Chrome(options=options)
browser.get('http://flight.naver.com')

# 캡처 저장
browser.get_screenshot_as_file('data/flight3.png')

# 세션 종료 → 브라우저 프로세스도 닫힘
browser.quit()