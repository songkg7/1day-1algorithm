# 연습문제
# level 2

import numpy as np

#
# arr1 = [[1, 4],
#         [3, 2],
#         [4, 1]]
# arr2 = [[3, 3],
#         [3, 3]]

arr1 = [[2, 3, 2],
        [4, 2, 4],
        [3, 1, 4]]
arr2 = [[5, 4, 3],
        [2, 4, 1],
        [3, 1, 1]]


def solution(arr1, arr2):
    return np.matmul(arr1, arr2)


print(solution(arr1, arr2))
