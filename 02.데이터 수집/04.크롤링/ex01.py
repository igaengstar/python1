from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
import time

browser = webdriver.Chrome()
browser.get('http://naver.com/')

btn = browser.find_element(By.CLASS_NAME, 'MyView-module_link_login__HpHMW')

btn.click()

browser.back()
browser.forward()
browser.refresh()

time.sleep(10)