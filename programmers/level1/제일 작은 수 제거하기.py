#
#
# 2021/07/10 1:28 오후

arr = [10]


def solution(arr):
    arr.remove(min(arr))
    return arr if arr else -1


print(solution(arr))
