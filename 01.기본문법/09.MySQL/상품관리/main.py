import os
from product import *
from shopdb import *
from classes import *
from salesMain import *


while True:
    os.system('clear')
    print('-----------------------')
    print('       상품관리        ')
    print('-----------------------')
    print('[1] 상품등록')
    print('[2] 상품검색')
    print('[3] 상품목록')
    print('[4] 상품정보수정')
    print('[5] 매출관리')
    print('[0] 프로그램종료')
    print('-----------------------')
    menu = input('메뉴선택>')

    if menu=='0':
        print('프로그램을 종료합니다.')
        break

    elif menu == '1':  # 매출 등록
        code = inputCode('상품코드> ')
        pro = read(int(code))                 # 상품 조회
        if pro is None:
            print('존재하지 않는 상품코드입니다.')
        else:
            pro.print()
            qnt = inputNum('수량> ')          # 수량 입력
            sale = Sale()
            sale.code  = pro.code
            sale.qnt   = qnt
            sale.price = pro.price
            sale.sum   = sale.price * sale.qnt
            sale_insert(sale)                 # ✅ 매출 입력 함수 호출
        
        input('아무키나 누르세요!')
    elif menu=='2':
        while True:
            value = input('검색어> ')
            if value == '': break

            products = search(value)
            if len(products) == 0:
                print('검색 결과가 존재하지 않습니다.')

            else:
                for product in products:
                    product.print()

        input('아무키나 누르세요!')
    

    elif menu == '3':  # 상품목록
        products = read_all_products()   # 또는 read_all_products(), select_all_products()
        if not products:
            print("등록된 상품이 없습니다.")
        else:
            for p in products:
                p.print()
        input('아무키나 누르세요!')




    elif menu=='4':
        code = input('상품코드>')
        product = read(code)

        if product==None:
            print('수정할 상품이 없습니다.')

        else:
            name = input(f'상품이름:{product.name}>')
            if name != '': product.name=name
            price = inputPrice(f'상품가격:{product.price}>')
            if price!= '': product.price=price
            sel = input('수정하실래요?(Y)> ')
            if sel.lower() == 'y':
                update(product)
                product.print()
            else:
                print('수정이 취소되었습니다.')


        input('아무키나 누르세요!')
    elif menu=='5':
        saleMenu()
    else:
        print('[0]~[5]번 메뉴를 선택하세요!')         