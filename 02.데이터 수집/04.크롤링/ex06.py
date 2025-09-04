#[네이버]-[네이버 항공권] 이번달 25일~26일 제주도 항공권 검색
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
)
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 15)

browser.get("https://flight.naver.com")

# (1) 팝업: 있을 때만 닫기
try:
    close_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".FullscreenPopup_suspend, .btn__suspend"))
    )
    close_btn.click()
    time.sleep(0.5)
except Exception:
    pass  # 팝업이 없으면 무시

# (2) 가는 날 열기: 텍스트/태그 변동 대비 (span/both)
go_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//button[.//span[normalize-space()="가는 날"] or normalize-space()="가는 날"]'
    ))
)
go_btn.click()

# (3) 날짜 선택: <b> 직접 클릭 대신 "25일" 버튼의 조상 button을 클릭
def click_day(day_text: str):
    # aria-label 기반(더 안정적): 예) "2025년 9월 25일"
    try:
        day_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, f'//button[contains(@aria-label, "{day_text}일")]'
        )))
    except Exception:
        # fallback: <b>25>를 감싸는 button
        day_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, f'//b[normalize-space()="{day_text}"]/ancestor::button'
        )))
    day_btn.click()

click_day("25")
click_day("26")

# (4) 도착 클릭 (태그 유연성)
arrive_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//button[.//span[normalize-space()="도착"] or normalize-space()="도착"]'
    ))
)
arrive_btn.click()

# (5) "제주" 선택 (추천/인기 목적지 버튼)
jeju_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//button[normalize-space()="제주" or .//span[normalize-space()="제주"]]'
    ))
)
jeju_btn.click()

# (6) 항공권 검색 클릭: span이 아닌 상위 button 클릭
search_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//button[.//span[normalize-space()="항공권 검색"] or normalize-space()="항공권 검색"]'
    ))
)
search_btn.click()

# (7) 결과 대기 후 카드 수집: 부분일치 클래스/role 사용
try:
    # 결과 리스트 영역 등장 대기 (의미 있는 컨테이너로 대기)
    result_wrap = wait.until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, '[class*="domestic_Result__"], [class*="result"], main'
        ))
    )

    cards = wait.until(
        EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, '[class*="domestic_Flight__"], [class*="FlightCard"], article'
        ))
    )

    with open('data/flight.txt', 'w', encoding='utf-8') as file:
        for idx, card in enumerate(cards):
            text = card.text.strip()
            if not text:
                continue
            file.write(f'[{idx}] {text}\n')
            file.write('-' * 50 + '\n')
finally:
    # detach=True면 굳이 닫지 않아도 됨. 닫고 싶으면 아래 유지.
    browser.quit()
    print('프로그램종료!')