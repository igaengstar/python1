from shopdb import *
from classes import *

#목록 읽기
def read_all_products():
    try:
        sql = 'SELECT * FROM product'
        cur.execute(sql)
        rows = cur.fetchall()
        if not rows:                     # ✅ 검색 결과 없음 처리
            return []

        products = []  
        for row in rows:
            pro = Product() # pro 를 list 로 받음
            pro.code = row['code']
            pro.name = row['name']
            pro.price = row['price']
            products.append(pro)
        return products

    except Exception as err:
        print('상품목록 오류', err)

def insert(product):
    try:
        sql = 'INSERT INTO product(code, name, price) VALUES(%s, %s, %s)'
        cur.execute(sql, (product.code, product.name, product.price))
        con.commit()
        print('상품등록 완료!')

    except Exception as err:
        print('상품등록 오류', err)

def search(value):
    try:
        sql = 'select * from product where code like %s or name like %s' 
        value = f'%{value}%'
        cur.execute(sql, (value, value))

        rows = cur.fetchall()

        if rows != None:
            products = []
            for row in rows:
                product = Product()
                product.code = row['code']
                product.name = row['name']
                product.price = row['price']

                products.append(product)

            return products

    except Exception as err:
        print('상품검색에러:', err)

def read(code):
    try:
        sql = f'SELECT * FROM product WHERE code=%s'
        cur.execute(sql, (code))
        row = cur.fetchone()
        if row != None:
            pro = Product()
            pro.code = row['code']
            pro.name = row['name']
            pro.price = row['price']
            return pro

    except Exception as err:
        print('상품읽기 오류!', err)

# code 입력
def inputCode(title):
    while True:
        code = input(title)
        if code=='': return code

        if len(code) != 3:
            print('상품코드는 3자리로 입력하세요.')

        elif not code.isnumeric():
            print('상품코드는 숫자로 입력하세요!')

        else:
            return code

#가격 수정    
def inputPrice(title):
    while True:
        price = input(title)
        if price=='':
            return 0
        elif not price.isnumeric():
            print('가격은 숫자로 입력하세요.')
        else:
            return int(price)

#매출 수정
def inputNum(msg):
    while True:
        try:
            num = int(input(msg))         # 입력값을 정수로 변환
            if num <= 0:                  # 0 이하 입력 방지 (필요 없으면 삭제 가능)
                print("0보다 큰 수를 입력하세요!")
                continue
            return num
        except ValueError:                # 정수 변환 실패 시
            print("숫자를 입력하세요!")

#상품 수정
def update(product):
    try:
        sql = f'UPDATE product SET name=%s, price=%s WHERE code=%s'
        cur.execute(sql, (product.name, product.price, product.code))
        con.commit()

    except Exception as err:
        print(f'상품수정 오류', err)




    