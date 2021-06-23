# 가장 긴 증가하는 부분 수열 2
# Binary Search, LIS
# 2021/06/22 7:16 오후

# TODO: 다시 풀기, bisect 의 활용

import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
a = list(map(int, input().split()))

lis = []
answer = 0

for num in a:
    if not lis or lis[-1] < num:
        lis.append(num)
        answer += 1
    else:
        index = bisect_left(lis, num)
        lis[index] = num

print(answer)

# ClearTime = 2021/06/22 7:31 오후
