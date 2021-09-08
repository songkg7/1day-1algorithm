# 팩토리얼
# 백준 10872번
# 재귀함수

# N = int(input())
N = 0
result = N

def factorial(N):
    global result
    if N == 1:
        return print(result)
    if N == 0:
        return print(1)
    result *= N - 1
    factorial(N - 1)

factorial(N)

# 다른 풀이법
import math
n = int(input())
x = math.factorial(n)
print(x)

# another answer
def factorial(N):
    if N == 0 or N == 1:
        return 1
    return N * factorial(N-1)