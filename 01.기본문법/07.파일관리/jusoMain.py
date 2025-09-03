from function import *         # 외부 function 모듈 불러오기 (메뉴 출력 등 유틸 함수)
from jusoFile import *         # 주소 파일 관리 모듈 불러오기 (Person 클래스, fileRead, fileWrite 등 포함)

# 새로운 일련번호(seq)를 생성하는 함수
def newSeq():  
    list = fileRead()                         # 현재 파일에서 전체 데이터 읽기
    if not list: return 1                     # 데이터가 없으면 1번부터 시작
    seqs = [p.seq for p in list]              # 전체 사람들의 seq만 모아서 리스트 생성
    return max(seqs)+1                        # 가장 큰 번호 + 1 리턴

# 특정 seq(번호)로 검색하는 함수
def searchSeq(seq):
    list = fileRead()                         # 전체 데이터 읽기
    result = [p for p in list if p.seq==seq]  # 해당 seq와 같은 Person만 추출
    if len(result) > 0: return result[0]      # 결과 있으면 첫 번째 Person 리턴


# 메인 메뉴 루프
while True:
    menuPrint('주소관리')                      # 메뉴 출력
    menu = input('메뉴선택>')                  # 메뉴 번호 입력
    if menu=="0":                             # 종료 메뉴
        print("프로그램을 종료합니다.")
        break

    elif menu=="1": # 입력
        person = Person()                     # 새로운 Person 객체 생성
        person.seq = newSeq()                 # 자동으로 새 번호 할당
        print(f"번호>{person.seq}")
        if person.seq == '': continue         # 번호가 없으면 다시 입력
        person.name = input("이름>")           # 이름 입력
        if person.name == '': continue
        person.address = input('주소>')        # 주소 입력
        fileAppend(person)                    # 파일에 저장
        person.print()                        # 입력한 데이터 출력 확인

    elif menu =='2': # 검색
        seq = inputNum("검색번호> ")
        while True:
            value = input('검색어> ')
            if value== '': break
            list = fileRead()
            result = [p for p in list if p.name.find(value)!=-1 or p.address.find(value)!=-1]
        if not result:
            print('검색 내용이 없습니다.')
            continue
        for person in result:
            person.print()


    elif menu=="3": # 목록 출력
        list = fileRead()                     # 전체 데이터 읽기
        for person in list:                   # 한 줄씩 출력
            person.print()

    elif menu=="4": # 삭제
        seq = inputNum("삭제번호>")            # 삭제할 번호 입력 (숫자 전용 입력 함수)
        list = fileRead()                     # 전체 데이터 읽기
        result = [p for p in list if p.seq==seq]
        if len(result)==0:
            print("삭제할 번호가 없습니다.")
            continue
        else:
            person = result[0]                    # 첫 번째 결과 선택
            person.print()                        # 삭제 대상 출력
            sel = input('삭제하실래요(Y)> ')      # 삭제 확인
            if sel.lower() == 'y':                #if sel == 'Y' or sel=='y'
                result = [p for p in list if p.seq!=seq] # 해당 번호 제외한 리스트 생성
                fileWrite(result)                   # 새 리스트를 파일에 덮어쓰기
                print("삭제성공!")

    elif menu =="5": #수정
        seq = inputNum('수정번호> ')             # 수정할 번호 입력 (정수로 받음)
        if seq == '':
            continue                             # 번호 입력이 비어 있으면 다시 메뉴로
    result = [p for p in list if p.seq==seq] # 리스트에서 해당 번호를 가진 사람만 검색
    if not result:                           # 검색 결과 없으면
        print("번호가 없습니다.")             
        continue
    person = result[0]                       # 첫 번째 검색 결과 선택 (Person 객체)
    
    # 이름 수정
    name = input(f'이름: {person.name} > ')  
    if name!='':                             # 입력값이 있으면
        person.name = name                   # 기존 이름을 새 값으로 변경
    
    # 주소 수정
    address = input(f'주소:{person.address} > ')
    if address!='':
        person.address = address
    
    # 수정 확인
    sel = input("수정하실래요? (y)> ")
    if sel.lower() =='y':                    # y 입력 시 최종 수정
        person.print()                       # 수정된 정보 출력
        fileWrite(list)                      # 변경된 전체 리스트를 파일에 덮어쓰기
        print('수정완료!')