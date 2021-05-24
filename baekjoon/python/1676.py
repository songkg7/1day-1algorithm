# 팩토리얼 0의 개수
# 정수론 및 조합론
import math

N = int(input())

a = math.factorial(N)

count = 0
a = list(str(a))
while True:
    if a[-1] == "0":
        count += 1
        a.pop()
    else:
        break

print(count)
