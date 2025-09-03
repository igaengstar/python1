from score import Score
from function import *

def insert(scores):
    score = Score()
    score.no = input("번호> ")
    score.name =  input("이름> ")
    score.kor =  int(input("국어> "))
    score.eng =  int(input("영어> "))
    score.mat = int(input("수학> "))
    print(score.to_dict())
    scores.append(score.to_dict())


scores = []
while True:
    menuPrint("성적관리")
    menu = input("메뉴선택> ")
    if menu == "0":
        break
    elif menu == "1":
        insert(scores)

        else:
            print("해당 번호가 없습니다.")

    elif menu =="2":
        no = input("검색번호> ")
        for s in scores:
            if no ==s['no']:
                print(s)

        else:
            print("해당 번호가 없습니다.")

    elif menu == "3":
        for s in scores:
            print(s)
        else:
            print("해당 번호가 없습니다.")
    
    elif menu == "4":
        no = input("삭제번호> ")
        for idx, s in enumerate(scores):
            if no ==s['no']:
                scores.pop(idx)
        else:
            print("해당 번호가 없습니다.")
