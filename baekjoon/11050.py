# 이항계수 1
# 정수론 및 조합론

import math

n, k = map(int, input().split())

a = math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
print(a)
