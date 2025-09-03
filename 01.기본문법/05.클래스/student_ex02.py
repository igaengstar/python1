from student import Student

students = [
    {'no':'01', 'name':'홍길동', 'dept':'전자과', 'birthday':'00-10-04'},
    {'no':'02', 'name':'심청이', 'dept':'전기과', 'birthday':'02-12-17'},
]

while True:
    print('------------------------------')
    print('|1.등록|2.목록|3.삭제|0.종료|')
    print('------------------------------')
    menu = input("메뉴선택> ")
    
    if menu=="0":   # 종료
        print("프로그램 종료")
        break

    elif menu=="1":   # 등록
        s = Student()
        s.no = input("번호> ")                  # 번호 입력
        s.name = input("이름> ")                # 이름 입력
        s.dept = input("학과> ")                # 학과 입력
        s.birthday = input("생일(YY-MM-DD)> ")  # 생일 입력
        students.append(s.info())               # 딕셔너리 형태로 저장
        print("등록완료!")

    elif menu=="2":   # 목록
        if not students:
            print("등록된 학생이 없습니다.")
        else:
            for s in students:
                stu = Student()
                stu.no = s['no']
                stu.name = s['name']
                stu.dept = s['dept']
                stu.birthday = s['birthday']
                stu.info_print()

    elif menu=="3":   # 삭제
        no = input("삭제번호> ")
        for idx, s in enumerate(students):
            if no == s['no']:
                students.pop(idx)
                print("삭제완료!")
                break
        else:
            print("해당 번호가 없습니다.")