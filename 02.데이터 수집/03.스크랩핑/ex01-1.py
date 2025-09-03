import requests
from bs4 import BeautifulSoup

# 1. 네이버 메인 페이지 주소
url = 'https://www.naver.com/'

# 2. URL 요청 → 응답(response) 객체 받기
res = requests.get(url)

# 3. 요청에 실패(404, 500 등)하면 에러 발생
res.raise_for_status()

# 4. BeautifulSoup 객체로 HTML 파싱 ('lxml' 파서 사용)
soup = BeautifulSoup(res.text, 'lxml')

# 5. <title> 태그 전체 가져오기
title = soup.title
print(1, title)             # <title>네이버 ...</title> 출력
print(2, title.get_text())  # 태그 안의 텍스트만 출력 (예: 'NAVER')

# 6. find() 메서드로도 <title> 태그 가져오기 (동일 결과)
title = soup.find('title')
print(3, title)

# 7. 문서에서 첫 번째 <a> 태그 가져오기
a = soup.a
print(4, a)  # <a ...>...</a> 형태 전체 출력

# 8. <a> 태그 안의 첫 번째 <span> 태그 가져오기
span = a.span
print(5, span.get_text())  # <span> 안의 텍스트만 출력 (예: '네이버')

# 9. <a> 태그의 속성(attribute)들 가져오기 (딕셔너리 형태)
attrs = a.attrs
print(6, attrs, type(attrs))  # 예: {'href': '...', 'class': [...]}

# 10. <a> 태그의 'href' 속성만 가져오기 (링크 주소)
href = a['href']
print(7, href)

# 11. 문서 안의 모든 <a> 태그를 리스트로 가져오기
items = soup.find_all('a')

# 12. 전체 <a> 태그 출력 (for문으로 순회)
for item in items:
    print(item)   # 각각의 <a> ... </a> 태그 전체 출력