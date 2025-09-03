from function import *          # 메뉴 출력 등 공통 함수 불러오기
from product import Product     # Product 클래스 불러오기

# 초기 상품 데이터(딕셔너리 리스트 형태)
products = [
    {'code': '001', 'name': 'LG 냉장고', 'price': 250},
    {'code': '002', 'name': 'LG 세탁기', 'price': 180},
]

# 특정 code로 상품의 리스트 인덱스(idx) 찾기
def search(code):
    """code로 상품의 리스트 인덱스(idx) 찾기. 없으면 None 반환"""
    for idx, p in enumerate(products):   # enumerate → (인덱스, 원소) 같이 반환
        if code == p['code']:            # code가 같으면
            return idx                   # 해당 idx 반환
    return None  # 없으면 명시적으로 None 반환


# 메인 루프: 무한 반복해서 메뉴 실행
while True:
    menuPrint("상품관리")     # 메뉴 출력 (function.py 안에 정의된 함수)
    menu = input("메뉴선택> ")   # 사용자 입력

    if menu == "0":   # 0 → 종료
        break

    elif menu == "1":  # 등록
        # 새 코드 자동 생성 (현재 상품 개수 +1, 세 자리수로 맞춤: 001, 002…)
        code_num = len(products) + 1
        code = f'{code_num:03d}'
        print(f"상품코드> {code}")   # 자동 부여된 코드 안내

        name = input("상품이름> ")
        if name == "": 
            continue                 # 이름이 없으면 등록 취소

        price = int(input("상품가격> "))  # 가격은 숫자로 입력받음

        # Product 객체 생성 → dict 변환 → 리스트에 추가
        p = Product(code, name, price)
        products.append(p.to_dict())  # Product의 to_dict() 사용
        print("상품등록완료!")

    elif menu == "3":  # 목록
        # 전체 상품 출력
        for p in products:
            print(p['code'], p['name'], p['price'])
        print(f'{len(products)}개 상품이 존재합니다!')

    elif menu == "2":  # 검색
        name = input("검색이름> ")
        key = name.upper()            # 대소문자 무시 위해 모두 대문자로 변환
        for p in products:
            if p['name'].upper().find(key) != -1:  # 이름에 검색어 포함되면
                print(p['code'], p['name'], p['price'])

    elif menu == "4":  # 삭제
        code = input("삭제코드> ")
        if code == "":
            continue
        idx = search(code)   # 해당 코드 위치 찾기
        if idx is None:      # 없으면 안내
            print(f'{code}번 상품이 없습니다.')
        else:
            products.pop(idx)   # 있으면 삭제
            print("상품삭제완료!")

    elif menu == "5":  # 수정
        code = input("수정코드> ")
        if code == "":
            continue
        idx = search(code)   # 수정할 상품 위치 찾기
        if idx is None:
            print(f'{code} 상품이 없습니다.')
            continue

        p = products[idx]   # 수정할 상품 가져오기
        # 이름 입력 (기존값 보여주고, 새 값 입력 없으면 그대로 유지)
        name = input(f"상품이름:{p['name']}> ")
        if name != "": 
            p['name'] = name

        # 가격 입력 (기존값 보여주고, 새 값 있으면 숫자로 바꿔서 저장)
        price = input(f"상품가격:{p['price']}> ")
        if price != "":
            p['price'] = int(price)

        print("상품수정 완료!")