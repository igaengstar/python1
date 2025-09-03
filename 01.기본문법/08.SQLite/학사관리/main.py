from function import *
from haksaDB import *

while True:
    menuPrint('학생관리')
    menu = input('메뉴선택> ')

    if menu == '0':
        print('프로그램을 종료합니다.')
        # 데이터베이스 모듈에서 연 전역 커서/커넥션을 종료
        try:
            cur.close()
        except Exception:
            pass
        try:
            con.close()
        except Exception:
            pass
        break

    elif menu == '1':  # 입력
        stu = Student()
        stu.id = newID()
        print(f'학번: {stu.id}')

        while True:
            stu.name = input('이름> ').strip()
            if stu.name == '':
                print('이름은 반드시 입력하세요!')
                continue
            break

        stu.dept = inputDept()   # 학과코드 선택 (int)
        insert(stu)              # DB 저장
        print('학생등록성공!')

        # ✔ 입력 직후 DB에서 다시 읽어 확인 (조인으로 dname까지 채워짐)
        saved = read(stu.id)
        if saved:
            saved.print()

    elif menu == '2':  # 검색
        while True:
            value = input('검색어> ').strip()
            if value == '':
                break

            students = search(value) or []  # FIX: None 방어
            if not students:
                print('검색 결과가 없습니다.')
                continue

            for stu in students:
                stu.print()
            print(f'{len(students)}명 학생이 존재합니다.\n')

    elif menu == '3':  # 목록
        students = list_students()  # ✅ haksaDB.py 에 만든 함수 사용
        for student in students:
            student.print()     # ✅ Student 객체의 메서드 호출
        print(f'{len(students)}명 학생이 존재합니다.\n')

    elif menu == '4':  # 삭제
        id = input('학번> ')
        if id == '': continue
        student = read(id)
        if student == None:
            print('삭제할 학생이 없습니다.')
        else:
            student.print()
            sel = input('삭제하실래요(Y)> ')
            if sel.lower() == 'y':
                delete(id)
                print('학생삭제완료!')



    elif menu == '5':  # 수정
        id = input('학번> ').strip()
        if id == '':
            continue

        stu = read(id)
        if stu is None:
            print('수정할 학생이 없습니다.')
            continue

        stu.print()

        # 이름 수정 (엔터면 유지)
        name = input(f'이름({stu.name})> ').strip()
        if name != '':
            stu.name = name

        # 학과 수정 (엔터면 유지)
        print(f'현재 학과코드: {stu.dept}')
        change = input('학과를 변경하시겠습니까? (Y)> ').strip().lower()
        if change == 'y':
            # inputDept()는 인자 없이 호출해야 하며, 유효성 검사까지 해줍니다.
            stu.dept = inputDept()          # ← 정수로 반환됨

        # DB 반영
        rc = update(stu)
        if rc == 1:
            print('학생수정완료!')
            saved = read(stu.id)            # 확인차 재조회 (dname 포함)
            if saved:
                saved.print()
        else:
            print('수정 실패 또는 변경 사항이 없습니다.')


    else:
        print('0~5 중 숫자 하나를 입력해 주세요!')