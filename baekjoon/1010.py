# 다리 놓기
# 정수론 및 조합론

# 이항계수를 구하는 문제

import math

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = math.factorial(m) // (math.factorial(m - n) * math.factorial(n))
    print(a)
