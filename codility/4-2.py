# Max Counters
# Counting Elements
# 2021/06/18 6:07 오후

# increase(X)
# [3, 2, 2, 4, 2]

A = [6, 6, 6, 6, 6, 6]
N = 5


def solution(N, A):
    counter = [0] * N

    for X in A:
        if X <= N:
            counter[X - 1] += 1
        else:
            counter = [max(counter)] * N

    return counter


print(solution(N, A))

# ClearTime = 2021/06/18 6:12 오후 - 66%
