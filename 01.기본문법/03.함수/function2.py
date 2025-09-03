#최댓값 구하는 하수
#새로운 코드를 생성함수
def newCode(list):
    if len(list) == 0:
        return 1
    
    codes = []
    for s in list:
        codes.append(s['code'])
    return max(codes)+1

#숫자 입력될 떄까지 계속 입력하는 함수 
def inputNum (title):
    while True:
        num = input(f"{title}") 
        if num.isnumeric(): #num 이 숫자인지 아닌지 판별하는 함수
            return int(num)
        elif num == "":
            return num
        else:
            print("숫자로 입력하세요!")


#검색 함수 (list 와 code 를 입력받아서 list에서 code를 검색)
def search(list, code):
    for index, item in enumerate(list):
        if item['code']==code:
            return index

#메뉴 출력 함수
def menuPrint(title):
    print(f"*****************{title}******************")
    print("-------------------------------------------")
    print("|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|")
    print("-------------------------------------------")

# 헤더 출력 함수
def printHeader():
    print("코드\t이름\t가격\t수량")

# 아이템 출력 함수
def printItem(item):
    for key in item.keys():      # keys = item.keys() 없이도 반복 가능
        val = item[key]
        if isinstance(val, int): # 값이 숫자면 천단위 구분자(,) 붙여 출력
            print(f"{val:,}", end="\t")
        else:
            print(val, end="\t") # 문자열이면 그대로 출력
    print()  # 각 상품을 한 줄로 출력 후 줄바꿈

sale = [
    {'code': 1, 'name': '냉장고', 'price': 2_500_000, 'qnt': 5},
    {'code': 2, 'name': '세탁기', 'price': 1_500_000, 'qnt': 3},
]

printHeader()
for s in sale:
    printItem(s)