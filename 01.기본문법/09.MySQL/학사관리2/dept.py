import os
from haksa2 import *

#학과 수정 함수
def menuDept():
    while True:
        os.system('clear')
        print(f"**********학과관리**********")
        print("-----------------------------")
        print("|1.등록|2.목록|3.수정|0.종료|")
        print("-----------------------------")
        menu = input('메뉴선택> ')

        if menu == '0':
            break

        elif menu=='1':
            dname = input('학과이름> ')
            if dname=='': continue
            insertDept(dname)

        elif menu=='2':
            result = listDept()
            for d in result:
                dept(f'학과코드> {d.dcode}, 학과이름> {d.dname}')
        
        elif menu=='3':
            dcode = inputCode('학과코드> ', 1)
            dept = readDept(dcode)
            dname = input(f'학과이름'> {dept.dname})