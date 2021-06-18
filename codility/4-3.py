# Missing Integer
# Counting Elements
# 2021/06/17 6:06 오후


def solution(A):
    n = list(set(A))
    n.sort()
    num = 1
    while num in n:
        num += 1
    return num

# ClearTime = 2021/06/17 6:10 오후
