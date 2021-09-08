# TITLE: GCD 합
# CATEGORY: math
# DATE: 2021/08/31 6:04 오후

import math
from itertools import combinations

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    candidates = list(combinations(nums[1:], 2))
    result = 0
    for cand in candidates:
        x, y = cand
        result += math.gcd(x, y)

    print(result)

# ClearTime = 2021/08/31 6:11 오후
