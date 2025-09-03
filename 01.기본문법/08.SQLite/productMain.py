from function import *
from productDB import *

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택> ')
    if menu=='0':
        print("프로그램을 종료합니다.")
        break
    elif menu=='1': #입력
        p = Product()
        p.name = input('상품이름> ')
        if p.name =='': continue
        p.price = inputNum('상품가격> ')
        if p.price =='': p.price = 0 
        insert(p)
        print('상품 등록 완료!')
        
    elif menu=='2': #검색
            value = input('검색어> ')
            if value =='': break
            rows = search(value)
            for row in rows:
                rowPrint(row)
    elif menu=='3': #목록
        while True:
            type=inputNum('1.코드순|2.상품명순|3.최저가순|4.최고가순')
            if type =='': break
            rows = list(type)
            for row in rows:
                rowPrint(row)
    elif menu=='4': #삭제
        code = inputNum('상품코드> ')
        if code =='': continue
        row = read(code)
        p = rowPrint(row)
        sel = input(f'삭제하실래요?(Y)> ')
        if sel.lower() == 'y':
            delete(code)
            print('상품삭제 완료!')


    elif menu=='5': #수정
        code = inputNum('상품코드> ')
        if code =='': continue
        row = read(code)
        p = rowPrint(row)
        
        if p != None:
            name = input(f'상품이름:{p.name}> ')
            if name !='': p.name = name
            price = inputNum(f'상품가격:{p.price}원> ')
            if price !='': p.price = price
            sel = input(f'수정하실래요?(Y)> ')
        if sel.lower() == 'y':
            update(p)
            print('상품수정 완료!')
    else:
        print('0~5번 숫자를 입력하세요!') 