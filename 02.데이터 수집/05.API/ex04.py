import os, requests

# 📌 카카오 이미지 검색 API 호출 함수
def getData(query):
    # API 요청 URL (검색어 + size=10개 결과)
    url = f"https://dapi.kakao.com/v2/search/image?query={query}&size=10"

    # 인증키 (발급받은 카카오 REST API 키 사용)
    headers={'Authorization': 'KakaoAK 4a8e1acc493134e630bb6e1dd8deb6eb'}

    # API 서버에 GET 요청
    res = requests.get(url, headers=headers)
    
    # 응답 JSON 중 'documents' 항목만 반환 (이미지 정보 리스트)
    data = res.json()['documents']
    return data

if __name__ == '__main__':
    query='지코'              # 검색어 지정
    list = getData(query)       # API 호출 → 이미지 데이터 리스트 받기

    for item in list:           # 검색된 이미지들 반복
        image_url = item['image_url']   # 이미지 원본 URL
        res = requests.get(image_url)   # 실제 이미지 파일 다운로드 요청

        if res.status_code==200:        # 정상 응답일 경우
            # URL에서 마지막 '/' 이후가 파일 이름
            index=image_url.rindex('/')
            file_name = image_url[index+1:]

            # 📌 로컬에 이미지 저장 (바이너리 모드 'wb')
            with open(f'02.데이터 수집/data/image/{file_name}', 'wb') as file:
                file.write(res.content)