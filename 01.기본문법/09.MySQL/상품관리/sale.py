from product import *
from classes import *

def view_list(value):                            # 매출목록 조회 (검색어 포함)
    try:
        sql = 'SELECT * FROM view_sale WHERE code LIKE %s OR name LIKE %s'
        value = f'%{value}%'                     # 검색어 앞뒤에 % 붙여 부분검색
        cur.execute(sql, (value, value))         # DB 실행 (code, name 대상)
        rows = cur.fetchall()

        if not rows:                             # 결과 없으면 빈 리스트 반환
            return []

        sales = []
        for row in rows:                         # 결과 행(row)마다 Sale 객체 생성
            s = Sale()
            s.seq = row['seq']                   # 일련번호
            s.code = row['code']                 # 상품코드
            s.name = row['name']                 # 상품명
            s.date = row['fdate']                # 판매일자
            s.price = row['price']               # 단가
            s.qnt = row['qnt']                   # 수량
            s.sum = row['qnt'] * row['price']    # 합계 금액 계산
            sales.append(s)                      # 리스트에 추가
        return sales                             # 완성된 매출 목록 반환

    except Exception as err:                     # 예외 발생 시
        print('매출 목록 오류:', err)
        return []                                # 안전하게 빈 리스트 반환


if __name__ == '__main__':                       # 단독 실행 시 테스트용
    sales = view_list("")                        # 검색어 없이 전체 조회
    for sale in sales:
        sale.print()                             # Sale 객체의 print 메서드 호출

#매출 입력 함수
def sale_insert(sale):
    try: 
        sql = 'insert into sale(code, date, qnt, price) values(%s, now(), %s, %s)'   
        cur.execute(sql, (sale.code, sale.qnt, sale.price))
        con.commit()
        print('매출등록 완료!')

    except Exception as err:
        print('매출등록 오류', err)
