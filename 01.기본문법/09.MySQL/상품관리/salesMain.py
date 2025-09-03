import os
from product import *
from sale import *

def saleMenu():
    while True:
        os.system('clear')   # 화면 지우기 (맥 호환)
        print('-----------------------')
        print('       매출관리        ')
        print('-----------------------')
        print('[1] 매출등록')
        print('[2] 매출검색')
        print('[3] 매출목록')
        print('[4] 매출정보수정')
        print('[5] 매출관리')
        print('[0] 상품관리')
        print('-----------------------')
        menu = input('메뉴선택>')

        if menu=='0':   # 종료
            print('프로그램을 종료합니다.')
            break
        
        elif menu=='1': # 매출 등록
            code = inputCode('상품코드> ')
            if code == '':
               input('아무키나 누르세요!')
               continue

            pro = read(int(code))            # 상품 조회
            if not pro:
               print('존재하지 않는 상품코드입니다.')
            else:
               qnt = inputNum('수량> ')     # 수량 입력(정수 입력 보조함수 가정)
               if qnt <= 0:
                  print('수량은 1 이상이어야 합니다.')
               else:
                  s = Sale()
                  s.code  = pro.code
                  s.name  = pro.name
                  s.price = pro.price
                  s.qnt   = qnt
                  s.sum   = s.price * s.qnt
                  sale_insert(s)                # sale 모듈의 insert(s) 가정
                  print('매출 등록 완료!')
            input('아무키나 누르세요!')
        
        elif menu=='2': # 매출 검색
            while True:
                value = input('검색어> ')
                if value == '': break
                sales = view_list(value)   # 검색 결과 가져오기
                if not sales:
                    print("검색 결과가 없습니다.")
                else:
                    for sale in sales:     # 각 매출 출력
                        sale.print()
            input('아무키나 누르세요!')
                 
        elif menu=='3': # 매출 목록
            sales = view_list("")
            if not sales:
                print("등록된 매출이 없습니다.")
            else:
                for sale in sales:         # 전체 매출 출력
                    sale.print()
            input('아무키나 누르세요!')
    
        elif menu=='4': # 매출 수정
           input('아무키나 누르세요!')
