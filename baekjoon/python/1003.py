# 피보나치 함수
# 동적 계획법 1

# TODO: 동적 계획법에 대한 더 많은 공부 필요

t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)
