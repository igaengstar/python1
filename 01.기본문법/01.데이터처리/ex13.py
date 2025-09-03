#Dictionary type
students={1:'홍길동', 2:'심청이', 3:'강감찬'} #딕셔너리(Dictionary)는 키:값 구조로 저장됨
print(students, type(students))

#students.get(key) : 안전하게 값 조회 (없으면 None 또는 기본값)
print(students.get(2)) 
#students[key] : 값 조회 (없으면 에러 발생)
print(students[2]) 

students[4] = '박명수' #추가
print(students, type(students))

print(4 in students) 

#students.get(key) : 안전하게 값 조회 (없으면 None 또는 기본값)
keys = students.keys()
print(keys, type(keys))

values = students.values()
print(values, type(values))

print('박명수' in values)