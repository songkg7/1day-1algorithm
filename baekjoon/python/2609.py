# 최대공약수와 최소공배수
# 정수론 및 조합론


import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


n, m = map(int, input().split())

print(math.gcd(n, m))
print(lcm(n, m))
