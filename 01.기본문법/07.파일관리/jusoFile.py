#주소 관리 클래스
class Person:
    def __init__(self):
        self.seq = 0
        self.name=''
        self.address='경기도 광명시'
    def print(self):
        print(f'번호: {self.seq}, 이름:{self.name}, 주소: {self.address}')

file_name = 'juso.txt' 

#파일에 객체를 추가하는 함수
def fileAppend(person):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{person.seq},{person.name},{person.address}\n')

#파일에 객체를 추가하는 함수
def fileWrite(list):
    with open(file_name, 'w', encoding='utf-8') as file:
        for person in list:
            file.write(f'{person.seq},{person.name},{person.address}\n')

def fileRead():
    list = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            items = line.strip().split(',')
            person = Person()
            person.seq = int(items[0])
            person.name = items[1]
            person.address = items[2]
            list.append(person)
        return list

'''#list 출력 테스트
list = fileRead()
for person in list:
    person.print()'''

#데이터 추가 테스트
def append():
    person = Person()
    person.seq=5
    person.name='이순신'
    person.address= '경기도 광명시 철산동'
    person.print()
    fileAppend(person)

#검색 함수
def search(type, value):
    list = fileRead()
    result = []
    if type == 1:  # seq 검색
        result = [person for person in list if int(person.seq) == int(value)]  # ← 수정: 타입 맞춰 비교
    elif type == 2:  # name 검색
        result = [person for person in list if person.name.find(value) != -1]
    elif type == 3:  # address 검색
        result = [person for person in list if person.address.find(value) != -1]
    return result


'''result = search(3, '인천')
if len(result) == 0:
    print("검색 결과가 없습니다.")
else:
    for person in result:
        person.print()'''

#삭제 함수
def delete(seq):
    list = fileRead()
    result = [person for person in list if person.seq != seq]
    fileWrite(result)

# 수정 함수 (조회 후 출력만)
def update(seq):
    list = fileRead()
    result = [person for person in list if person.seq==seq]
    if len(result)==0:
        print("해당 번호가 없습니다.")
    else:
        person = result[0]
        #person.print()
        name = input(f'이름:{person.name}> ')
        if name !='': person.name = name
        address = input(f'주소:{person.address}> ')
        if address !='': person.address = address
        fileWrite(list)
        person.print()
                        
    

# 실행부
# seq = input("수정번호> ")
# update(seq)



