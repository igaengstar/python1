from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #브라우저창이 항상 오픈
browser = webdriver.Chrome(options=options)

browser.maximize_window()

url = 'http://flight.naver.com'
browser.get(url)

browser.get_screenshot_as_file('data/flight.png') #화면을 캡처해서 파일로 저장

browser.quit()