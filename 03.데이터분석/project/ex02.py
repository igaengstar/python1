import os # 운영체제
import pandas as pd # 판다스    

score_name = 'data/학생성적.csv' # 파일 경로
score = pd.read_csv(score_name) # 파일 읽기

def inputNumber(message): # 숫자 입력 함수
    while True: # 무한루프
            num = input(message) # 숫자 입력
            if num =='':
                return 0 # 빈 문자열이면 0 반환
            elif not num.isdigit(): # 숫자가 아니면
                print('숫자를 입력하세요.') # 메시지 출력
            else:
                return int(num)

while True: # 무한루프
    os.system('clear') # 화면 지우기
    print('-'* 50)
    print('*************  성적 처리 프로그램  **************') # 제목
    print('-'* 50)
    print('1.등록|2.조회|3.검색|4.삭제|5.수정|0.종료') # 메뉴
    print('-'* 50)
    menu = input('메뉴를 선택하세요 : ') # 메뉴 선택
    if menu == '0': # 종료
        print('프로그램을 종료합니다.')
        break # 무한루프 탈출
    elif menu == '1': # 등록
        input('등록할 학생 이름을 입력하세요 : ')

    elif menu == '2': # 목록
        for i in range(5):
            print(f'{i+1}번째 학생 이름 : ')
        input('계속하려면 Enter를 누르세요.')


    elif menu == '3': # 검색
        input('검색할 학생 이름을 입력하세요 : ')

    elif menu == '4': # 삭제
        input('삭제할 학생 이름을 입력하세요 : ')

    elif menu == '5': # 수정
        input('수정할 학생 이름을 입력하세요 : ')

    else: # 잘못된 입력
        print('잘못된 입력입니다. 0~5번 중 다시 선택하세요.')
    