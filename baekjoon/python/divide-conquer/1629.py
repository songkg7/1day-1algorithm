# 곱셈
# Divide and Conquer
# 2021/06/23 4:01 오후

# TODO: 다시 풀기
# 10^10 이라면 (10^5)^2 으로 바꿔주며 계산한다.
# 10^11 이라면 (10^5)^2*10 으로 바꿔서 계산한다.

A, B, C = map(int, input().split())


def fpow(A, B):
    if B == 1:
        return A % C
    else:
        x = fpow(A, B // 2)
        if B % 2 == 0:
            return x * x % C
        else:
            return x * x * A % C


print(fpow(A, B))

# ClearTime = 2021/06/23 4:29 오후
