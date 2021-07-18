# 가운데를 말해요
# priority queue
# 2021/07/18 9:07 오후

import bisect
import math

nums = []

N = int(input())

for _ in range(N):
    n = int(input())
    bisect.insort_left(nums, n)

    t = nums[math.ceil(len(nums) / 2 - 1)]
    print(t)

# ClearTime = 2021/07/18 9:16 오후 - time over
