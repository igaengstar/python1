#숫자인 체크 함수
def isNumber(s):
    if s.isnumeric():
        return True
    else:
        print("숫자로 입력하세요!")
        return False
    
#학점구하기 함수
def grade(score):
    grade=""
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    return grade

#숫자 입력 함수
def inputNum(title):
    while True:
        s = input(f"{title}>")
        if s.isnumeric():
            return int(s)
        elif s == "":
            return 0
        else:
            print(f"{title}을(를) 숫자로 입력하세요!")


#메뉴 출력 함수
def menuPrint(title):
    print(f"*****************{title}******************")
    print("-------------------------------------------")
    print("|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|")
    print("-------------------------------------------")