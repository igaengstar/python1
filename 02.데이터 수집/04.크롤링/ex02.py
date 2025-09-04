from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get('http://naver.com/')

# 로그인 버튼 클릭
btn = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, '로그인'))
)
btn.click()
time.sleep(2)

# 아이디 / 비밀번호 입력
id_box = browser.find_element(By.ID, 'id')
id_box.send_keys('leekyungyen')

pw_box = browser.find_element(By.ID, 'pw')
pw_box.send_keys('여기에_비밀번호')

time.sleep(2)

# 로그인 버튼 클릭 (괄호 반드시!)
login = browser.find_element(By.ID, 'log.login')
login.click()

time.sleep(100)  # 로그인 후 화면 유지