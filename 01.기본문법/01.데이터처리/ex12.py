#list 타입
names = ['홍길동', '심청이', '강감찬', 0, True]
print(names, type(names))

names.append('박명수')
print(names,type(names))

names.pop()
print(names)

names.insert(1, '박명수')
names.append('박명수')
print(names)

print(names.count('박명수'))
print(names, names[1:3])