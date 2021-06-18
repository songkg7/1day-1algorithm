# Perm Check
# Counting Elements
# 2021/06/18 8:04 오후


def solution(A):
    n = set([i for i in range(1, len(A) + 1)])
    return 1 if n == set(A) else 0

# ClearTime = 2021/06/18 8:09 오후
