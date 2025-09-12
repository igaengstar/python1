# 도서 검색 프로그램 (카카오 책 검색 API 사용)
import requests
import os

# 도서 검색 함수
def getBooks(url, query, page, size):
    try:
        # API 인증키를 헤더에 포함 (카카오에서 발급받은 키)
        headers = {'Authorization': 'KakaoAK 4a8e1acc493134e630bb6e1dd8deb6eb'}
        
        # 검색할 URL (쿼리, 페이지, 개수 포함)
        url = f'{url}?query={query}&page={page}&size={size}'
        
        # GET 방식으로 요청 보내기
        res = requests.request(method='get', url=url, headers=headers)
        
        # 응답을 JSON 형태로 변환
        data = res.json()
        
        # 도서 정보 리스트 추출
        documents = data['documents']
        
        # 검색 결과가 없을 경우 메시지 출력
        if len(documents) == 0:
            print('검색 도서가 없습니다.')
        
        # 검색된 도서들 출력
        for doc in documents:
            title = doc['title']               # 책 제목
            price = doc['sale_price']          # 판매 가격
            authors = doc['authors']           # 저자 (리스트)
            publisher = doc['publisher']       # 출판사
            
            # authors가 리스트이므로 join()으로 문자열 변환
            print(title, price, ','.join(authors), publisher)
    
    except Exception as err:
        # 예외(오류) 발생 시 출력
        print('접속오류:', err)


# 메인 실행 부분
if __name__ == '__main__':
    url = 'https://dapi.kakao.com/v3/search/book'  # API 기본 주소
    page = 1                                       # 페이지 번호
    size = 10                                      # 한 번에 가져올 개수

    os.system('clear')  # 콘솔 화면 지우기 (맥 기준)
    
    # 무한 반복으로 사용자 입력 받기
    while True:
        print()
        query = input('검색도서명>')  # 검색어 입력
        if query == '': break         # 엔터 입력 시 종료
        getBooks(url, query, page, size)  # 도서 검색 함수 실행