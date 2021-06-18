#
# Time complexity
# 2021/06/18 12:13 오후

# A = [1, 2, 3, 5]


def solution(A):
    if not A:
        return 1
    return sum(range(1, len(A) + 2)) - sum(A)

# ClearTime = 2021/06/18 12:38 오후
