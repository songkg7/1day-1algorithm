# TITLE: 조합
# CATEGORY: 조합론
# DATE: 2021/09/09 9:26 오후

import math
import sys

n, m = map(int, sys.stdin.readline().split())

result = math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
print(result)

# ClearTime = 2021/09/09 9:34 오후
