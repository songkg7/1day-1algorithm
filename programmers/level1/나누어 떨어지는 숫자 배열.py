#
#
# 2021/07/04 12:59 오후

arr = [5, 9, 7, 10]
divisor = 5


def solution(arr, divisor):
    return sorted(i for i in arr if i % divisor == 0) or [-1]


print(solution(arr, divisor))

# ClearTime = 2021/07/04 1:04 오후
