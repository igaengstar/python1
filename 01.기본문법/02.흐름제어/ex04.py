#1~100 합계
total=0
for j in range(1, 101): 
    total += j #total = total + j (j를 누적해서  total)

print(total)

#2~100 짝수합계
total2=0
for j in range(2, 101, 2):
    total2 += j

print(total2)

#1~99 홀수합계
total3=0
for j in range(1, 100, 2):
    total3 += j

print(total3)