#
#
# 2021/07/19 2:13 오전

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]


def solution(arr1, arr2):
    return list(list(map(sum, zip(*i))) for i in zip(arr1, arr2))


print(solution(arr1, arr2))

# ClearTime = 2021/07/19 2:25 오전
