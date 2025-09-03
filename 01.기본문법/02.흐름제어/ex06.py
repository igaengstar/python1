no = int(input('학생 수:'))

names = []
for i in range(no): #0~n-1
    name=input('이름:')
    names.append(name)

for i in range(len(names)):
    print(i,names[i], end=',')
print()

for i, name in enumerate(names):
    print(i, name, end=',')