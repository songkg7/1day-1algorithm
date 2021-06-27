#
#
# 2021/06/27 7:57 오후

nums = [3, 1, 2, 3]


def solution(nums):
    return min(len(set(nums)), len(nums) // 2)


print(solution(nums))

# ClearTime = 2021/06/27 8:08 오후 - 시간초과
# ClearTime = 2021/06/27 11:01 오후
