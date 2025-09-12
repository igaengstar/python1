import json, requests

# -------------------------------------------------------
# (1) 로컬 JSON 파일에서 할리스 매장 정보 불러오기
# -------------------------------------------------------
def getAddress():
    with open('/Users/undan_lee/python/02.데이터 수집/data/hollys.json', 'r', encoding='utf-8') as file:
        address = json.load(file)   # JSON 파일 → 파이썬 객체 변환 (리스트일 가능성 높음)
        
        store_list = []
        for add in address:  # JSON 안의 각 매장 데이터 반복
            data = {
                'name': add['name'],        # 매장 이름
                'address': add['address'],  # 매장 주소
                'phone': add['phone']       # 매장 전화번호
            }
            store_list.append(data)         # 필요한 정보만 뽑아 새 리스트에 저장
        return store_list                   # 최종 리스트 반환


# -------------------------------------------------------
# (2) 카카오 API를 이용해 주소 → 좌표(x, y) 변환
# -------------------------------------------------------
def getXY(query):
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    
    # 카카오 REST API 인증키 (발급받은 키 사용해야 함)
    headers = {'Authorization': 'KakaoAK 4a8e1acc493134e630bb6e1dd8deb6eb'}
    
    # 검색 파라미터
    params = {'query': query}

    # API 요청
    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    # documents 안에 결과가 들어 있음
    documents = data.get('documents', [])

    if not documents:  # 결과가 없으면 None 반환
        print('검색 결과가 없습니다:', query)
        return None, None

    # 첫 번째 결과의 좌표 추출
    x = documents[0]['x']
    y = documents[0]['y']
    return x, y


# -------------------------------------------------------
# (3) 주소 앞 4단어만 잘라 출력하는 함수 (보조용)
# -------------------------------------------------------
def getAddress2(store_list):
    for add in store_list:
        parts = add['address'].split()           # 공백 단위로 분리
        print(' '.join(parts[:4]))               # 앞의 4단어만 합쳐서 출력


# -------------------------------------------------------
# (4) 메인 실행부
# -------------------------------------------------------
if __name__ == '__main__':
    store_list = getAddress()   # JSON에서 매장 데이터 가져오기
    result_list = []            # 최종 결과(좌표 포함) 담을 리스트

    for add in store_list:
        name = add['name']
        phone = add['phone']
        full_address = add['address']

        # 주소를 앞의 4단어까지만 추출 (짧은 주소 버전)
        parts = full_address.split()
        short_address = ' '.join(parts[:4]) if parts else full_address

        # 좌표 구하기 (정확도를 위해 전체 주소 사용)
        x, y = getXY(full_address)

        # 결과 딕셔너리 구성
        data = {
            'name': name,             # 매장 이름
            'address': short_address, # 잘린 주소
            'phone': phone,           # 전화번호
            'x': x,                   # 경도
            'y': y                    # 위도
        }
        result_list.append(data)

    # 결과 확인 출력
    for store in result_list:
        print(store)