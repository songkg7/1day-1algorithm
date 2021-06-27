#
#
# 2021/06/27 7:57 오후

from itertools import combinations

nums = [3, 1, 2, 3]


def solution(nums):
    candidates = list(combinations(nums, len(nums) // 2))
    return max(set(map(lambda x: len(set(x)), candidates)))


print(solution(nums))

# ClearTime = 2021/06/27 8:08 오후 - 시간초과
