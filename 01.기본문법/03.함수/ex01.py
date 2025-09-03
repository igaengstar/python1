#함수
#성적 입력시 학점 구하는 함수

def grade(score):
    if score >= 90:
        grade = 'A'
    
    elif score >= 80:
        grade = 'B'
    
    elif score >= 70:
        grade = 'C'
    
    elif score >= 60:
        grade = 'D'
    
    else:
        grade = 'F'

    return grade
    #print(f"점수: {score}, 학점: {grade}")
    
while True:
    score = input('점수(종료:0)> ')
    if score == "0":
        print('프로그램을 종료합니다.')
        break

    elif not score.isnumeric():
        print('숫자를 입력해주세요!')

    else:
        grade(int(score))
        print(grade)