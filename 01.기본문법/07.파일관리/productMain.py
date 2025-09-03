from function import *
from productFile import *


def newCode():
    products = fileRead()                                   # ▶ list → products
    if not products:                                        # ▶ 빈 목록 먼저 체크(안전+빠름)
        return 1
    result = sorted(products, key=lambda p: p.code, reverse=True)
    return result[0].code + 1

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택: ')
    if menu == '0':
        print('프로그램을 종료합니다.')
        break

    elif menu == '1':  # 입력
        p = Product()
        p.code = newCode()
        print(f'상품코드> {p.code}')
        # (이름/가격 입력, fileAppend(p) 는 이후에 붙이면 됨)

    elif menu == '2':  # 검색
        pass

    elif menu == '3':  # 목록
        while True:
            sort = inputNum('1.코드순|2.이름순|3.최저가|4.최고가|0.뒤로> ')
            if sort == 0:                                   # ▶ '' → 0 (정수 비교)
                break

            products = fileRead()                           # ▶ list → products
            result = []
            if sort == 1:
                result = sorted(products, key=lambda p: p.code)
            elif sort == 2:
                result = sorted(products, key=lambda p: p.name)
            elif sort == 3:
                result = sorted(products, key=lambda p: p.price)
            elif sort == 4:
                result = sorted(products, key=lambda p: p.price, reverse=True)
            else:
                print('0~4 중에서 선택하세요.')
                continue

            print()
            for p in result:
                p.print()
            break  # 한 번 보여주고 목록 메뉴로 복귀

    elif menu == '4':  # 삭제
        pass
    elif menu == '5':  # 수정
        pass
    else:
        print('0~5번 숫자를 입력하세요! ')