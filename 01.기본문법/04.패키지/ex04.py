import inspect
import random

# 모듈 자체를 가져오기
import travel.thailand as thailand
import travel.vietnam as vietnam

# 함수 호출
thailand.thailand1()
thailand.thailand2()
vietnam.vietnam1()

# 모듈 경로 확인
print(1, inspect.getfile(random))
print(2, inspect.getfile(thailand))
print(3, inspect.getfile(vietnam))