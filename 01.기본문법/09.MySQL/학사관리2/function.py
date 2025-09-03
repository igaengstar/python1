#메뉴 출력 함수
def menuPrint(title):
    print(f"***********************{title}***********************")
    print("------------------------------------------------------")
    print("|1.입력|2.검색|3.목록|4.삭제|5.수정|6.학과관리|0.종료|")
    print("------------------------------------------------------")

#숫자입력 함수
def inputNum(title):
    while True:
        str = input(title)
        if str.isnumeric():
            return int(str)
        elif str =="":
            return str
        else:
            print("숫자로 입력하세요!")