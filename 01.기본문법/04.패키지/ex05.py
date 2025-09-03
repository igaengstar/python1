import os

path = os.getcwd()
print('현재폴더', path)

check = path + "travel2"
if os.path.exists(check):
    print('폴더가 존재합니다.')
else: 
    os.makedirs(check)
    print('폴더가 생성되었습니다')