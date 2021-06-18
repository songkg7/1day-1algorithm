# Cyclic Rotation
# Arrays
# 2021/06/17 6:33 오후

from collections import deque

A = [1,2,3,4]
K = 4


def solution(A, K):
    n = deque(A)
    n.rotate(K)
    return list(n)


print(solution(A, K))

# ClearTime = 2021/06/17 6:38 오후
