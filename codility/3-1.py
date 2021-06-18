# FrogJmp
# Time Complexity
# 2021/06/18 12:02 오후


def solution(X, Y, D):
    distance = Y - X
    return distance // D if distance % D == 0 else (distance // D) + 1

# ClearTime = 2021/06/18 12:11 오후
