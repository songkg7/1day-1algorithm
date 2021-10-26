# TITLE: 초6 수학
# CATEGORY: 정수론
# DATE: 2021/10/15 9:55 오후

import math

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(math.lcm(a, b), math.gcd(a, b))

# ClearTime = 2021/10/15 10:04 오후
