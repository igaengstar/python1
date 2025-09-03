import os
path = os.path.dirname(os.path.realpath(__file__))
# print('현재패스', path)
file_name = path + '/product.txt'
# print('파일명', file_name)

class Product:
    def __init__(self):
        self.code = 0
        self.name = ''
        self.price = 0
    def print(self):
        print(f'코드:{self.code}, 상품명:{self.name}, 가격:{self.price:,}만원')
        print('-'*70)

# 모든 데이터를 읽는 함수
def fileRead():
    with open(file_name, 'r', encoding='utf-8') as file:
        list = []
        lines = file.readlines()
        for line in lines:
            items = line.split(',')
            p = Product()
            p.code = int(items[0])
            p.name = items[1]
            p.price = int(items[2].replace('\n', ''))
            list.append(p)
    return list

# 데이터 하나 추가 함수
def fileAppend(p):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{p.code},{p.name},{p.price}\n') 

# 모든 데이터를 다시 쓰기 함수
def fileWrite(list_items):                               # ✅ 인자 이름만 명확화
    with open(file_name, 'w', encoding='utf-8') as file:
        for p in list_items:                             # ✅ 리스트 전체를 덮어쓰기
            file.write(f'{p.code},{p.name},{p.price}\n')

# 코드 삭제 함수
def delete(code):
    list_items = fileRead()
    result = [p for p in list_items if p.code != code]
    fileWrite(result)

def productAppend():
    p = Product()
    p.code = 2
    p.name = '세탁기'
    p.price = 500
    fileAppend(p)
    print('등록성공!')

def list():
    items = fileRead()                                   # ✅ 내부 변수명 충돌 방지(권장)
    for p in items:
        p.print()

def update():                                            # ✅ 콜론 추가
    code = 1
    list_items = fileRead()
    result = [p for p in list_items if p.code == code]   # ✅ 수정 대상은 == 로 검색
    if not result:
        print('수정 대상 코드가 없습니다.')
        return
    p = result[0]
    p.name = '아무게'
    fileWrite(list_items)                                 # ✅ 변경사항 저장

if __name__ == '__main__':
    # productAppend()
    # list()
    delete(2)