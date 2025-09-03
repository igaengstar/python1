from function import *   # 공통 함수 모듈 (menuPrint, inputNum 등 사용)
from product import Product  # 상품 클래스
from sale import Sale        # 매출 클래스

# 초기 상품 데이터 (테스트용)
products = [
    {'code':'001', 'name':'LG 냉장고', 'price':250},
    {'code':'002', 'name':'LG 세탁기', 'price':180},
]

# 매출 데이터 저장 리스트
sale = []

# 상품코드로 상품 검색하는 함수
def search(code):
    for p in products:
        if code == p['code']:
            return p   # 찾으면 상품 딕셔너리 반환
    return None        # 못 찾으면 None 반환

# 현재 매출 중 가장 큰 일련번호(seq) 구하는 함수
def max_seq():
    seqs = []
    for s in sale:
        seqs.append(s['seq'])   # sale 리스트에서 seq만 추출
    if len(seqs) == 0:          # 매출이 하나도 없으면
        return 0
    else:
        return max(seqs)        # 가장 큰 seq 값 반환

# -------------------- 메인 프로그램 --------------------
while True:
    menuPrint('매출관리')      # 메뉴 출력
    menu = input("메뉴선택> ")
    if menu == "0":            # 종료
        break

    elif menu == "1": # 매출 등록
        code = input("상품코드>")   # 상품코드 입력
        if code == "": continue    # 입력 없으면 건너뜀
        p = search(code)           # 상품코드로 상품 찾기
        if p == None:              # 없으면 안내 메시지
            print(f"{code}번 상품이 없습니다.")
        else:
            name = p['name']       # 상품 이름
            price = p['price']     # 상품 가격
            print(f'상품명:{name}, 가격:{price}')
            qnt = inputNum("수량>") # 판매 수량 입력
            if qnt == "": continue
            s = Sale(code, name, price, qnt) # 매출 객체 생성
            s.seq = max_seq() + 1  # 일련번호(seq) 자동 생성
            sale.append(s.dict())  # 딕셔너리로 변환 후 저장
            print("매출등록완료!")

    elif menu == "3": # 매출 목록
        for s in sale:
            print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원,", end="")
            print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")

    elif menu == "2": # 매출 검색 (이름으로)
        name = input("검색이름> ")
        for s in sale:
            # 대소문자 무시하고 이름 포함 여부 확인
            if s['name'].upper().find(name.upper()) != -1:
                print(f"{s['code']},{s['name']},{s['price']:,}만원,", end="")
                print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
                isFind = True
            if isFind == False: print()

    elif menu == "4": # 매출 삭제
        seq = inputNum("삭제번호> ")
        if seq == "": continue
        for idx, s in enumerate(sale):
            if s['seq'] == seq: # 일련번호 일치하는 매출 찾기
                # 삭제 전 확인용 출력
                print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원,", end="")
                print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
                sel = input("삭제하실래요?(Y)")
                if sel == "Y" or sel == "y":
                    sale.pop(idx)  # 해당 인덱스 삭제
                    print("매출삭제완료!")

    elif menu == "5": # 매출 수정 (수량만 수정)
        seq = inputNum("수정번호> ")
        if seq == "": continue
        for s in sale:
            if seq == s['seq']:
                # 기존 데이터 출력
                print(f"상품코드:{s['code']}")
                print(f"상품이름:{s['name']}")
                print(f"판매일:{s['date']}")
                # 새 수량 입력 (빈 값이면 유지)
                qnt = inputNum(f"판매수량:{s['qnt']}>")
                if qnt != "":
                    s['qnt'] = qnt
                print("매출수정완료!")


name -