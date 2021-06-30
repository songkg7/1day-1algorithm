#
#
# 2021/06/30 1:57 오후

a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]


def solution(a, b):
    return sum(map(lambda x: x[0] * x[1], zip(a, b)))


print(solution(a, b))

# ClearTime = 2021/06/30 2:01 오후
