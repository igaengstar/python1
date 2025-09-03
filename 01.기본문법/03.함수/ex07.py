from function import menuPrint, inputNum

sale = [
    {'code': 1, 'name': '냉장고',   'price': 250, 'qnt': 5},
    {'code': 2, 'name': '세탁기',   'price': 150, 'qnt': 3},
    {'code': 3, 'name': '전자레인지', 'price': 100, 'qnt': 4}
]

# 검색함수: code가 0이면 전체 출력, 아니면 해당 코드만 출력
def search(code: int) -> bool:
    isFind = False
    for index, s in enumerate(sale):   # ❌ (index in enumerate) → ✅ (index, s in enumerate)
        if code == 0 or s['code'] == code:   # ❌ (if s['code'] == code: or (code==0)) → ✅ 조건문 수정
            isFind = True
            total = s['price'] * s['qnt']
            print(index, s['code'], s['name'], s['price'], s['qnt'], total)
    if isFind == False:                # 들여쓰기 위치 수정 (for문 밖으로 빼야 함)
        print("상품이 존재하지 않습니다.")
    return isFind                      # return도 for문 밖으로 이동해야 함


# 목록 함수
def list_items():   # ❌ list()는 파이썬 기본함수 이름과 충돌 → list_items()으로 수정
    if len(sale) == 0:                 # ❌ 콜론 누락 (if len(sale) == 0:) → ✅
        print("상품이 존재하지 않습니다.")
    else:
        for index, s in enumerate(sale):  # (index, s)로 받아야 함
            total = s['price'] * s['qnt']
            print(index, s['code'], s['name'], s['price'], s['qnt'], total)
        print(len(sale), "상품이 존재합니다.")


# 삭제 함수
def delete(code: int):
    isFind = search(code)   # ❌ search(code): → ✅ search(code)
    if isFind == True:
        for index, s in enumerate(sale):
            if s['code'] == code:
                sale.pop(index)
                print("삭제성공")
                break   # 한 건만 삭제 후 종료

#입력 함수
def insert():
    codes=[]
    for s in sale:
        codes.append(s['code'])
    new_code = max(codes) + 1
    print(f"상품코드> {new_code}")
    name = input("상품이름")
    price = inputNum("상품가격")
    qnt = inputNum("판매수량")
    sale.append({'code':new_code, 'name':name, 'price':price,'qnt':qnt})
    print("등록성공")

while True:
    menuPrint("매출관리")
    menu = input("메뉴선택> ")
    if menu == "0":
        print("프로그램 종료합니다.")
        break

    elif menu == "1": #목록
        list_items()   # ❌ list() → ✅ list_items()

    elif menu == "2": #검색
        code = inputNum("검색코드")
        search(code)

    elif menu == "3": #삭제
        code = inputNum("삭제코드")
        delete(code)

    elif menu == "4":
        pass
    elif menu == "5":
        pass