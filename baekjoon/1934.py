# 최소공배수
# 정수론 및 조합론
# 유클리드 알고리즘

def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
