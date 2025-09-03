#문자열 함수
str = 'python is amazing'
print(1, str.lower()) #lowercase
print(2, str.upper()) #uppercase'
print(3, str.capitalize()) #capitalizing
print(4, str[0].islower())
print(5, len(str))
print(str.replace('python', '파이썬'))

index = str.index('a')
print(index)
print(str[index:].upper())

print(7, str.find('ab')) #문자열 찾는 함수
print(7, str.count('i')) #문자열이 몇개인지 세는 함수
